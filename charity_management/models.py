from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.FileField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username


class Volunteer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.FileField(null=True)
    idpic   = models.FileField(null=True)
    aboutme = models.CharField(max_length=300,null=True)
    status  = models.CharField(max_length=20,null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    adminreview = models.CharField(max_length=300,null=True)
    updationdate = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username


class Ngo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=300, null=True)
    userpic = models.FileField(null=True)
    idpic = models.FileField(null=True)
    aboutme = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=20, null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    adminreview = models.CharField(max_length=300, null=True)
    updationdate = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username


class DonationAreas(models.Model):
    areaname = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=300, null=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.areaname




class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donationname = models.CharField(max_length=50, null=True)
    donationpic = models.FileField(null=True)
    collectionlocation = models.CharField(max_length=300,null=True)
    description = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=50, null=True)
    donationdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(max_length=300, null=True)
    updationdate = models.DateTimeField(null=True)
    volunteer =  models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    donationarea = models.ForeignKey(DonationAreas,on_delete=models.CASCADE)
    ngo =  models.ForeignKey(Ngo, on_delete=models.CASCADE)
    volunteerremark = models.CharField(max_length=300, null=True)
    updationdate = models.DateTimeField(null=True)

    def __str__(self):
        return self.id


class Gallery(models.Model):
    donation = models.ForeignKey(Donor, on_delete=models.CASCADE)
    deliverypic = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id





