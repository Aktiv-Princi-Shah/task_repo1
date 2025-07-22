file_system = {"documents":{"work":{"report.docx": None,
                                    "summary.xlsx": None,},
                            "personal":{"photos":{  "vacation.jpg": None,
                                                    "birthday.png": None,},},
                             },
                "downloads": {"software": {"setup.exe": None,},
                                 "music": {"song.mp3": None,},
                             },
                }
                
file_to_find = "birthday.png"
def search_file(folder, path):
    for name in folder:
        if name == file_to_find:
            print("File found at:", path + "/" + name)
            return True
        if isinstance(folder[name], dict):
            if search_file(folder[name], path + "/" + name):    
                return True
    return False
print("File",file_to_find)
search_file(file_system,"")  

