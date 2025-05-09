from utils.db import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Fail_Machine

class FailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Fail_Machine