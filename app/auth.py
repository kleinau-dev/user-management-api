from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:    
    #bcrypt suporta no máximo 72 bytes
    if len(password.encode('utf-8')) > 72:
        password = password.encode("utf-8")[:72].decode("utf-8", erros="ignore")
        
    return pwd_context.hash(password)
