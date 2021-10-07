# Shellywell123's 1st Server

My first attempt at creating a simple server application, written using python3.

## Features:
 - `GET` request to retrieve the current date,time,client-device,client-ip
 - `POST` request to add a data entry to `saved_data.csv` on the host server 
 - `DEL` request to delete an existing data entry from the `saved_data.csv` on the host server by a suplied username. The file `saved_data.csv` will be auto created with the first `POST` request.
 - `locate_user.py` script to gather the geographical location of an account by a supplied username

## Usage:
Start server host.
```bash
python3 server.py

```

```
 Welcome to
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄░█░████░▄▄█░██░██░██░█░███░█░▄▄█░██░██▀░██░▄░█░▄▄░█░█░▄▄██
██▄▄▄▀▀█░▄▄░█░▄▄█░██░██░▀▀░█▄▀░▀▄█░▄▄█░██░███░███▀▄███▄▀███▄▄▀██
██░▀▀▀░█▄██▄█▄▄▄█▄▄█▄▄█▀▀▀▄██▄█▄██▄▄▄█▄▄█▄▄█▀░▀█░▀▀█░▀▀░███▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
      █▀░██░▄▄█▄░▄████░▄▄▄░█░▄▄█░▄▄▀█▀███▀█░▄▄█░▄▄▀█░██
      ██░██▄▄▀██░█████▄▄▄▀▀█░▄▄█░▀▀▄██░▀░██░▄▄█░▀▀▄█▄██
      █▀░▀█▄▄▄██▄█████░▀▀▀░█▄▄▄█▄█▄▄███▄███▄▄▄█▄█▄▄█▀██
      ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

starting server...
Server listening on 127.0.0.1:3299
```

Connect to server as a client.
```bash
python3 client.py
```

```
========================================
Welcome to Shellywell123's 1st Server!
========================================

Server options:
 - "GET" : Get Client Device Info
 - "POST": Add a new account entry
 - "DEL" : Delete a previous account entry
 - "q"   : Leave the server

```

## To be developed:
 - threading to allow multiple users
 - checking of duplicate usernames before adding new entry to csv
