from fastapi import FastAPI
from backend.domains.api import auth_routes, product_routes, order_routes
from backend.domains.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Ecommerce API")

app.include_router(auth_routes.router)
app.include_router(product_routes.router)
app.include_router(order_routes.router)

