"""
Lab 2.4 – Functional Tools Practice
"""

PRICES = [12.5, 9.9, 15.0, 22.3, 5.0]
QUANTITIES = [2, 5, 1, 3, 4]


# Part A: Functional style

def item_totals(prices: list[float], quantities: list[int]) -> list[float]:
    """Calculate item totals using map()."""
    return list(map(lambda p, q: p * q, prices, quantities))


def filter_above(totals: list[float], threshold: float = 30) -> list[float]:
    """Return totals greater than threshold using filter()."""
    return list(filter(lambda total: total > threshold, totals))


def pair_up(prices: list[float], quantities: list[int]) -> list[tuple]:
    """Pair prices and quantities using zip()."""
    return list(zip(prices, quantities))


# Part B: List comprehensions

def item_totals_comp(prices: list[float], quantities: list[int]) -> list[float]:
    """Calculate item totals using a list comprehension."""
    return [p * q for p, q in zip(prices, quantities)]


def filter_above_comp(totals: list[float], threshold: float = 30) -> list[float]:
    """Filter totals using a list comprehension."""
    return [total for total in totals if total > threshold]


if __name__ == "__main__":
    totals = item_totals(PRICES, QUANTITIES)
    print("Totals:", totals)

    print("Totals > 30:", filter_above(totals))

    print("Price-quantity pairs:", pair_up(PRICES, QUANTITIES))

    totals_comp = item_totals_comp(PRICES, QUANTITIES)
    print("Totals (comprehension):", totals_comp)

    print("Totals > 30 (comprehension):",
          filter_above_comp(totals_comp))

    print("I find list comprehensions easier to read.")
