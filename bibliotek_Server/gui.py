from appJar import gui

app = gui("Library","600x600", useTtk = True)
app.setTtkTheme("xpnative")
try:
    import Classes
    librarian = Classes.Librarian()
    librarian.get_Books_From_File()
    librarian.get_CDs_From_File()
    librarian.get_Movies_From_File()
except ModuleNotFoundError:
    app.errorBox("FileError", "Cant find file Classes.py")
except FileNotFoundError:
    pass

def click(btn):
    """Buttons Book, Cd, Movie

        Switches between Frames where you add media object.
    """
    #Isent working as i want, read more in readme.
    if btn == "Book": app.firstFrame("Media")
    if btn == "Cd": app.nextFrame("Media")
    if btn == "Movie": app.lastFrame("Media")
def create_book():
    """Button Add Book"""
    try:
        title = app.getEntry("title_book").capitalize()
        writer = app.getEntry("writer").capitalize()
        pages = int(app.getEntry("pages"))
        purchased_Price_Book = int(app.getEntry("purchased_Price_Book"))
        purchased_Year_Book = int(app.getEntry("purchased_Year_Book"))
        
        media_object = Classes.Book(title,writer,purchased_Price_Book, pages, purchased_Year_Book)
        librarian.save_Object_To_List(media_object)
        librarian.save_Input_Object(media_object)
    except ValueError:
        app.errorBox("ValueError", "Wrong input, please try agian.")
def create_Cd():
    """Button Add CD"""
    try:
        title = app.getEntry("title_Cd").capitalize()
        artist = app.getEntry("artist").capitalize()
        amount_Songs = int(app.getEntry("amount_Songs"))
        length_Cd = float(app.getEntry("length_Cd"))
        purchase_Price_Cd = float(app.getEntry("purchased_Price_Cd"))
        copys_cd = librarian.check_Existing_CD(title,artist)
        
        media_object = Classes.Cd(title,artist,amount_Songs,length_Cd, purchase_Price_Cd, copys_cd)
        librarian.save_Object_To_List(media_object)
        librarian.save_Input_Object(media_object)
    except ValueError:
        app.errorBox("ValueError", "Wrong input, please try agian.")
def create_Movie():
    """Button Add Movie"""
    try:
        title = app.getEntry("title_Movie").capitalize()
        director = app.getEntry("director").capitalize()
        length_Movie = int(app.getEntry("length_Movie"))
        purchase_Price_Movie = float(app.getEntry("purchased_Price_Movie"))
        purchase_Year_Movie = int(app.getEntry("purchased_Year_Movie"))
        dmg_movie = int(app.getEntry("dmg_movie"))
        
        media_object = Classes.Movie(title,director,length_Movie,purchase_Price_Movie,purchase_Year_Movie,dmg_movie)
        librarian.save_Object_To_List(media_object)
        librarian.save_Input_Object(media_object)
    except ValueError:
        app.errorBox("ValueError", "Wrong input, please try agian.")

def save_To_File():
    """Button Save to File
    
        Calls on librarian.save_To_File
    """
    librarian.save_To_File()
def clear():
    """Button Clear
    
    Clears all Entries
    """
    app.clearAllEntries(callFunction = False)
def show_input():
    """Button Print all inputed media.

        Clears the listBox then calls on 1 function, 
        that will print all the inputed media.
    """
    app.clearListBox("Media Objects", callFunction = True)
    show_list("BOOKS", librarian.input_Book_list)
    show_list("CDS", librarian.input_Cd_list)
    show_list("MOVIES", librarian.input_Movie_list)
def show_list(object_type, object_list):
    """Input type of object and all its objects in a list.

        Will then add the object type first then all the objects
        to the listBox.
    """
    app.addListItem("Media Objects", object_type)
    app.addListItems("Media Objects", object_list)
def show_All_Media():
    """Button Print all media.

        Clears the listBox then calls on 1 function, 
        that will print all the media.
    """
    app.clearListBox("Media Objects", callFunction = True)
    show_list("BOOKS", librarian.book_list)
    show_list("CDS", librarian.cd_list)
    show_list("MOVIES", librarian.movie_list)
def sort_list():
    """Sorts all the list"""
    librarian.sort_list()


app.startFrameStack("Media")

app.startFrame("Book_Frame")
app.setSticky("WE")
app.addLabel("Adding a Book")
app.addLabel("Title of Book")
app.addEntry("title_book")
app.addLabel("Writer")
app.addEntry("writer")
app.addLabel("Pages of the books")
app.addEntry("pages")
app.addLabel("Purchased price of Book")
app.addEntry("purchased_Price_Book")
app.addLabel("Purchase year")
app.addEntry("purchased_Year_Book")
app.addButton("Add Book", create_book)

app.stopFrame()

app.startFrame("Cd_Frame")
app.setSticky("WE")
app.addLabel("Adding a CD")
app.addLabel("Title of Cd")
app.addEntry("title_Cd")
app.addLabel("Artist")
app.addEntry("artist")
app.addLabel("Amount of songs")
app.addEntry("amount_Songs")
app.addLabel("Cd length in min")
app.addEntry("length_Cd")
app.addLabel("Purchased price of Cd")
app.addEntry("purchased_Price_Cd")
app.addButton("Add Cd", create_Cd)
app.stopFrame()

app.startFrame("Movie_Frame")
app.setSticky("WE")
app.addLabel("Adding a Movie")
app.addLabel("Title of Movie")
app.addEntry("title_Movie")
app.addLabel("Director")
app.addEntry("director")
app.addLabel("Movie length in min")
app.addEntry("length_Movie")
app.addLabel("Purchased price of Movie")
app.addEntry("purchased_Price_Movie")
app.addLabel("Purchase Year")
app.addEntry("purchased_Year_Movie")
app.addLabel("Damage of Movie(1-10)")
app.addEntry("dmg_movie")
app.addButton("Add Moive", create_Movie)
app.stopFrame()
app.stopFrameStack()

app.startFrame("menu_frame", column = 1 , row = 0)
app.addButton("Book", click)
app.addButton("Cd", click)
app.addButton("Movie", click)
app.addButton("Print all media", show_All_Media)
app.addButton("Print all inputed media", show_input)
app.addButton("Sort the list", sort_list)
app.addButton("Save to File", save_To_File)
app.addButton("Clear", clear)
app.setSticky("WE")
app.setStretch("ROW")
app.stopFrame()

app.startFrame("output_frame", colspan=2, sticky="WE")
app.addListBox("Media Objects")
app.stopFrame()
app.go()