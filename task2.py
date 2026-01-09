from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save("encrypted.png")
    print("Image encrypted and saved as encrypted.png")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save("decrypted.png")
    print("Image decrypted and saved as decrypted.png")


choice = input("Type encrypt or decrypt: ").lower()
key = int(input("Enter key value: "))

if choice == "encrypt":
    encrypt_image("input.png", key)
elif choice == "decrypt":
    decrypt_image("encrypted.png", key)
else:
    print("Invalid choice")
