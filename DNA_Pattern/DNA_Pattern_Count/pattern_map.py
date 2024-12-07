def update_pattern_map(pattern_map, current_pattern):
    """Updates the pattern map with the current pattern.

    Args:
        pattern_map (dict): Dictionary storing pattern counts.
        current_pattern (list): List representing the current pattern.
    """
    pattern = ''.join(current_pattern)
    if pattern in pattern_map:
        pattern_map[pattern] += 1
    else:
        pattern_map[pattern] = 1

def filter_patterns(pattern_map, threshold):
    """Filters patterns that appear more than the threshold number of times.

    Args:
        pattern_map (dict): Dictionary storing pattern counts.
        threshold (int): Minimum number of occurrences for a pattern to be included.

    Returns:
        dict: Filtered pattern map.
    """
    return {pattern: count for pattern, count in pattern_map.items() if count > threshold}
