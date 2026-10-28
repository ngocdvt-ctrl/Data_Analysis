from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

sample = Image.open("tiger.png")

print(type(sample))
print(sample)
print(sample.size)
print(sample.format)
print(sample.mode)

sample_2 = Image.open("tiger_gray.png")
print(sample_2.mode)

crop_img = sample_2.crop((0, 0, 1200, 800))
crop_img.save("crop_img.png")

num_img = np.array(sample)
print(num_img.shape)
print(num_img[0, 0])
print(num_img[1000, 1000])


