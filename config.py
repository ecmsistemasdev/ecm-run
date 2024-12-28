from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '3d6f45a5fc12445dbac2f59c3b6c7cb1')
    MP_ACCESS_TOKEN = os.getenv('APP_USR-4419840842819511-121317-8c522deb54aff8ea290465f557bcdf0b-96531112')
    MP_PUBLIC_KEY = os.getenv('APP_USR-0b9acce0-2c45-48b5-9837-9279769b5e31')