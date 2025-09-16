from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel

class LoginUser (BaseModel):
    'id' : str 
    'password' : str