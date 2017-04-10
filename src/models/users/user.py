import uuid
from src.common.database import Database
import src.models.users.errors as UserErrors
from src.common.utils import Utils


class User(object):
    def __init__(self,email,password,_id=None):
        self.email=email
        self.password=password
        self._id= uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email,password):
        '''
        To verify if the email and associated password are valid
        :param email: user's email
        :param password: sha512 hashed password
        :return: True if valid False otherwise
        '''
        user_data = Database.find_one("users",{'email':email})
        if user_data is None:
            #Tell user that email does not exist
            raise UserErrors.UserNotExistError("The user does not exist")

        if not Utils.check_hashed_password(password,user_data['password']):
            #Tell user that their password is wrong
            raise UserErrors.IncorrectPasswordError ("Your Password is wrong")

        return True

    @staticmethod
    def register_user(email,password):
        user_data = Database.find_one("users", {'email': email})
        if user_data is not None:
            # Tell user that email already exist & can not register
            raise UserErrors.UserAlreadyRegisteredError("The email is already registered")

        if not Utils.email_is_valid(email):
            #Tell user that their e-mail is not constructed properly
            raise UserErrors.InvalidEmailError("The email is not in the right format")

        User(email,Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert("users",self.json())

    def json(self):
        return {
            "_id":self._id,
            "email":self.email,
            "password":self.password
        }