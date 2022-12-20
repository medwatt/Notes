#!/usr/bin/env python

#######################################################################
#                       pwl waveform generator                        #
#######################################################################

from collections import namedtuple


#######################################################################
#                              waveforms                              #
#######################################################################

delay_field = ('duration')
pulse_field = ('duration', 'pulse_value', 'delay_before', 'delay_after', 'cycles')
square_field = ('duration', 'start_value', 'end_value', 'delay_before', 'delay_after', 'cycles')
triangle_field = ('duration', 'pulse_value', 'delay_before', 'delay_after', 'cycles')
sawtooth_field = ('duration', 'start_value', 'end_value', 'delay_before', 'delay_after', 'cycles')

Delay = namedtuple("Delay", delay_field, defaults=(0,))
Pulse = namedtuple("Pulse", pulse_field, defaults=(0,0,0,0,1))
Square = namedtuple("Square", square_field, defaults=(0,0,0,0,0,1))
Triangle = namedtuple("Triangle", triangle_field, defaults=(0,0,0,0,1))
Sawtooth = namedtuple("Sawtooth", sawtooth_field, defaults=(0,0,0,0,0,1))

#######################################################################
#                         generator function                          #
#######################################################################

def pwl_helper(
    last_x_point, last_y_point,
    duration, start_value, middle_value, end_value, delay_before, delay_after, cycles,
    transition_time):

    pwl_x, pwl_y = [], []

    for _ in range(cycles):
        if  delay_before > 0:
            last_x_point += delay_before
            pwl_x.append(last_x_point)
            pwl_y.append(last_y_point)

        if start_value != 0:
            last_x_point += transition_time
            pwl_x.append(last_x_point)
            pwl_y.append(last_y_point + start_value)

        if middle_value != 0:
            last_x_point += duration / 2
            pwl_x.append(last_x_point)
            pwl_y.append(last_y_point + middle_value)
            if middle_value == start_value:
                last_x_point += transition_time
                pwl_x.append(last_x_point)
                pwl_y.append(last_y_point + end_value)
                last_x_point += duration / 2
                pwl_x.append(last_x_point)
                pwl_y.append(last_y_point + end_value)
            else:
                last_x_point += duration / 2
                pwl_x.append(last_x_point)
                pwl_y.append(last_y_point)
        else:
            last_x_point += duration
            pwl_x.append(last_x_point)
            pwl_y.append(last_y_point + end_value)

        if end_value != 0:
            last_x_point += transition_time
            pwl_x.append(last_x_point)
            pwl_y.append(last_y_point)

        if delay_after > 0:
            last_x_point += delay_after
            pwl_x.append(last_x_point)
            pwl_y.append(last_y_point)

        last_x_point = pwl_x[-1]
        last_y_point = pwl_y[-1]
    return (last_x_point, last_y_point), (pwl_x, pwl_y)

def pwl_waveform_generator(waveform, transition_time=1, scale="n", dc_baseline=0.0):
    pwl_x, pwl_y = [0], [dc_baseline]

    for wave in waveform:
        last_x_point = pwl_x[-1]
        last_y_point = pwl_y[-1]

        if isinstance(wave, Delay):
            x = [last_x_point + wave.duration]
            y = [last_y_point]

        elif isinstance(wave, Pulse):
            (last_x_point, last_y_point), (x, y) = pwl_helper(
                last_x_point = last_x_point,
                last_y_point = last_y_point,
                duration = wave.duration,
                start_value = wave.pulse_value,
                middle_value = 0,
                end_value = wave.pulse_value,
                delay_before = wave.delay_before,
                delay_after = wave.delay_after,
                cycles = wave.cycles,
                transition_time = transition_time
            )

        elif isinstance(wave, Square):
            (last_x_point, last_y_point), (x, y) = pwl_helper(
                last_x_point = last_x_point,
                last_y_point = last_y_point,
                duration = wave.duration,
                start_value = wave.start_value,
                middle_value = wave.start_value,
                end_value = wave.end_value,
                delay_before = wave.delay_before,
                delay_after = wave.delay_after,
                cycles = wave.cycles,
                transition_time = transition_time
            )

        elif isinstance(wave, Sawtooth):
            (last_x_point, last_y_point), (x, y) = pwl_helper(
                last_x_point = last_x_point,
                last_y_point = last_y_point,
                duration = wave.duration,
                start_value = wave.start_value,
                middle_value = 0,
                end_value = wave.end_value,
                delay_before = wave.delay_before,
                delay_after = wave.delay_after,
                cycles = wave.cycles,
                transition_time = transition_time
            )

        elif isinstance(wave, Triangle):
            (last_x_point, last_y_point), (x, y) = pwl_helper(
                last_x_point = last_x_point,
                last_y_point = last_y_point,
                duration = wave.duration,
                start_value = 0,
                middle_value = wave.pulse_value,
                end_value = 0,
                delay_before = wave.delay_before,
                delay_after = wave.delay_after,
                cycles = wave.cycles,
                transition_time = transition_time
            )

        pwl_x.extend(x)
        pwl_y.extend(y)

    waveform = []
    for i in range(len(pwl_x)):
        waveform.append(f"{round(pwl_x[i], 2)}{scale} \t {round(pwl_y[i], 2)}")

    return waveform

#######################################################################
#                              testbench                              #
#######################################################################

waveform = [
    Delay(duration=20),
    Pulse(duration=10, pulse_value=2, delay_before=10, delay_after=0, cycles=5),
    Delay(duration=40),
    Pulse(duration=10, pulse_value=-2, delay_before=10, delay_after=0, cycles=5),
    Delay(duration=40),
    Square(duration=20, start_value=-2, end_value=2, cycles=5),
    Delay(duration=40),
    Sawtooth(duration=20, start_value=2, end_value=0, delay_before=0, delay_after=0, cycles=2),
    Delay(duration=40),
    Sawtooth(duration=20, start_value=-2, end_value=0, delay_before=0, delay_after=0, cycles=2),
    Delay(duration=40),
    Sawtooth(duration=20, start_value=-2, end_value=2, delay_before=0, delay_after=0, cycles=2),
    Delay(duration=40),
    Sawtooth(duration=40, start_value=2, end_value=-2, delay_before=0, delay_after=0, cycles=2),
    Delay(duration=20),
    Triangle(duration=40, pulse_value=2, delay_before=0, delay_after=0, cycles=2),
]

w = pwl_waveform_generator(waveform, transition_time=0.01, scale="n", dc_baseline=0.01)

for x in w:
    print(x)
