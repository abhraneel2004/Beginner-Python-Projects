import PIL.Image
import os

nw = 240
ascii_chars = ['@', '#', '$', '%', '?', '*', '+', ';', ':', ',', "."]

def resize_image(image, new_width=nw):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale(image):
    grayscale_image = image.convert('L')
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ascii_chars[pixel // 25] for pixel in pixels])
    return characters

def main(new_width=nw):
    file_name = input("Enter the file name to save the ASCII art (without extension): ") + '.txt'
    file_name = os.path.join("Output_Images", file_name)
    file_path = input("Enter the full path where you want to save the file: ")

    try:
        image = PIL.Image.open(file_path)
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print("An error occurred:", e)
        return

    new_image_data = pixels_to_ascii(grayscale(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    with open(file_name, 'w') as f:
        f.write(ascii_image)

if __name__ == "__main__":
    main()
