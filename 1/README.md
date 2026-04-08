# Assignment 1: Rule-Based AI Agent

## Objective

Build a simple AI agent using **rule-based logic**.
The agent should take user input, identify intent using keywords, and perform the corresponding action.

---

## Approach

### Input → Decision → Action Pipeline

The agent follows a structured flow:

```
User Input
   ↓
Decision Logic (intent detection)
   ↓
Action Execution
   ↓
Output
```

---

### Input Handling

* The agent accepts a text query from the user
* Input is normalized (lowercased and stripped)

---

### Decision Logic

* Uses **keyword matching** to identify intent
* Maps input to predefined intents:

  * calculation
  * date
  * greeting

---

### Action Execution

* Based on the detected intent:

  * **Calculator** → evaluates arithmetic expression
  * **Date** → returns current system date
  * **Greeting** → returns a greeting message
* If no intent matches → fallback response

---

## Files

### `agent.ipynb`

#### Key Components

**1. Input Function**

* Captures user input from console

**2. Decision Function**

* Uses conditional checks (`if/elif`)
* Maps input to intent

**3. Action Function**

* Executes logic based on intent

**4. Execution Cell**

* Runs the full pipeline
* Prints final output

---

## Example Usage

```
Input: hello
Output: Hello
```

```
Input: date
Output: 2026-04-07
```

```
Input: calculate 2 + 3 * 4
Output: 14
```

```
Input: random text
Output: Unknown command
```

---

## Key Design Choices

* **Simple rule-based system** (no external dependencies)
* **Clear separation of components**:

  * input
  * decision
  * action
* **Minimal logic** to focus on agent fundamentals

---

## Learning Outcomes

* Understanding basic agent architecture
* Designing input → decision → action pipelines
* Implementing rule-based reasoning
* Structuring code for clarity and modularity

---

## Summary

This assignment introduces the core idea of an AI agent using simple rules.
It establishes the foundation for more advanced agents by clearly separating decision-making from execution.
