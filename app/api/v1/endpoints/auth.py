from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.schemas.token import Token, RefreshTokenRequest
from app.services.auth_service import register_user, authenticate_user, generate_tokens, get_current_user
from app.core.security import decode_token, create_access_token, create_refresh_token
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/auth", tags=["Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user_dep(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return get_current_user(db, token)

@router.post("/register", response_model=UserResponse, status_code=201)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user_data)

@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_data.email, user_data.password)
    return generate_tokens(user)

@router.post("/refresh", response_model=Token)
def refresh(body: RefreshTokenRequest, db: Session = Depends(get_db)):
    payload = decode_token(body.refresh_token)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token inválido")
    user = get_current_user(db, body.refresh_token)
    return generate_tokens(user)

@router.get("/me", response_model=UserResponse)
def me(current_user=Depends(get_current_user_dep)):
    return current_user