import uvicorn
from fastapi import FastAPI, Depends
from notes import models, schemas
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=models.engine)


def get_db():
    db = models.MySession()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello, there!'}


@app.post('/note/create')
def note_create(request: schemas.Note, db: Session = Depends(get_db)):
     new_note = models.Note(title=request.title, body=request.body)
     db.add(new_note)
     db.commit()
     db.refresh(new_note)
     
     return new_note
 
 
@app.get('/note/list')
def note_list(db: Session = Depends(get_db)):
    all_notes = db.query(models.Note).all()
    return all_notes
    
    
@app.get('/note/{id}')
def note_details(id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == id).first()
    return note
     


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
