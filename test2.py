#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage


# Assuming you have a state instance and you are using FileStorage
state = State(name="California")
# Save the state to storage
state.save()

# Assuming you have City instances related to this state
city1 = City(name="Los Angeles", state_id=state.id)
city2 = City(name="San Francisco", state_id=state.id)
# Save the cities to storage
city1.save()
city2.save()

# Access the cities property
print(state.cities)  # This should print [city1, city2]


