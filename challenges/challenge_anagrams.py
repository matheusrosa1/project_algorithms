def merge_sort(word: str) -> str:
    if len(word) <= 1:
        return word

    mid = len(word) // 2
    left = merge_sort(word[:mid])
    right = merge_sort(word[mid:])

    return merge(left, right, word)


def merge(left: list[str], right: list[str], merged: list[str]) -> list[str]:
    merged = []
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged.append(left[left_cursor])
            left_cursor += 1
        else:
            merged.append(right[right_cursor])
            right_cursor += 1

    merged.extend(left[left_cursor:])
    merged.extend(right[right_cursor:])

    return "".join(merged)


def verifyng_is_anagram(first_string, second_string): ...


def is_anagram(first_string, second_string):
    merged_first_string = merge_sort(first_string).lower()
    merged_second_string = merge_sort(second_string).lower()
    if merged_first_string == merged_second_string:
        return (merged_first_string, merged_second_string, True)
    else:
        return False


print(is_anagram("Amor", "roma"))
