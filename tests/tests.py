import math
roman = "XCI"

lib = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

result = []
def solution(romanNumber):
    result = []
    for i in romanNumber:
        result.append(lib.get(i))
    return result

print(solution(roman))
print(f'''
    {roman}: {solution(roman)}
    III: {solution('III')}
''')

def calculateCubesWithBlueSides (amountOfCuts):
    innerCubeSize = (amountOfCuts - 1) ** 3
    outerCubeSize = (amountOfCuts + 1) ** 3
    return outerCubeSize - innerCubeSize

print(calculateCubesWithBlueSides(1))
print(calculateCubesWithBlueSides(16))