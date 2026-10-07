from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from swagger_ui import setup_swagger_ui

app = FastAPI(
    title="API Data Mahasiswa",
    description=(
        "REST API CRUD untuk data mahasiswa (NAMA, ALAMAT, IPK, SEMESTER, HOBI).\n\n"
        "**Informasi:** API ini mendukung operasi CRUD (Create, Read, Update, Delete) dengan status error"
        "standar REST (404/409), serta dokumentasi Swagger UI kustom "
        "(lihat file swagger_ui.py)."
    ),
    version="0.0",
    docs_url=None,
)

# Dokumentasi kustom di /docs (desain ada di file swagger_ui.py)
setup_swagger_ui(app)


# model data
class Item(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    ipk: Optional[float] = None
    semester: Optional[int] = None
    hobi: Optional[str] = None


# simulasi database
items_db = {}

# ROOT
# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}


# CREATE (POST)
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in items_db:
        raise HTTPException(status_code=409, detail="Item already exists")
    items_db[item_id] = item.model_dump()
    return {"message": "Item created successfully", "item": items_db[item_id]}


# READ (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": items_db[item_id]}


# UPDATE (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.model_dump()
    return {"message": "Item updated successfully", "item": items_db[item_id]}


# DELETE (DELETE)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted successfully", "deleted_item": deleted_item}
