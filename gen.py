import itertools

alp = ["a", "b", "c", "d", "e"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def gens(num, alphabet, len, password):
    all_char = list(itertools.chain(num, alphabet))
    prods = itertools.product(all_char, repeat=len)
    a = ""
    while a != password:
        a = next(prods)
        a = "".join(a)
    print("STOP: Yours password is:", a) 



gens(nums, alp, 4, "6b1d")
