# sProfiler 
[![PyPI version](https://badge.fury.io/py/sprofiler.svg)](https://badge.fury.io/py/sprofiler) 

Python script profiler/timer supporting code checkpoints and reporting.

## Installation
```
pip install sprofiler
```

## Usage
Use the `Profiler` to create named checkpoints throughout your code. Checkpoints need `start` and `stop` calls, and 
multiple iterations are combined to summarize how long it takes to complete each leg. The `report` function
prints the results from all checkpoints. If `stop` is not supplied a checkpoint name, the profiler will close and calculate elapsed time from the last open checkpoint (i.e. last in, first out).
```
import sprofiler as sp
from time import sleep

pr = sp.Profiler()

pr.start('my_script')
sleep(1)
for _ in range(10):
    pr.start('sleep_1s')
    sleep(1)
    pr.stop('sleep_1s')
pr.stop('my_script')
    
pr.report()
```

The printed report appears as:
```
my_script | 11.0 s ± 0.0 s per iteration, n = 1
sleep_1s | 1.0 s ± 0.0 s per iteration, n = 10
```

## Logging

sProfiler automatically logs results by default. You can change the destination filename, as well as the level of verbosity: 0 - no logging, 1 - only elapsed times, 2 - start and stop times. Defaults are `logname='profiler.log'` and `verbose=2`.
```
import sprofiler as sp
from time import sleep

pr = sp.Profiler(logname='my_log.log', verbose=1)
```

## Function Decorators
sProfiler also supports timing functions with decorators, via `Profiler.time_func`. Demonstrating on the first example:
```
pr = sp.Profiler()

@pr.time_func
def sleep_1s():
    sleep(1)
    
@pr.time_func
def my_script():
    sleep(1)
    for _ in range(10):
        sleep_1s()
        
pr.report()
```

The printed report appears as:
```
my_script | 11.0 s ± 0.0 s per iteration, n = 1
sleep_1s | 1.0 s ± 0.0 s per iteration, n = 10
```

## Future Directions

* Potential support for more complex profiling
