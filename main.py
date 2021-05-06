import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)

def grays(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width =100):
    path = input("Dosyanin ismini girin: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Böyle bir dosya yok")

    new_image_data = pixels_to_ascii(grays(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()
