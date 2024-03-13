from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from model import ProdRecommender

app = FastAPI()
templates = Jinja2Templates(directory="templates")

sent_recomm_model = ProdRecommender()


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/predict')
async def predict(request: Request):
    form = await request.form()
    user_name_input = form['username'].lower()
    sent_recomm_output = sent_recomm_model.top5_recommendations(user_name_input)

    if sent_recomm_output:
        return templates.TemplateResponse("index.html", {"request": request, "output": sent_recomm_output})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "message_display": "This User Name doesn't exist. Please provide a valid user name!"})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
