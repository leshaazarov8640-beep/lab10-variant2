from fastapi import FastAPI
import httpx

app = FastAPI()

GO_SERVICE_URL = "http://localhost:8080/target"

@app.get("/ping")
async def ping():
    """Простой эндпоинт для проверки работоспособности Python-сервиса"""
    return {"message": "pong from Python"}

@app.get("/call-go")
async def call_go_service():
    """
    Задание №4: FastAPI-сервис, который вызывает Go-сервис через HTTP.
    Мы идем по адресу localhost:8080/target, забираем данные и отдаем их пользователю.
    """
    async with httpx.AsyncClient() as client:
        try:
    
            response = await client.get(GO_SERVICE_URL)

            response.raise_for_status()

            go_data = response.json()
            
            return {
                "status": "Success",
                "message": "FastAPI successfully reached Go service",
                "data_from_go": go_data
            }
        except httpx.HTTPError as e:
            
            return {
                "status": "Error",
                "message": f"Could not connect to Go service: {str(e)}"
            }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
