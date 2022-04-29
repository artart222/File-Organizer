import os, shutil, time


def mover(directory_name, item):
    os.chdir(path)
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        pass

    try:
        shutil.move(path + "/" + item, path + "/" + directory_name)
    except shutil.Error:
        print("\n\nthere is another file named " + item + " " + path)
        print("1) do you want to skip moving " + item + " file")
        print("2) do you want to replace file named " + item + " with " + item)
        print("3) do you want to rename file named " + item)
        move_error = int(input("\nPlease enter with number: "))

        # Skiping moving
        if move_error == 1:
            pass

        # Replacing file
        elif move_error == 2:
            os.remove(path + "/" + directory_name + "/" + item)
            shutil.move(path + "/" + item, path + "/" + directory_name)

        # Renaming file
        elif move_error == 3:
            while item in os.listdir(directory_name):
                old_name = item
                item = input("\nWhat is new name for file named " + item + ": ")

                shutil.move(path + "/" + old_name, path + "/" + item)

            shutil.move(path + "/" + item, path + "/" + directory_name)


def first_letter(path):
    for item in os.listdir(path):
        if os.path.isfile(path + "/" + item):
            # Find first letter of file
            directory_name = item[0]
            mover(directory_name, item)


def extension(path):
    for item in os.listdir(path):
        if os.path.isfile(path + "/" + item):
            # Find extension of file
            directory_name = item.split(".")[-1]
            mover(directory_name, item)


def size(path):
    how_many_directory = int(
        input("\n\nHow many directory you want to program build: ")
    )

    for time in range(how_many_directory):
        lowes_size = int(input("\nWhat is lowes size of file do you want: "))
        highest_size = int(input("What is highest size of file do you want: "))

        for item in os.listdir(path):
            if os.path.isfile(path + "/" + item):
                # Find size of file
                size_of_file = os.path.getsize(path + "/" + item)
                # Set this string for directory_name variable
                directory_name = (
                    "file beetwen " + str(lowes_size) + " and " + str(highest_size)
                )
                if lowes_size <= size_of_file and highest_size >= size_of_file:
                    mover(directory_name, item)


def date(path):
    for item in os.listdir(path):
        if os.path.isfile(path + "/" + item):
            print("\n\n1) Do you want to organize your file based on created time")
            print("2) Do you want to organize your file based on modified time")
            print("3) Do you want to organize your file based on accessed time")
            time_type = int(input("\nPlease enter with number: "))

            if time_type == 1:
                directory_name = time.localtime(os.path.getctime(path + "/" + item))
            elif time_type == 2:
                directory_name = time.localtime(os.path.getmtime(path + "/" + item))
            elif time_type == 3:
                directory_name = time.localtime(os.path.getatime(path + "/" + item))

            print("\n\n1) Do you want to organize your file based on they're year")
            print("2) Do you want to organize your file based on they're month")
            print("3) Do you want to organize your file based on they;re day")
            date_type = int(input("\nPlease enter with number: "))

            if date_type == 1:
                directory_name = directory_name[:3]
            elif date_type == 2:
                directory_name = directory_name[:2]
            elif date_type == 3:
                directory_name = directory_name[:1]
                directory_name = str(directory_name).replace(",", "")

            directory_name = str(directory_name).replace(")", "")
            directory_name = str(directory_name).replace("(", "")
            mover(directory_name, item)


def type(path, type):
    for item in os.listdir(path):
        if os.path.isfile(path + "/" + item):
            # Walking on files_type dictionary
            for type, extensions in files_type.items():
                for extension in extensions:
                    if extension == item.split(".")[-1]:
                        directory_name = type
                        mover(directory_name, item)


files_type = {
    "Audios": ["aif", "cda", "mid", "midi", "mp3", "mpa", "ogg", "wav", "wma", "wpl"],
    "Compresseds": ["7z", "arj", "deb", "pkg", "rar", "rpm", "tar", "gz", "z", "zip"],
    "Discs and medias": ["bin", "dmg", "iso", "toast", "vcd"],
    "Datas and databases": [
        "csv",
        "dat",
        "db",
        "dbf",
        "log",
        "mdb",
        "sav",
        "sql",
        "tar",
        "xml",
    ],
    "E-mails": ["email", "eml", "emlx", "msg", "oft", "ost", "pst", "vcf"],
    "Executables": [
        "apk",
        "bat",
        "bin",
        "cgi",
        "pl",
        "com",
        "exe",
        "gadget",
        "jar",
        "msi",
        "wsf",
    ],
    "Fonts": ["fnt", "fon", "otf", "ttf"],
    "Images": [
        "ai",
        "bmp",
        "gif",
        "ico",
        "jpeg",
        "jpg",
        "png",
        "ps",
        "psd",
        "svg",
        "tif",
        "tiff",
    ],
    "Internet relateds": [
        "asp",
        "aspx",
        "cer",
        "cfm",
        "cgi",
        "pl",
        "css",
        "htm",
        "html",
        "js",
        "jsp",
        "part",
        "php",
        "rss",
        "xhtml",
    ],
    "Presentations": ["key", "odp", "pps", "ppt", "pptx"],
    "Programmings": [
        "c",
        "cpp",
        "class",
        "cs",
        "h",
        "java",
        "pl",
        "sh",
        "swift",
        "vb",
        "py",
    ],
    "Spreadsheets": ["ods", "xls", "xlsm", "xlsx"],
    "System relateds": [
        "bak",
        "cab",
        "cfg",
        "cpl",
        "cur",
        "dll",
        "dmp",
        "drv",
        "icns",
        "ico",
        "ini",
        "ink",
        "sys",
        "tmp",
    ],
    "Videos": [
        "3g2",
        "3gp",
        "avi",
        "flv",
        "h264",
        "m4v",
        "mkv",
        "mov",
        "mp4",
        "mpg",
        "mpeg",
        "rm",
        "swf",
        "vob",
        "wmv",
    ],
    "Word processor and texts": [
        "doc",
        "docx",
        "odt",
        "pdf",
        "rtf",
        "tex",
        "txt",
        "wpd",
    ],
}


print("How many directory you want to program organize")
time_of_program_run = int(input("Please enter with number: "))

for run in range(time_of_program_run):

    path = input("\n\nWhich directory you want to organize: ")

    print("\n\n1) organize based on first letter of files")
    print("2) organize based on extension of files")
    print("3) organize based on size of files")
    print("4) organize based on date of files")
    print("5) organize based on type of files")
    how_to_organize = int(input("\nPlease enter with number: "))

    if how_to_organize == 1:
        first_letter(path)
    elif how_to_organize == 2:
        extension(path)
    elif how_to_organize == 3:
        size(path)
    elif how_to_organize == 4:
        date(path)
    elif how_to_organize == 5:
        type(path, type)
