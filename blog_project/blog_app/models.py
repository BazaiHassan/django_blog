from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    # The author is connected to super user (auth.User)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    # This function will help us to get the current time when we clicked publish post button
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # This function is for approving comments that we will use it futhur
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    # This function should be written exactly like this, ...
    # ... it will redirect user to post_detail page when he/she publish the post
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title
    

class Comments(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
    

    def __str__(self):
        return self.text
    


