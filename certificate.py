def certified_mail_numbers(number : str, qnty : int):
    """
    number : certified mail starting number
    qnty : quantity of numbers to generate
    """
    if (len(number) == 20) and (number.isdigit()):
        numbers = [number]
        for _ in range(qnty-1):
            number = numbers[-1]
            next11_1 = str(int(number[12:-1])+1).zfill(7)
            number = f"{number[:12]}{next11_1}{number[-1]}"
            original = number
            number = list(map(lambda n: int(n), number[:-1]))
            sum_odd = sum(number[::2])
            sum_even = sum(number[1::2])
            odds_by_3 = sum_odd*3
            sumprod_eve = sum_even + odds_by_3
            # sumofprod = sum([number[i]*2 if i%2==0 else number[i] for i in range(len(number))])
            remainder = sumprod_eve%10
            checkDigit = 10-remainder if remainder else 0
            numbers += [f"{original[:-1]}{checkDigit}"]
        return numbers
    return None

if __name__ == "__main__": 
    firstNumber = "70140150000183858951"
    numbers = certified_mail_numbers(firstNumber, 4)
    for number in numbers:
        print(number)
