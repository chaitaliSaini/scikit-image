"""
=================================================
Non-local means denoising for preserving textures
=================================================

In this example, we denoise a detail of the Lena image using the non-local
means filter. The non-local means algorithm replaces the value of a pixel by an
average of a selection of other pixels values: small patches centered on the
other pixels are compared to the patch centered on the pixel of interest, and
the average is performed only for pixels that have patches close to the current
patch. As a result, this algorithm can restore well textures, that would be
blurred by other denoising algoritm.
"""
import numpy as np
import matplotlib.pyplot as plt

from skimage import data, img_as_float
from skimage.filter import nl_means_denoising


lena = img_as_float(data.lena())
lena = lena[200:300, 100:200]

noisy = lena + 0.6 * lena.std() * np.random.random(lena.shape)
noisy = np.clip(noisy, 0, 1)

denoise = nl_means_denoising(noisy, 7, 9, 0.06)

fig, ax = plt.subplots(ncols=2, figsize=(8, 4))

ax[0].imshow(noisy)
ax[0].axis('off')
ax[0].set_title('noisy')
ax[1].imshow(denoise)
ax[1].axis('off')
ax[1].set_title('non-local means')

fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)

plt.show()
