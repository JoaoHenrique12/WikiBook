from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, User

# sender: the model class that is sending the signal (in this case, User)
# instance: the actual model instance that was saved

# created: a boolean indicating whether the instance was just created
# or already existed


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
