def move_alphabets(word, alphabet):
    """
    Move all characters in the word which matches 'alphabet' to end of the word
    while maintaining the relative order of the other characters in the word.

    Args:
        word (str): A string between 'a-z' (inclusive)
        alphabet (str): A character between 'a-z' (inclusive).

    Return:
        word(str): Final result where all the matched alphabets moved to end of the word
    """

    if len(word) <= 1:
        return word
    elif word[0] == alphabet:
        return move_alphabets(word[1:], alphabet) + word[0]
    else:
        return word[0] + move_alphabets(word[1:], alphabet)


def missing_number(nums):
    """
    Return the only number in the range that is missing from the array.

    Args:
        nums (list): An array containing n distinct numbers in the range [0, n]. 'n' is length of the array.

    Return:
        result(int): An integer, which is the missing number from the given array.
    """

    n = len(nums)

    nums_sum = 0
    for num in nums:
        nums_sum += num

    result = (n * (n + 1)) // 2 - nums_sum
    return result
