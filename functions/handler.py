# functions/handler.py
import serverless_wsgi
from app import app as flask_app # Import your Flask app instance

def handler(event, context):
  """
  This function is the serverless handler.
  It wraps the Flask app with serverless_wsgi to handle the request.
  """
  return serverless_wsgi.handle(flask_app, event, context)