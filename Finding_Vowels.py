#finding vowels in user entered string
ch=input("Enter the desired sentence or word\n")
ch=list(ch)
sizeoflist=len(ch)
logic_holder=[0,0,0,0,0]

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

if logic_holder==[0,0,0,0,0]:
    print("No vowels found")
else:
    print("Found Vowels (in format [A,E,I,O,U]):\n", logic_holder)