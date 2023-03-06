import uvicorn
from app import *
from routers import *
from swagger import *

import os

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=int(os.getenv('WEB_PORT'))
    )