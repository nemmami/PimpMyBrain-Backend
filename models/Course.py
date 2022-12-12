from models.Category import Category
from models.User import User


class Course(object):

    def __init__(self, id_category, id_teacher, course_description, price_per_hour, city, country, level):
        self._id_course = None
        self.id_category = id_category
        self.id_teacher = id_teacher
        self.course_description = course_description
        self.price_per_hour = price_per_hour
        self.city = city
        self.country = country
        self.level = level

    @property
    def id_course(self):
        return self._id_course

    @id_course.setter
    def id_course(self, id_course):
        self._id_course = id_course

    def convert_to_json(self):
        json = {"course_description": self.course_description,
                "price_per_hour": self.price_per_hour,
                "city": self.city,
                "country": self.country,
                "level": self.level
                }
        if type(self.id_teacher) is User:
            json["teacher"] = self.id_teacher.convert_to_json()
        else:
            json["id_teacher"] = self.id_teacher
        if type(self.id_category) is Category:
            json["category"] = self.id_category.convert_to_json()
        else:
            json["id_category"] = self.id_category

        if self.id_course is not None:
            json["id_course"] = self.id_course
        return json
