class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        print(str(name))

    def change_age(self, age):
        print(int(age))

    def add_track(self, tracks):
        print(list(tracks.split(",")))

    def get_score(self, score):
        print(float(score))

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print(Bob)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX, Python")
Bob.get_score(90)
