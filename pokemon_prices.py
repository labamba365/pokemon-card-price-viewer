"""
Pokemon card price viewer.

This command‑line tool reads a local JSON dataset of Pokémon card prices
(`cards_data.json`) and allows the user to see the top cards ranked by
various price metrics (low, mid, high, market). The dataset contains
sample pricing data for demonstration purposes. In a real application,
you would likely fetch up‑to‑date prices from an external API such as
the Pokémon TCG API (https://docs.pokemontcg.io/) or another price
service. However, external API calls are restricted in this
environment, so the data is baked into a local file instead.

Usage:
    $ python3 pokemon_prices.py

Follow the prompts to choose which price metric to rank by. The top
ten cards for the selected metric will be printed to the console.
"""

import json
import os
from typing import List, Dict

DATA_FILE = os.path.join(os.path.dirname(__file__), "cards_data.json")


def load_card_data() -> List[Dict[str, float]]:
    """Load the card data from the JSON file.

    Returns:
        A list of dictionaries with card information.
    """
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_top_cards(cards: List[Dict[str, float]], metric: str, top_n: int = 10) -> List[Dict[str, float]]:
    """
    Sort the list of cards by the specified price metric and return the top N.

    Args:
        cards: List of card dictionaries.
        metric: The price metric to sort by (one of "low", "mid", "high", "market").
        top_n: Number of top results to return.

    Returns:
        A list of the top N cards sorted by the chosen metric (descending order).
    """
    if metric not in {"low", "mid", "high", "market"}:
        raise ValueError(f"Invalid metric: {metric}. Must be one of low, mid, high, market.")
    sorted_cards = sorted(cards, key=lambda card: card.get(metric, 0), reverse=True)
    return sorted_cards[:top_n]


def print_cards(cards: List[Dict[str, float]], metric: str) -> None:
    """Print the card data in a tabular format."""
    print(f"\nTop {len(cards)} cards by {metric} price:\n")
    print(f"{'Rank':<5}{'Name':<15}{'Low':>10}{'Mid':>10}{'High':>10}{'Market':>10}")
    print("-" * 60)
    for idx, card in enumerate(cards, 1):
        print(
            f"{idx:<5}{card['name']:<15}{card['low']:>10.2f}{card['mid']:>10.2f}{card['high']:>10.2f}{card['market']:>10.2f}"
        )


def main() -> None:
    cards = load_card_data()
    print("Welcome to the Pokémon Card Price Viewer!")
    print("We have a local dataset of Pokémon card prices. Choose a price metric to see the top cards.")
    while True:
        print("\nAvailable price metrics: low, mid, high, market")
        metric = input("Enter a metric to sort by (or type 'quit' to exit): ").strip().lower()
        if metric in {"quit", "exit"}:
            print("Goodbye!")
            break
        if metric not in {"low", "mid", "high", "market"}:
            print("Invalid choice. Please choose one of the available metrics.")
            continue
        try:
            top_cards = get_top_cards(cards, metric)
        except ValueError as e:
            print(e)
            continue
        print_cards(top_cards, metric)


if __name__ == "__main__":
    main()
