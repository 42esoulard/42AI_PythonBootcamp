from ColorFilter import ColorFilter
cf = ColorFilter()
import matplotlib.pyplot as plt
arr = plt.imread("tt.png")
gr = cf.to_grayscale(arr, 'm')
plt.imshow(gr)
plt.show()