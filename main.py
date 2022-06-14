class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        """Initializing name, age, tracks and score attributes."""
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        """Return the value of the name parameter"""
        self.name = name
        return self.name

    def change_age(self, age):
        """Return the value of the age parameter"""
        self.age = int(age)
        return self.age

    def add_track(self, tracks):
        """Return a list of all the tracks"""
        self.tracks += tracks.split(",")
        return self.tracks

    def get_score(self):
        """Return the instance's score"""
        return float(self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX, Python"))
print(Bob.get_score())
