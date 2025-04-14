# Add your clarifying questions here
# Is the list always non-empty?
# Yes.
# Will the shift always be to the right?
# Yes. We'll never shift to the left.
# What if the shift_by number is larger than our length?
# Shift_by will always be less than the length.
# input - [1, 2, 3], 2
# output - [2, 3, 1]
# input - ["a", "b", "c", "d"], 1
# output - ["d", "a", "b", "c"]


def rotate_list(lst, shift_by):
    shift_by = shift_by % len(lst)
    #lst[:] = lst[-shift_by:] + lst[:-shift_by]
    return lst[-shift_by:] + lst[:-shift_by] #O(n) space complexity
    #lst = lst[-shift_by:] + lst[:-shift_by]

    # input - [1, 2, 3], 2
    #[2, 3] + [1]
    #[2, 3, 1]

# input - ["a", "b", "c", "d"], 1
#["d"] +["a", "b", "c"]

def rotate_list(lst, shift_by):
    for i in range(shift_by):
        last_item = lst.pop()
        lst.insert(0, last_item) #O(1) space complexity


assert rotate_list([1, 2, 3], 2) == [2, 3, 1]
assert rotate_list(["a", "b", "c", "d"], 1) == ["d", "a", "b", "c"]
