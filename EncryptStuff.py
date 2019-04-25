import pyAesCrypt

def encryptDat(i):
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    password = "foopassword"
    # encrypt
    pyAesCrypt.encryptFile("data" + (str(i)) + ".aes", "data" + (str(i+1)) + ".aes", password, bufferSize)
for i in range (1, 10):
    for i in range (1, 10):
      encryptDat(i)
print("Done!")
