import datetime
import os
class Librarian():
    """Handles each object list and save methods."""
    #The class that saves objects to their list, can also print and sort the lists.
    #Will also read and create object from the file.
    #It will also write and save to the file.
    def __init__(self):
        self.book_list = []
        self.cd_list = []
        self.movie_list = []
        self.input_Cd_list = []
        self.input_Book_list = []
        self.input_Movie_list = []

    def get_type_object(self, media_object):
        """Gets the type of the object in a string."""
        if type(media_object) is Book:
            return "Book"
        if type(media_object) is Cd:
            return "Cd"
        if type(media_object) is Movie:
            return "Movie"
    def save_Object_To_List(self, media_object):
        """Saves the object to the right list

            Will check what type of object it is.
            Then saves it to the right list.
            Input is the object.
        """
        type_object = self.get_type_object(media_object)
        if type_object == "Book":
            self.book_list.append(media_object)
        if type_object == "Cd":
            self.cd_list.append(media_object)
        if type_object == "Movie":
            self.movie_list.append(media_object)
    def check_Existing_CD(self, title, artist):
        """Checks if there are any existing CDs in the list.

            Input is title and artist of the CD that it will check.
            Returns an int of how many copies of the CD.
        """
        copys_cd = 1
        for cd in self.cd_list:
            if cd.title == title and cd.creater == artist:
                copys_cd = copys_cd + 1
        return copys_cd
    def save_Input_Object(self, media_object):
        type_object = self.get_type_object(media_object)
        if type_object == "Book":
            self.input_Book_list.append(media_object)
        if type_object == "Cd":
            self.input_Cd_list.append(media_object)
        if type_object == "Movie":
            self.input_Movie_list.append(media_object)

    def print_input_list(self):
        """Prints the input lists"""
        if len(self.input_Book_list) > 0:
            print("----Books----")
            for Book in self.input_Book_list:
                print(Book)
        if len(self.input_Cd_list) > 0:
            print("----Cds----")
            for Cd in self.input_Cd_list:
                print(Cd)
        if len(self.input_Movie_list) > 0:
            print("----Movies----")
            for Movie in self.input_Movie_list:
                print(Movie)
        if len(self.input_Book_list) == 0 and len(self.input_Cd_list) == 0 and len(self.input_Movie_list) == 0:
            print("There is no media inputed.")
    def print_Book_List(self):
        """Prints all Books in book_list."""
        print("\t\t----Books----")
        if len(self.book_list) == 0:
            print("There are no books!")
        else:
            for books in self.book_list:
                print(books.__str__())
    def print_Cd_List(self):
        """Prints all CDs in cd_list."""
        print("\t\t----Cds----")
        if len(self.cd_list) == 0:
            print("There are no Cds!")
        else:
            for cd in self.cd_list:
                print(cd.__str__())
    def print_Movie_List(self):
        """Prints all Movies in movie_list."""
        print("\t\t----Movies----")
        if len(self.movie_list) == 0:
            print("There are no Movies!")
        else:
            for movies in self.movie_list:
                print(movies.__str__())
    def print_All_List(self):
        """Calls on each Print list functions."""
        self.print_Book_List()
        self.print_Cd_List()
        self.print_Movie_List()
    def sort_list(self):
        """Sort each object in every list after title."""
        self.book_list.sort(key=lambda book: book.title)
        self.cd_list.sort(key=lambda cd: cd.title)
        self.movie_list.sort(key=lambda movie: movie.title)
        self.input_Book_list.sort(key=lambda book: book.title)
        self.input_Cd_list.sort(key=lambda cd: cd.title)
        self.input_Movie_list.sort(key=lambda movie: movie.title)
    def save_To_File(self):
        """Save objects Attributes to a file.

            Will save the objects values in a 
            predefined order to a file.
            Will be separated by ,.
        """

        with open ("Books.txt", "a+") as book_file:
            for book in self.book_list:
                book_file.write(book.get_Book_Attribute() + "\n")
        with open ("Cds.txt", "a+") as cd_file:
            for cd in self.cd_list:
                cd_file.write(cd.get_Cd_Attribute() + "\n") 
        with open("Movies.txt", "a+") as movie_file:
            for movie in self.movie_list:
                movie_file.write(movie.get_Movie_Attribute() + "\n")       
    
    def get_splited_line(self, file_line):
        """Inputs a string, returns a list with words. 

            Removes newline and splits the line at ",". 
            Returns a list with each word as one element.
        """
        raw_line = file_line.replace("\n", "")
        splitted_line = raw_line.split(",")
        return splitted_line
    
    #All the Get_X_From_File, is the same but with diffrent list and file.
    #It will take a line from the file, split it and save the words into a list.
    #Then it will add each word into the right attribute for the object.
    #It can do this because i know the order of the attributes.
    def get_All_Media_From_File(self):
        self.get_Books_From_File()
        self.get_CDs_From_File()
        self.get_Movies_From_File()

    def get_Books_From_File(self):
        """Reads info from file and creates a book with the info."""
        b_file = os.path.dirname(__file__) + "/Books.txt"
        with open (b_file, "r") as book_file:
            for book_line in book_file:
                splitted_line = self.get_splited_line(book_line)

                title = splitted_line[0]
                writer = splitted_line[1]
                pages = int(splitted_line[2])
                price = float(splitted_line[3])
                year = int(splitted_line[4])
                value_today = float(splitted_line[5])
                
                book = Book(title,writer,pages,price,year)
                book.value_Today = value_today
                self.book_list.append(book)
    def get_CDs_From_File(self):
        """Reads info from file and creates a cd with the info."""
        c_file = os.path.dirname(__file__) + "/Cds.txt"
        with open(c_file, "r") as cd_file:
            for cd_line in cd_file:
                splitted_line = self.get_splited_line(cd_line)

                title = splitted_line[0]
                artist = splitted_line[1]
                amount_Songs = int(splitted_line[2])
                length = float(splitted_line[3])
                price = float(splitted_line[4])
                value_today = float(splitted_line[5])
                copys_cd = int(splitted_line[6])            
                cd = Cd(title,artist,amount_Songs,length,price,copys_cd)
                cd.value = value_today
                self.cd_list.append(cd)
    def get_Movies_From_File(self):
        """Reads info from file and creates a movie with the info."""
        m_file = os.path.dirname(__file__) + "/Movies.txt"
        with open(m_file, "r") as movie_file:
            for movie_line in movie_file:
                splitted_line = self.get_splited_line(movie_line)
                title = splitted_line[0]
                director = splitted_line[1]
                length = float(splitted_line[2])
                price = float(splitted_line[3])
                year = int(splitted_line[4])
                value_today = float(splitted_line[5])
                damage = int(splitted_line[6])

                movie = Movie(title,director,length,price,year,damage)
                movie.value_Today = value_today
                self.movie_list.append(movie)

    def get_Books_From_Client(self, media_info):
        """
            Appends the book info to the book list.
            Input media info.
        """
        splitted_media_info = media_info.split(",")

        title = splitted_media_info[0].capitalize()
        writer = splitted_media_info[1].capitalize()
        pages = int(splitted_media_info[2])
        price = float(splitted_media_info[3])
        year = int(splitted_media_info[4])
        
        book = Book(title,writer,pages,price,year)
        
        self.book_list.append(book)
    def get_CDs_From_Client(self, media_info):
        """
            Appends the Cd info to the Cd list.
            Input media info.
        """        
        splitted_line = media_info.split(",")

        title = splitted_line[0].capitalize()
        artist = splitted_line[1].capitalize()
        amount_Songs = int(splitted_line[2])
        length = float(splitted_line[3])
        price = float(splitted_line[4])
        copys_cd = self.check_Existing_CD(title,artist)

        cd = Cd(title,artist,amount_Songs,length,price,copys_cd)
        
        self.cd_list.append(cd)
    def get_Movies_From_Client(self, media_info):
        """
            Appends the Movie info to the Movie list.
            Input media info.
        """
        splitted_line = media_info.split(",")
        title = splitted_line[0].capitalize()
        director = splitted_line[1].capitalize()
        length = float(splitted_line[2])
        price = float(splitted_line[3])
        year = int(splitted_line[4])
        damage = int(splitted_line[5])

        movie = Movie(title,director,length,price,year,damage)
        
        self.movie_list.append(movie)
class Media_Object():
    """Superclass of all the Media.
    
        Input is Title, Creater, Purchased price and Length
    """
    def __init__(self, title, creater, purchase_Price, length):
        self.title = title
        self.creater = creater
        self.purchase_Price = purchase_Price
        self.length = length
        self.age = 0
    def get_price_overtime(self, price):
        """Gets the decreased price over years.

            Creates a loop that will run depending on how old the
            mediaobject is. Each year the price will decrease with 10%.
            Returns the decreased price as an float with 1 decimal.

        """
        for _ in range(self.age):
            ten_percent = (price/100) * 10
            price = price - ten_percent
        price = round(price, 1)
        return price
    def get_year_diffrence(self,year):
        """Gets the diffrence between the year today and the input year.

        Will take todays year - the input year and save the diffrence.
        This value will tell how old the media is.
        Returns the year as an int.
        """
        date = datetime.datetime.now()
        year_diffrence = date.year - int(year)
        return year_diffrence
    
class Book(Media_Object):
    """Book class, subclass to Media Object
    
        Input is inherit from superclass and purchased Year. \n
        Attritbute is Purchased year, Age and Value today plus inherited attributes.
    """
    def __init__(self, title, writer, purchase_Price, pages, purchase_Year):
        super().__init__(title, writer, purchase_Price, int(pages))
        self.purchase_Year = purchase_Year
        self.age = super().get_year_diffrence(self.purchase_Year)
        
        #Checks if its over 50 years old.
        if self.check_year_over_fifty(self.purchase_Year) == True:
            self.value_Today = self.get_price_over_fifty(self.purchase_Year, self.purchase_Price)
        else:
            self.value_Today = super().get_price_overtime(price = self.purchase_Price)
    def check_year_over_fifty(self, purchase_Year):
        """Checks if purchase year is over 50 years ago.

            If the purchase years is over 50 years ago, then it returns
            True else it will return False
        """
        if self.age > 50:
            return True
        else:
            return False
    def get_price_over_fifty(self, purchase_Year, purchase_Price):
        """Gets the price when its older then 50 years old.
        
            Creates a loop that will run depending on how old the
            mediaobject is. Each year the price will increase with 8%.
            Returns the increased price as an float with 1 decimal.       
        """
        years_over_fifty = self.age - 50
        for _ in range(years_over_fifty):
            eight_percent = (purchase_Price/100) * 8
            purchase_Price = purchase_Price + eight_percent
        purchase_Price = round(purchase_Price, 1)
        return purchase_Price
    def __str__(self):
        """Prints info about the Book object"""
        #Taken from the internet
        return (f"Title: {self.title}, Writer: {self.creater}, " 
                f"Pages: {self.length}, Price: {self.purchase_Price}, "
                f"Year: {self.purchase_Year}, Value Today: {self.value_Today}")
    def get_Book_Attribute(self):
        """Returns the objects attribute in a string, splitted by ,.
        
            This is the string that will be stored in the file.
        """
        file_str = f"{self.title},{self.creater},{self.length},{self.purchase_Price},{self.purchase_Year},{self.value_Today}"
        return file_str
class Cd(Media_Object):
    """Cd class, subclass to Media Object
    
        Input is inherit from superclass and amount of songs. \n
        Attritbute is Amount of songs, Copys of song and Value today plus inherited attributes.
    """
    def __init__(self, title, artist, amount_Songs, length, purchase_Price, copys_cd):
        super().__init__(title, artist, purchase_Price, length)
        self.amount_Songs = amount_Songs
        self.copys_cd = copys_cd
        self.value_Today = purchase_Price/copys_cd
        
    def get_Cd_Attribute(self):
        """Returns the objects attribute in a string, splitted by ,.
        
            This is the string that will be stored in the file.
        """
        pretty_file_str = f"{self.title},{self.creater},{self.amount_Songs},{self.length},{self.purchase_Price},{self.value_Today},{self.copys_cd}"
        return pretty_file_str
    def __str__(self):
        """Prints out info about the CD object."""
        #Taken from the internet
        return (f"Title: {self.title}, Artist: {self.creater}, " 
            f"Songs: {self.amount_Songs}, Length: {self.length}," 
            f"Price: {self.purchase_Price}, Value today: {self.value_Today}")
class Movie(Media_Object):
    """Movie class, subclass to Media Object
    
        Input is inherit from superclass and purchased Year and Damage. \n
        Attritbute is purchased Year, Damage, Age, Value over time and Value today plus inherited attributes.
    """
    def __init__(self, title, director, length, purchase_Price, 
                                    purchase_Year, damage_input):
        super().__init__(title, director, purchase_Price, length)
        self.purchase_Year = purchase_Year
        self.damage_input = damage_input
        self.age = super().get_year_diffrence(self.purchase_Year) 

        self.value_Over_Time = super().get_price_overtime(self.purchase_Price)
        self.value_Today = self.get_movie_value(self.damage_input, self.value_Over_Time)
    def get_movie_value(self, dmg, value_Over_Time):
        """Gets Todays value from the movie.

            If damage value is 10 then the value wont change.
            If its between 1-9 it will decreased with 0.dmg * value_Over_Time.
            Returns the movie value as an float, rounded by 2  
        """
        if dmg < 10:
            dmg_percent = dmg / 10
            movie_Value = value_Over_Time * dmg_percent 
        else:
            movie_Value = value_Over_Time
        return round(movie_Value,2)
    def get_Movie_Attribute(self):
        """Returns the objects attribute in a string, splitted by ,.
        
            This is the string that will be stored in the file.
        """
        pretty_file_str = f"{self.title},{self.creater},{self.length},{self.purchase_Price},{self.purchase_Year},{self.value_Today},{self.damage_input}"
        return pretty_file_str
    def __str__(self):
        """Prints info about the Movie object"""
        return (f"Title: {self.title}, Director: {self.creater}, " 
                f"Length: {self.length}, Price: {self.purchase_Price}, "
                f"Year: {self.purchase_Year}, Value Today: {self.value_Today}")    