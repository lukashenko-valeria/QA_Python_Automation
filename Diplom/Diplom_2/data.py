import fakers

class Urls:
    burger_url = 'https://stellarburgers.nomoreparties.site/'
    register_user = 'api/auth/register'
    user_info = 'api/auth/user'
    login = 'api/auth/login'
    order = 'api/orders'
    ingredients = 'api/ingredients'

class InvalidUser:
    data = {'password': fakers.generated_password(), 'name': fakers.generated_login()}
    data_2 = {'email': fakers.generated_email(), 'password': fakers.generated_password()}

class Messages:
    SHOULD_BE_AUTHORIZED = 'You should be authorised'
    INTERNAL_SERVER_ERROR = 'Internal Server Error'
    USER_ALREADY_EXISTS = 'User already exists'
    REQUIRED_FIELDS = 'Email, password and name are required fields'
    INCORRECT_CREDENTIALS = 'email or password are incorrect'
