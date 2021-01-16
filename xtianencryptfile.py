import pyAesCrypt
from os import stat, remove
# have to install pip3 install pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "123456789" # place your key here

# encrypt
with open("wordpress.json", "rb") as fIn:
    with open("wordpress-enc.json", "wb") as fOut: # change here
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# get encrypted file size
encFileSize = stat("wordpress-enc.json").st_size # change here

# decrypt
with open("wordpress-enc.json", "rb") as fIn: # change here
    try:
        with open("wordpress.json", "wb") as fOut: # change here
            # decrypt file stream
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
    except ValueError:
        # remove output file on error
        remove("wordpress-enc.json") # change here
