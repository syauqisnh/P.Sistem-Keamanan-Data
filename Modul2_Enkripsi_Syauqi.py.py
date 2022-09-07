from array import array
from cryptography.fernet import Fernet

print("TUGAS PROGRAM ENKRIPSI TEKS (string)")

message = input("Masukkan Nama Anda : ")

key = Fernet.generate_key();

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("enkripsi string : ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("deskripsi string : ", decMessage)
