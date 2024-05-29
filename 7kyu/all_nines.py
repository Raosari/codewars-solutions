def all_nines(x):
    if x > 4000:
        return -1
    m = 1
    while m <= 4000:
        curr_res = str(x*m)
        for i,c in enumerate(curr_res):
            if c != "9":
                break
            if i == len(curr_res) - 1:
                return m
        m += 1
    return -1

print(all_nines(1))