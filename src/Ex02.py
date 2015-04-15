__author__ = 'JoaoVictor'

class Struct:
    def __init__(self, char, quantity):
        self.char = char
        self.quantity = quantity

def main():

    enterstring = input("Enter a string: ")

    found = 0
    list = []
    best = Struct(enterstring[0], 1)

    for c in enterstring:
        for obj in list:
            if(c == obj.char):
                found = 1
                obj.quantity = obj.quantity + 1
                if(obj.quantity > best.quantity):
                    best = obj
        if (found == 0):
            list.append(Struct(c, 1))
        found = 0

    print("A letra mais recorrent é '"+best.char+"', aparecendo "+str(best.quantity)+" vezes.")

if __name__ == "__main__":
    main()
