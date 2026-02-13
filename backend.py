import random
import smtplib
from email.mime.text import MIMEText

class AuthBackend:

    generated_otp = None
    email = None

    sender_email = 'sihhackara@gmail.com'
    app_password = 'wnax xnkk zzez ahbb'

    @staticmethod
    def send_otp(email):

        AuthBackend.email = email
        AuthBackend.generated_otp = str(random.randint(1000,9999))

        subject = "TRACKH2O Verification OTP"
        body = f"Your OTP is: {AuthBackend.generated_otp}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = AuthBackend.sender_email
        msg['To'] = email

        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(AuthBackend.sender_email, AuthBackend.app_password)
            server.sendmail(AuthBackend.sender_email, email, msg.as_string())
            server.quit()

            print("OTP Sent to Email")

        except Exception as e:
            print("Email Failed:", e)


    @staticmethod
    def verify_otp(user_otp):
        return user_otp == AuthBackend.generated_otp
