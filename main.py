from logic.encrypt_decrypt import EncryptDecrypt
from controller.handle_txt import HandleTxt
from utils.util_text import UtilText

getText = HandleTxt('test.txt')
getTextEncrypted = HandleTxt('test_encrypt.txt')
encryptObj = EncryptDecrypt()

util_text = UtilText(getText, encryptObj)
util_text_decrypt = UtilText(getTextEncrypted, encryptObj)

# encrypt to test_encrypt.txt
print(util_text.encryptText())

# decrypt it from test_encrypt.txt
print(util_text_decrypt.decryptText())