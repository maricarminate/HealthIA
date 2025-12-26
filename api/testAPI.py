from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get('/pagina')
async def read_page():
    return {"pagina": "Esta é a página de teste da API HealthIA."}

@app.get('/modelo')
async def read_modelo():
    return {"modelo": "Este é o modelo de teste da API HealthIA."}

def main():
    uvicorn.run(app, port = 8000)

if __name__ == "__main__":
    main()