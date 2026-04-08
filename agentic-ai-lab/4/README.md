# Agentic AI Lab – Day 4: Multi-Step Agent (Planning)

## Overview

This assignment implements a **multi-step AI agent** capable of solving complex tasks by breaking them into smaller steps, executing them sequentially, and using external tools when required.

The agent is built using:

* **LangChain (v1.x)**
* **Ollama (local LLM – llama3.2:3b)**
* A custom **ReAct-style reasoning loop**

---

## Objective

To design an agent that can:

* Decompose tasks into multiple steps
* Use tools dynamically
* Execute steps sequentially
* Provide intermediate outputs
* Produce a final answer based on observations

---

## Tools Implemented (`tools.py`)

The agent uses the following tools:

1. **Calculator**

   * Evaluates mathematical expressions
2. **Weather**

   * Returns mock weather data for cities
3. **Summarizer**

   * Generates short summaries of text
4. **Greet**

   * Returns a greeting message
5. **Date**

   * Returns current date

---

## Agent Design

### Architecture

The agent follows a **ReAct (Reasoning + Acting)** pattern:

```
User Input → Thought → Action → Observation → Repeat → Final Answer
```

### Key Components

* **LLM (Ollama)**

  * Model: `llama3.2:3b`
  * Runs locally (no API required)

* **Custom Agent Loop**

  * Handles:

    * Planning
    * Tool selection
    * Execution
    * Context memory

* **Tool Mapping**

  * Dynamically selects and executes tools

---

## Why Custom Agent (Important)

LangChain 1.x requires models that support **tool binding** (`.bind_tools()`).

However:

* Ollama local models **do not support tool binding**

Therefore:

* A **manual ReAct loop** is implemented instead of using:

  * `create_agent`
  * `AgentExecutor`

---

## Workflow

1. User enters a query
2. Agent generates a **Thought**
3. Agent selects a **Tool (Action)**
4. Tool executes and returns **Observation**
5. Observation is fed back into the agent
6. Steps repeat until final answer is produced

---

## Example

### Input

```
Find the average of 5, 10, 15 and summarize the result
```

### Execution Flow

```
Thought: Calculate average
Action: calculator
Action Input: (5+10+15)/3

Observation: 10

Thought: Summarize result
Action: summarize
Action Input: The average is 10

Observation: The average is 10.

Final Answer: The average is 10.
```

