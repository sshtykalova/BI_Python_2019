def group_equal(els):
    spisok = []
    full_spisok = []
    if len(els) == 1:
        full_spisok.append(els)
    else:
        for i in range(0, len(els)):
            if i != len(els) - 1:
                if els[i] == els[i + 1]:
                    spisok.append(els[i])
                else:
                    if els[i] == els[i - 1]:
                        spisok.append(els[i])
                        full_spisok.append(spisok)
                        spisok = []
                    else:
                        spisok.append(els[i])
                        full_spisok.append(spisok)
                        spisok = []
            else:
                if els[i] == els[i - 1]:
                    spisok.append(els[i])
                    full_spisok.append(spisok)
                else:
                    spisok.append(els[i])
                    full_spisok.append(spisok)
                    spisok = []
    return full_spisok
