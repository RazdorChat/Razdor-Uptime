from sanic import *
from sanic.response import text, json
from sanic_jinja2 import SanicJinja2
from jinja2 import FileSystemLoader
from datetime import datetime
import time
from funcs import *
import os
import json as json_read # rename to avoid conflicts with sanic json

config = json_read.load(open("config.json", "r"))
WEB_URL = config["WEB"]
API_URL = config["API"]
WS_URL = config["WS"]

app = Sanic(__name__)

# Load html and css files
app.static("static", os.path.abspath('../static'))
template_dir = "../template"

# Create jinja object
jinja = SanicJinja2(app, pkg_name="main", loader=FileSystemLoader(searchpath=template_dir))

@app.get("/")
def index(request):
    web_status = check_web_service(WEB_URL)
    api_status = check_api_service(API_URL)
    ws_status = check_websocket_service(WS_URL)
    if web_status and api_status and ws_status:
        value = True
    else:
        value = False
    return jinja.render("index.html", request, value=value, web_status = web_status, api_status = api_status, ws_status = ws_status)

@app.get("/web")
async def web_chk(request):
    web_status = check_web_service(WEB_URL)
    timestamp = datetime.now()
    if web_status:
        return json({"SERVICE": "WEB", "STATUS": "ONLINE", "TIMESTAMP": str(time.mktime(timestamp.timetuple()))})
    else:
        return json({"SERVICE": "WEB", "STATUS": "OFFLINE", "TIMESTAMP": str(time.mktime(timestamp.timetuple()))})
    
@app.get("/api")
async def api_chk(request):
    api_status = check_api_service(API_URL)
    timestamp = datetime.now()
    if api_status:
        return json({"SERVICE": "API", "STATUS": "ONLINE", "TIMESTAMP": str(time.mktime(timestamp.timetuple()))})
    else:
        return json({"SERVICE": "API", "STATUS": "OFFLINE", "TIMESTAMP": str(time.mktime(timestamp.timetuple()))})

@app.get("/ws")
async def ws_chk(request):
    ws_status = check_websocket_service(WS_URL)
    timestamp = datetime.now()
    if ws_status:
        return json({"SERVICE": "WS", "STATUS": "ONLINE", "TIMESTAMP": str(time.mktime(timestamp.timetuple()))})
    else:
        return json({"SERVICE": "WS", "STATUS": "OFFLINE", "TIMESTAMP": str(time.mktime(timestamp.timetuple()))})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, access_log=False, debug=False) # Turn debug on for extra output