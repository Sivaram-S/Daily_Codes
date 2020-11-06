def sum_possible(listing, number):
    total = listing[0]
    for i in listing[1:]:
        if total + i == number:
            return True
    if len(listing) > 2:
        return sum_possible(listing[1:], number)
    else:
        return False


if __name__ == "__main__":
    ans = sum_possible([10,15,3,35,240], 25)
    print(ans)
