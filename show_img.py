import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image

an_array = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 9, 99, 99, 94, 0],
                     [0, 0, 0, 25, 99, 99, 79, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 56, 99, 99, 49, 0],
                     [0, 0, 0, 73, 99, 99, 31, 0],
                     [0, 0, 0, 91, 99, 99, 13, 0],
                     [0, 0, 9, 99, 99, 94, 0, 0],
                     [0, 0, 27, 99, 99, 77, 0, 0],
                     [0, 0, 45, 99, 99, 59, 0, 0],
                     [0, 0, 63, 99, 99, 42, 0, 0],
                     [0, 0, 80, 99, 99, 24, 0, 0],
                     [0, 1, 96, 99, 99, 6, 0, 0],
                     [0, 16, 99, 99, 88, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]])
print(an_array.shape)
plt.imshow(an_array)
plt.show()

image = image.imread('tshirt_test.jpg')
# summarize shape of the pixel array
print(image.dtype)
print(image.shape)
# display the array of pixels as an image
plt.imshow(image)
plt.show()
new_image = np.copy(image)
for x, col in enumerate(new_image):
    for y, row in enumerate(col):
        print(new_image[x, y])
        avgv = (row[0] + row[1] + row[2]) / 3
        new_image[x,y] =  np.float32(avgv)
        # new_image[x, y, 0] = avgv
        # new_image[x, y, 1] = avgv
        # new_image[x, y, 2] = avgv

plt.imshow(new_image)
plt.show()
