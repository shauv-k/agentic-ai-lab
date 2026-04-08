import re
from datetime import datetime
from langchain.tools import tool


@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression and return the result."""
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
}


@tool
def weather(city: str) -> str:
    """Get weather details for a given city."""
    city = city.lower().strip()
    if city in WEATHER:
        d = WEATHER[city]
        return f"{city.title()}: {d['temp']}°C, {d['condition']}, {d['humidity']}%"
    return f"{city} not found"


@tool
def summarize(text: str) -> str:
    """Summarize the given text into 1-2 sentences."""
    parts = re.split(r"[.!?]", text)
    parts = [p.strip() for p in parts if p.strip()]
    if not parts:
        return "No text provided"
    return ". ".join(parts[:2]) + "."


@tool
def greet(_: str = "") -> str:
    """Return a greeting message."""
    return "Hello"


@tool
def date(_: str = "") -> str:
    """Return the current date."""
    return datetime.now().strftime("%Y-%m-%d")


TOOLS = [calculator, weather, summarize, greet, date]