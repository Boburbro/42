def generate(n: int) -> list:
    if n < 1:
        return []
    _step = 1
    _result = [[1]]
    while n > _step:
        _step += 1
        row = [ 
            num if index == 0 else num + _result[_step - 2][index - 1]
            for index, num in enumerate(_result[_step - 2])
        ]
        row.append(1)
        _result.append(row)

        print(_step)

    return _result

print(generate(5))