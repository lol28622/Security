from PIL import Image
import random
import numpy as np
import matplotlib.pyplot as plt

def gcd(a, h):
    while True:
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp
#calculam cel mai mare divizor comun
def multiplicative_inverse(e, phi):
    d = None
    i = 1
    while True:
        temp1 = phi * i + 1
        d = float(temp1 / e)
        d_int = int(d)
        i += 1
        if d_int == d:
            break
    return int(d)
#calculeaza inversul multiplicativ al lui e
def rsa_key_generation():
    p = 37  # Choose prime numbers (e.g., 37 and 23) for demonstration purposes
    q = 23
    n = p * q
    totient = (p - 1) * (q - 1)
    e = random.randrange(1, totient)
    g = gcd(e, totient)
    while g != 1:
        e = random.randrange(1, totient)
        g = gcd(e, totient)
    d = multiplicative_inverse(e, totient)
    return e, d, n
#generam cheile

def encrypt_text(text_msg, key, n):
    encrypted_list = [(ord(char) ** key) % n for char in text_msg]
    return encrypted_list
#criptam text

def decrypt_text(encrypted_list, key, n):
    decrypted_list = [chr((char ** key) % n) for char in encrypted_list]
    return ''.join(decrypted_list)
#decript text
def encrypt_decrypt_image(img_1D, key, n, img_shape):
    encrypted_list = [(int(pixel) ** key) % n for pixel in img_1D]
    return np.array(encrypted_list).reshape(img_shape)
#cripta imagine
def main():
    while 1:#loop pentru a alege ce sa criptam

        print("Choose an option:")
        print("1. Encrypt text from console input")
        print("2. Encrypt text from a file")
        print("3. Encrypt and decrypt an image")
        print("4. Quit the program\n")

        choice = input("Enter your choice (1/2/3/4): ")

        e, d, n = rsa_key_generation()

        if choice == '1':
            text_msg = input("Enter the text message to encrypt: ")
            encrypted_msg = encrypt_text(text_msg, e, n)  # Use 'e' for encryption
            print(f"Encrypted message: {encrypted_msg}")
            decrypted_msg = decrypt_text(encrypted_msg, d, n)  # Use 'd' for decryption
            print(f"Decrypted message: {decrypted_msg}")#alegem sa criptam mesaj de la terminal

        elif choice == '2':
            file_path = input("Enter the path of the file to encrypt: ")
            with open(file_path, 'r') as file:
                text_msg = file.read()
            encrypted_msg = encrypt_text(text_msg, e, n)
            print(f"Encrypted message: {encrypted_msg}")
            decrypted_msg = decrypt_text(encrypted_msg, d, n)
            print(f"Decrypted message: {decrypted_msg}")#alegem sa criptam file

        elif choice == '3':
            img_path = input("Enter the path of the image to encrypt: ")
            img = Image.open(img_path).convert('L')  # Convert to grayscale
            data = np.array(img)
            img_1D = data.ravel()

            enc_img = encrypt_decrypt_image(img_1D, e, n, data.shape)
            plt.imshow(enc_img, cmap='gray')
            plt.title("Encrypted Image")
            plt.show()

            dec_img = encrypt_decrypt_image(enc_img.ravel(), d, n, data.shape)
            plt.imshow(dec_img, cmap='gray')
            plt.title("Decrypted Image")
            plt.show()
        elif choice == '4':
            print("Quit successfully")
            return 1
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
#alegem sa criptam imagine

if __name__ == "__main__":
    main()
