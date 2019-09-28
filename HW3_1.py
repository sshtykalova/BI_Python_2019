def checkio(main_checkio: list) -> list:
    sort_checkio = sorted(main_checkio)
    not_unique_checkio = []
    answer_checkio = main_checkio
    for i in range(0, len(sort_checkio) - 1):
        if sort_checkio[i] == sort_checkio[i + 1] and sort_checkio[i] not in not_unique_checkio:
            not_unique_checkio.append(sort_checkio[i])
    if not_unique_checkio == []:
        return []
    else:
        if main_checkio[-1] not in not_unique_checkio:
            answer_checkio.remove(main_checkio[-1])
        for i in range(0, len(main_checkio) - 1):
            if main_checkio[i] not in not_unique_checkio:
                answer_checkio.remove(main_checkio[i])
        main_checkio = answer_checkio
    return main_checkio
