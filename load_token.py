def loadToken(filename):
    with open(filename, "r") as fl:
        token = fl.readline()
        return token
    return ""
