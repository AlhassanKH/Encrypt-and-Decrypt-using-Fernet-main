### Encrypt-and-Decrypt-using-Fernet-main

### Encrypt-and-Decrypt-using-Fernet
This Python script offers a simple and interactive way to encrypt your files. It uses Fernet symmetric encryption to securely encrypt and decrypt your selected files. Just choose a file, and the script will encrypt it using a password file found on the desktop

# DISCLAIMER: THIS PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USE IT AT YOUR OWN RISK. I, THE CREATOR SHALL NOT BE LIABLE FOR ANY DAMAGES OR LOSSES, WHETHER DIRECT, INDIRECT, INCIDENTAL, CONSEQUENTIAL, OR OTHERWISE, ARISING FROM THE USE OR INABILITY TO USE THIS PROGRAM. BY USING THIS PROGRAM, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.

This Python script provides a user interface for encrypting and decrypting files using the Fernet symmetric encryption method from the `cryptography` library. It offers the following functionalities:

1. Key Management: The script can generate a new Fernet key and save it to a specified file (`pass.txt`). If the key file already exists, the script can load the existing key. Additionally, the script can generate a Fernet key from a given string, providing an alternative way to create keys.

2. File Encryption: The user can select a file through a file dialog window, and the script will encrypt the file's contents using the Fernet key. The original file is then overwritten with the encrypted data.

3. File Decryption: Similarly, the user can select an encrypted file, and the script will decrypt its contents using the Fernet key. The encrypted file is then overwritten with the original (decrypted) data.

4. User Interaction: The script prompts the user to choose whether to encrypt or decrypt a file. It then opens a file dialog window for the user to select the file to be processed. The script provides feedback on the actions taken, such as successful encryption or decryption and any errors that occur (e.g., if the file does not exist or the decryption fails).

5. Error Handling: The script includes basic error handling to manage situations such as missing files, invalid actions, and decryption failures.

Note:
- Encrypt file manual.py doesn't open a window to select a file to encrypt, type the file path for both the desired file and password file

  ### Step to use.
  Run in your python coding platform. Prompt to pick E (encrypt) or D (Decrypt). Next, it will open a window. Pick the file wishes to be en/de/crypted. Password is stored in the pass.txt file on the desktop. DO NOT FORGET OR LOSE FILE
  
### Almost anything can be encrypted and vice versa


