"""Check finite events and transfer bounds for the two-slot repeater schedule.

Uses only Python's standard library. Run without -O to enable the checks.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, prod


def block_partitions(edges):
    """All ordered contiguous partitions with at least two edges per block."""
    for blocks in range(1, edges // 2 + 1):
        for cuts in combinations(range(2, edges - 1), blocks - 1):
            boundaries = (0, *cuts, edges)
            lengths = tuple(right - left for left, right in zip(boundaries, boundaries[1:]))
            if min(lengths) >= 2:
                yield lengths


def selected_profile(first_slot, lengths, starts_on_left):
    """Determine retry positions solely from the first-slot source flags."""
    profile = [2] * len(first_slot)
    start = 0
    for index, length in enumerate(lengths):
        oriented_edges = range(start, start + length)
        keep_from_left = starts_on_left if index % 2 == 0 else not starts_on_left
        if not keep_from_left:
            oriented_edges = reversed(oriented_edges)
        for edge in oriented_edges:
            if not first_slot[edge]:
                break
            profile[edge] = 1
        kept = profile[start:start + length].count(1)
        if kept == 0 or kept == length:
            return None
        start += length
    return tuple(profile)


def simulated_swaps(first_slot, profile):
    """Simulate the two physical ports at each interior station by birth time."""
    occupancy = [dict() for _ in range(len(profile) - 1)]
    peak = 0
    waiting = 0
    exposures = []

    for slot in (1, 2):
        for station, ports in enumerate(occupancy):
            for edge in (station, station + 1):
                if (slot == 1 and first_slot[edge]) or (slot == 2 and profile[edge] == 2):
                    assert edge not in ports
                    ports[edge] = slot
            peak = max(peak, len(ports))
            if slot == 1:
                for edge in tuple(ports):
                    if profile[edge] == 2:
                        del ports[edge]
            if len(ports) == 2:
                exposures.append(sum(slot - birth for birth in ports.values()))
                ports.clear()
        if slot == 1:
            waiting = sum(len(ports) for ports in occupancy)

    assert len(exposures) == len(profile) - 1
    assert all(not ports for ports in occupancy)
    return peak, waiting, exposures


def check_schedule():
    probabilities = (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4))
    checked_schedules = 0
    checked_profiles = 0
    checked_trials = 0

    for edges in range(2, 9):
        all_flags = tuple(product((0, 1), repeat=edges))
        for lengths in block_partitions(edges):
            blocks = len(lengths)
            factor = prod(length - 1 for length in lengths)
            short, extra = divmod(edges, blocks)
            balanced_factor = (short - 1) ** (blocks - extra) * short ** extra
            assert factor <= balanced_factor

            for starts_on_left in (True, False):
                histories = defaultdict(Counter)
                for first_slot in all_flags:
                    profile = selected_profile(first_slot, lengths, starts_on_left)
                    if profile is None:
                        continue
                    retry = tuple(edge for edge, birth in enumerate(profile) if birth == 2)

                    peak, waiting, exposures = simulated_swaps(first_slot, profile)
                    assert peak <= 2 and waiting == blocks, (lengths, first_slot, profile)
                    assert exposures.count(1) == blocks and sum(exposures) == blocks
                    assert sum(a != b for a, b in zip(profile, profile[1:])) == blocks

                    # Count all potential flags, including those at unattempted slots.
                    first_successes = sum(first_slot)
                    for second_slot in all_flags:
                        if all(second_slot[edge] for edge in retry):
                            histories[profile][first_successes + sum(second_slot)] += 1

                assert len(histories) == factor, (lengths, starts_on_left)
                for p in probabilities:
                    q = 1 - p
                    weights = [p**successes * q**(2 * edges - successes)
                               for successes in range(2 * edges + 1)]
                    for profile, counts in histories.items():
                        brute = sum(count * weights[successes] for successes, count in counts.items())
                        assert brute == p**edges * q**blocks, (lengths, p, profile)

                checked_schedules += 1
                checked_profiles += len(histories)
                checked_trials += len(all_flags) ** 2

    return checked_schedules, checked_profiles, checked_trials


def check_isolated_late_births():
    """Count first-success profiles with isolated late interior births."""
    checked = 0
    for edges in range(2, 13):
        interior = range(1, edges - 1)
        for late in range((edges - 1) // 2 + 1):
            count = 0
            for positions in combinations(interior, late):
                if any(right - left == 1 for left, right in zip(positions, positions[1:])):
                    continue
                profile = tuple(int(i in positions) for i in range(edges))
                assert sum(abs(a - b) for a, b in zip(profile, profile[1:])) == 2 * late
                count += 1
            assert count == comb(edges - late - 1, late)
            checked += 1
    return checked


def check_first_success_bound():
    """Compare the weighted run bound with exact geometric-profile sums."""
    checked = 0
    for edges in range(1, 9):
        max_exposure = min(edges - 1, 4)
        coefficients = [Counter() for _ in range(max_exposure + 1)]
        for heights in product(range(max_exposure + 1), repeat=edges):
            if min(heights) != 0:
                continue
            exposure = sum(abs(left - right) for left, right in zip(heights, heights[1:]))
            if exposure <= max_exposure:
                coefficients[exposure][sum(heights)] += 1

        for p in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
            q = 1 - p
            weighted = Fraction(0)
            for budget, counts in enumerate(coefficients):
                weighted += sum(count * q**height for height, count in counts.items())
                actual = weighted / (1 - q**edges)
                bound = (3 * max(1, q / p))**budget * comb(edges - 1, budget // 2) / p
                assert 0 < actual <= bound, (edges, p, budget, actual, bound)
                checked += 1
    return checked


def main():
    schedules, profiles, trials = check_schedule()
    isolated_cases = check_isolated_late_births()
    weighted_cases = check_first_success_bound()
    print(f"Verified {schedules} schedules, {profiles} accepted time profiles, and {trials:,} flag histories.")
    print(f"Verified {isolated_cases} isolated-late counts and {weighted_cases} exact weighted first-success bounds.")


if __name__ == "__main__":
    main()
