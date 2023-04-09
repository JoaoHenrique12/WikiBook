from django.templatetags.static import static

def get_image_or_default(profile_image_link='', profile_gender=''):
    if profile_image_link:
        return profile_image_link
    
    if profile_gender == 'F':
        profile_image_link = static('social_media/images/profile/female.jpg')
    elif profile_gender == 'M':
        profile_image_link = static('social_media/images/profile/male.jpg')
    else:
        profile_image_link = static('social_media/images/profile/not_informed.jpg')

    return profile_image_link