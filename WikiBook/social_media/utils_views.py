from typing import List

from django.templatetags.static import static

from .models import Profile


def get_image_or_default(profile_image_link='', profile_gender='') -> str:
    if profile_image_link:
        return profile_image_link

    if profile_gender == 'F':
        profile_image_link = static('social_media/images/profile/female.jpg')
    elif profile_gender == 'M':
        profile_image_link = static('social_media/images/profile/male.jpg')
    else:
        profile_image_link = static(
            'social_media/images/profile/not_informed.jpg')

    return profile_image_link


def get_profiles_with_images(profiles: List[Profile]) -> List[Profile]:
    profiles_with_images = []

    for p in profiles:
        p.image_link = get_image_or_default(p.image_link, p.gender)
        profiles_with_images.append(p)
    return profiles_with_images
