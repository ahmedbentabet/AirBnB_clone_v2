#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.engine.file_storage import FileStorage

new_state = State(name="taza")
print(new_state.to_dict())
print(new_state)