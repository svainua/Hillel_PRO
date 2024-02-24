from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# string the key in a file
with open("filekey.key", "wb") as filekey:
    filekey.write(key)

# Open the file that contains the key.
with open("filekey.key", "rb") as filekey:
    key = filekey.read()

# Initialize the Fernet object and store it in the fernet variable.
fernet = Fernet(key)

# Read the original file.
with open("nba.csv", "rb") as file:
    original = file.read()

# Encrypt the file and store it into an object.
encrypted = fernet.encrypt(original)

# Then write the encrypted data into the same file nba.csv.
with open("nba.csv", "wb") as encrypted_file:
    encrypted_file.write(encrypted)


# ======================================================================

# Decrypt the encrypted file

# # Open the file that contains the key.
# with open("filekey.key", "rb") as filekey:
#     key = filekey.read()

# # Initialize the Fernet object and store it in the fernet variable.
# fernet = Fernet(key)

# # Read the encrypted file.
# with open("nba.csv", "rb") as encrypted_file:
#     encrypted = encrypted_file.read()

# # Decrypt the file and store it into an object.
# decrypted = fernet.decrypt(encrypted)

# # Then write the decrypted data into the same file nba.csv.
# with open("nba.csv", "wb") as decrypted_file:
#     decrypted_file.write(decrypted)
