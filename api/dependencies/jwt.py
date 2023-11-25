import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, Header,status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()


SECRET_KEY = "rakBank"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_current_token(authorization: HTTPAuthorizationCredentials = Depends(security)):
    return authorization

def create_access_token(data: dict,):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str = Header(...)):
    token = token.split('Bearer ')[-1]
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        print("Decoded token:", decoded_token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has been expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")