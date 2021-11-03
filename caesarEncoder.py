from os import system


class Encrypter:
    def __init__(self):
        self.word = ""
        self.charList = list()
        self.alphabet = ("a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö",
                         "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z")
        self.alphabetConverted = list()
        self.key = 0
        self.input()
        self.caesarencryption()
        self.finalword()

    def input(self):
        self.word = input("Enter word: ")
        self.key = int(input("Enter key: "))
        self.word = self.word.lower()
        self.charList = list()
        for i in range(0, len(self.word)):
            self.charList.append(self.word[i])
        self.alphabetConverted = self.alphabet[self.key:] + self.alphabet[:self.key]
        system("cls")

    def caesarencryption(self):
        for i in range(0, len(self.word)):
            for j in range(0, len(self.alphabet)):
                if self.charList[i] == self.alphabet[j]:
                    self.charList[i] = self.alphabetConverted[j]
                    break
                else:
                    continue

    def finalword(self):
        self.word = ""
        for i in range(0, len(self.charList)):
            self.word += self.charList[i]
        system("cls")
        print("Encrypted word: " + self.word)
        input("Success\n\nPress enter to continue...")
