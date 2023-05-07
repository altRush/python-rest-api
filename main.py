from fastapi import FastAPI, Path

app = FastAPI()

allEvents = [{
    "id":          1,
    "title":       "Introduction to Python",
    "description": "Come join us for a chance to learn how Python and FastAPI work and get to eventually try it out.",
}, {
    "id":          2,
    "title":       "Introduction to Python again",
    "description": "Come join us for a chance to learn how Python and FastAPI work and get to eventually try it out again.",
}]


@app.get("/")
def read_root():
    return "Hello world"


@app.get("/event/{id}")
def getEventById(id: int = Path(..., description="ID of the event"), gt=0):
    for event in allEvents:
        if event["id"] == id:
            return event
    return "No match event by specified ID found"


@app.get("/get-by-title")
def getEventByTitle(title: str):
    for event in allEvents:
        if event["title"] == title:
            return event
    return "No match event by specified title found"
