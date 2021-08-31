from django.db import models
from django.utils.dateparse import parse_date
from datetime import date

# Create your models here.
class Network(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TVShowManager(models.Manager):
    # Note: Most of these are already validated using the "required"
    #       attribute in the HTML, but adding here due to the assignment.
    #       Validations tested before adding the "required" attributes.
    def validate(self, POST):
        errors = {}
        if not POST['title']:
            errors['title1'] = 'TV Show title is a required field.'
        elif POST['edit-type'] == 'Create' and TVShow.objects.filter(title=POST['title']).count() > 0:
            errors['title2'] = f'The TV Show "{POST["title"]}" already exists in the database.  Cannot add another record.  Either edit the existing record or delete it before creating a new record for this TV Show.'
        if not POST['network']:
            errors['network'] = 'The Network that produced the show is a required field.'
        if not POST['release_date']:
            errors['release_date1'] = 'The initial release date of the show\'s first episode is a required field.'
        elif parse_date(POST['release_date']) >= date.today():
            errors['release_date2'] = 'The release date must be a date in the past.'
        if POST['description'] and len(POST['description']) < 10:
            errors['description'] = 'When entering a description, a minimum of 10 characters is required.'
        return errors


class TVShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.ForeignKey('Network', on_delete=models.CASCADE)
    release_date = models.DateField(auto_now=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TVShowManager()
