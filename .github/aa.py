import smtplib
import random
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    sender_email = "salve_sg@mgmcen.ac.in"  # Replace with your Gmail email address
    sender_password = getpass.getpass("Enter your email password: ")

    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())

if __name__ == "__main__":
    recipient_email = input("Enter your email address: ")
    
    otp = generate_otp()
    send_otp_email(recipient_email, otp)
    print(otp)
    print("OTP sent successfully to your email address.")