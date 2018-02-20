from flask import *
from StorageTypes import *
from Module import Module
from View import View


class Controller:
    def __init__(self, mod, view, app):
        self.module = mod
        self.view = view
        self.app = app
        self.__siteCount = 0

    def generateRoute(self, path, tempPath, tempData):
        exec("@app.route(\"" + path + "\")\ndef Site" + str(self.__siteCount) + "(): return self.view.generateTemplate(tempPath, self.module, tempData)", {"self":self, "tempPath":tempPath, "tempData":tempData, "app":self.app})
        self.__siteCount += 1

#print("def tempFunc" + str(x) + "(controller): return {\"BookDesc\": cont.module.getData(" + str(x) + ", Book)}\ncont.generateRoute(\"/" + str(x) + "\",\"info.html\", tempFunc" + str(x) + ")")
#exec("def tempFunc" + str(x) + "(controller): return {\"BookDesc\": cont.module.getData(" + str(x) + ", Book)}\ncont.generateRoute(\"/" + str(x) + "\",\"info.html\", tempFunc" + str(x) + ")", {"cont": cont, "Book": Book})