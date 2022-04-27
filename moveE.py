def calculateEulersNumber():
    e = 1
    f = 1
    for i in range(1, 1000):
        f = f * (1.0 / i)
        if f == 0:
            break
        e += f

    return e


def readFile():
    with open("EulersNum.txt", "r") as f:
        data = f.read()
        data.strip(" ")
        data = data.replace(".", "")
        data = data.replace(" ", "")

        return data


e = readFile()


