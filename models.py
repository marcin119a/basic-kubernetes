from pydantic import BaseModel


class PricePrediction(BaseModel):
    area_m2: float
    rooms: int
    photos: int
    locality: str
    street: str
    property_type: str
    city: str
    price: float