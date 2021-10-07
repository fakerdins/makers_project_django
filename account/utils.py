from django.core.mail import send_mail

def send_activation_code(email, activation_code):
    message = f"""
    activation code is: {activation_code}
    """
    send_mail(
        'Account activation',
        message,
        'test@gmail.com',
        [email]
    )
