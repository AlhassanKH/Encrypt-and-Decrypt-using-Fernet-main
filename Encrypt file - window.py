from cryptography.fernet import Fernet
import sys
import os
import hashlib
import base64
import tkinter as tk
from tkinter import filedialog

#Encrypt a file by having a window pop up

KEY_FILE = r'C:\Users\hassa\Desktop\pass.txt'

def generate_key():
    """Generate a Fernet key and save it into a file"""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    print(f"Key has been generated and saved to {KEY_FILE}")
    return key

def generate_key_from_string(string):
    """Generate a Fernet key from a given string"""
    hash = hashlib.sha256(string.encode()).digest()
    return base64.urlsafe_b64encode(hash[:32])

def load_or_generate_key():
    """Load the existing key from pass.txt or generate a new one"""
    if not os.path.isfile(KEY_FILE) or os.path.getsize(KEY_FILE) == 0:
        return generate_key()
    else:
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
            if len(key) == 44: # Check if key length is 44, which is valid for a Fernet key
                return key
            else:
                # Assuming the key is a string, not a Fernet key, convert it
                with open(KEY_FILE, 'r') as key_file:
                    string = key_file.read()
                    return generate_key_from_string(string)

def encrypt(filename, key):
    """Encrypt the file and overwrite the original file with encrypted data"""
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
    print(f"The file {filename} has been encrypted and overwritten with encrypted data.")

def decrypt(filename, key):
    """Decrypt the file and overwrite the encrypted file with decrypted data"""
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)
    print(f"The file {filename} has been decrypted and overwritten with original data.")

def select_file():
    """Open a file dialog window to select a file"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

if __name__ == "__main__":
    action = input("Would you like to (E)ncrypt or (D)ecrypt a file? ").upper()
    if action not in ['E', 'D']:
        print("Invalid action.")
        sys.exit(1)

    key = load_or_generate_key()

    if action == 'E':
        # Encrypt the file
        secret_file = select_file()
        if not os.path.exists(secret_file):
            print(f"The file {secret_file} does not exist.")
            sys.exit(1)
        encrypt(secret_file, key)
    elif action == 'D':
        # Decrypt the file
        secret_file = select_file()
        if not os.path.exists(secret_file):
            print(f"The file {secret_file} does not exist.")
            sys.exit(1)
        try:
            decrypt(secret_file, key)
        except Exception as e:
            print(f"An error occurred: {e}")
