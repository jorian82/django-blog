from django.db import models

# classes are the tables themselves.
# Watch tutorial 7 to get the views and templates url

class Post(models.Model):
	# properties are the columns, django automatically adds an ID column to every table
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()

	#this is to return the title when the object is called
	def __str__(self):
		return self.title