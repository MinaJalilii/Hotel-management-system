from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

IdentityTypeChoices = (
    ('National ID', 'National ID'),
    ('National Passport', 'National Passport'),
)


def user_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.id, filename)
    return "user_{0}/{1}".format(instance.user.id, filename)


class User(AbstractUser):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="other")
    otp = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pid = ShortUUIDField(length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvwxyz123")
    image = models.FileField(upload_to=user_dir_path, default='default.jpg', null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="other")
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    identity_type = models.CharField(max_length=20, choices=IdentityTypeChoices, default="National ID", null=True,
                                     blank=True)
    identity_image = models.FileField(upload_to=user_dir_path, default='id.jpg', null=True, blank=True)
    facebook = models.URLField(null=True, blank=True, max_length=255)
    twitter = models.URLField(null=True, blank=True, max_length=255)
    wallet = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0.00)
    verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        if self.full_name:
            return self.full_name
        else:
            return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
