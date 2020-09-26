import numpy as np
from collections import namedtuple

UniformJobs = namedtuple("UniformJobs", ("num_machines", "num_jobs", "job_lengths"))


class Simulator:

    def __init__(self,
                 random_seed=0):
        self.random = np.random.RandomState(random_seed)
        pass

    def next(self,
             num_machines,
             num_jobs,
             method="uniform"):
        job_lengths = list()
        for _ in range(num_jobs):
            job_lengths.append(self.random.uniform())

        return UniformJobs(num_machines, num_jobs, job_lengths)

