#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.engine.file_storage import FileStorage

my_model3 = State()
my_model4 = State()
# storage.delete(my_model)

print(storage.all(State))
print(storage.all())

# my_model1 = BaseModel()
# my_model2 = BaseModel()
# my_model.name = "My First Model"
# my_model.my_number = 89
# print(my_model)

# my_model1.save()
# print(storage.all())
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))