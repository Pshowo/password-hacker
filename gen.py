import itertools

alp = ["a", "b", "c", "d", "e"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def gens(num, alphabet, len, password):
    """
    Password generator
    :params num: <list> with nums
    :params alphabet: <list> with chars
    :params len: <int> length password generator
    """
    all_char = list(itertools.chain(num, alphabet))
    prods = itertools.product(all_char, repeat=len)
    a = ""
    while a != password:
        a = next(prods)
        a = "".join(a)
    print("STOP: Yours password is:", a) 

if __name__ == "__main__":
    print("RUNS")
    gens(nums, alp, 4, "6b1d")
