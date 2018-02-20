import StorageTypes as Storage


class Module:
    def __init__(self, dataPath):
        self.storage = dataPath
        self.data = None
        try:
            with open(dataPath, "r") as f:
                self.data = eval(f.read())
        except FileNotFoundError:
            with open(dataPath, "w") as f:
                s = "{ "
                for x in Storage.types:
                    s += "\"" + x.__name__ + "\": {}, "
                s = s[:-2] + "}"
                self.data = eval(s)
                f.write(s)

    def getData(self, key, sType):
        try:
            return sType(*list(self.data[sType.__name__][key].values()))
        except KeyError:
            print("[ERROR] No data found with the key: ' " + str(key) + " ' of the type ' " + sType.__name__ + " '")
            return sType(-1)

    def getType(self, sType):
        return self.data[sType.__name__]

    def writeData(self, key, data):
        self.data[type(data).__name__][key] = data.raw
        with open(self.storage, "w") as f:
            f.write(str(self.data))

    def removeData(self, key, sType):
        try:
            del self.data[sType.__name__][key]
            with open(self.storage, "w") as f:
                f.write(str(self.data))
        except KeyError:
            print("[WARNING] No data found with the key: ' " + str(key) + " ' of the type ' " + sType.__name__ + " ' so it cannot be deleted")