import os

class File:
    def __init__(self) -> None:
        pass
    
    def getFileList(self):
        list = []
        # directory_path = os.getcwd()
        directory_path = 'J:/testingbang'
        ignore_dirs_and_files = ["app", "__pycache__",'.git','key.txt','main.py']  

        for root, directories, files in os.walk(directory_path):
            directories[:] = [d for d in directories if d not in ignore_dirs_and_files]
            files[:] = [d for d in files if d not in ignore_dirs_and_files]

            for file in files:
                file_path = os.path.join(root, file)
                list.append(file_path)
        
        return list