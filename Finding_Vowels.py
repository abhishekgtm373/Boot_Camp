#finding vowels in user entered string
#Code by abhishekgtm373

# Variable Declarations-------------------------------------------------
ch=input("Enter the desired sentence or word\n")
ch=list(ch)
sizeoflist=len(ch)
found=[]
logic_holder=[0,0,0,0,0]
vowels=['a','e','i','o','u']
#-----------------------------------------------------------------------

#Detecting the vowels in given string-----------------------------------
for i in ch:
        if i in vowels:
            if i not in found:
                found.append(i)
i=0
#-----------------------------------------------------------------------

#Counting the occurence of each particular Vowel------------------------
for i in range (sizeoflist):
    if ch[i]=='a' or ch[i]=='A':
        logic_holder[0]=int(logic_holder[0])+1
    elif ch[i]=='e' or ch[i]=='E':
        logic_holder[1]=int(logic_holder[1])+1
    elif ch[i] =='i' or ch[i]=='I':
        logic_holder[2]=int(logic_holder[2])+1
    elif ch[i] =='o' or ch[i]=='O':
        logic_holder[3]=int(logic_holder[3])+1
    elif ch[i] =='u' or ch[i]=='U':
        logic_holder[4]=int(logic_holder[4])+1
#-----------------------------------------------------------------------

#Deleting the vowels which do not exist in the giver sting--------------
for i in range(4,-1,-1):
    if logic_holder[i]==0:
        del logic_holder[i]
#-----------------------------------------------------------------------

#Printing the final desirable output------------------------------------
found.sort()
print('vowels in sentence—',found,'\n','vowel repeated as—',logic_holder)
#-----------------------------------------------------------------------