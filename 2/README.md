# Assignment 2: Tool-Using Agent

## Objective

Extend the rule-based agent by introducing **modular tools**.
The agent should decide which tool to use based on user input, execute it, and return the result.

---

## Approach

### Tool-Based Design

Instead of directly handling logic inside the agent, functionality is separated into **independent tools**:

* Each tool performs a specific task
* The agent only decides **which tool to call** and **what input to pass**

---

### Decision Logic

* The agent uses **keyword-based routing**
* It maps user queries to:

  * a tool name
  * an input argument
* This replaces direct action execution from Assignment 1

---

### Execution Pipeline

```
User Input
   ↓
Decision Logic (select tool)
   ↓
Extract arguments
   ↓
Call tool function
   ↓
Return result
```

---

## Files

### `tools.py`

Contains all tool implementations:

* `calculator` → evaluates arithmetic expressions
* `get_weather` → returns mocked weather data
* `summarize` → extracts first 1–2 sentences
* `greet` → handles greetings
* `get_date` → returns current system date

Also includes:

* `TOOLS` dictionary mapping tool names to functions

---

### `agent.ipynb`

#### Key Components

**1. Decision Function**

* Uses keyword matching
* Returns:

  * tool name
  * input argument

**2. Agent Function**

* Calls decision function
* Looks up tool in `TOOLS`
* Executes the tool
* Returns result

**3. Execution Cell**

* Takes user input
* Runs agent
* Displays selected tool and output

---

## Example Usage

```
Input: calculate 10 + 5
Tool: calculator
Output: 10 + 5 = 15
```

```
Input: weather in mumbai
Tool: weather
Output: Mumbai: 30°C, Humid & Hazy, 78% humidity
```

```
Input: hello
Tool: greet
Output: Hello
```

```
Input: what is today's date
Tool: date
Output: 2026-04-07
```

---

## Key Design Choices

* **Modular tools** for clean separation of concerns
* **Tool registry (`TOOLS`)** for scalability
* **Simple rule-based routing** (no AI yet)
* **Reusable structure** for future assignments

---

## Learning Outcomes

* Tool abstraction and modular programming
* Function-based architecture
* Input parsing and routing
* Preparing systems for LLM integration

---

## Summary

The agent evolves from a direct rule-based system into a **tool-driven architecture**, enabling better modularity, scalability, and preparation for LLM-based decision making in the next assignment.
