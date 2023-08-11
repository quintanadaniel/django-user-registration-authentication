from django.db import models


class Member(models.Model):

    name = models.CharField(max_length=300)

    MY_CHOICES = (
        ("a", "Stadard"),
        ("b", "Premium"),
        ("c", "Premium Delux"),
    )

    membership_plan = models.CharField(max_length=1, choices=MY_CHOICES)
    unique_code = models.CharField(max_length=300)
