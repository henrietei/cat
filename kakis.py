class Cat:
    name=None
    age=None
    isHappy=None

    def __init__(self, name=None, age=None, isHappy=None):
        self.name=name
        self.age=age
        self.isHappy=isHappy
        self.get_data()

    def set_data(self, name=None, age=None, isHappy=None):
        self.name=name
        self.age=age
        self.isHappy=isHappy

    def get_data(self):
        print (self.name, 'age:', self.age, 'Happy:', self.isHappy)

cat1=Cat()
"""cat1=Cat("toms", 6, True)
cat2=Cat("henriete", 18, False)

cat1.set_data("toms", 6, True)
cat1.get_data()

cat2=Cat()
cat2.set_data("henriete", 18, False)
cat2.get_data()


cat1.name="Milka"
cat1.age="11"
cat1.isHappy=True
print(cat1.name, cat1.age, cat1.isHappy)


cat2=Cat()
cat2.name="pucins"
cat2.age=3
cat2.isHappy=False
print(cat2.name, cat2.age, cat2.isHappy)"""