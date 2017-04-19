from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher= re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        '''
        hashes the user input password using pbkdf2_sha512 
        :param password: Password from login/register form 
        :return: sha512 -> pbkdf2_sha512 encrypted password
        '''
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password,hashed_password):
        '''
        To check if the password sent by the user matches that in the database
        :param password: sha512-hashed-password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True id passwords matches else False 
        '''
        return pbkdf2_sha512.verify(password, hashed_password)