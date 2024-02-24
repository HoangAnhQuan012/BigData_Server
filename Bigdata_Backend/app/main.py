import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import Models.models as models
import Routers.users as users
import Routers.ranked_presc as ranked_presc
import Routers.df_city_sel as df_city_sel
import Routers.df_presc_sel as df_presc_sel
import Routers.presc_of_the_city as presc_of_the_city
from config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Thiết lập CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(router=users.router, prefix="/user", tags=["user"])
app.include_router(router=ranked_presc.router, prefix="/ranked_presc", tags=["ranked_presc"])
app.include_router(router=df_city_sel.router, prefix="/df_city_sel", tags=["df_city_sel"])
app.include_router(router=df_presc_sel.router, prefix="/df_presc_sel", tags=["df_presc_sel"])
app.include_router(router=presc_of_the_city.router, prefix="/presc_of_the_city", tags=["presc_of_the_city"])


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

