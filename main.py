from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Concert Hall")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/hall", response_class=HTMLResponse)
def hall():
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Схема зала</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background: #0f172a;
            font-family: Arial, sans-serif;
            color: white;
        }
        h1 {
            text-align: center;
        }
        .row {
            display: flex;
            justify-content: center;
            margin-bottom: 10px;
        }
        .seat {
            width: 32px;
            height: 32px;
            margin: 4px;
            background: #22c55e;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 12px;
        }
        .seat.taken {
            background: #6b7280;
        }
    </style>
</head>
<body>

<h1>🎭 Партер</h1>

<div class="row">
    <div class="seat">1</div>
    <div class="seat">2</div>
    <div class="seat">3</div>
    <div class="seat">4</div>
    <div class="seat">5</div>
</div>

<div class="row">
    <div class="seat">6</div>
    <div class="seat taken">7</div>
    <div class="seat">8</div>
    <div class="seat">9</div>
    <div class="seat">10</div>
</div>

</body>
</html>
    """