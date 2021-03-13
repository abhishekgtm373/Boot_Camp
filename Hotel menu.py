#Restraunt menu-----------------------------------------------------------------------------------------------------
#Code designed by abhishekgtm373____________________________________________________________________________________

#------------------------------------------------------------------------------------
#  ___  _     _     _     _          _         _              _____  ___________    |
# / _ \| |   | |   (_)   | |        | |       | |            |____ ||___  /____ |   |
#/ /_\ \ |__ | |__  _ ___| |__   ___| | ____ _| |_ _ __ ___      / /   / /    / /   |
#|  _  | '_ \| '_ \| / __| '_ \ / _ \ |/ / _` | __| '_ ` _ \     \ \  / /     \ \   |
#| | | | |_) | | | | \__ \ | | |  __/   < (_| | |_| | | | | |.___/ /./ /  .___/ /   |
#\_| |_/_.__/|_| |_|_|___/_| |_|\___|_|\_\__, |\__|_| |_| |_|\____/ \_/   \____/    |
#                                         __/ |                                     |
#                                        |___/                                      |
#------------------------------------------------------------------------------------

import sys
check=0

#Loop to order umprepared only two times----------------------------------------------------------------------------
while(check<2):

#Variable declaration-----------------------------------------------------------------------------------------------
    menu = ['idli', 'momos', 'roti', 'naan', 'pizza', 'pasta', 'burger', 'sandwich']
    price = [80, 60, 10, 15, 400, 150, 200, 70]
    prepared = ['idli', 'momos', 'roti', 'naan']
    unprepared = ['pizza', 'pasta', 'burger', 'sandwich']
    logicforprep = 1
    priceholder = 0
    threemusketeers=0
#-------------------------------------------------------------------------------------------------------------------

#Printing menu------------------------------------------------------------------------------------------------------
    for i in range(len(menu)):
        print(menu[i])
#-------------------------------------------------------------------------------------------------------------------

#Taking input from user---------------------------------------------------------------------------------------------
    orderid = input("\nEnter your order\n")
#-------------------------------------------------------------------------------------------------------------------

#Checking of food is prepared or not--------------------------------------------------------------------------------
    for j in range(len(unprepared)):
        if orderid == unprepared[j]:
            logicforprep = 0
#-------------------------------------------------------------------------------------------------------------------

#Taking price of order----------------------------------------------------------------------------------------------
    for k in range(len(menu)):
        if menu[k] == orderid:
            priceholder = price[k]
#-------------------------------------------------------------------------------------------------------------------

#Logical conditions for prepared food and unprepared food-----------------------------------------------------------
    if logicforprep == 1:
        print(orderid, priceholder, '\n', 'THANKS FOR ORDERING WITH US...')
        sys.exit()
    elif logicforprep == 0:
        print(
            'The food you ordered is unprepared. Please choose an option given below\n1.wait\n2.cancel\n3.return to menu')
        threemusketeers = input('Enter your choice\n')
#-------------------------------------------------------------------------------------------------------------------

#Actions for unprepared food----------------------------------------------------------------------------------------
    if int(threemusketeers) == 1:
        print('Thanks for waiting\nHere are your order details\n', orderid, priceholder)
        sys.exit()
    elif int(threemusketeers) == 2:
        print('Hope to see you again\nHave a good day...')
        sys.exit()
    elif int(threemusketeers) == 3:
        check=check+1
        threemusketeers=0
#-------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------

#Final processing for unprepared food-------------------------------------------------------------------------------
if int(check)>1:

    print('Please enter prepared food\n','\nPrepared food:')

    for l in range(len(prepared)):
        print(prepared[l])

    orderid = input("\nEnter your order\n")

    for n in range(len(menu)):
        if menu[n] == orderid:
            priceholder = price[k]

    for m in range(len(prepared)):
        if orderid==prepared[m]:
            print(orderid, priceholder,'\n','THANKS FOR ORDERING WITH US...')
            sys.exit()

####################################################################################################################
