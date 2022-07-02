from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Link(models.Model):
    """
NOTICE: A model is python class that subclasses django.db.models.Model,
The containers (Target_urls... etc) are the fields of the model class (links),
Each of this field is specified as the class (links) attribute(NB: attribute is another term for a field) , by which each attribute maps to a database column,                                                     

"""
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifiers = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_date = models.DateTimeField(auto_created=True, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.target_url