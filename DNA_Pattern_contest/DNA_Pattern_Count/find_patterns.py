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
    current = linked_list.head



    # Populate the initial pattern with Initial usser requaREMENT LENGHT 
    for _ in range(k):
        if current:
            current_pattern.append(current.data)
            current = current.next







    # Traverse the rest of the linked list
    while current:
        update_pattern_map(pattern_map, current_pattern)
        current_pattern.pop(0)  # Remove the first element
        current_pattern.append(current.data)  # Add the next element
        current = current.next






    # Include the last pattern
    update_pattern_map(pattern_map, current_pattern)





    # Filter patterns based on the threshold PROVIDED BY USER 
    filtered_patterns = filter_patterns(pattern_map, threshold)
    return filtered_patterns




# Example usage AND PRINT 
if __name__ == "__main__":
    dna_sequence = "ACGTACGTACGTACGAA"
    k = 3
    threshold = 2

    linked_list = LinkedList()
    for nucleotide in dna_sequence:
        linked_list.append(nucleotide)

    patterns = find_patterns(linked_list, k, threshold)
    print(patterns)
