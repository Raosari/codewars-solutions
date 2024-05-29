# Trigrams are a special case of the n-gram, where n is 3. One trigram is a continous sequence of 3 chars in phrase. Wikipedia

# return all trigrams for the given phrase
# replace spaces with underscore (_)
# return an empty string for phrases shorter than 3
# Example:

# "the quick red" --> "the he_ e_q _qu qui uic ick ck_ k_r _re red"

def trigrams(phrase):
    if len(phrase) < 3:
        return ""
    res = []
    for i in range(0,len(phrase) - 2):
        triagram = phrase[i:i+3]
        cl_triagram = triagram.replace(" ","_")
        res.append(cl_triagram)
    return " ".join(res)