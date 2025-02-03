def calculator(inputbyuser):
    ourstring = inputbyuser.strip().split()
    if len(ourstring) != 3:
        raise ValueError("т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
    a, symbol, b = ourstring

    try:
        a = int(a)
        b = int(b)
    except:
        raise ValueError("Калькулятор умеет работать только с целыми числами.")

    if a <1 or a>10:
        raise ValueError("Калькулятор должен принимать на вход числа от 1 до 10 включительно, не более.")
    if b<1 or b>10:
        raise ValueError("Калькулятор должен принимать на вход числа от 1 до 10 включительно, не более.")

    if symbol == "+":
        result = a + b
    elif symbol == "-":
        result = a - b
    elif symbol =="*":
        result = a*b
    elif symbol == "/":
          if b == 0:
            raise ValueError("На ноль делить нельзя")
          result = a//b
    else:
        raise ValueError("формат не верен.Поддерживаются только +, -, *, /")
    return result

calcu = input("введите выражение")

print (calculator(calcu))




