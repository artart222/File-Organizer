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
        print("\n\nThere is another file named '" + item + "' in " + path)
        print("1) Do you want to skip moving '" + item + "' file")
        print("2) Do you want to replace file named '" + item + "' with '" + item + "'")
        print("3) Do you want to rename file named '" + item + "'")
        move_error = int(input("\nPlease enter with number: "))

        # Skipping moving
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
                item = input("\nWhat is the new name for the file named '" + item + "': ")

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
        input("\n\nHow many directories do you want the program to create: ")
    )

    for time in range(how_many_directory):
        min_size = int(input("\nWhat is the minimum file size you want: "))
        max_size = int(input("What is the maximum file size you want: "))

        for item in os.listdir(path):
            if os.path.isfile(path + "/" + item):
                # Find size of file
                size_of_file = os.path.getsize(path + "/" + item)
                # Set this string for directory_name variable
                directory_name = (
                    "file between " + str(min_size) + " and " + str(max_size)
                )
                if min_size <= size_of_file and max_size >= size_of_file:
                    mover(directory_name, item)


def date(path):
    for item in os.listdir(path):
        if os.path.isfile(path + "/" + item):
            print("\n\n1) Do you want to organize your files based on creation time")
            print("2) Do you want to organize your files based on modified time")
            print("3) Do you want to organize your files based on accessed time")
            time_type = int(input("\nPlease enter with number: "))

            if time_type == 1:
                directory_name = time.localtime(os.path.getctime(path + "/" + item))
            elif time_type == 2:
                directory_name = time.localtime(os.path.getmtime(path + "/" + item))
            elif time_type == 3:
                directory_name = time.localtime(os.path.getatime(path + "/" + item))

            print("\n\n1) Do you want to organize your files based on their year")
            print("2) Do you want to organize your files based on their month")
            print("3) Do you want to organize your files based on their day")
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


print("How many directories do you want the program to organize")
time_of_program_run = int(input("Please enter with number: "))

for run in range(time_of_program_run):

    path = input("\n\nWhich directory you want to organize: ")

    print("\n\n1) Organize based on file first letter")
    print("2) Organize based on file extension")
    print("3) Organize based on file size")
    print("4) Organize based on file date")
    print("5) Organize based on file type")
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
