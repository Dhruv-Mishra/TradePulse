from pydantic import BaseModel

class Order(BaseModel):
    id: int = 0
    date: str = ""
    symbol: str = ""
    security: str = ""
    client: str = ""
    action: str = ""
    quantity: int = 0
    price: float = 0.0
    remarks: str = ""