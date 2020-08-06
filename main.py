import os , shutil , time


"""
With this function i move files
dirName is name of directory
that program must make and
item is the name of file or
directory program must move
"""
def mover(dirName , item):
    os.chdir(path)
    """
    trying to make directory
    if FileExistsError raise
    then do nothing
    (becuse the directory was
    build before)
    """
    try:
        os.mkdir(dirName)
    except FileExistsError:
        pass
    """
    trying to move file
    if shutil.Error raise
    it means the file with
    same name is in dirName
    directory so do things in
    except block
    """
    try:
        shutil.move(path + "/" + item , path + "/" + dirName)
    except shutil.Error:
        print("there is another file named " + item + " " + path)
        print("1) do you want to skip moving " + item + " file")
        print("2) do you want to replace file named " + item + " with " + item)
        print("3) do you want to rename file named " + item)
        """
        moveError is variable
        that has the number
        user enter for dealing
        with error
        """
        moveError = int(input("Please enter with number: "))
        #skiping moving
        if moveError == 1:
            pass
        #replacing file
        elif moveError == 2:
            os.remove(path + "/" + dirName + "/" + item)
            shutil.move(path + "/" + item , path + "/" + dirName)
        elif moveError == 3:
            while item in os.listdir(dirName):
                pastItem = item
                item = input("What is new name for file named " + item + ": ")
                shutil.move(path + "/" + pastItem , path + "/" + item)
            shutil.move(path + "/" + item , path + "/" + dirName)



"""
moving files based on
they're first letter
"""
def firstLetter(path):
    for item in os.listdir(path):
        if os.path.isfile(path + "/" + item):
            #find first letter of file
            dirName = item[0]
            mover(dirName , item)


"""
moving file based on
they're extension
"""
def extension(path):
    for item in os.listdir(path):
        if os.path.isfile(path + "/" + item):
            #find extension of file
            dirName = item.split(".")[-1]
            mover(dirName , item)


"""
moving file based on
they're size
"""
def size(path):
    """
    ask user how many directory
    want to program make
    """
    howManyDir = int(input("How many directory you want to program build: "))
    for time in range(howManyDir):
        """
        ask user for lowest size
        and highest size of directory
        """
        lowesSize = int(input("What is lowes size of file do you want: "))
        highestSize = int(input("What is highest size of file do you want: "))
        for item in os.listdir(path):
            if os.path.isfile(path + "/" + item):
                #find size of file
                sizeOfFile = os.path.getsize(path + "/" + item)
                #set this string for dirName variable
                dirName = ("file beetwen " + str(lowesSize) + " and " + str(highestSize))
                """
                check if file is beetwen of these
                two variable move file to dirName
                """
                if lowesSize <= sizeOfFile and highestSize >= sizeOfFile:
                    mover(dirName , item)


"""
moving file based on they're
different type of date
"""
def date(path):
    for item in os.listdir(path):
        if os.path.isfile(path + "/" + item):
            """
            ask user for which type of date
            want for organizing
            """
            print("1) Do you want to organize your file based on created time")
            print("2) Do you want to organize your file based on modified time")
            print("3) Do you want to organize your file based on accessed time")
            timeType = int(input("Please enter with number: "))

            if timeType == 1:
                dirName = time.localtime(os.path.getctime(path + "/" + item))
            elif timeType == 2:
                dirName = time.localtime(os.path.getmtime(path + "/" + item))
            elif timeType == 3:
                dirName = time.localtime(os.path.getatime(path + "/" + item))
            """
            ask user for which type of date
            want based on year , month or day
            """
            print("1) Do you want to organize your file based on they're year")
            print("2) Do you want to organize your file based on they're month")
            print("3) Do you want to organize your file based on they;re day")
            dateType = int(input("Please enter with number: "))

            if dateType == 1:
                dirName = dirName[:3]
            elif dateType == 2:
                dirName = dirName[:2]
            elif dateType == 3:
                dirName = dirName[:1]
                dirName = str(dirName).replace("," , "")
            """
            remove ) and ( beacuse
            dirName is tuple and i
            dont want ) and ( in
            directory name
            """
            dirName = str(dirName).replace(")" , "")
            dirName = str(dirName).replace("(" , "")
            mover(dirName , item)


def type(path , type):
    for item in os.listdir(path):
        if os.path.isfile(path + "/" + item):
            #walking on typeOfFile dictionary
            for type , extensions in typeOfFile.items():
                for extension in extensions:
                    """
                    find extension of file and
                    check if file extension is
                    equal to extension set extension
                    for dirName variable
                    """
                    if extension == item.split(".")[-1]:
                        dirName = type
                        mover(dirName , item)


typeOfFile = {
"Audios" : ["aif" , "cda" , "mid" , "midi" , "mp3" , "mpa" , "ogg" , "wav" , "wma" , "wpl"] ,
"Compresseds" : ["7z" , "arj" , "deb" , "pkg" , "rar" , "rpm" , "tar" , "gz" , "z" , "zip"] ,
"Discs and medias" : ["bin" , "dmg" , "iso" , "toast" , "vcd"] ,
"Datas and databases" : ["csv" , "dat" , "db" , "dbf" , "log" , "mdb" , "sav" , "sql" , "tar" , "xml"] ,
"E-mails" : ["email" , "eml" , "emlx" , "msg" , "oft" , "ost" , "pst" , "vcf"] ,
"Executables" : ["apk" , "bat" , "bin" , "cgi" , "pl" , "com" , "exe" , "gadget" , "jar" , "msi" , "wsf"] ,
"Fonts" : ["fnt" , "fon" , "otf" , "ttf"] ,
"Images" : ["ai" , "bmp" , "gif" , "ico" , "jpeg" , "jpg" , "png" , "ps" , "psd" , "svg" , "tif" , "tiff"] ,
"Internet relateds" : ["asp" , "aspx" , "cer" , "cfm" , "cgi" , "pl" , "css" , "htm" , "html" , "js" , "jsp" , "part" , "php" , "rss" , "xhtml"] ,
"Presentations" : ["key" , "odp" , "pps" , "ppt" , "pptx"] ,
"Programmings" : ["c" , "cpp" , "class" , "cs" , "h" , "java" , "pl" , "sh" , "swift" , "vb" , "py"] ,
"Spreadsheets" : ["ods" , "xls" , "xlsm" , "xlsx"] ,
"System relateds" : ["bak" , "cab" , "cfg" , "cpl" , "cur" , "dll" , "dmp" , "drv" , "icns" , "ico" , "ini" , "ink" , "sys" , "tmp"] ,
"Videos" : ["3g2" , "3gp" , "avi" , "flv" , "h264" , "m4v" , "mkv" , "mov" , "mp4" , "mpg" , "mpeg" , "rm" , "swf" , "vob" , "wmv"] ,
"Word processor and texts" : ["doc" , "docx" , "odt" , "pdf" , "rtf" , "tex" , "txt" , "wpd"]
}


print("How many directory you want to program organize")
timeOfProgramRun = int(input("Please enter with number (not letter): "))

for run in range(timeOfProgramRun):

    path = input("Which directory you want to organize: ")

    print("1) organize based on first letter of files")
    print("2) organize based on extension of files")
    print("3) organize based on size of files")
    print("4) organize based on date of files")
    print("5) organize based on type of files")
    howToOrganize = int(input("Please enter with number: "))

    if howToOrganize == 1:
        firstLetter(path)
    elif howToOrganize == 2:
        extension(path)
    elif howToOrganize == 3:
        size(path)
    elif howToOrganize == 4:
        date(path)
    elif howToOrganize == 5:
        type(path , type)
