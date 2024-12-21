def count_patterns(dna_sequence, k):
    pattern_map = {}
    for i in range(len(dna_sequence) - k + 1):
        pattern = dna_sequence[i:i+k]
        if pattern in pattern_map:
            pattern_map[pattern] += 1
        else:
            pattern_map[pattern] = 1
    return pattern_map
