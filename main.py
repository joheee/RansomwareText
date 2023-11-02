from logic.EncryptDecrypt import EncryptDecrypt
from controller.HandleTxt import HandleTxt

getText = HandleTxt('test.txt')
file_contents = getText.getTextFill()

# encrypt to test_encrypt.txt
encryptObj = EncryptDecrypt()
print(encryptObj.encrypt(file_contents))
getText.writeTextToFile(encryptObj.encrypt(file_contents))

# decrypt it from test_encrypt.txt
getText = HandleTxt('test_encrypt.txt')
file_contents = getText.getTextFill()
print(encryptObj.decrypt(file_contents))
