from django.db import models

# Create your models here.

class Tweet(models.Model):
  """docstring for Tweet"""
  content  = models.TextField()

  def __str__(self):
    return str(self.content)