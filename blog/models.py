from ckeditor.fields import RichTextField
from django.db import models
from user.models import User


class BlogModel(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=255)
    blog_subtitle = models.CharField(max_length=255, null=True, blank=True)
    blog_content = RichTextField()
    blog_image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    totalViewCount = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.blog_title + " by " + self.author.name

    @property
    def number_of_comments(self):
        return BlogCommentModel.objects.filter(blogpost_connected=self).count()

    # def save(self, *args, **kwargs):
    #     slug_str = "%s %s" % (self.blog_title, self.date_posted)
    #     self.slug = slugify(slug_str)
    #     super(BlogModel, self).save(*args, **kwargs)


class BlogCommentModel(models.Model):
    blog_post = models.ForeignKey(BlogModel, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.name, self.blog_post.blog_title[:40])


class BlogViewModel(models.Model):
    viewer = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.viewer.name + " viewed " + self.viewed.blog_title


class KeywordModel(models.Model):
    keyword = models.CharField(max_length=255)
    total_count = models.IntegerField(default=0)


class BlogSearchKeywordModel(models.Model):
    searched_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    searched_for = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
