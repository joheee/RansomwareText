class UtilText:
    def __init__(self,getText,encryptObj):
        self.getText = getText
        self.encryptObj = encryptObj
    
    def encryptText(self):
        try:
            file_contents = self.getText.getTextFill()
            self.getText.writeTextToFile(self.encryptObj.encrypt(file_contents))
            return True  
        except Exception as e:
            print(f"An error occurred at UtilText.encryptText: {e}")
            return False  
        
    def decryptText(self):
        try:
            file_contents = self.getText.getTextFill()
            return True  
        except Exception as e:
            print(f"An error occurred at UtilText.decryptText: {e}")
            return False  