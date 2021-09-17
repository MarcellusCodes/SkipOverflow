from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from utils.server import app
from utils.template import templates
from core.views.landing import landing

app.mount("/static", StaticFiles(directory="static"), name="static")


