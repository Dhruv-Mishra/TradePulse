from pydantic import BaseModel

class Item(BaseModel):
    id: int = 0
    name: str = ""
    description: str = ""
    price: float = 0.0
    tax: float = 0.0
