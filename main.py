from caesarEncoder import Encrypter
from caesarDecoder import Decrypter
from os import system
from time import sleep
from sys import exit

while True:
    while True:
        choose = 0
        while True:
            system("cls")
            try:
                choose = int(input("[1]Encoder\n[2]Decoder\n[3]Quit\n\nSelect an option: "))
                break
            except ValueError:
                print("\nPlease enter a number...")
                sleep(1)
                system("cls")
                continue
        if choose == 1:
            system("cls")
            Encrypter()
            continue
        elif choose == 2:
            system("cls")
            Decrypter()
            continue
        elif choose == 3:
            system("cls")
            print("Quitting...")
            sleep(1)
            exit()
        else:
            system("cls")
            print("Wrong selection...")
            continue
