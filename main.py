from fastapi import FastAPI, HTTPException
from mockData import product
from pydantic import BaseModel
class Patient(BaseModel):
    name:str
    age:int

app = FastAPI()
patient_info={'name':'nitish','age':30}
patient1=Patient(**patient_info)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/products")
def get_products():
    return product

##path params
@app.get("/product/{product_id}") 
def get_one_product(product_id:int):
    ##if prod available with id return prod id , else return error message
    for oneProduct in product:
        if oneProduct.get("id")==product_id:
            return oneProduct       
    return{
        "error":"prod not found"
    }

##query params

@app.get("/greet")
def greet_user(name:str):
    return {
        "greet":f"hello {name}?"
    }

##different types of HTTP methods

@app.post("/create_product")
def create_product():
    return{"status":"prod_created_successfully!"}
##how to validate data-DTOS data transfer object
##how to call diff HTTP methods-tool