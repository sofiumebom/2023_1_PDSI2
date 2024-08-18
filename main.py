from fastapi import FastAPI, status, Depends, Response
import classes
import model
from database import engine, get_db
from sqlalchemy.orm import Session
from webscraping import menu_scraping

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "lalalalalalalalala"}

@app.post("/criar", status_code=status.HTTP_201_CREATED)
def criar_valores(nova_mensagem: classes.Mensagem, db: Session = Depends(get_db)):
    mensagem_criada = model.Model_Mensagem(**nova_mensagem.model_dump())
    db.add(mensagem_criada)
    db.commit()
    db.refresh(mensagem_criada)
    return {"Mensagem": mensagem_criada}

@app.post("/menu", status_code=status.HTTP_201_CREATED)
def criar_menu_nav(db: Session = Depends(get_db)):
    menu_items = menu_scraping()
    for item in menu_items:
            new_menu_item = model.Model_Menu(**item.model_dump())
            db.add(new_menu_item)
    db.commit()
    return {"Mensagem": "Scraped!"}

@app.get("/menu", status_code=status.HTTP_200_OK)
def buscar_menu_nav(db: Session = Depends(get_db)):
    menu_items = db.query(model.Model_Menu).all()
    return {"dados": menu_items}
    # return menu_items

@app.get("/quadrado/{num}")
def square(num: int):
     return num ** 3
