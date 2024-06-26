import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')
