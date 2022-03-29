# ctimer
Code profiler/timer supporting code checkpoints and reporting.

## Installation
```
pip install ctimer
```

## Usage
Use the `Timer` to create named checkpoints throughout your code. Checkpoints need a 'start' and a 'stop', and 
multiple iterations are combined to summarize how long it takes to complete each leg. The `report()` function
prints the results from all checkpoints.
```
import ctimer
from time import sleep

ct = ctimer.Timer()

ct.start('program')
print('Code outside loop')
sleep(1)
    
for _ in range(10):
    ct.start('loop')
    print('Code in loop')
    sleep(1)
    ct.stop('loop')
ct.stop('program')
    
ct.report()
```

The printed report appears as:
```
program | 11.0 s ± 0.0 s per iteration, n = 1
loop | 1.0 s ± 0.0 s per iteration, n = 10
```

## Future Directions

* Automatic logging, so that `report()` isn't strictly needed
* Potential support for more complex profiling
