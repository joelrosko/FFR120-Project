import numpy as np

prob = np.array([0.006, 0.002, 0.002, 0.003, 0.003, 0.006, 0.005, 0.009, 0.01, 0.033, 0.04,
                 0.04, 0.05, 0.07, 0.083, 0.083, 0.07, 0.025, 0.009, 0.004, 0.003, 0.001,
                 0.006, 0.002, 0.002, 0.003, 0.003, 0.006, 0.005, 0.009, 0.01, 0.033, 0.05,
                 0.04, 0.04, 0.06, 0.07, 0.083, 0.05, 0.025, 0.009, 0.004])
np.save('spawn_probabilities.npy', prob)