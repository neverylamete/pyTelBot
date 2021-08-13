def loadToken(filename):
    with open(filename, "r") as fl:
        token = fl.readline()
        print(token)
        return token
    return ""
