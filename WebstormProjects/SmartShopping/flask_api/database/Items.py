from .db import db
from .Manufacters import Manufacter


class Item(db.Document):
    name = db.StringField(required=True)
    manufacters = db.EmbeddedDocumentListField(Manufacter)
