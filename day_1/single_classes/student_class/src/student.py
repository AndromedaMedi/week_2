
class Student:

    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort

    def talk(self):
        return "I can talk!"
    
    # def say_favourite_language(self, input_language):
    #     self.language = input_language
    #     return self.say_favourite_language("Python")
        
    def say_favourite_language(self, input_language):
        if input_language == "Python":
            return "I love Python"