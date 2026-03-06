from pydantic import BaseModel


class ProductDTO(BaseModel):
    id: int
    title: str
    price: int
