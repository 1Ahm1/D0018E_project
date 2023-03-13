from pydantic import BaseModel
class CustomerInitData(BaseModel):
    user_id: int
    email: str = None
    phone_number: str = None
    name: str = None
    image_id: str = None
class CreateAccountRequest(BaseModel):
    user_id: int
    email: str = None
    phone_number: str = None
    name: str = None
    image_id: str = None
    password: str
class CreateBookRequest(BaseModel):
    book_id: int
    name: str = None
    author: str = None
    description: str = None
    

class CreateProductRequest(BaseModel):
    product_id: int
    price: int
    quantity: int
    book_id: int
class CreateOrderRequest(BaseModel):
    order_id: int
    price: int
    quantity: int
    product_id: int
    customer_id: int

class CreateManagerRequest(BaseModel):
    user_id: int
    company_permissions: str=None
    