# The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.

# The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).

# If the score < 0, return 0.

def check_exam(arr1,arr2):
    res = 0
    for idx,answer in enumerate(arr1):
        if not arr2[idx]:
            continue
        elif answer == arr2[idx]:
            res += 4
        elif answer != arr2[idx]:
            res -= 1 
    return res if res >= 0 else 0