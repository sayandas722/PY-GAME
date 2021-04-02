def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1] == player_two[p2]):
        print("DRAW")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player one wins!!")
    elif(player_one[p1]=="Rock" and player_two[p2] == "Paper"):
        print("Player two wins!!")
    elif(player_one[p1] == "Paper" and player_two[p2] == "Scissor"):
        print("Player two wins!! ")
    elif(player_one[p1] == "Paper" and player_two[p2] == "Rock"):
        print("Player one wins!! ")
    elif(player_one[p1] == "Scissor" and player_two[p2] == "Rock"):
        print("Player two wins!! ")
    elif(player_one[p1] == "Scissor" and player_two[p2] == "Paper"):
        print("Player one wins!! ")

print("0: Stone\n1: Paper\n2: Scissor\n")
player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Rock',1:'Paper',2:'Scissor'}
ch='y'
while(ch!='n'):
    num1=input("Player one, Enter your choice how you want to arrange Store, Paper and Scissor by entering 123 in any combination: ")
    num2 =input("Player two, Enter your choice how you want to arrange Store, Paper and Scissor by entering 123 in any combination: ")
    bit1= int(input("Player one, Enter the a Number from 0 to 2: "))
    bit2 = int(input("Player two, Enter the a Number from 0 to 2: "))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("DO YOU WANT  TO CONTIENUE? y/n ")

