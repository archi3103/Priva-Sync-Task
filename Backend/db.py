from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from fastapi import FastAPI, Depends, HTTPException, APIRouter

from pwdlib import PasswordHash

router = APIRouter()


# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=True)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str

password_hash = PasswordHash.recommended()

# API endpoint to create an item
@router.post("/users/", response_model = UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # db_user = User(**user.dict())
    db_user = User(
        username = user.username,
        email = user.email,
        full_name = user.full_name,
        # hashed_password = user.password,
        hashed_password = password_hash.hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# API endpoint to read an item by ID
@router.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_user