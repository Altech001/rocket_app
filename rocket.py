from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

async def send_verification_email(email: str, token: str):
    message = MessageSchema(
        subject="Rocket Account Activation",
        recipients=[email],
        body=f"""
        Your Activation code is: {token}
        Please use this 6-digit code to verify your email address.
        Your code will be our reference to all further communication.
        
        If you didn't request this Activation code, please ignore this email.
        """,
        subtype="html"
    )
    
    fm = FastMail(conf)
    await fm.send_message(message)