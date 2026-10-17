# AI Travel Planning System using LangGraph Results

## Landing_gage
![alt text](Landing_gage.PNG)

## Prompt
![alt text](Prompt.PNG)

## Agent_pipeline
![alt text](Agent_pipeline.PNG)

## Hotel_agent
![alt text](Hotel_agent.PNG)

## Itinery_agent
![alt text](Itenery_agent.PNG)

## Final_agent
![alt text](Final_agent.PNG)

## Download_final_plane
![alt text](Download_final_plane.PNG)


# AI Travel Planning System using LangGraph

A multi-agent travel planning application built with LangGraph, Groq, and Tavily. The system takes a user travel request, gathers flight and hotel information, generates an itinerary, and presents a final travel plan through a Streamlit interface.

## Overview

This project demonstrates a simple LangGraph workflow with four stages:

1. Flight agent searches for flight-related information
2. Hotel agent searches for lodging options
3. Itinerary agent creates a travel plan
4. Final agent composes the final response for the user

The app also stores memory in PostgreSQL using LangGraph's checkpointing support.

## Features

- ✈️ Flight-search agent
- 🏨 Hotel-search agent
- 🗓️ Itinerary generation using LLM
- 🤖 Final travel response synthesis
- 🧠 PostgreSQL memory/checkpoint support
- 🌐 Streamlit web UI
- 🔎 Real-time web search via Tavily

## Tech Stack

- Python
- LangGraph
- LangChain
- Groq
- Tavily API
- PostgreSQL
- Streamlit

## Project Structure

```text
.
├── main.py
├── frontend.py
├── tools/
│   ├── flight_tool.py
│   └── tavily_tool.py
├── travel_plans/
├── .env
├── README.md
└── requirements.txt (optional, if added later)
```

## Prerequisites

- Python 3.10+
- PostgreSQL installed and running
- Groq API key
- Tavily API key

## 1) Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

## 2) Install dependencies

```bash
pip install langgraph langchain langchain-groq langchain-community langchain-core python-dotenv streamlit tavily-python psycopg[binary,pool] langgraph-checkpoint-postgres
```

If you prefer a more explicit install for PostgreSQL support:

```bash
pip install "psycopg[binary,pool]"
pip install langgraph-checkpoint-postgres
```

## 3) Install and start PostgreSQL

Download PostgreSQL from: https://www.postgresql.org/download/

After installation, create a database:

```sql
CREATE DATABASE langgraph_memory_demo;
```

## 4) Create a .env file

Create a file named `.env` in the project root with the following values:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/langgraph_memory_demo
```

> Update the password and port to match your local PostgreSQL setup.

## 5) Get API keys

- Groq: https://console.groq.com
- Tavily: https://www.tavily.com/

## 6) Run the app

### Terminal mode

```bash
python main.py
```

This runs the LangGraph workflow in the terminal and prints the final travel response.

### Streamlit app

```bash
streamlit run frontend.py
```

This launches the web interface for creating travel requests.

## Example prompts

```text
Plan a 7-day trip to Japan with flights, hotels, and sightseeing under 2 lakhs.

Create a 5-day trip to Bali including flights and budget-friendly hotels.

Plan a weekend vacation to Dubai with flights and luxury stays.
```

## How the workflow works

- The user enters a travel query
- `flight_agent` searches flight information
- `hotel_agent` searches hotel information
- `itinerary_agent` builds a trip plan using the results
- `final_agent` generates a polished travel response
- PostgreSQL stores checkpoints and conversation memory for the LangGraph state

## Notes

- The current flight tool uses Tavily search results to collect flight-related information.
- The hotel tool also uses Tavily search results.
- The model in `main.py` is configured as `openai/gpt-oss-120b` on Groq, so the Groq API must be valid and accessible.

## Troubleshooting

- If PostgreSQL connection fails, confirm the database exists and the `DATABASE_URL` is correct.
- If the app cannot fetch results, verify your `TAVILY_API_KEY` and `GROQ_API_KEY` values.
- If Streamlit fails to start, ensure the environment is activated and dependencies are installed.

## License

This project is for educational and demonstration purposes.

