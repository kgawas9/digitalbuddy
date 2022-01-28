from django.db import models

# Create your models here.
class NewJoinerDetails(models.Model):
    PSID = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False)
    other_phone = models.CharField(max_length=20, null=False, unique=True)
    grade = models.CharField(max_length=10, null=False)
    dept_id = models.IntegerField()
    email_address = models.EmailField(max_length=200, null=False, unique=True)
    date_of_joining = models.DateTimeField()
    work_location = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.first_name

    class Meta:
        managed = False
        db_table = 'NewJoinerCandidateData'
