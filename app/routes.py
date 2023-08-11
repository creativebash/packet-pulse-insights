from fastapi import APIRouter, Request, WebSocket
from fastapi.templating import Jinja2Templates
from app.model import Model

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

interface = "Wi-Fi"

# instantiate the class model and pass in the interface to sniff.
model = Model()
model.capture_packets(interface=interface)
events = model.siem_events or model.sample_events
chart_html = model.plotly_chart()

# Webpages routes

# Webpages routes
@router.get("/chart")
async def get_chart(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "captured_events": events, "plotly_chart": chart_html},
    )

@router.get("/get_new_data")
async def get_new_data():
    # Generate and return new data for the live updates
    model.capture_packets(interface=interface)
    new_data = model.get_events_type_data()
    new_x_data = new_data["x_data"]
    new_y_data = new_data["y_data"]
    return {"x_data": new_x_data, "y_data": new_y_data}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

@router.get("/web/events")
def get_events(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "captured_events": events, "plotly_chart": chart_html},
    )

# API routes
@router.get("/")
def read_root():
    return model.welcomeMsg

@router.get("/events/")
def get_events():
    return model.sample_events

# You can add more API endpoints to handle data retrieval and event correlation logic here...