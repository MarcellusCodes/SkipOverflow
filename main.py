from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from utils.server import app
from utils.template import templates
from core.views.landing import landing


