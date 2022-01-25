import numpy as np

array = np.array([[True, True, True, True, False],
                  [False, False, False, True, False],
                  [False, True, False, True, False],
                  [False, False, True, True, True],
                  [True, False, False, False, False]])

print(axis0 := np.all(array, axis=0), axis1 := np.all(array, axis=1))

print(np.any(axis0) or np.any(axis1))
