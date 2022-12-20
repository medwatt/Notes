# PWL Waveform Generator


```python
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
```

![image](./waveform.svg)
