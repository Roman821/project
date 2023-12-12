name = "Шерлок Холмс"
age = 33
hobbies = ["литература", "скрипка", "дедукция"]
interests = ["наука", "загадки"]
projects = ["Этюд в розовых тонах", "Собака Баскервиль"]


class Character:
    def __init__(self, name, age, hobbies, interests, projects):
        self.name = name
        self.age = age
        self.hobbies = hobbies
        self.interests = interests
        self.projects = projects


# Cоздаём экземпляр класса Character
character_info = Character(
    name="Шерлок Холмс",
    age=33,
    hobbies=["литература", "скрипка", "дедукция"],
    interests=["наука", "загадки"],
    projects=["Этюд в розовых тонах", "Собака Баскервиль"]
)
