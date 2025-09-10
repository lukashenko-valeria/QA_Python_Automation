import fakers

def generate_user_data():
    return {
        'email': fakers.generated_email(),
        'password': fakers.generated_password(),
        'name': fakers.generated_login()
    }
