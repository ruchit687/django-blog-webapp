# we'll be using sqlite3 for development/testing and Postgres for production (databases)
# This is actually happening because of ORM (Object Relational Mapping) - Django own ORM
# so you're not required to change code again for production level. All we'll be needing is to set up different dbs
# in the settings. Django ORM... we can represent our db structure as classes (models).

# blog app will requires 'users' and their 'posts'. Django has built-in authentication system. It takes care of 'users'.
# as django already has user-model, we've also seen how to create users. We'll later see how to add custom fields
# as of now we'll make a post model, inherited from models class of django
# use python manage.py sqlmigrate blog [migration number... like = 0001]

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# so the Post Model and User model will have a relationship since Users are going to author post, specifically this
# will be called one to many relationship, because one user can have multiple posts. to do this in django we'll use a
# foreign key.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # auto_now_add = True // set the date_posted to current date time only when the object is created , this sounds
    # exactly what we want, but there is a caviar over here; so using auto_now_add argument you can't ever update the
    # date_posted value... this may be fine.
    # [but if you wish to change the date in future; then you should use default argument set to  timezone.now]
    # last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete > if user gets deleted then what happens to post, models.cascade tells django to delete posts related to
    # the user who created them, and this is one way as if user delete posts, that won't delete the user.

    # magic methods/ special methods
    def __str__(self):
        return self.title
