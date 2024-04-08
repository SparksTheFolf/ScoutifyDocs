"""
tbaEvents - Opensource multithreaded event scraper for The Blue Alliance

# TBA Multithreaded Data Puller
# Copyright 2024 Nolan Trapp (STF)


"""

__version__ = "0.1.0"

import json
import os
import requests

# Global TBA API key
API_KEY = ""

def fetch_match_data(year, event_code, match_keys):
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