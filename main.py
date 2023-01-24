from typing import List
from fastapi import FastAPI, Header, HTTPException
from magnum import Magnum
from functools import wraps

app = FastAPI()
magnum = Magnum(tenant_id="your_tenant_id", client_id="your_client_id", client_secret="your_client_secret")

def role_validation(roles:List[str]):
    def auth_decorator(func):
        @wraps(func)
        async def wrapper(authorization: str = Header(None), *args, **kwargs):
            is_valid = await magnum.validate_jwt_token(authorization, roles)
            if is_valid:
                return await func(*args, **kwargs)
            else:
                raise HTTPException(status_code=401, detail="Not authorized")
        return wrapper
    return auth_decorator

@app.get("/admin")
@role_validation(["admin"])
async def admin_endpoint():
    return {"message": "Admin endpoint accessed"}

@app.get("/user")
@role_validation(["user"])
async def user_endpoint():
    return {"message": "User endpoint accessed"}