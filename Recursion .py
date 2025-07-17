'''
Problem Scenario: Finding a File in a Folder
Imagine you have a file system with folders and files. You want to recursively search for a specific file within a folder structure with the use of recursion.


Problem:
file_system = {
    "documents": {
        "work": {
            "report.docx": None,
            "summary.xlsx": None,
        },
        "personal": {
            "photos": {
                "vacation.jpg": None,
                "birthday.png": None,
            },
        },
    },
    "downloads": {
        "software": {
            "setup.exe": None,
        },
        "music": {
            "song.mp3": None,
        },
    },
}

file_to_find = "birthday.png"

O/P: 
File 'birthday.png' 
found at: /documents/personal/photos/birthday.png
'''
file_system = {
                "documents": {   "work": {  "report.docx": None,
                                            "summary.xlsx": None,
                                         },
                                 "personal": {   "photos": { "vacation.jpg": None,
                                                             "birthday.png": None,
                                                           },
                                             },
                             },
                "downloads": {   "software": {   "setup.exe": None,  },
                                 "music": {   "song.mp3": None,   },
                             },
                }
print(file_system)
print("-------------------------------------------------------------------------------")
file_to_find = "birthday.png"
print("----------------------------------File Search----------------------------------")
def search_file(folder, path):
    for name in folder:
        if name == file_to_find:
            print("The file name is: ",name)
            print("The file found at : ",path)
            return True
        if isinstance(folder[name], dict):
            if search_file(folder[name], path + "/" + name):
                print("The details")    
                return True
    return False
    
search_file(file_system,"")
