# Assignment 3: LLM-Based Agent

## Objective

Replace rule-based decision logic with an LLM to dynamically select tools and generate appropriate inputs. The agent should interpret user queries, decide which tool to use, execute it, and return the result.

---

## Approach

### LLM for Decision Making

The agent uses a local LLM (via Ollama) to:

* Identify the correct tool
* Extract the required input for that tool

Instead of hardcoded rules, a **structured prompt** is used to guide the model.

---

### Prompt Design

The prompt is tightly constrained to ensure deterministic behavior:

* Explicit list of allowed tools
* Strict output format
* Clear mapping rules
* Few-shot examples

The LLM must return:

```
tool:<tool_name>
input:<value>
```

This avoids ambiguity and ensures reliable parsing.

---

### Tool Execution Pipeline

1. User enters a query
2. LLM selects tool and input
3. Output is parsed
4. Corresponding tool function is executed
5. Result is returned

---

## Files

### `tools.py`

Contains all reusable tools from previous assignments:

* `calculator` → evaluates arithmetic expressions
* `get_weather` → returns mocked weather data
* `summarize` → extracts first 1–2 sentences
* `greet` → handles greetings
* `get_date` → returns current date

Also includes:

* `TOOLS` dictionary mapping tool names to functions

---

### `agent.ipynb`

#### Key Components

**1. LLM Decision Function**

* Sends prompt to Ollama
* Receives structured output
* Extracts:

  * tool name
  * input argument

**2. Agent Function**

* Calls decision function
* Validates tool
* Executes corresponding function from `TOOLS`
* Returns structured response

**3. Execution Cell**

* Takes user input
* Runs agent
* Prints:

  * Input
  * Selected tool
  * Output

---

## Model Used

* Ollama (local runtime)
* Model: `llama3.2:3b`

---

## Key Design Choices

* **Strict output schema** to control LLM behavior
* **Tool registry pattern** for modularity
* **Reusability** by building on previous assignments
* **Local LLM usage** for offline execution

---

## Learning Outcomes

* Prompt engineering for structured outputs
* Integrating LLMs into software pipelines
* Replacing rule-based logic with AI-driven reasoning
* Designing modular agent architectures

---

## Summary

The agent transitions from deterministic logic to LLM-driven decision making while maintaining control through structured prompts and modular design.
