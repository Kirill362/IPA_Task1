import numpy as np
from PIL import Image


def median_filter(image_array, k):
    pad = k // 2
    padded = np.pad(image_array, ((pad, pad), (pad, pad), (0, 0)), mode='reflect')
    h, w, c = image_array.shape
    result = np.zeros_like(image_array)

    for y in range(h):
        for x in range(w):
            for channel in range(c):
                window = padded[y:y + k, x:x + k, channel].flatten()
                result[y, x, channel] = np.median(window)
    return result


if __name__ == "__main__":
    img = Image.open("img/test_image.png").convert("RGB")
    img.show()

    img_array = np.array(img)

    denoised_array = median_filter(img_array, 3)
    denoised_img = Image.fromarray(denoised_array.astype(np.uint8))
    denoised_img.save("img/denoised_image(k=3).jpg")
    denoised_img.show()

    denoised_array = median_filter(img_array, 5)
    denoised_img = Image.fromarray(denoised_array.astype(np.uint8))
    denoised_img.save("img/denoised_image(k=5).jpg")
    denoised_img.show()

    denoised_array = median_filter(img_array, 7)
    denoised_img = Image.fromarray(denoised_array.astype(np.uint8))
    denoised_img.save("img/denoised_image(k=7).jpg")
    denoised_img.show()
