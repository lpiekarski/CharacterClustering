from skimage.transform import resize
import numpy as np
from PIL import Image


def get_prepared_image_flat(image_file, img_size=128):
    image = Image.open(image_file.strip())
    image_array = np.array(image)
    image_grayscale = np.empty((image_array.shape[0], image_array.shape[1]))
    for y in range(image_array.shape[1]):
        for x in range(image_array.shape[0]):
            image_grayscale[x, y] = (255. * 3. - image_array[x, y, 0] - image_array[x, y, 1] - image_array[x, y, 2]) / (255. * 3.)
    center_mass_x = 0
    sum_weights = 0
    center_mass_y = 0
    for y in range(image_array.shape[1]):
        for x in range(image_array.shape[0]):
            center_mass_x = center_mass_x + (x * image_grayscale[x, y])
            center_mass_y = center_mass_y + (y * image_grayscale[x, y])
            sum_weights = sum_weights + image_grayscale[x, y]
    if sum_weights == 0:
        return np.zeros((img_size, img_size))
    center_mass_x = (center_mass_x / sum_weights)
    center_mass_y = (center_mass_y / sum_weights)
    if center_mass_x == 0:
        return np.zeros((img_size, img_size))
    if center_mass_y == 0:
        return np.zeros((img_size, img_size))
    scale = (img_size / 2.) / center_mass_x
    if int(image_array.shape[0] * scale) > img_size or int(image_array.shape[1] * scale) > img_size:
        scale = (img_size / 2.) / center_mass_y
        if int(image_array.shape[0] * scale) > img_size or int(image_array.shape[1] * scale) > img_size:
            scale = (img_size / 2.) / (image_array.shape[0] - center_mass_x)
            if int(image_array.shape[0] * scale) > img_size or int(image_array.shape[1] * scale) > img_size:
                scale = (img_size / 2.) / (image_array.shape[1] - center_mass_y)
    center_mass_x = center_mass_x * scale
    center_mass_y = center_mass_y * scale
    translation_x = int((img_size / 2.) - center_mass_x)
    translation_y = int((img_size / 2.) - center_mass_y)
    image_resized = resize(image_grayscale, (int(image_array.shape[0] * scale), int(image_array.shape[1] * scale)))
    final_image = np.zeros((img_size, img_size))
    for y in range(image_resized.shape[1]):
        if y + translation_y < 0 or y + translation_y >= img_size:
            continue
        for x in range(image_resized.shape[0]):
            if x + translation_x < 0 or x + translation_x >= img_size:
                continue
            final_image[x + translation_x, y + translation_y] = image_resized[x, y]
    return final_image.flatten()


def get_prepared_image_raw(image_file, img_size=128):
    image = Image.open(image_file.strip())
    image_array = np.array(image)
    image_grayscale = np.empty((image_array.shape[0], image_array.shape[1], 1))
    for y in range(image_array.shape[1]):
        for x in range(image_array.shape[0]):
            image_grayscale[x, y, 0] = (255. * 3. - image_array[x, y, 0] - image_array[x, y, 1] - image_array[
                x, y, 2]) / (255. * 3.)
    center_mass_x = 0
    sum_weights = 0
    center_mass_y = 0
    for y in range(image_array.shape[1]):
        for x in range(image_array.shape[0]):
            center_mass_x = center_mass_x + (x * image_grayscale[x, y, 0])
            center_mass_y = center_mass_y + (y * image_grayscale[x, y, 0])
            sum_weights = sum_weights + image_grayscale[x, y, 0]
    return image_grayscale.reshape((img_size, img_size, 1))


def get_prepared_image(image_file, img_size=128):
    image = Image.open(image_file.strip())
    image_array = np.array(image)
    image_grayscale = np.empty((image_array.shape[0], image_array.shape[1], 1))
    for y in range(image_array.shape[1]):
        for x in range(image_array.shape[0]):
            image_grayscale[x, y, 0] = (255. * 3. - image_array[x, y, 0] - image_array[x, y, 1] - image_array[x, y, 2]) / (255. * 3.)
    center_mass_x = 0
    sum_weights = 0
    center_mass_y = 0
    for y in range(image_array.shape[1]):
        for x in range(image_array.shape[0]):
            center_mass_x = center_mass_x + (x * image_grayscale[x, y, 0])
            center_mass_y = center_mass_y + (y * image_grayscale[x, y, 0])
            sum_weights = sum_weights + image_grayscale[x, y, 0]
    if sum_weights == 0:
        return np.zeros((img_size, img_size, 1))
    center_mass_x = (center_mass_x / sum_weights)
    center_mass_y = (center_mass_y / sum_weights)
    if center_mass_x == 0:
        return np.zeros((img_size, img_size, 1))
    if center_mass_y == 0:
        return np.zeros((img_size, img_size, 1))
    scale = (img_size / 2.) / center_mass_x
    if int(image_array.shape[0] * scale) > img_size or int(image_array.shape[1] * scale) > img_size:
        scale = (img_size / 2.) / center_mass_y
        if int(image_array.shape[0] * scale) > img_size or int(image_array.shape[1] * scale) > img_size:
            scale = (img_size / 2.) / (image_array.shape[0] - center_mass_x)
            if int(image_array.shape[0] * scale) > img_size or int(image_array.shape[1] * scale) > img_size:
                scale = (img_size / 2.) / (image_array.shape[1] - center_mass_y)
    center_mass_x = center_mass_x * scale
    center_mass_y = center_mass_y * scale
    translation_x = int((img_size / 2.) - center_mass_x)
    translation_y = int((img_size / 2.) - center_mass_y)
    image_resized = resize(image_grayscale, (int(image_array.shape[0] * scale), int(image_array.shape[1] * scale)))
    final_image = np.zeros((img_size, img_size, 1))
    for y in range(image_resized.shape[1]):
        if y + translation_y < 0 or y + translation_y >= img_size:
            continue
        for x in range(image_resized.shape[0]):
            if x + translation_x < 0 or x + translation_x >= img_size:
                continue
            final_image[x + translation_x, y + translation_y, 0] = image_resized[x, y]
    return final_image


def get_prepared_images_flat(image_files, img_size=128):
    data = np.empty((len(image_files), img_size * img_size))
    for i in range(len(image_files)):
        data[i] = get_prepared_image_flat(image_files[i], img_size)
        if i % 100 == 99 or i + 1 == len(image_files):
            print(f"{i + 1}/{len(image_files)}")
    return data


def get_prepared_images(image_files, img_size=128):
    data = np.empty((len(image_files), img_size, img_size, 1))
    for i in range(len(image_files)):
        data[i] = get_prepared_image(image_files[i], img_size)
        if i % 100 == 99 or i + 1 == len(image_files):
            print(f"{i + 1}/{len(image_files)}")
    return data
