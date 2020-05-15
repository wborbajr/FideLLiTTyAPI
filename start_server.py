import uvicorn

from fidellittyapi.bootstrap import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7070, reload=True)
