from django.db import models

MARKS = enumerate(range(1, 11))


class PerformanceModel(models.Model):
    active = models.PositiveIntegerField(choices=MARKS)
    mark_for_practice = models.PositiveIntegerField(choices=MARKS)
    mark_for_teories = models.PositiveIntegerField(choices=MARKS)
    visits = [('offline', 1), ('online', 2), ('exited', 0)]
    visiting = models.PositiveIntegerField(choices=visits)


class CoursePerformanceModel(models.Model):
    performance = models.ForeignKey("PerformanceModel", on_delete=models.CASCADE)
    course = models.ForeignKey("PerformanceModel", on_delete=models.CASCADE)
    person = models.ForeignKey("PerformanceModel", on_delete=models.CASCADE)


class AddressModel(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    flat = models.CharField(max_length=100)
    post_office = models.CharField(max_length=100, blank=True)


class CourseModel(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    hours = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ManyToManyField('PersonModel', limit_choices_to={'status.title': 'teacher'})
# _______________________________________________________________________________________________________

class StatusModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class PersonModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.ForeignKey('AddressModel', on_delete=models.CASCADE)
    courses = models.ManyToManyField('CourseModel', through_fields=("course", "person"),
                                     through='CoursePerformanceModel')
    status = models.ManyToManyField('StatusModel')
    date_created = models.DateTimeField(auto_created=True)
    changed = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')
    performance = models.ForeignKey('PerformanceModel', on_delete=models.CASCADE)

#123123
