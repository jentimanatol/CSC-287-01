from linked_list import LinkedList
from pattern_map import update_pattern_map, filter_patterns

def find_patterns(linked_list, k, threshold):
    """Finds patterns in the DNA sequence stored in a linked list.

    Args:
        linked_list (LinkedList): The linked list containing the DNA sequence.
        k (int): The length of the pattern to search for.
        threshold (int): The minimum number of occurrences for a pattern to be considered.

    Returns:
        dict: Filtered pattern map.
    """
    pattern_map = {}
    current_pattern = []
    current_index = 0
    dna_length = len(linked_list)

    # Convert linked list to list for easier access
    linked_list_as_list = list(linked_list)

    while current_index < dna_length:
        if len(current_pattern) < k:
            current_pattern.append(linked_list_as_list[current_index])
        else:
            update_pattern_map(pattern_map, current_pattern)
            current_pattern.pop(0)
            current_pattern.append(linked_list_as_list[current_index])
        current_index += 1

    filtered_patterns = filter_patterns(pattern_map, threshold)
    return filtered_patterns

# Example usage
if __name__ == "__main__":
    dna_sequence = "ACGTACGTACGTACGAA"
    k = 3
    threshold = 2

    linked_list = LinkedList()
    for nucleotide in dna_sequence:
        linked_list.append(nucleotide)

    patterns = find_patterns(linked_list, k, threshold)
    print(patterns)
