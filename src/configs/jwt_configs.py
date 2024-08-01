import os
from datetime import timedelta

JWT_SECRET = os.getenv('JWT_SECRET', 'your_secret_key')
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION_DELTA = timedelta(hours=1)
