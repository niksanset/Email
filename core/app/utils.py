import smtplib
from email.mime.text import MIMEText
from django.conf import settings



def send_password_reset_emails(users_emails, reset_links):

    smtp_server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    smtp_server.starttls()  # Включение шифрования TLS
    smtp_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)


    for email, reset_link in zip(users_emails, reset_links):
        msg = MIMEText(f"Для сброса пароля перейдите по ссылке: {reset_link}")
        msg['Subject'] = 'Сброс пароля'
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = email
        smtp_server.send_message(msg)

 
    smtp_server.quit()
    
    
users_emails = ['user1@example.com', 'user2@example.com']
reset_links = ['http://example.com/reset/1', 'http://example.com/reset/2']
send_password_reset_emails(users_emails, reset_links)