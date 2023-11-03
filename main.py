from logic.encrypt_decrypt import EncryptDecrypt
from controller.controller_text import ControllerText
from utils.util_text import UtilText

# encryption method and key generation
encryptObj = EncryptDecrypt()

# encrypt to test_encrypt.txt
# getText = ControllerText('test/one.txt')
# util_text = UtilText(getText, encryptObj)
# print(util_text.encryptText())

# decrypt it from test_encrypt.txt
getTextEncrypted = ControllerText('test/one_encrypt.txt')
util_text_decrypt = UtilText(getTextEncrypted, encryptObj)
print(util_text_decrypt.decryptText('ngOujH7RM6x2gjZlJG5IcRAjiOwnpuZP6MZPNAwso_M='))
