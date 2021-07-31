#Modified from the code written by Dr.Dutt,Brad and Connor
#Current problem, check what hex val 0x200000 does, turn off for 2.5s?

import numpy as np
from PyQt5 import QtCore
from pathlib import Path

def units():
    ns = 1.0
    us = 1000.0
    ms = 1000000.0
    se = 1000000000.0

    return ns,us,ms,se


class PulseTrain:


    def __init__(self,time_on='0ns', width='20ns', separation='20ns',
                 pulses_in_train=1, pulse_train_index=0,channels=[0]):

        ns,us,ms,se = units()
        self.min_pulse_length = (1 / 400) * 1000
        self.min_instr_length = 5 * self.min_pulse_length
        self.max_instr_length = 630.0
        self.channels = channels
        self.time_val = time_on
        self.width_val = width
        self.sep_val = separation
        self.pulse_train_index = pulse_train_index
        self.time_on = float(time_on[:-2]) * eval(time_on[-2:])
        self.width = float(width[:-2]) * eval(width[-2:])
        self.separation = float(separation[:-2]) * eval(separation[-2:])
        self.pulses_in_train = pulses_in_train
        self.pulse_on_times = []
        for i in range(self.pulses_in_train):
            self.pulse_on_times.append(round(self.time_on + i * (self.width + self.separation), 10))

        self.latest_pulse_train_event = round(np.amax(np.array(self.pulse_on_times)) + self.separation+self.width,10)
        self.first_pulse_train_event = round(np.amin(np.array(self.pulse_on_times)),10)


class PulseSequence(QtCore.QThread):

    ps_status = QtCore.pyqtSignal(str)

    def __init__(self,parent=None):
        super().__init__(parent)

        self.min_pulse_length = (1/400)*1000
        self.min_instr_length = 5*self.min_pulse_length
        self.max_instr_length = 630.0
        self.num_of_pulse_trains = 0
        self.pulse_train_index = 0
        self.pulse_trains = []
        self.first_sequence_event = 0


    def check(self,width_val,separation_val,time_on_val,pulses_in_train,channels):

        ns,us,ms,se = units()

        time_on = float(time_on_val[:-2]) * eval(time_on_val[-2:])
        width = float(width_val[:-2]) * eval(width_val[-2:])
        separation = float(separation_val[:-2]) * eval(separation_val[-2:])

        if(time_on!=0 and time_on<self.min_instr_length):
            self.ps_status.emit("Pulse on time must be greater than 12.5ns")
            raise Exception("Pulse on time must be greater than 12.5ns")

        if(len(channels)==0):
            self.ps_status.emit("Please select a channel")
            raise Exception("Please select a channel")

        if (width % 2.5 != 0):
            self.ps_status.emit("Width must be multiple of 2.5ns")
            raise Exception("Width must be multiple of 2.5ns")

        if (time_on % 2.5 != 0):
            self.ps_status.emit("On time must be multiple of 2.5ns")
            raise Exception("On time must be multiple of 2.5ns")

        if (separation % 2.5 != 0):
            self.ps_status.emit("Separation must be multiple of 2.5ns")
            raise Exception("Separation must be multiple of 2.5ns")

        if (width < self.min_instr_length):
            if (width not in [2.5, 5.0, 7.5, 10.0]):
                self.ps_status.emit("Invalid Pulse size")
                raise Exception("Invalid Pulse size")

        if (separation < self.min_instr_length):
            if (separation not in [2.5, 5.0, 7.5, 10.0]):
                self.ps_status.emit("Invalid separation size")
                raise Exception("Invalid separation size")

        if (pulses_in_train <= 0):
            self.ps_status.emit("Number of Pulses in train must be greater than 0")
            raise Exception("Number of Pulses in train must be greater than 0")

        if (width < self.min_instr_length and separation < self.min_instr_length):

            if (pulses_in_train % 2 != 0):
                self.ps_status.emit("This choice of pulse width and separation requires even number of pulses")
                raise Exception("This choice of pulse width and separation requires even number of pulses")

            if (width == 2.5):
                if (separation != 10.0):
                    self.ps_status.emit("Separation size must be 10ns or greater than 22.5ns for this choice of width")
                    raise Exception("Separation size must be 10ns or greater than 22.5ns for this choice of width")

            if (width == 5):
                if (separation != 7.5):
                    self.ps_status.emit("Separation size must be 7.5ns or greater than 20ns for this choice of width")
                    raise Exception("Separation size must be 7.5ns or greater than 20ns for this choice of width")

            if (width == 7.5):
                if (separation != 5):
                    self.ps_status.emit("Separation size must be 5ns or greater than 17.5ns for this choice of width")
                    raise Exception("Separation size must be 5ns or greater than 17.5ns for this choice of width")

            if (width == 10):
                if (separation != 2.5):
                    self.ps_status.emit("Separation size must be 2.5ns or greater than 15ns for this choice of width")
                    raise Exception("Separation size must be 2.5ns or greater than 15ns for this choice of width")

        if (width < self.min_instr_length and separation >= self.min_instr_length):
            time_alr_off = self.min_instr_length - width
            new_time = separation - time_alr_off
            if (new_time < 12.5):
                self.ps_status.emit("Invalid separation size for choice of width, valid choice is either %s "
                                    "or greater than %s" % (time_alr_off, time_alr_off + self.min_instr_length))
                raise Exception("Invalid separation size, valid choice is either %s "
                                "or greater than %s" % (time_alr_off, time_alr_off + self.min_instr_length))

        if (separation < self.min_instr_length and width >= self.min_instr_length):
            time_alr_on = self.min_instr_length - separation
            new_time = width - time_alr_on
            if (new_time < 12.5):
                self.ps_status.emit("Invalid width size for choice of separation, valid choice is either %s "
                                    "or greater than %s" % (time_alr_on, time_alr_on + self.min_instr_length))
                raise Exception("Invalid separation size, valid choice is either %s "
                                "or greater than %s" % (time_alr_on, time_alr_on + self.min_instr_length))


    def add_pulse_train(self, time_on='15ns', width='15ns', separation='15ns', pulses_in_train=1, channels=[]):
        # add this pulse to the current sequence
        self.check(width_val=width,separation_val=separation,time_on_val=time_on,pulses_in_train=pulses_in_train,channels=channels)

        pulse_train = PulseTrain(time_on=time_on, width=width, separation=separation,
                                 pulses_in_train=pulses_in_train,
                                 pulse_train_index=self.pulse_train_index, channels=channels)


        self.pulse_trains.append(pulse_train)

        if(self.has_coincident_events()):
            self.ps_status.emit("Overlapping Pulses not allowed")
            self.pulse_trains.pop()
            raise Exception("Overlapping Pulses not allowed")


        self.set_first_sequence_event()
        self.pulse_train_index += 1
        self.num_of_pulse_trains += 1


    def delete_pulse_train(self, pulse_train_index):
        if self.num_of_pulse_trains > 0:
            for pos,pulse_train in enumerate(self.pulse_trains):
                if(pulse_train.pulse_train_index == pulse_train_index):
                    self.pulse_trains.pop(pos)
                    self.num_of_pulse_trains -= 1
                    return True
            return False
        else:
            return False


    def has_coincident_events(self):
        found_coincident_event = False
        pulses = []

        for pulse_train in self.pulse_trains:
            first_event = pulse_train.first_pulse_train_event
            second_event = pulse_train.latest_pulse_train_event
            pulses.append((first_event,second_event))

        sorted_pulses = sorted(pulses,key=lambda j: j[0])

        for k in range(len(sorted_pulses)-1):
            if(sorted_pulses[k][1]>sorted_pulses[k+1][0]):
                found_coincident_event = True
        return found_coincident_event


    def order_events(self):
        pulses = []

        for pulse_train in self.pulse_trains:
            first_event = pulse_train.first_pulse_train_event
            last_event = pulse_train.latest_pulse_train_event
            index = pulse_train.pulse_train_index
            separation = pulse_train.separation
            width = pulse_train.width
            channels = pulse_train.channels
            num_of_pulses = pulse_train.pulses_in_train
            pulses.append((channels, first_event, last_event, index, separation, width, num_of_pulses))

        sorted_pulses = sorted(pulses, key=lambda j: j[1])

        return sorted_pulses

    def small_pulse(self, time,channels):

        ONE_PERIOD = 0x200000
        TWO_PERIOD = 0x400000
        THREE_PERIOD = 0x600000
        FOUR_PERIOD = 0x800000

        if time == 2.5:
            loc = ONE_PERIOD
        elif time == 5.0:
            loc = TWO_PERIOD
        elif time == 7.5:
            loc = THREE_PERIOD
        elif time == 10.0:
            loc = FOUR_PERIOD
        else:
            self.ps_status.emit("Time issue with small pulses")
            raise Exception("Time issue with small pulses")

        for channel in channels:
            loc |= 2 ** channel
        hex_val = "0x%X" % loc

        return hex_val

    def normal_pulse(self, channels):

        ON = 0xE00000
        loc = ON
        for channel in channels:
            loc |= 2 ** channel
        hex_val = "0x%X" % loc

        return hex_val

    def long_pulse(self, time, channels):

        ON = 0xE00000
        loc = ON
        ns = 1.0

        LONG_DELAY_STEP = 500 * ns
        delay_num = int(time / LONG_DELAY_STEP)
        left_over = time - delay_num * LONG_DELAY_STEP

        while left_over <= 12.5:
            LONG_DELAY_STEP = LONG_DELAY_STEP + 2.5
            delay_num = int(time / LONG_DELAY_STEP)
            left_over = time - delay_num * LONG_DELAY_STEP

            if(LONG_DELAY_STEP>self.max_instr_length):
                self.ps_status.emit("Problem in long pulse function")
                raise Exception("Problem in long pulse function")

        for channel in channels:
            loc |= 2 ** channel
        hex_val = "0x%X" % loc

        return (LONG_DELAY_STEP, delay_num, left_over, hex_val)


    def set_first_sequence_event(self):
        if self.num_of_pulse_trains > 1:
            self.first_sequence_event = sorted(self.pulse_trains, key=lambda x: x.first_pulse_train_event)[
                0].first_pulse_train_event
        elif self.num_of_pulse_trains == 1:
            self.first_sequence_event = self.pulse_trains[0].first_pulse_train_event
        else:
            self.first_sequence_event = 0

    def write_instruction_file(self, filename):
        path = str(((Path().resolve()).joinpath(Path("InstructionFiles"))).joinpath(filename))
        q = self.generate_instructions()
        with open(path, 'w') as f:
            for i in q:
                print(i, file=f)

    def generate_instructions_from_file(self, filename):
        path = str(((Path().resolve()).joinpath(Path("InstructionFiles"))).joinpath(filename))
        file = open(path, "r")
        lines = file.readlines()
        instructions = []

        for line in lines:
            instructions.append(line[:-1])

        return instructions


    def generate_instructions(self):

        if (self.has_coincident_events()):
            self.ps_status.emit("Overlapping Pulses not allowed, Could not generate instructions")
            raise Exception("Overlapping Pulses not allowed")

        instructions = []
        self.set_first_sequence_event()

        if(self.first_sequence_event != 0):

            if (self.first_sequence_event <= self.max_instr_length and self.first_sequence_event >= self.min_instr_length):
                instructions.append("0x000000, CONTINUE, 0, %s" % (self.first_sequence_event))

            elif(self.first_sequence_event > self.max_instr_length):
                LONG_DELAY_STEP, delay_num, left_over,_ = self.long_pulse(time=self.first_sequence_event,channels=[])

                instructions.append("0x000000, LONG_DELAY, %s, %s" % (delay_num,LONG_DELAY_STEP))
                instructions.append("0x000000, CONTINUE, 0, %s" % (left_over))

            else:
                self.ps_status.emit("Error assigning first sequence event")
                raise Exception("Error assigning first sequence event")



        ordered_pulses = self.order_events()
        counter = 1
        le = 0

        for pulse in ordered_pulses:

            channels, first_event, last_event, index, separation, width, num_of_pulses = pulse

            if (counter != 1):
                off_time = first_event - le
                if (off_time != 0.0):
                    if (off_time < 12.5):
                        self.ps_status.emit("Distance between pulses must be at least 12.5ns")
                        raise Exception("Distance between pulses must be at least 12.5ns")

                    elif (off_time <= self.max_instr_length and off_time >= self.min_instr_length):
                        instructions.append("0x000000, CONTINUE, 0, %s" % (off_time))

                    elif (off_time > self.max_instr_length):
                        LONG_DELAY_STEP, delay_num, left_over, _ = self.long_pulse(time=off_time, channels=[])

                        instructions.append("0x000000, LONG_DELAY, %s, %s" % (delay_num, LONG_DELAY_STEP))
                        instructions.append("0x000000, CONTINUE, 0, %s" % (left_over))


            if (width < self.min_instr_length and separation < self.min_instr_length):

                hex_val = self.small_pulse(time=width, channels=channels)

                nums = int(num_of_pulses/2)

                instructions.append("%s, LOOP, %s, 12.5" % (hex_val, nums))
                instructions.append("%s, END_LOOP, loop, 12.5" % (hex_val))


            elif (width < self.min_instr_length and separation <= self.max_instr_length and separation >= self.min_instr_length):

                hex_val_width = self.small_pulse(time=width, channels=channels)

                time_alr_off = self.min_instr_length - width
                new_time = separation - time_alr_off

                instructions.append("%s, LOOP, %s, 12.5" % (hex_val_width, num_of_pulses))
                instructions.append("0x000000, END_LOOP, loop, %s" % (new_time))


            elif (width < self.min_instr_length and separation > self.max_instr_length):

                time_alr_off = self.min_instr_length - width
                new_time = separation-time_alr_off

                hex_val_width = self.small_pulse(time=width, channels=channels)
                LONG_DELAY_STEP, delay_num, left_over, _ = self.long_pulse(time=new_time, channels=channels)

                instructions.append("%s, LOOP, %s, 12.5" % (hex_val_width, num_of_pulses))
                instructions.append("0x000000, LONG_DELAY, %s,%s" % (delay_num, LONG_DELAY_STEP))
                instructions.append("0x000000, END_LOOP, loop, %s" % (left_over))

            elif (width <= self.max_instr_length and width >= self.min_instr_length and separation < self.min_instr_length):


                time_alr_on = self.min_instr_length - separation
                new_time = width - time_alr_on
                hex_val_width = self.normal_pulse(channels=channels)
                hex_val_sep = self.small_pulse(time=time_alr_on, channels=channels)

                instructions.append("%s, LOOP, %s, %s" % (hex_val_width, num_of_pulses, new_time))
                instructions.append("%s, END_LOOP, loop, 12.5" % (hex_val_sep))


            elif (width > self.max_instr_length and separation < self.min_instr_length):

                time_alr_on = self.min_instr_length - separation
                new_time = width - time_alr_on

                LONG_DELAY_STEP, delay_num, left_over, hex_val_width = self.long_pulse(time=new_time, channels=channels)
                hex_val_sep = self.small_pulse(time=time_alr_on, channels=channels)

                instructions.append("%s,LOOP,%s,%s" % (hex_val_width, num_of_pulses, left_over))
                instructions.append("%s,LONG_DELAY,%s,%s" % (hex_val_width, delay_num, LONG_DELAY_STEP))
                instructions.append("%s,END_LOOP,loop,12.5" % (hex_val_sep))


            elif (width <= self.max_instr_length and width >= self.min_instr_length and separation <= self.max_instr_length and separation >= self.min_instr_length):

                hex_val_width = self.normal_pulse(channels=channels)

                instructions.append("%s, LOOP, %s, %s" % (hex_val_width, num_of_pulses, width))
                instructions.append("0x000000, END_LOOP, loop, %s" % (separation))


            elif (width > self.max_instr_length and separation <= self.max_instr_length and separation >= self.min_instr_length):

                LONG_DELAY_STEP, delay_num, left_over, hex_val_width = self.long_pulse(time=width, channels=channels)

                instructions.append("%s,LOOP,%s,%s" % (hex_val_width, num_of_pulses, left_over))
                instructions.append("%s,LONG_DELAY,%s,%s" % (hex_val_width, delay_num, LONG_DELAY_STEP))
                instructions.append("0x000000, END_LOOP, loop, %s" % (separation))


            elif (width <= self.max_instr_length and width >= self.min_instr_length and separation > self.max_instr_length):

                hex_val_width = self.normal_pulse(channels=channels)
                LONG_DELAY_STEP, delay_num, left_over, _ = self.long_pulse(time=separation, channels=channels)

                instructions.append("%s, LOOP, %s, %s" % (hex_val_width, num_of_pulses, width))
                instructions.append("0x000000, LONG_DELAY, %s,%s" % (delay_num, LONG_DELAY_STEP))
                instructions.append("0x000000, END_LOOP, loop, %s" % (left_over))


            elif (width > self.max_instr_length and separation > self.max_instr_length):

                LONG_DELAY_STEP_hi, delay_num_hi, left_over_hi, hex_val_width = self.long_pulse(time=width,
                                                                                                channels=channels)
                LONG_DELAY_STEP_lo, delay_num_lo, left_over_lo, _ = self.long_pulse(time=separation, channels=channels)

                instructions.append("%s, LOOP, %s, %s" % (hex_val_width, num_of_pulses, left_over_hi))
                instructions.append("%s, LONG_DELAY, %s,%s" % (hex_val_width, delay_num_hi, LONG_DELAY_STEP_hi))

                instructions.append("0x000000, LONG_DELAY, %s,%s" % (delay_num_lo, LONG_DELAY_STEP_lo))
                instructions.append("0x000000, END_LOOP, loop, %s" % (left_over_lo))


            le = last_event
            counter = 2

        instructions.append("0x000000, CONTINUE,0,50")
        instructions.append("0x000000, STOP,0,100")
        return instructions





if __name__ == '__main__':
    pass
  #  p = PulseSequence()
  #  p.add_pulse_train(time_on='1se',width='100ms',separation='100ms',
  #             pulses_in_train=2,channels=[0])
   # p.add_pulse_train(time_on='30ns', width='2.5ns', separation='10ns',
    #                  pulses_in_train=2, channels=[0])
  #  print(p.generate_instructions())
