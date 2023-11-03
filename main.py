from app.logic.encrypt_decrypt import EncryptDecrypt
from app.controller.controller_text import ControllerText
from app.utils.util_text import UtilText
from app.utils.file import File

# encryption method and key generation
encryptObj = EncryptDecrypt()
file = File()

# encrypt
# for file_path in file.getFileList():
#     getText = ControllerText(file_path)
#     util_text = UtilText(getText, encryptObj)
#     print(f'encrypt {file_path} is {util_text.encryptText()}')

# decrypt
for file_path in file.getFileList():
    getText = ControllerText(file_path)
    util_text = UtilText(getText, encryptObj)
    print(f"decrypt {file_path} is {util_text.decryptText('EXJ1oa4fwTlLb7di9CP2uTbwnIgAoHutNzRijFdktDc=')}")
