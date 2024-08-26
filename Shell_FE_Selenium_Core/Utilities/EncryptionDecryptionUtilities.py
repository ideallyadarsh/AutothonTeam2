import json
import os
from cryptography.fernet import Fernet
dict_check = {}
from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities

class EncryptionDecryption:
    """EncryptionDecryption class contains reusable methods to encrypt, decrypt and key generation data ."""

    current_working_directory = os.path.dirname(os.getcwd())
    testdata = current_working_directory + "/Shell_FE_Behave_Tests/TestData/"
    logobj = LoggingUtilities()
    log = logobj.logger()

    @staticmethod
    def generate_key():
        """
        Generates a key and save it into a file
        """
        fname = EncryptionDecryption.testdata + "secret.key"
        if not os.path.isfile(fname):
            key = Fernet.generate_key()
            with open(fname, "wb") as key_file:
                EncryptionDecryption.log.info(f"Generating secret key ...")
                key_file.write(key)
        else:
            EncryptionDecryption.log.info(f"secret.key Key already present in path")

    @staticmethod
    def load_key():
        """
        Load the previously generated key
        """
        fname = EncryptionDecryption.testdata + "secret.key"
        return open(fname, "rb").read()

    @staticmethod
    def encrypt_message(message):
        """
        Encrypts a message
        """
        key = EncryptionDecryption.load_key()
        encoded_message = message.encode()
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message)
        return encrypted_message

    @staticmethod
    def encrypt_user_creds(env="UAT", user_role="", username="", password=""):

        EncryptionDecryption.generate_key()
        fname = EncryptionDecryption.testdata + "creds.json"
        pos= user_role
        env = env.upper()
        name = username.lower()
        password = EncryptionDecryption.encrypt_message(password)
        encrypt_pswrd = password.decode()

        dict_check[env] = {}
        dict_check[env][pos] = [name, encrypt_pswrd]
        try:
            if not os.path.isfile(fname):
                with open(fname, mode='w') as f:
                    f.write(json.dumps(dict_check, indent=2))
            else:
                with open(fname) as feedsjson:
                    feeds = json.load(feedsjson)

                    dict_org = feeds
                    if env in dict_org.keys():

                        if pos in dict_org[env].keys():
                            dict_org[env][pos] = [name, encrypt_pswrd]
                        else:
                            dict_org[env][pos] = [name, encrypt_pswrd]

                    else:
                        dict_org.update(dict_check)

                with open(fname, mode='w') as f:
                    f.write(json.dumps(dict_org, indent=2))
            return True

        except:
            return False

    @staticmethod
    def decrypt_message(message):
        """
        Decrypts a message
        """
        key = EncryptionDecryption.load_key()
        encoded_message = message.encode()
        f = Fernet(key)
        decrypted_message = f.decrypt(encoded_message)
        decrypted_message = decrypted_message.decode("utf-8")
        return decrypted_message

    @staticmethod
    def decrypt_user_creds(environment = "", position = "", name = ""):

        fname = EncryptionDecryption.testdata + "creds.json"

        environment= environment.upper()
        name = name.lower()

        with open(fname, 'r') as json_file:
            dictionary_values = json.load(json_file)
        try:
            if dictionary_values[environment][position][0] == name:
                encyptpassword = dictionary_values[environment][position][1]
                decrypted_password = EncryptionDecryption.decrypt_message(encyptpassword)
                EncryptionDecryption.log.info(f"Decrypted Password {decrypted_password} ")
                return decrypted_password
        except:
            EncryptionDecryption.log.info(f"Username not found")