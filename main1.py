class india():
    def capital(self):
        print("new delhi is the capital of india")
    def language(self):
        print("hindi is the official language of india")
    def type(self):
        print("india is a developing country")
class usa():
    def capital(self):
        print("washington dc is the capital of usa")
    def language(self):
        print("english is the official language of usa")
    def type(self):
        print("usa is a developed country")
i = india()
u = usa()
for j in (i,u):
    j.capital()
    j.language()
    j.type()