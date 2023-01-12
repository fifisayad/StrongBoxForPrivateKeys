import os
import time
import logging


class StrongBox:
    def __init__(self):
        """
        We are going to define items in the class
        """
        self.private_keys = None
        self.password = None
        self.encoded_private_keys = None

    def get_input(self):
        """

        :return: Through this method our private keys and password will be given by user.
        """
        while True:
            private_keys_file_path = str(input("Please Write Your Private Keys File(just .txt file): "))
            # Checking The Existence of File
            if os.path.exists(private_keys_file_path):
                with open(private_keys_file_path, "r") as infile:
                    self.private_keys = infile.read()
                    logging.info("Private Keys is loaded")
                    break
            else:
                logging.error("This file doesn't exist!")
                time.sleep(0.05)
        while True:
            password = str(input("Please Enter Your Password: "))
            confirmation = str(input("Please Enter Your Password again for Confirmation: "))
            if password == confirmation:
                self.password = password
                logging.info("Done! ")
                break
            else:
                logging.error("Your password and Confirmation are not equal")
                time.sleep(0.05)
