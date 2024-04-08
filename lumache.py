"""
Module to fetch match data from The Blue Alliance API.

This module provides functions to fetch match data for specific events
from The Blue Alliance API and store it locally.

Author: Nolan Trapp (nolantrapp.com)

Usage:
    - Ensure you have a valid TBA API key set in the global variable API_KEY.
    - Use fetch_match_data() function to fetch match data for a specific event.

Example:
    $ python fetch_match_data.py

Attributes:
    API_KEY (str): The global TBA API key for authentication.

Functions:
    fetch_match_data(year, event_code, match_keys):
        Fetches match data for a specific event and stores it locally.
    main():
        Main function to fetch match data for all events listed in events.json.
"""

import json
import os
import requests

API_KEY = ""  # Set your TBA API key here

def fetch_match_data(year, event_code, match_keys):
    """
    Fetch match data for a specific event and store it locally.

    Args:
        year (str): The year of the event.
        event_code (str): The code of the event.
        match_keys (list): List of match keys for the event.

    Returns:
        None

    Raises:
        None
    """
    event_folder = os.path.join("../matches", year, event_code)
    os.makedirs(event_folder, exist_ok=True)

    total_matches = len(match_keys)
    matches_done = 0

    for match_key in match_keys:
        match_url = f"https://www.thebluealliance.com/api/v3/match/{match_key}"
        headers = {'X-TBA-Auth-Key': API_KEY}

        response = requests.get(match_url, headers=headers)
        if response.status_code == 200:
            match_data = response.json()

            with open(os.path.join(event_folder, f"{match_key}.json"), "w") as file:
                json.dump(match_data, file, indent=4)

            matches_done += 1
            percentage_done = (matches_done / total_matches) * 100
            print(f"Fetching match data for event {event_code}: {percentage_done:.2f}% done", end="\r")
        else:
            print(f"Failed to fetch match data for {match_key}")

    print(f"Fetching match data for event {event_code}: 100% done")
    print(f"Done fetching match data for event {event_code}")

def main():
    """
    Main function to fetch match data for all events listed in events.json.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    with open("events.json", "r") as file:
        events = json.load(file)

    for event_code in events:
        year = event_code[:4]  # Extract year from event code
        match_keys_url = f"https://www.thebluealliance.com/api/v3/event/{event_code}/matches/keys"
        headers = {'X-TBA-Auth-Key': API_KEY}

        response = requests.get(match_keys_url, headers=headers)
        if response.status_code == 200:
            match_keys = response.json()
            fetch_match_data(year, event_code, match_keys)
        else:
            print(f"Failed to fetch match keys for event {event_code}")

    print("Done fetching match data for all events")

if __name__ == "__main__":
    main()
