import numpy as np


class Checkpoint(object):
    def __init__(self, name):
        """
        Create checkpoint to save times
        """
        self.name = name
        self.starts = []
        self.stops = []
        self.elapsed = []
        
    def _get_elapsed(self):
        self.elapsed = [y - x for (x, y) in zip(self.starts, self.starts)]
        
    def add_times(self, start, stop):
        self.starts.append(start)
        self.stops.append(stop)
        self.elapsed.append(stop - start)
        
    def __str__(self):
        n_iter = len(self.elapsed)
        mean = np.mean(self.elapsed)
        std = np.std(self.elapsed)
        
        return f'{self.name} | iter: {n_iter}, mean: {mean}, std dev: {std}'