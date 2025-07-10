Solution 1 -
import numpy as np

a = 36
arr = np.array([12, 20, 29, 37, 44, 51, 63, 70])
diff = np.abs(arr - a)
idx = np.argmin(diff)
closest = arr[idx]
print("Closest element:", closest)

Solution 2 -
import numpy as np

arr = np.array([5, 8, 13, 16, 21, 22, 27, 30])
arr[arr % 2 == 0] = -1
print(arr)
