

from jose import jwt, JWTError
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta



load_dotenv()
secretkey = os.getenv("secretkey")
algorithm = os.getenv("algorithm")
token_access_time = int(os.getenv("token_access_time"))

def create_token(user_id: int) -> str:
    now = datetime.utcnow()
    expire = now + timedelta(minutes=token_access_time)
    
    data = {
        "sub": str(user_id), 
        "exp": int(expire.timestamp()),
        }
    
    token = jwt.encode(data, secretkey, algorithm=algorithm)
    return token

def decode_token(token: str) -> str:
    data = jwt.decode(token, secretkey, algorithms=[algorithm])
    user_id = data.get("sub")
    if not user_id:
        raise JWTError("No sub")
    return user_id
