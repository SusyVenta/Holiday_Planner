from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# user model is already created by django
# every time i create new models, need to run py -3.6 manage.py makemigrations and
# py -3.6 manage.py migrate
# to see sql run: py -3.6 manage.py sqlmigrate plans 0001
# py -3.6 manage.py shell ###to exit: exit()
# In [1]: from plans.models import Plan
# In [2]: from django.contrib.auth.models import User
# In [3]: User.objects.all()
# Out[3]: <QuerySet [<User: susanna>, <User: TestUser>]>
# user = User.objects.filter(username="susanna").first() --> user.pk
# create a plan: plan_1 = Plan(title="plan 4", content="4d plan content", author=user) --> plan_1.save()
# Plan.objects.all()
# In [9]: plan_2 = Plan(title="plan 2", content="content 2!", author_id=user.id)
# In [10]: plan_2.save()
# plan = Plan.objects.first()   --> plan.author.email
# to see all plans created by a user: user.plan_set.all()


class Plan(models.Model):
    title = models.CharField(max_length=200)
    """ Unrestricted text """
    content = models.TextField()
    """ now = models.DateTimeField(auto_now=True) 
    date_posted = models.DateTimeField(default=timezone.now)
    """
    date_posted = models.DateTimeField(default=timezone.now)
    # if user is deleted, plans get deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # defines how post is displayed when queried

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Needed for django to redirect to plan detail after plan is created
        Redirect redirects to a specic route vs reverse returns an url as string to the route
        """
        return reverse('plan-detail', kwargs={'pk': self.pk})