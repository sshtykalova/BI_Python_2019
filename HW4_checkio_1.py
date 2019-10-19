def checkio(first, second):
    first = list(first.split(','))
    second = list(second.split(','))
    third = []
    for words in first:
        if words in second:
            third.append(words)
    third.sort()
    answer = ','.join(third)
    answer = '"' + answer + '"'
    return answer
