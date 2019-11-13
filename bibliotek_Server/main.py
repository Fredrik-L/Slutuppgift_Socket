#Import the class file and gets the objects from file.
#Will only show error if the CLasses file cant be found. 
try:
    import Classes
    import os
    librarian = Classes.Librarian()
    librarian.get_Books_From_File()
    librarian.get_CDs_From_File()
    librarian.get_Movies_From_File()
except ModuleNotFoundError:
    print("Cant find file Classes")
except FileNotFoundError:
    pass
def get_str_input(str_output):
    """Gets input that needs to be a string

        Handles wrong input, will run untill right input.
        Returns the input as a capitalized string. 
    """
    user_info = input(str_output)
    if user_info == "":
        print("You cant leave it blank.")
        return get_str_input(str_output)
    return user_info.capitalize()

def get_float_input(int_output):
    """Gets input that needs to be a float

        Catches ValueErrors and will ask untill its a number.
        Returns the input as a float, rounded by 2.
    """
    try:
        user_input = float(input(int_output))
        return round(user_input,2)
    except ValueError:
        print("Please enter a number.")
        return get_float_input(int_output)

#Loop that will run until user quits.
#Will send objects to files when it quits.
while True:
    try:
        user_input = input("What would you like to do?\n"
        "{1}Add a Book\n{2}Add a CD\n{3}Add a Movie\n{4}Print all media\n{5}Sort all media\n{6}Print all inputs\n>")
        #user_input = input("What type of media do you wanna add into the library "
        #            "a {1}Book, a {2}CD or a {3}Movie or {4} to print all medias or {5} to sort the list or {6} to print all the inputed media: \n>")
        
        if user_input.isdigit():
            user_input = int(user_input)
            #Book Case.
            if user_input == 1:
                title = get_str_input("Enter the title of the book: ")
                writer = get_str_input("Enter the writer of the book: ")
                pages = int(get_float_input("Enter the pages of the book: "))
                purchase_Price = get_float_input("Enter the price of the book: ")
                purchase_Year = int(get_float_input("Enter the year when you purchased the book: "))
                
                #Creates Book object and save it to Book list.
                media_object = Classes.Book(title,writer,purchase_Price, pages,purchase_Year)
                librarian.save_Input_Object(media_object)
                librarian.save_Object_To_List(media_object)
                os.system("cls")
                print("Successfully added Book\n")                
            #Cd Case.
            if user_input == 2:
                title = get_str_input("Enter the title of the CD: ")
                artist = get_str_input("Enter the artist of the CD: ")
                amount_Songs = int(get_float_input("Enter how many songs is on the CD: "))
                length = get_float_input("Enter the length of the whole CD in minutes: ")
                purchase_Price = get_float_input("Enter the price of the CD: ")
                copys_cd = librarian.check_Existing_CD(title,artist)
                
                #Creates Cd object and save it to CD list.
                media_object = Classes.Cd(title, artist, amount_Songs, length, purchase_Price, copys_cd)
                librarian.save_Input_Object(media_object)
                librarian.save_Object_To_List(media_object)
                os.system("cls")
                print("Successfully added Cd\n")  
            #Movie Case.
            if user_input == 3:
                title = get_str_input("Enter the title of the movie: ")
                director = get_str_input("Enter the name of the director: ")
                length = int(get_float_input("Enter the length of the movie, in min: "))
                purchase_Price = get_float_input("Enter the price of the movie: ")
                purchase_Year = int(get_float_input("Enter the year when you purchased the movie: "))
                #Loop that handles wrong input, needs to be between 1-10
                while True:
                    damage_input = int(get_float_input("Enter the damage of the tape, between 1-10."
                    "(1 is bad and 10 is perfect): "))
                    if damage_input < 11 and damage_input > 0:
                        break
                    print("It has to be a number between 1-10.")

                #Creates Movie object and save it to the Movie list.
                media_object = Classes.Movie(title, director, length, purchase_Price, purchase_Year, damage_input)
                librarian.save_Input_Object(media_object)
                librarian.save_Object_To_List(media_object)
                os.system("cls")
                print("Successfully added Movie\n")  
            #Print all objects.
            if user_input == 4:
                os.system("cls")
                librarian.print_All_List()
            #Sort all lists after title.
            if user_input == 5:
                librarian.sort_list()
                print("Successfully sorted list")
            if user_input == 6:
                os.system("cls")
                librarian.print_input_list()
        #Quits case, save the lists to the files and quits.
        if user_input == "q" or user_input == "Q":
            librarian.save_To_File()
            print("Goodbye!")
            exit()
    #Handles EOFError and KeyBoardInterrupt, save the lists to the files and quits.
    except (EOFError, KeyboardInterrupt):
        librarian.save_To_File()
        print("Goodbye!")
        exit()