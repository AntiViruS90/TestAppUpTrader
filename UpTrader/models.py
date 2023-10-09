from django.db import models as m


class User(m.Model):
    firstname = m.CharField(max_length=30)
    lastname = m.CharField(max_length=30)
    email = m.EmailField(max_length=30)
    phone = m.CharField(max_length=20)

    def __str__(self):
        return self.firstname
