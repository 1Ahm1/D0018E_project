from fastapi import FastAPI, APIRouter
app = FastAPI(title="Recipe API", openapi_url="/openapi.json")
user_now=0

# notice: when creating a new router file under /routers folder, add it here

from api.routers import  customer,login,book,product,order,manager

app.include_router(customer.router)
app.include_router(login.router)
app.include_router(book.router)
app.include_router(product.router)
app.include_router(order.router)
app.include_router(manager.router)



##app.include_router(auth.router)


