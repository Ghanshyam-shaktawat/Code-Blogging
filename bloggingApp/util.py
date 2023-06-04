import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
	"""This generates a random string up to max of 10 characters"""
	return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug = None):
	"""
    This check is the slug already exists in the database and if yes then,
    concate the random generated string at the end of the slug.
    """
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.title)

	Klass = instance.__class__
	max_length = Klass._meta.get_field('slug').max_length
	slug = slug[:max_length]
	qs_exists = Klass.objects.filter(slug = slug).exists()
	
	if qs_exists:
		new_slug = "{slug}-{randstr}".format(
			slug = slug[:max_length-5], randstr = random_string_generator(size = 3))
			
		return unique_slug_generator(instance, new_slug = new_slug)
	return slug
