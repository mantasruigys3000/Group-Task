"""
Title: Application to add records to a password file
Author: Unknown - Edited by Group
Date: 18-02-2019

Note:
Format for username and passwords file
username:password:salt
username2:password2:salt
"""

import hashlib
import random


def get_valid_username(cred_dict):
    """
    Prompt user for username, checking that a record doesn't already exist
    :param cred_dict: the existing credentials dictionary
    :return: the username
    """
    prompt_string = "Enter the desired username: "
    user_name = input(prompt_string)

    while not user_name:
        print("Username cannot be empty.")
        user_name = input(prompt_string)

    while user_name in cred_dict.keys():
        print("Username already exists.")
        user_name = input(prompt_string)

    return user_name


def get_valid_password():
    """
    Prompt the user for a password, does not accept blank passwords
    Will ask the user to re-enter the password for verification
    :return: Password after validation
    """
    valid_password = False

    while not valid_password:
        password_orig = input("Password: ")
        # ensure no blank passwords
        while not password_orig:
            password_orig = input("Password: ")

        # validate password
        password_check = input("Re-enter password: ")
        while password_orig != password_check and not password_check == "0":
            print("Passwords do not match. Type 0 to enter a new password.")
            password_check = input("Re-enter password: ")

            if password_orig == password_check:
                valid_password = True

    return password_orig


def hash_password(pwd):
    """
    :param pwd: the plaintext password
    :return: tuple of (hashed password, salt)
    """

    salt = random.randint(1000, 1000000)
    hashed_password = hashlib.sha512(pwd + salt).hexdigest()

    return tuple(hashed_password, salt)


def credentials_to_dictionary(file_path):
    """
    Reads credentials from file then stores them in a dictionary
    Assumes that the format for each line is
    username:password:salt
    :param file_path: path to credentials file
    :return: the dictionary containing credentials and salt
    """
    credential_dict = {}

    try:
        with open(file_path, "r") as file:
            for line in file:
                values = line.split(":")
                credential_dict[values[0]] = tuple(values[1], values[2])
    except OSError as e:
        print("Error: ".format(e))
        print("Could not read from file: {}".format(file_path))
        pass

    return credential_dict


def output_credentials(file_path, credentials_dict):
    """
    Open file and output credentials
    :param file_path: path for credentials file
    :param credentials_dict: the dictionary of user,pass and salt values in memory
    """
    # open file and output credentials
    try:
        with open(file_path, "w") as f:
            for key, value in credentials_dict.items():
                f.write("{}:{}:{}".format(key, value[0], value[1]))
    except OSError as e:
        print("Error: ".format(e))
        print("Could not write to file: {}".format(file_path))
        pass


def add_to_dictionary(cred_dict, user, pwd, salt):
    """
    Simply adds the values to the dictionary, no return only side effects

    :param cred_dict: the dictionary
    :param user: username
    :param pwd: hashed password
    :param salt: the salt
    """
    cred_dict[user] = tuple(pwd, salt)


# open and store password file
password_file_path = input("Enter the filename where the credentials are stored: ")
credentials_dictionary = credentials_to_dictionary(password_file_path)

# prompt user for credentials
username = get_valid_username(credentials_dictionary)
password_and_salt = hash_password(get_valid_password())

# add new credentials to dictionary and output
add_to_dictionary(credentials_dictionary, username, password_and_salt[0], password_and_salt[1])
output_credentials(password_file_path, credentials_dictionary)
