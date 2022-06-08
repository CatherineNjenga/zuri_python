class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        print(f"{str(self.name)}")

    def change_age(self, age):
        print(f"{int(self.age)}")

    def add_track(self, tracks):
        print(f"{list(self.tracks)}")

    def get_score(self, score):
        print(f"{float(self.score)}")

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print(Bob)
# Expected methods
peter = Bob.change_name("Peter")
print(peter)
Bob.change_age(34)
Bob.add_track("UI/UX, Python")
Bob.get_score(90)
