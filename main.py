from fastapi import FastAPI
from api.routes import user, weather, recommendations
from db.database import engine
from db.models import Base
import uvicorn

# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
Base.metadata.create_all(bind=engine)


app.include_router(user.router, prefix="/user", tags=["users"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])
app.include_router(
    recommendations.router, prefix="/recommendation", tags=["recommendation"]
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
