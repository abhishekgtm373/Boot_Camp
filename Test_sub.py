from os import system,name
system('cls')
while True:
    import keyword
    import sys


    def list_keywords():
        print("list of keywords:\n", keyword.kwlist)


    def swapping():
        aa = input("Enter first number")
        bb = input("Enter second number")
        cc = input("Enter third number")
        aa, bb, cc = cc, aa, bb
        print("Swapped values=", aa, ", ", bb, ", ", cc)


    def size():
        qw = input("Enter the value whose size to be found")
        print("storage size:\n", sys.getsizeof(qw))


    def address():
        we = input("Enter desired value")
        print("Address of entered value:\n", id(we))


    def conversion():
        print("For binary to octal enter 1\nFor binary to hexadecimal enter 2 \n")
        con = input("Enter your choice")
        x = input("Enter to value to be converted")
        if int(con) == 1:
            print("Binary to octal=", oct(int(x)))
        elif int(con) == 2:
            print("binary to hexadecimal=", hex(int(x)))
        else:
            print("are you trying to crack a joke cause it ain't funny...")


    def EXIT():
        sys.exit()


    print(
        "List of avaiable functions:\n*List of keywords (enter '1')\n*Swapping  of 3 numbers (enter '2')\n*Display storage size (enter '3')\n*Display address (enter '4')\n*BinaryConversions (enter '5')\nTo exit enter 6")
    a = input("Enter your choice\n")
    if int(a) == 1:
        list_keywords()
    elif int(a) == 2:
        swapping()
    elif int(a) == 3:
        size()
    elif int(a) == 4:
        address()
    elif int(a) == 5:
        conversion()
    elif int(a) == 6:
        EXIT()
    else:
        print("are you trying to crack a joke cause it ain't funny...")