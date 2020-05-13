from mongoengine import StringField, FloatField, EmbeddedDocument


class Manufacter(EmbeddedDocument):
    name = StringField(required=True)
    price = FloatField(required=True)
