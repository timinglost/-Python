def symbols(num, counter):
    if num > 127:
        return ''
    answer = ''
    answer = answer + f'{num} - {chr(num)} '
    if counter == 1:
        counter = 11
        answer += '\n'
    return answer + symbols(num + 1, counter - 1)
print(symbols(32, 10))