import socket, sys, os
from passlib.hash import scrypt
from Crypto.Cipher import AES
from Crypto.Util import Counter

ref_password = "0"*4 # XXX: fake PIN, to be fixed
allowed_charset = "0123456789"

SCRYPT_ROUNDS = 14

COMM_AES_KEY = b"\x00"*16 # XXX: fake key, to be fixed
COMM_IV = 0

def check_password(pwd):
    if len(ref_password) != len(pwd):
        return False 
    for i in range(len(ref_password)):
        if pwd[i] not in allowed_charset:
            return False
    for i in range(len(ref_password)):
        a = scrypt.hash(ref_password[i].encode(), salt_size=0, rounds=SCRYPT_ROUNDS)
        b = scrypt.hash(pwd[i].encode(), salt_size=0, rounds=SCRYPT_ROUNDS)
        if a != b:
            return False
    return True

def server():
    global COMM_AES_KEY
    global COMM_IV

    host = "localhost"
    port = 5000

    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, port))

    print("[+] Server listening ...")

    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("[+] Connection from: " + str(address))

    while True:
        # Wait for the password (max 16 bytes) and decrypt it
        password = conn.recv(16)
        if not password:
            conn.close()
            sys.exit(-1)
        # Decrypt and check
        ctr = Counter.new(128, initial_value=COMM_IV)
        aes = AES.new(COMM_AES_KEY, AES.MODE_CTR, counter=ctr)
        COMM_IV += 1
        password = aes.decrypt(password).decode()
        if check_password(password) is True:
            conn.send("OK".encode())
            break
        else:
            conn.send("NOK".encode()) 

    print("[+] Password OK! Goodbye ...")
    conn.close()

if __name__ == '__main__':
    server()
