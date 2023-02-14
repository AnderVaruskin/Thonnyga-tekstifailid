with open('sammud.txt', 'r') as file:
    sammud = [int(line.strip()) for line in file.readlines()]

    kokku = sum(sammud)
    print("Kokku sammud: ", kokku)

    keskmine = round(kokku / len(sammud))
    print("Keskmine sammud: ", keskmine)

    maksimum = max(sammud)
    miinimum = min(sammud)
    max_index = sammud.index(maksimum)
    min_index = sammud.index(miinimum)

    print("Suurim sammude arv: ", maksimum, "päeval", max_index + 1)
    print("Väikseim sammude arv: ", miinimum, "päeval", min_index + 1)