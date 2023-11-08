from re import match, compile

def unpack_sausages(truck):
    counter = ""
    pack_number = 1
    pattern = compile(r"\[(.)\1{3}\]")
    for box in truck:
        for package in box:
            if pattern.match(package) and pack_number % 5 != 0:
                for i in range(1,len(package)-1):
                    counter += package[i] + " "
                pack_number += 1

    counter = counter[:len(counter)-1]
    return counter

truck = [ [ "(-)", "[IIII]", "[║║║║]" ], [ "IuI", "[llll]" ], [ "[@@@@]", "UwU","[IlII]" ], [ "IuI", "[))))]", "x" ], [] ]
print(unpack_sausages(truck))