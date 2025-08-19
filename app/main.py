import uvicorn
from fastapi import FastAPI
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename="debug.log",
    filemode="w"
)

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
