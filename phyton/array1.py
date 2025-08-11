import numpy as np

arr = np.array(['','',''], dtype='U')
xarr = np.empty_like(arr)
yarr = np.empty_like(arr)
carr = np.empty_like(arr)



def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))