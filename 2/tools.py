import re
from datetime import datetime

def calculator(expression: str) -> str:
    expr = re.sub(r"[^0-9\+\-\*\/\.\(\)\s]", "", expression).strip()
    if not expr:
        return "No valid expression found"
    try:
        return f"{expr} = {eval(expr, {'__builtins__': {}})}"
    except ZeroDivisionError:
        return "Division by zero"
    except Exception:
        return "Calculation error"

WEATHER = {
    "delhi": {"temp": 34, "condition": "Sunny", "humidity": 42},
    "mumbai": {"temp": 30, "condition": "Humid & Hazy", "humidity": 78},
    "bangalore": {"temp": 25, "condition": "Partly Cloudy", "humidity": 65},
    "london": {"temp": 12, "condition": "Rainy", "humidity": 88},
}

def get_weather(city: str) -> str:
    city = city.lower().strip()
    if city in WEATHER:
        d = WEATHER[city]
        return f"{city.title()}: {d['temp']}°C, {d['condition']}, {d['humidity']}%"
    return f"{city} not found"

def summarize(text: str) -> str:
    parts = re.split(r"[.!?]", text)
    parts = [p.strip() for p in parts if p.strip()]
    if not parts:
        return "No text provided"
    return ". ".join(parts[:2]) + "."

def greet(_: str = "") -> str:
    return "Hello"

def get_date(_: str = "") -> str:
    return datetime.now().strftime("%Y-%m-%d")

TOOLS = {
    "calculator": calculator,
    "weather": get_weather,
    "summarize": summarize,
    "greet": greet,
    "date": get_date,
}