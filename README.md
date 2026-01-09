## Task Name
**Task-02: Image Encryption and Decryption Using Python**

---

## Objective
To implement a basic image encryption and decryption mechanism using a secret key by manipulating pixel values.

---

## Project Description
This project demonstrates a simple image security technique where an image is encrypted by modifying its RGB pixel values using a key. The same key is used to decrypt the image and restore it to its original form. This task helps understand image processing and basic encryption concepts.

---

## Tools Used
- Python  
- Pillow (PIL – Python Imaging Library)

---

## How It Works
- The program reads an image file (`input.png`)
- For encryption, a key value is added to each RGB pixel using modulo 256
- The encrypted image is saved as `encrypted.png`
- For decryption, the same key is subtracted from each RGB pixel
- The decrypted image is saved as `decrypted.png`

---

## How to Run
1. Install Pillow:
   ```bash
   pip install pillow****
