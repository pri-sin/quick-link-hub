# functions/handler.py
import serverless_wsgi
from app import app as flask_app

def handler(event, context):
  return serverless_wsgi.handle(flask_app, event, context)