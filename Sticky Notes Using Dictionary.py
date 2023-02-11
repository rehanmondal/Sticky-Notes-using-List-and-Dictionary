note_dict={}

print("\n <<<<<<  STIKY NOTES  >>>>>> ")

while True:
    choice=input("Add Note press Y | To exit press N : ")
    if choice.lower()=='y':
        k   =   input("Give Title - ")
        v   =   input("Enter Note - ")
        note_dict.update({k: v})

    elif choice.lower()=='n':
        print("Succesfully Saved\n")
        break
    else:
        print("Invalid Choice ! ")

print("<<<  Check List  >>>\n")

for keys,value in note_dict.items():
    print(keys,value,sep=" - ") 
print("\n")

