from cryptography.fernet import Fernet



def GenerateRandomKey():
    return Fernet.generate_key()
