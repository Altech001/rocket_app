from fastapi import FastAPI, BackgroundTasks, Depends, HTTPException
from model import ClientData
from rocket import send_verification_email
import secrets
import random
import jinja2
from pathlib import Path
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
import os


load_dotenv()

# Create templates directory if it doesn't exist
TEMPLATES_DIR = Path("templates")
TEMPLATES_DIR.mkdir(exist_ok=True)

# Setup Jinja2 template environment
template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates')
)

app = FastAPI()

#Email Service depencey

def render_template(template_name: str, **kwargs) -> str:
    template = template_env.get_template(template_name)
    return template.render(**kwargs)


load_dotenv()

# Create templates directory if it doesn't exist
TEMPLATES_DIR = Path("templates")
TEMPLATES_DIR.mkdir(exist_ok=True)

# Setup Jinja2 template environment
template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates')
)

config = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER=str(TEMPLATES_DIR)
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def rocket_code():
    
    # for i in range(2):
    token =random.randint(1000, 9999)
    return token

def rocket_url():
    url_token = f"http://localhost:8000/activate/{secrets.token_hex(16)}"
    return url_token

def render_template(template_name: str, **kwargs) -> str:
    template = template_env.get_template(template_name)
    return template.render(**kwargs)

async def contact_us(email: str, message: str, subject: str = "Rocket Account Activation", token: str = rocket_code(),url_token :str = rocket_url()): # type: ignore
    html_content = render_template(
        "rocket_feed.html",
        message=message,
        token  = token,
        url_token = url_token
    )
    
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=html_content,
        subtype=MessageType.html,
        attachments=[
            {
                "file": "assets/rocket.png",
                "headers": {"Content-ID": "<company_logo>"},
                "mime_type": "image/jpg",
                "mime_subtype": "jpg",
            }
        ]
    )
    
    fm = FastMail(config) # checks for the email send configurations and associated images / info
    await fm.send_message(message)


@app.post("/root")
async def root(client_data: ClientData):
    try:
        await contact_us(client_data.client_email, client_data.client_message)
        return {"message": "Email has been sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


