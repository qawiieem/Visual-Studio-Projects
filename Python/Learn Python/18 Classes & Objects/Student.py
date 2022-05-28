class Pupil:               #Creating Student data type

    def __init__(self, name, major, gpa, is_on_probation ):
        self.name = name                        # 'self' is referring to the actual obj.
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
