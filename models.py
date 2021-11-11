from django.db import models


# Created the Model here for the project with its respective attributes
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField(default="", blank=True, null=False)
    Instructor_Name = models.CharField(max_length=300, default="", blank=True)
    Duration = models.FloatField()
# Model manager inputted below, provides interface between database and django model
    objects = models.Manager()

    def __str__(self):
        return self.Title

