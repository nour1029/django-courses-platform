from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from tinymce.models import HTMLField



# Create your models here.
class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    subtitle = models.CharField(_("Sub-Title"), max_length=90)
    image = models.ImageField(_("Image"), upload_to='courses/photos/')
    price = models.FloatField(_("price"))
    preview_video = models.FileField(_("Preview Video"), upload_to='courses/videos/preview/', max_length=100)
    description = HTMLField(_("Desc"))
    category = models.ForeignKey("Category", verbose_name=_("Category"), on_delete=models.CASCADE)
    language = models.CharField(_("Language"), max_length=50)
    what_you_learn = HTMLField(_("What Will You Learn"))
    requirements = HTMLField()
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    date_modified = models.DateTimeField(_("Date Modified"), auto_now=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(Course, verbose_name=_("Course"), related_name="course_section", on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name

class Lucture(models.Model):
    course = models.ForeignKey(Course, verbose_name=_("Course"), related_name="course_lucture", on_delete=models.CASCADE)
    section = models.ForeignKey(Section, verbose_name=_("Section"), related_name="section_lucture", on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=50)
    subtitle = models.CharField(_("Sub-Title"), max_length=90)
    video = models.FileField(_("Video"), upload_to='courses/videos/luctures', max_length=100)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), related_name="user_review", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=_("Course"), related_name="course_review", on_delete=models.CASCADE)
    rating = models.IntegerField(_(""))
    content = models.TextField(_("Content"))
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)

    def __str__(self):
        return self.user