# # # # # # # # # # # # # # # # # #
#   calcoloCodiceMigrazione 1.0   #
#   by Matteo Tramontina          #
# # # # # # # # # # # # # # # # # #
#
#   Contact me via:
#   - e-mail: info@matteotramontina.it
#   - github: @tr4mo
#   - instagram: @tr4mo
#


# funzione per calcolare il char di parità
def getParity(string):
    parity = 0

    for i in range(len(string)):
        if i % 2:
            match string[i]:
                case "0":
                    parity += 0
                case "1":
                    parity += 1
                case "2":
                    parity += 2
                case "3":
                    parity += 3
                case "4":
                    parity += 4
                case "5":
                    parity += 5
                case "6":
                    parity += 6
                case "7":
                    parity += 7
                case "8":
                    parity += 8
                case "9":
                    parity += 9
                case "A":
                    parity += 0
                case "B":
                    parity += 1
                case "C":
                    parity += 2
                case "D":
                    parity += 3
                case "E":
                    parity += 4
                case "F":
                    parity += 5
                case "G":
                    parity += 6
                case "H":
                    parity += 7
                case "I":
                    parity += 8
                case "J":
                    parity += 9
                case "K":
                    parity += 10
                case "L":
                    parity += 11
                case "M":
                    parity += 12
                case "N":
                    parity += 13
                case "O":
                    parity += 14
                case "P":
                    parity += 15
                case "Q":
                    parity += 16
                case "R":
                    parity += 17
                case "S":
                    parity += 18
                case "T":
                    parity += 19
                case "U":
                    parity += 20
                case "V":
                    parity += 21
                case "W":
                    parity += 22
                case "X":
                    parity += 23
                case "Y":
                    parity += 24
                case "Z":
                    parity += 25
        else:
            match string[i]:
                case "0":
                    parity += 1
                case "1":
                    parity += 0
                case "2":
                    parity += 5
                case "3":
                    parity += 7
                case "4":
                    parity += 9
                case "5":
                    parity += 13
                case "6":
                    parity += 15
                case "7":
                    parity += 17
                case "8":
                    parity += 19
                case "9":
                    parity += 21
                case "A":
                    parity += 1
                case "B":
                    parity += 0
                case "C":
                    parity += 5
                case "D":
                    parity += 7
                case "E":
                    parity += 9
                case "F":
                    parity += 13
                case "G":
                    parity += 15
                case "H":
                    parity += 17
                case "I":
                    parity += 19
                case "J":
                    parity += 21
                case "K":
                    parity += 2
                case "L":
                    parity += 4
                case "M":
                    parity += 18
                case "N":
                    parity += 20
                case "O":
                    parity += 11
                case "P":
                    parity += 3
                case "Q":
                    parity += 6
                case "R":
                    parity += 8
                case "S":
                    parity += 12
                case "T":
                    parity += 14
                case "U":
                    parity += 16
                case "V":
                    parity += 10
                case "W":
                    parity += 22
                case "X":
                    parity += 25
                case "Y":
                    parity += 24
                case "Z":
                    parity += 23

    parity % 26

    parity = chr(parity + 13)

    return parity



# Lista dei tuoi codici COW
cowList = ["AAA","AAB","AAC","AAD","AAE","AAF","AAG","AAH","AAI","AAJ"]

# Prima e seconda parte del codice COR
firstCOR = "123ABC"
secondCOR = "4568DEF"

string = cowList[0] + firstCOR + secondCOR

string += str(getParity(string))

print(string)
