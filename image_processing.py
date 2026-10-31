import numpy as np

image = np.array([[50, 100, 150],
                  [100, 150, 200],
                  [150, 200, 250]])

print("Original Image:")
print(image)


reshaped = image.reshape(1, 9)
print("\nReshaped Image:")
print(reshaped)

region = image[0:2, 0:2]
print("\nSliced Region:")
print(region)

bright = np.clip(image + 50, 0, 255)
print("\nBrightness Adjusted Image:")
print(bright)

transform = np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]])

result = np.dot(image, transform)
print("\nTransformed Image:")
print(result)





