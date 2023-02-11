
Note_list=[]
print("\n <<<<<<  STIKY NOTES  >>>>>> ")

while True:
    choice=input("Add Note press Y | To exit press N : ")
    if choice.lower()=='y':
        user_note=input("Give note - ")
        Note_list.append(user_note)
        
    elif choice.lower()=='n':
        print("Succesfully Saved\n")
        break
    else:
        print(("Invalid Choice ! "))
print("<<<  Check List  >>>\n")

for i in range(len(Note_list)):
    print(i+1,".", Note_list[i])
    
print("\n")