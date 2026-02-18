
from .home import router as home
from .authentication import router as authentication
from .products import router as products

routers = [
    home, authentication, products
]
