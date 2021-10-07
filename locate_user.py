import csv
import requests
import json

def main():
    """
    """
    
    current_data = []
    with open('saved_data.csv', mode ='r') as file:
      csvFile = csv.reader(file)
      for row in csvFile:
        current_data.append(row)

    def ask():
        """
        """
        username_to_loc = input('Enter the user name of the account you want to locate:\n')

        for i in range(0,len(current_data)):
            entry = current_data[i]
            entry_username = entry[1]
            if entry_username == username_to_loc:
                print('username found.')
                client_data = entry[3]
                ip = eval(client_data)['IP']
                # then locate
                api_url = "https://api.iplocation.net/?ip={}".format(ip)
                location = requests.get(api_url).json()

                for (k,v) in location.items():
                    print(k,' : ',v)

                return location
        print('Username not found, please try again.')
        ask()

    ask()


if __name__ == "__main__":
    main()