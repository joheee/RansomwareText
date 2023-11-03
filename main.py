from logic.encrypt_decrypt import EncryptDecrypt
from controller.handle_txt import HandleTxt
from utils.util_text import UtilText

# encryption method and key generation
encryptObj = EncryptDecrypt()

# encrypt to test_encrypt.txt
# getText = HandleTxt('test.txt')
# util_text = UtilText(getText, encryptObj)
# print(util_text.encryptText())

# decrypt it from test_encrypt.txt
getTextEncrypted = HandleTxt('test_encrypt.txt')
util_text_decrypt = UtilText(getTextEncrypted, encryptObj)
print(util_text_decrypt.decryptText('LzZscC50NQEmSVNb9FBlP9dJsYWPZZowYkR6Ds_v-K8='))
