keypad = {
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
}

n = ["ADH", "ADI"]
combinations = []


def get_terms(digits):
    terms = []
    for i in digits:
        terms.append(keypad[int(i)])
    return terms


def combine(terms, accum):
    last = len(terms) == 1
    n = len(terms[0])
    for i in range(n):
        item = accum + terms[0][i]
        if last:
            combinations.append(item)
        else:
            combine(terms[1:], item)


def get_words(combinations, n):
    words = []
    for i in combinations:
        if i in n:
            words.append(i)
    return words


def answer(digits):
    combine(get_terms(digits), "")
    print(combinations)
    print(get_words(combinations, n))


answer("234")
