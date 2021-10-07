import socket
from config import server_config
import csv
from datetime import datetime 

########################
# retrieve server config params
#######################
HOST = server_config['HOST_ADDRESS']
PORT = server_config['PORT'] 
FORMAT = server_config['FORMAT'] 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

def server_init():
    """
    """
    s.listen()
    print(f'Server listening on {HOST}:{PORT}')
    while True:
        conn, addr = s.accept()
        handle_client(conn,addr)


def handle_client(conn, addr):
    """
    """
    with conn:
        print(f'New connection from {addr}')
        conn.send(bytes("="*40+"\nWelcome to Shellywell123's 1st Server!\n"+"="*40, FORMAT))
        while True:
            #recieve bytes of data from 
            data = conn.recv(4096)
            if not data:
                break
            
            #######################################
            # all responses should be in form 
            # str(['responsetype',{dict of data}])
            ########################################

            data = data.decode(FORMAT)
            response_type = eval(data)[0]

            if response_type == 'GET':
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
                GET_DATA = str({'DATE':date,'TIME':time})
                conn.send(bytes(GET_DATA, FORMAT))

            if response_type == 'POST':
                account_data = eval(data)[1]
                print(account_data)
                save_data_to_csv(account_data)

            if response_type == 'DEL':
                username_to_del = eval(data)[1]
                delete_data_from_csv_by_USERNAME(conn,username_to_del)

#######################################
# 3 save and manage data
#######################################


def save_data_to_csv(data):
    """
    """
    print(data.values())
    # check if username already exists then save
    with open('saved_data.csv', 'a') as f:  
        writer = csv.writer(f)
        writer.writerow(list(data.values()))

def delete_data_from_csv_by_USERNAME(conn,username_to_del):
    """
    """
    
    current_data = []
    with open('saved_data.csv', mode ='r') as file:
      csvFile = csv.reader(file)
      for row in csvFile:
        current_data.append(row)

    for i in range(0,len(current_data)):
        entry = current_data[i]
        entry_username = entry[1]
        if entry_username == username_to_del:
            # then username is in saved file
            del current_data[i]
            with open('saved_data.csv', 'w') as f:  
                writer = csv.writer(f)
                for entry in current_data:
                    writer.writerow(entry)
            conn.send(bytes("Username found, account data deleted", FORMAT))
            return 0
    #then username not in file
    conn.send(bytes("Username not found, please try again.", FORMAT))



def main():
    """
    Server side for interacting with Shellywell123's 1st server
    """
    print(server_config['STARTUP_TITLE']
)    
    print('starting server...')
    server_init()

if __name__ == "__main__":
    main()