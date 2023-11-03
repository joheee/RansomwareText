from app.logic.encrypt_decrypt import EncryptDecrypt
from app.controller.controller_text import ControllerText
from app.utils.util_text import UtilText

# encryption method and key generation
encryptObj = EncryptDecrypt()

# encrypt to test_encrypt.txt
# getText = ControllerText('test/one.txt')
# util_text = UtilText(getText, encryptObj)
# print(util_text.encryptText())

# decrypt it from test_encrypt.txt
# getTextEncrypted = ControllerText('test/one_encrypt.txt')
# util_text_decrypt = UtilText(getTextEncrypted, encryptObj)
# print(util_text_decrypt.decryptText('lI997vsniXL4Oh4nGjUn4ktp4GkCT8l6vt2QiNCCrRM='))
