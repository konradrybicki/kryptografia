# -*- coding: utf-8 -*-

from crypto.symetric import Symetric
from crypto.asymetric import Asymetric

from fastapi import FastAPI


app = FastAPI()


@app.get("/symetric/key")
def read_symmetric_key():
    return {"Generated symetric key: ": Symetric.generateKey()}

@app.post("/symetric/key")
def create_symmetric_key(key: str):
    return key

@app.post("/symetric/encode")
def create_token(message: bytes):
    
    key = Symetric.generateKey()
    token = Symetric.encode(message, key)
    
    return token

@app.post("/symetric/decode")
def create_message(token: bytes):
    
    key = Symetric.generateKey()
    message = Symetric.decode(token, key)
    
    return message

# TODO endpointy dla asymetrycznej