class View:
    def __init__(self): pass

    def generateTemplate(self, tPath, mod, tempData=0):
        from flask import render_template
        return render_template(tPath, Page=mod, tempData=tempData)