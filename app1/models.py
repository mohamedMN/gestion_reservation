from ast import Pass
import datetime
from distutils.command.upload import upload
from pyexpat import model
from tokenize import Name
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


#table utilisateur
"""class Utilisateur(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    nom = models.CharField(max_length=190,null=True)
    prenom = models.CharField(max_length=190,null=True)
    ROLE = (
        ('enseignant','enseignant'),
        ('doctorant','doctorant'),
    )
    avatar=models.ImageField(blank=True,null=False,default="profile.png")
    role = models.CharField(max_length=190,null=True,choices=ROLE)
    telephone = models.CharField(max_length=190,null=True)
"""

class Utilisateur(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    nom = models.CharField(max_length=190,null=True)
    prenom = models.CharField(max_length=190,null=True)
    telephone = models.CharField(max_length=190,null=True)
    avatar=models.ImageField(null=True,blank=True,default="profile.png")
    def __str__(self):
        return self.nom



#table salle
class Salle(models.Model):   
    NOM = (
        ('doctorant','doctorant'),
    )
    nom = models.CharField(max_length=190,null=True,choices=NOM,default="doctorant")

    def __str__(self):
        return self.nom



#table place
class Place(models.Model):
    numero=models.IntegerField(null=True,blank=True)
     #ForeignKey
    salleID = models.ForeignKey(Salle,null = True,on_delete=models.SET_NULL )
 

    def __str__(self):
        return str(self.id)



#table reservation
class Reservation(models.Model):
    check_in= models.DateTimeField(blank=True,null=True)
    check_out=models.DateTimeField(blank=True,null=True)

    #ForeignKey
    place = models.ForeignKey(Place,null=True,on_delete=models.CASCADE)   
    utilisateurID = models.ForeignKey(Utilisateur,null = True,on_delete=models.SET_NULL )

    def __str__(self):
        return "%s %s" % (self.utilisateurID,self.place)


    





