import os

class HandleTxt:
    def __init__(self, text):
        self.text = text
        
    def getTextFill(self):
        with open(self.text, 'r') as file:
            return file.read()
        
    def writeEncryptTextToFile(self, data):
        base_filename, extension = self.text.split('.')
        new_filename = f"{base_filename}_encrypt.{extension}"
        try:
            with open(new_filename, 'wb') as file:
                file.write(data)
                os.remove(self.text)
            return True  
        except Exception as e:
            print(f"An error occurred at HandleTxt.writeEncryptTextToFile: {e}")
            return False  
        
    def writeDecryptTextToFile(self, data):
        before_extension, extension = self.text.rsplit('.', 1)
        base_filename, _ = before_extension.rsplit('_',1)  
        new_filename = f"{base_filename}_decrypt.{extension}"
        try:
            with open(new_filename, 'wb') as file:
                file.write(data.encode('utf-8'))
                os.remove(self.text)
            return True  
        except Exception as e:
            print(f"An error occurred at HandleTxt.writeDecryptTextToFile: {e}")
            return False  
        
    def writeKey(self,key):
        try:
            with open(self.text, 'wb') as file:
                file.write(key)
            return True  
        except Exception as e:
            print(f"An error occurred at HandleTxt.writeKey: {e}")
            return False  