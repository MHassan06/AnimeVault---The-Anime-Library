
import json

print("\nWelcome to your AnimeVault\n\nPlease Choose your desired Category: ")

Cat_List = ["Watched: Experiences already seen.", "Anticipated: Upcoming titles; Not yet released.", "Bucket List: Yet to watch.", "Exit: Exit the realm."]
Menu_List = ["1. Add", "2. Remove", "3. Replace", "4. Return to main menu"]

try:
    with open("AnimeVault - The Anime Library.json", "r") as File:
        Anime_Data =json.load(File)
  
except FileNotFoundError:
    Anime_Data = {

        "Watch_List": [],
        "Ant_List": [],
        "Bucket_List": []
        }
    
Watch_List = Anime_Data["Watch_List"]
Ant_List = Anime_Data["Ant_List"]
Bucket_List = Anime_Data["Bucket_List"]



#Writing/Saving the content

def Save_data():
    with open("AnimeVault - The Anime Library.json", "w") as File:
        json.dump(Anime_Data, File, indent=4)




#Adding relevent Lists

def add_entry(My_List, Category_Name):
    print(f"\nYour Collection so far in {Category_Name}: ")
    if My_List:       
        for i, Entry in enumerate(My_List, start=1):
            print(f"\n{i}. {Entry}")
    
    else:
        print("\nNothing in your entry so far.")

#Menu system
     

def Menu_Choice(My_List, Category_Name):
    while True:
        

          

        while True:
            print(f"\nWhat would you like to do in {Category_Name}? ")

            for Choice in Menu_List:
                print(f"\n{Choice}")
            Menu_Selec = input(f"\nEnter your choice in {Category_Name}: ")
            
           
            
                                                              #Menu_List = ["1. Add", "2. Remove", "3. Replace"]
            if Menu_Selec in ["1", "2", "3", "4"]:
                break
            print("Invalid Entry; Enter a number between 1-4: ")

        # ADD AN ENTRY

        if Menu_Selec == "1":
            Added_Entry = input(f"\nEnter an entry to add in {Category_Name} or type Cancel to return: ")
            if Added_Entry.capitalize() == "Cancel":
                continue
            My_List.append(Added_Entry)
            Save_data()
            add_entry(My_List, Category_Name)

        #REMOVE AN ENTRY 
        
        elif Menu_Selec == "2":
            To_Remove = input(f"\nEnter the entry which you would like to Remove in {Category_Name} or type Cancel to go back: ")
            if To_Remove.capitalize() == "Cancel":
                continue
            if To_Remove.isdigit():

                To_Remove = int(To_Remove)

            else:
                 print("\nPlease enter a valid number.")
                 continue
            

            for i, Entry in enumerate(My_List, start=1):
                print(f"\n{i}. {Entry}")

            if 1 <= To_Remove <= len(My_List):
                My_List.pop(To_Remove - 1)
                Save_data()
                add_entry(My_List, Category_Name)

            else:
                print(f"\nEntry doesn't exist in {Category_Name}; Please try again")

        #REPLACE AN ENTRY

        elif Menu_Selec == "3":
            To_Replace = input(f"\nEnter the entry which you would like to Replace in {Category_Name} or type Cancel to go back: ")
            if To_Replace.capitalize() == "Cancel":
                 continue
            if To_Replace.isdigit():
                To_Replace = int(To_Replace)
            else:
                print("\nPlease enter a valid number.")
                continue

            
            for i, Entry in enumerate(My_List, start=1):
                print(f"\n{i}. {Entry}")

            if 1 <= To_Replace <= len(My_List):
                new_entry = input(f"Enter the name of an experience in {Category_Name} to replace: ")
                My_List[To_Replace - 1] = new_entry
                Save_data()
                add_entry(My_List, Category_Name)
            else:
                print(f"Entry Doesn't exit in {Category_Name}; Please try again")

        #GO BACK TO MAIN MENI

        else:
            print("\nInto the Main Menu Again")
            break

                            

# START 


    



while True:
    for i, Entry in enumerate(Cat_List, start=1):
        print(f"\n{i}. {Entry}")
       
    while True:
        

        Menu = input("\nEnter a number between 1-4 to enter a realm: ")
        if Menu in ["1", "2", "3", "4"]:
            break

        print("Invalid entry; Enter a number between 1-4: ")
    
      
    if Menu == "1":
        print(f"\n{Cat_List[0]}")
        add_entry(Watch_List, "--Watched--")
        Menu_Choice(Watch_List, "--Watched--")

    elif Menu == "2":
        print(f"\n{Cat_List[1]}")
        add_entry(Ant_List, "-Anticipated-")
        Menu_Choice(Ant_List, "--Anticipated--")

    elif Menu == "3":
        print (f"\n{Cat_List[2]}")
        add_entry(Bucket_List, "--Bucket List--")
        Menu_Choice(Bucket_List, "--Bucket List--")
#EXIT CONFIRMATION
    else:
        while True:
            Confirm = input("\nDo you really wish to exit the animeVault? ").capitalize()
            if Confirm in ["Yes", "No"]:
                break
            

            print("\nInvalid entry; Please Enter Yes or no")

        if Confirm == "Yes":
            print("\nSee ya next time")
            break

        elif Confirm == "No":
            
            print("\nGreat! Let's go back to enter a realm.")
       
            


        
        
      

        


        


 
    


    


 

    








