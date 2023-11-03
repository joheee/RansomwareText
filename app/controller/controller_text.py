import os

class ControllerText:
    def __init__(self, text):
        self.text = text
        
    def getTextFill(self):
        with open(self.text, 'r') as file:
            return file.read()
        
    def writeEncryptTextToFile(self, data):
        before_extension, extension = self.text.split('.')
        base_filename = before_extension.rsplit('_')  
        new_filename = f"{base_filename[0]}_encrypt.{extension}"
        try:
            with open(new_filename, 'wb') as file:
                file.write(data)
                os.remove(self.text)
            return True  
        except Exception as e:
            print(f"An error occurred at ControllerText.writeEncryptTextToFile: {e}")
            return False  
        
    def writeDecryptTextToFile(self, data):
        before_extension, extension = self.text.rsplit('.', 1)
        base_filename = before_extension.rsplit('_')  
        new_filename = f"{base_filename[0]}.{extension}"
        try:
            with open(new_filename, 'wb') as file:
                file.write(data.encode('utf-8'))
                os.remove(self.text)
            return True  
        except Exception as e:
            print(f"An error occurred at ControllerText.writeDecryptTextToFile: {e}")
            return False  
        
    def writeKey(self,key):
        try:
            with open(self.text, 'wb') as file:
                file.write(key)
            return True  
        except Exception as e:
            print(f"An error occurred at ControllerText.writeKey: {e}")
            return False  