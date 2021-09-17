from fastapi import Request
from utils.server import app
from utils.template import templates


@app.get("/")
async def landing(request: Request):
    return templates.TemplateResponse('landing.html', context={'request': request})