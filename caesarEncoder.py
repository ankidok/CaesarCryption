from time import sleep
from os import system

class encrypter():
    def __init__(self):
        self.input()
        self.stringToCharList()
        self.caesarEncryption()
        self.finalWord()
    def input(self):
        self.word = input("Enter word: ")
        self.word = self.word.lower()
        self.charList = list()
        system("cls")
    def stringToCharList(self):
        for i in range(0,len(self.word),1):
            self.charList.append(self.word[i])
    def caesarEncryption(self):
        for i in range(0,len(self.word),1):
            if self.charList[i] == "a":
                self.charList[i] = "ç"
            elif self.charList[i] == "b":
                self.charList[i] = "d"
            elif self.charList[i] == "c":
                self.charList[i] = "e"
            elif self.charList[i] == "ç":
                self.charList[i] = "f"
            elif self.charList[i] == "d":
                self.charList[i] = "g"
            elif self.charList[i] == "e":
                self.charList[i] = "ğ"
            elif self.charList[i] == "f":
                self.charList[i] = "h"
            elif self.charList[i] == "g":
                self.charList[i] = "ı"
            elif self.charList[i] == "ğ":
                self.charList[i] = "i"
            elif self.charList[i] == "h":
                self.charList[i] = "j"
            elif self.charList[i] == "ı":
                self.charList[i] = "k"
            elif self.charList[i] == "i":
                self.charList[i] = "l"
            elif self.charList[i] == "j":
                self.charList[i] = "m"
            elif self.charList[i] == "k":
                self.charList[i] = "n"
            elif self.charList[i] == "l":
                self.charList[i] = "o"
            elif self.charList[i] == "m":
                self.charList[i] = "ö"
            elif self.charList[i] == "n":
                self.charList[i] = "p"
            elif self.charList[i] == "o":
                self.charList[i] = "r"
            elif self.charList[i] == "ö":
                self.charList[i] = "s"
            elif self.charList[i] == "p":
                self.charList[i] = "ş"
            elif self.charList[i] == "r":
                self.charList[i] = "t"
            elif self.charList[i] == "s":
                self.charList[i] = "u"
            elif self.charList[i] == "ş":
                self.charList[i] = "ü"
            elif self.charList[i] == "t":
                self.charList[i] = "v"
            elif self.charList[i] == "u":
                self.charList[i] = "y"
            elif self.charList[i] == "ü":
                self.charList[i] = "z"
            elif self.charList[i] == "v":
                self.charList[i] = "a"
            elif self.charList[i] == "y":
                self.charList[i] = "b"
            elif self.charList[i] == "z":
                self.charList[i] = "c"
            else:
                continue
    def finalWord(self):
        self.word = ""
        for i in range(0,len(self.charList),1):
            self.word += self.charList[i]
        print("Encryted word: "+self.word)
        input("Success\n\nPress enter to continue...")
        system("cls")