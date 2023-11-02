class HandleTxt:
    def __init__(self, text):
        self.text = text
        
    def getTextFill(self):
        with open(self.text, 'r') as file:
            return file.read()
        
    def writeTextToFile(self, data):
        base_filename, extension = self.text.split('.')
        new_filename = f"{base_filename}_encrypt.{extension}"
        with open(new_filename, 'wb') as file:
            file.write(data)