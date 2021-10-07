import socket
from config import server_config
import platform
import requests

########################
# retrieve server config params
#######################
HOST = server_config['HOST_ADDRESS']
PORT = server_config['PORT'] 
FORMAT = server_config['FORMAT'] 

def get_req(c):
    """
    """

    c.send(bytes("['GET',]", FORMAT))
    data = c.recv(1024)
    data=eval(data.decode(FORMAT))
    data['DEVICE'] = platform.platform()
    data['IP'] = requests.get('http://ip.42.pl/raw').text
    print(data)
    return data

def post_req(c):
    """
    """
    #################################
    # create data to post to server
    #################################

    NAME     = input('Enter Your Name:\n')
    USERNAME = input('Enter a Username:\n')
    INTRESTS = input('List your interests (comma seperated):\n')
    GET_INFO = get_req(c)

    ###################################
    # sends data to server in form of str(dict)
    ###################################
    account_data = str(['POST',{'NAME':NAME,'USERNAME':USERNAME,'INTRESTS':INTRESTS,'GET_INFO':GET_INFO}])
    c.send(bytes(account_data, FORMAT))

def del_req(c):
    """
    """
    username_to_del = input('Enter the username of the account you want to delete:\n')
    c.send(bytes(f"['DEL','{username_to_del}']", FORMAT))

    #recieve confirmation from server
    msg = c.recv(1024)
    print(msg.decode(FORMAT))

def main():
    """
    Client side for interacting with Shellywell123's 1st server
    """

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((HOST, PORT))

    #################################
    #recieve server welcome message
    #################################
    msg = c.recv(1024)
    print(msg.decode(FORMAT))

    def ask(c):

        print("""
Server options:
 - \"GET\" : Get Client Device Info
 - \"POST\": Add a new account entry
 - \"DEL\" : Delete a previous account entry
 - \"q\"   : Leave the server\n""")

        opt = input()
        if opt == 'GET' or opt == 'get':
            get_req(c)
        if opt == 'POST' or opt == 'post':
            post_req(c)
        if opt =='DEL' or opt == 'del':
            del_req(c)
        if opt == 'Q'or opt == 'q':
            c.close()
        else:
            ask(c)

    ask(c)

if __name__ == "__main__":
    main()