"""Main module for showcasing the use of secure configrable with FastAPI"""

import config  # pylint: disable=unused-import

import uvicorn
from fastapi import FastAPI
from secure_configurable import secure_headers

app = FastAPI()


@app.middleware("http")
async def set_secure_headers(request, call_next):
    """Set the headers to enhance security"""
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


@app.get("/")
async def root():
    """Response for the get request for the root route"""
    return {"message": "Secure"}


if __name__ == "__main__":
    uvicorn.run(app, port=8081, host="localhost", server_header=False)
