from PIL import Image
import json
import random

with open('settings.json') as f:
    data = json.load(f)
    ASCII_CHARS = data['ASCII_CHARS']  # 그릴때 사용한 아스키코드
    random.shuffle(ASCII_CHARS)
    OUTPUT_WIDTH = data['OUTPUT_WIDTH']  # 출력 높이
    DETAIL_PRIORITY = data['DETAIL_PRIORITY']  # 낮을수록 디테일하게 출력


def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.6)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def pixels_to_ascii(image, detail_priority):
    pixels = image.getdata()

    characters = "".join([ASCII_CHARS[(pixel // detail_priority) % len(ASCII_CHARS)] for pixel in pixels])
    return characters


def image_to_ascii(image):
    new_img_data = pixels_to_ascii(grayify(resize_image(image, OUTPUT_WIDTH)), DETAIL_PRIORITY)
    pixel_cnt = len(new_img_data)
    ascii_image = "\n".join(new_img_data[i:(i+OUTPUT_WIDTH)] for i in range(0, pixel_cnt, OUTPUT_WIDTH))
    return ascii_image


def numpy_to_image(array):
    return Image.fromarray(array)


if __name__ == '__main__':
    img = Image.open('bonsim.jpg')
    print(image_to_ascii(img))
