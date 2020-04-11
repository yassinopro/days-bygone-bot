import matplotlib.pyplot as plt
import os
import skimage
import numpy as np

from skimage import io, color, measure
from skimage.transform import resize

filename1 = "BattleButton.PNG"
image1 = io.imread(filename1)
image1 = color.rgb2gray(image1)
image1_rescaled = resize(image1, (123, 274), anti_aliasing=True)

filename2 = "BattleButton1.PNG"
image2 = io.imread(filename2)
image2 = color.rgb2gray(image2)
image2_rescaled = resize(image2, (123, 274), anti_aliasing=True)

filename3 = "BattleButton2.PNG"
image3 = io.imread(filename3)
image3 = color.rgb2gray(image3)
image3_rescaled = resize(image3, (123, 274), anti_aliasing=True)

filename4 = "BattleButton3.PNG"
image4 = io.imread(filename4)
image4 = color.rgb2gray(image4)
image4_rescaled = resize(image4, (123, 274), anti_aliasing=True)

print(skimage.measure.compare_mse(image1_rescaled, image2_rescaled))
print(skimage.measure.compare_nrmse(image1_rescaled, image2_rescaled))
print(skimage.measure.compare_psnr(image1_rescaled, image2_rescaled))
print(skimage.measure.compare_ssim(image1_rescaled, image2_rescaled))
print()

print(skimage.measure.compare_mse(image1_rescaled, image3_rescaled))
print(skimage.measure.compare_nrmse(image1_rescaled, image3_rescaled))
print(skimage.measure.compare_psnr(image1_rescaled, image3_rescaled))
print(skimage.measure.compare_ssim(image1_rescaled, image3_rescaled))
print()

print(skimage.measure.compare_mse(image1_rescaled, image4_rescaled))
print(skimage.measure.compare_nrmse(image1_rescaled, image4_rescaled))
print(skimage.measure.compare_psnr(image1_rescaled, image4_rescaled))
print(skimage.measure.compare_ssim(image1_rescaled, image4_rescaled))
print()



# fig, axes = plt.subplots(nrows=2, ncols=2)
# ax = axes.ravel()
#
# ax[0].imshow(image1_rescaled, cmap='gray')
# ax[0].set_title("Rescaled image (aliasing)")
#
# ax[1].imshow(image2_rescaled, cmap='gray')
# ax[1].set_title("Rescaled image (aliasing)")
#
# ax[2].imshow(image3_rescaled, cmap='gray')
# ax[2].set_title("Rescaled image (aliasing)")
#
# ax[3].imshow(image4_rescaled, cmap='gray')
# ax[3].set_title("Rescaled image (aliasing)")
#
#
# plt.tight_layout()
# plt.show()