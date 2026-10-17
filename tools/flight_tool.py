
# Example free API usage
# - AviationStack


# create api key
# https://aviationstack.com/ 
# pip install requests


    
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


def search_flights(query):

    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "limit": 5
    }

    response = requests.get(url, params=params)

    data = response.json()

    flights = []

    if "data" in data:

        for flight in data["data"][:5]:

            airline = flight.get("airline", {}).get("name", "Unknown")

            departure = flight.get(
                "departure", {}
            ).get("airport", "Unknown")

            arrival = flight.get(
                "arrival", {}
            ).get("airport", "Unknown")

            status = flight.get("flight_status", "Unknown")

            flights.append(
                f"""
Airline: {airline}
Departure: {departure}
Arrival: {arrival}
Status: {status}
"""
            )

    return "\n".join(flights)


# import os
# from tavily import TavilyClient
# from dotenv import load_dotenv

# load_dotenv()

# client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# def search_flights(query):
#     try:
#         # Tavily se flights aur ticket prices search karwayein
#         response = client.search(
#             query=f"Flight options, airlines, and ticket prices for {query}",
#             max_results=5
#         )
        
#         flights = []
#         for r in response.get("results", []):
#             title = r.get("title", "Flight Info")
#             snippet = r.get("content", "").strip()
#             # Text ko chota rakhein taake LLM confuse na ho
#             if len(snippet) > 300:
#                 snippet = snippet[:300] + "..."
            
#             flights.append(f"- {title}: {snippet}")
            
#         return "\n".join(flights) if flights else "No flight data found."
        
#     except Exception as e:
#         return f"Flight search failed: {str(e)}"