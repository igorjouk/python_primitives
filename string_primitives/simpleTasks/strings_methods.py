
def remove_duplicate(seq):
   # order preserving
   noDupes = []
   [noDupes.append(i) for i in seq if not noDupes.count(i)]
   return noDupes

def dividers_find():
    number = int(input('Please enter a number >>'))
    dividers = []
    d = 2
    while  d * d <= number:
        if number % d == 0:
            dividers.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        dividers.append(number)

    unique_dividers = remove_duplicate(dividers)

    for divider in unique_dividers:
        print(divider)

dividers_find()