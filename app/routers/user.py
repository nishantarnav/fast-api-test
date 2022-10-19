
from sqlalchemy.orm import Session
from fastapi import status,HTTPException,Depends,APIRouter
from .. import models,schemas,utils,database

router= APIRouter(
    prefix='/users',
    tags= ['Users']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:Session=Depends(database.get_db)):

    #hash the password first
    hashed_pw= utils.hash(user.password)
    user.password=hashed_pw
    new_user=models.User(**user.dict()) #unpacking post
    db.add(new_user)
    db.commit()
    db.refresh(new_user) #alteranate to returning sql
    return new_user

@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id:int,db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The users with id :{id} was not found')
        
    return user 

