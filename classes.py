class abstr:
    def getstr(self):
        self.text = input("Input the text:")
        print(self.text)
    def getupper(self):
        print(self.text.upper())
a = abstr()
a.getstr()
a.getupper()