# Pokémon Card Price Viewer

This mini‑project demonstrates how to build a simple command‑line tool in Python
that reads data from a local JSON file, sorts it, and displays the results. In
this example, we work with a small dataset of Pokémon trading cards and their
estimated prices. Because outbound internet access is restricted in this
environment, the price data is included as a static file rather than being
fetched in real time from an external API.

## Features

* **Local dataset** – The script reads from `cards_data.json`, which contains
  sample price data (low, mid, high and market values) for a handful of
  popular Pokémon cards.
* **Interactive CLI** – Users are prompted to choose which price metric they’d
  like to sort by (e.g. `market` or `high`). The script then displays the top
  ten cards for that metric in a nicely formatted table.
* **Extensible design** – In a real‑world scenario you could replace the
  static dataset with calls to an API such as the [Pokémon TCG
  API](https://docs.pokemontcg.io/) or another price service. You’d simply
  modify `load_card_data()` to fetch live data instead of reading from a file.

## Running the script

1. Ensure you have Python 3 installed.
2. From the `pokemon_card_prices` directory, run:

   ```bash
   python3 pokemon_prices.py
   ```

3. Follow the on‑screen prompts to select a price metric. Enter `quit` when
   you’re done.

Here’s an example of the output when sorting by the `market` price:

```
Welcome to the Pokémon Card Price Viewer!
We have a local dataset of Pokémon card prices. Choose a price metric to see the top cards.

Available price metrics: low, mid, high, market
Enter a metric to sort by (or type 'quit' to exit): market

Top 10 cards by market price:

Rank Name               Low       Mid      High    Market
------------------------------------------------------------
1    Charizard        200.00    300.00    500.00    350.00
2    Rayquaza         120.00    180.00    300.00    200.00
3    Mew              100.00    150.00    250.00    160.00
4    Umbreon           90.00    140.00    220.00    150.00
5    Espeon            85.00    130.00    210.00    140.00
6    Mewtwo            80.00    120.00    200.00    130.00
7    Dragonite         60.00     90.00    150.00    100.00
8    Gyarados          70.00    100.00    180.00    110.00
9    Blastoise         50.00     75.00    120.00     80.00
10   Venusaur          40.00     65.00    100.00     70.00
```

## Next steps

If you’d like to expand on this project, consider these ideas:

* **API integration** – Replace the static JSON with real data from the
  Pokémon TCG API or another pricing service.
* **Web interface** – Use a lightweight web framework like Flask to display
  the sorted card list in a browser.
* **Data persistence** – Periodically fetch and cache price data to keep it
  up‑to‑date without hitting rate limits.

Have fun hacking on Pokémon cards!
