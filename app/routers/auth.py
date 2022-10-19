from telnetlib import AUTHENTICATION
from fastapi import APIRouter, Depends,status, HTTPException
from sqlalchemy.orm import Session
from .. import models,schemas,utils,database,oauth2
from fastapi.security import OAuth2PasswordRequestForm

router= APIRouter(
    tags=['AUTHENTICATION']
)

@router.post('/login',response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credetials')
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credetials')
#create a token
    access_token= oauth2.create_access_token(data={"user_id":user.id})
#return a token
    return {"access_token":access_token,"token_type":"bearer"}



