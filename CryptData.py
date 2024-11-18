from cryptography.fernet import Fernet

salt=b'mHHXAa8m_3wQPrnDnlPxM9Gw_VzmzEl4GA2du2djG28='

fernet=Fernet(salt)

def CryptByteArray(a):
    return fernet.encrypt(a)

def DeCryptByteArray(a):
    return fernet.decrypt(a).decode("UTF-8")