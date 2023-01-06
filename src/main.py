import uvicorn
from fastapi import FastAPI

from configuration import ApiConfig
from rest_api.endpoints import neutralisation_router

app = FastAPI(
    title="Gender Neutralisation",
    description="Simple REST-API to replace gendered language in text "
        "with gender neutral equivalents. This uses a general "
        "purpose large language model, meaning there is a "
        "risk of edits beyond gendered language. It is upto the"
        "user to validate the output before distribution or usage",
)
app.include_router(neutralisation_router)

if __name__ == '__main__':
    api_config = ApiConfig()
    uvicorn.run("src.main:app", host=api_config.host, port=api_config.port, reload=True)
