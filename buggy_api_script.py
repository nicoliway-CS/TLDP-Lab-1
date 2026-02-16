"""
Lab 1 — Part 2 Starter (BUGGY ON PURPOSE)
API: Cat Facts — https://catfact.ninja/
Goal: Fetch ONE cat fact and save it to data/cat_fact.txt

❗ Your job: run this script, read the error(s), consult the docs linked above,
fix the bugs, and add brief comments explaining each fix.

Hints:
- Check the endpoint path (facts vs. fact)
- Verify keys in the JSON payload
- Ensure timeouts and types are correct
- Make sure files/directories exist before writing
- Double‑check typos in file names and variables
"""


import requests #changed it from json to requests

#wrong endpoint, this one returns a random fact instead of a list of facts
API_URL = "https://catfact.ninja/fact"  

def get_cat_fact():
    """Fetch a single cat fact string from the API and return it."""
    
    resp = requests.get(API_URL, timeout=5)  #changed the timeout from a string to an integer
    data = resp.json()

    fact = data["fact"]

    return fact

def save_fact_to_file(text):
    """Save the provided text to data/cat_fact.txt"""
    out_path = "data/cat_fact.txt"
    #created the data folder
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Saved to cat_fact.txt")  #added the extra t to make txt

def main():
    fact = get_cat_fact()
    #added 2 extra conditionals in the if statement
    if fact and isinstance(fact, str) and fact != None and len(fact) != 0:
        save_fact_to_file(fact)
    else:
        print("No fact fetched. Check API response structure.")

if __name__ == "__main__":
    main()
