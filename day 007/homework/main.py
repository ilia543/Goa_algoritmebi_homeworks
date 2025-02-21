def func(numb, whicsystem):
    if whicsystem == "decimal to binary":
        numb = int(numb)
        result = []
        while numb != 0:
            result.append(str(numb % 2))
            numb //= 2
        result = result[::-1]
        return "".join(result)
    else:
        xarisxi = -1
        numb = numb.split()
        numb = numb[::-1]
        result = []
        for i in numb:
            xarisxi += 1
            if whicsystem == "binary to decimal":
                result.append(int(i) * (2 ** xarisxi))
            elif whicsystem == "octal to decimal":
                result.append(int(i) * (8 ** xarisxi))
            elif whicsystem == "hexadecimal to decimal":
                result.append(int(i) * (16 ** xarisxi))
        return sum(result)
    
    
print(func("1 1 1 1 0 1 0 0 1", "binary to decimal"))
print(func("1 3 4 6", "octal to decimal"))
print(func("1 3 4 6", "hexadecimal to decimal"))
print(func("53", "decimal to binary"))