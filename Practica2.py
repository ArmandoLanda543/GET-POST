from fastapi import FastAPI, File, UploadFile
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

def my_schema():
   openapi_schema = get_openapi(
       title="Practica 1",
       version="1.0",
       description="API con GET y POST",
       routes=app.routes,
   )
   app.openapi_schema = openapi_schema
   return app.openapi_schema

app=FastAPI()

class User(BaseModel):
    PassengerId:int
    Survived:int
    Pclass:int
    Name:str   
    Sex:str
    Age:int

users_list=[User(PassengerId=1, Survived=0, Pclass=3, Name='Braund, Mr. Owen Harris', Sex='male', Age=22),
            User(PassengerId=2, Survived=1, Pclass=1, Name='Cumings, Mrs. John Bradley (Florence Briggs Thayer)', Sex='female',Age=38),
            User(PassengerId=3, Survived=1, Pclass=3, Name= 'Heikkinen, Miss. Laina', Sex='female', Age=26),
            User(PassengerId=4, Survived=1, Pclass=1, Name='Futrelle, Mrs. Jacques Heath (Lily May Peel)', Sex='female', Age=35),
            User(PassengerId=5, Survived=0, Pclass=3, Name='Allen, Mr. William Henry', Sex='male', Age=35),
            User(PassengerId=6, Survived=0, Pclass=3, Name='Moran, Mr. James', Sex='male', Age=0),
            User(PassengerId=7, Survived=0, Pclass=1, Name='McCarthy, Mr. Timothy J', Sex='male', Age=54),
            User(PassengerId=8, Survived=0, Pclass=3, Name='Palsson, Master. Gosta Leonard', Sex='male', Age=2),
            User(PassengerId=9, Survived=1, Pclass=3, Name='Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)', Sex='female', Age=27),
            User(PassengerId=10, Survived=1, Pclass=2, Name='Nasser, Mrs. Nicholas (Adele Achem)', Sex='female', Age=14),
            User(PassengerId=11, Survived=1, Pclass=3, Name='Sandstrom, Miss. Marguerite Rut', Sex='female', Age=4),
            User(PassengerId=12, Survived=1, Pclass=1, Name='Bonnell, Miss. Elizabeth', Sex='female', Age=58),
            User(PassengerId=13, Survived=0, Pclass=3, Name='Saundercock, Mr. William Henry', Sex='male', Age=20),
            User(PassengerId=14, Survived=0, Pclass=3, Name='Andersson, Mr. Anders Johan', Sex='male', Age=39),
            User(PassengerId=15, Survived=0, Pclass=3, Name='Vestrom, Miss. Hulda Amanda Adolfina', Sex='female', Age=14),
            User(PassengerId=16, Survived=1, Pclass=2, Name='Hewlett, Mrs. (Mary D Kingcome)', Sex='male', Age=22),
            User(PassengerId=17, Survived=0, Pclass=3, Name='Rice, Master. Eugene', Sex='male', Age=2),
            User(PassengerId=18, Survived=1, Pclass=2, Name='Williams, Mr. Charles Eugene', Sex='male', Age=0),
            User(PassengerId=19, Survived=0, Pclass=3, Name='Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)', Sex='female', Age=31),
            User(PassengerId=20, Survived=1, Pclass=3, Name='Masselmani, Mrs. Fatima', Sex='female', Age=0),
            User(PassengerId=21, Survived=0, Pclass=2, Name='Fynney, Mr. Joseph J', Sex='male', Age=35),
            User(PassengerId=22, Survived=1, Pclass=2, Name='Beesley, Mr. Lawrence', Sex='male', Age=34),
            User(PassengerId=23, Survived=1, Pclass=3, Name='McGowan, Miss. Anna ""Annie""', Sex='female', Age=15),
            User(PassengerId=24, Survived=1, Pclass=1, Name='Sloper, Mr. William Thompson', Sex='male', Age=28),
            User(PassengerId=25, Survived=0, Pclass=3, Name='Palsson, Miss. Torborg Danira', Sex='female', Age=8)]

@app.get("/MuestraUsuarios")
async def get_users():
    return users_list

###########################################POST##################################################

@app.post("/MuestraUsuarios/")
async def add_user(user:User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerId == user.PassengerId:
            return {"Error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return {"Success": "Usuario agregado"}
        return user