def create_intervals(my_set):
    spisok = sorted(list(my_set))
    full_spisok = [[spisok[0]]]
    final_spisok = []
    for element in range(1, len(spisok)):
        if spisok[element] == (full_spisok[-1][-1] + 1):
            full_spisok[-1].append(spisok[element])
        else:
            full_spisok.append([spisok[element]])
    for sublist in full_spisok:
        final_answer = (sublist[0], sublist[-1])
        final_spisok.append(final_answer)
    return final_spisok
