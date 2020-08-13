from django.core.mail import send_mail


def send_activation_email(email, activation_code):
    activation_url = f'http://localhost:8000/v1/account/activate/{activation_code}/'
    message = f'''
        Thank you for signing up. Please activate your account via the following link.
        Activation link: {activation_url}
    '''
    send_mail(
        'Acitvate your account',
        message,
        'test@blog_api.com',
        [email],
        fail_silently=False
    )