from cryptography.fernet import Fernet, InvalidToken


class Cipher:
    @staticmethod
    def encrypt(key: str, data: str) -> str:
        """
        To encrypt data, usually used to encrypt account/password.

            Params:
                key (str): Secret key used to encrypt data
                data (str): Data that needs to encrypt

            Returns:
                encrypted_data (str): Encrypted data
        """
        try:
            cipher_suite = Fernet(bytes(key, 'utf-8'))
        except ValueError:
            raise

        encrypted_data = cipher_suite.encrypt(bytes(data, 'utf-8')).decode("utf-8")

        return encrypted_data

    @staticmethod
    def decrypt(key: str, data: str) -> str:
        """
        To decrypt encrypted data.

            Params:
                key (str): Secret key used to decrypt data
                data (str): Encrypted data that needs to decrypt

            Returns:
                decrypted_data (str): Decrypted data
        """
        try:
            cipher_suite = Fernet(bytes(key, 'utf-8'))
        except ValueError:
            raise

        try:
            decrypted_data = cipher_suite.decrypt(bytes(data, 'utf-8')).decode("utf-8")
        except InvalidToken:
            print('---Secret key might wrong, please check secret key again---')
            raise

        return decrypted_data

    @staticmethod
    def generate_secret_key() -> str:
        """
        Generate a secret key.
            Params:
                None

            Returns:
                key (str): Secret key
        """
        return Fernet.generate_key().decode('utf-8')


if __name__ == '__main__':
    cipher = Cipher()
    secret_key = cipher.generate_secret_key()
    print(f'secret key: {secret_key}')

    test_string = 'This is a test'
    print(f'before encrypt: {test_string}')

    enc_string = cipher.encrypt(secret_key, test_string)
    print(f'after encrypt: {enc_string}')

    dec_string = cipher.decrypt(key=secret_key, data=enc_string)
    print(f'after decrypt: {dec_string}')
