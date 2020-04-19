from django.db import models

import random #placeholder for CRN score
from django.utils import timezone

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    # middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    # Financial Factors
    INCOME = (
        (1, '<$15k'),
        (2, '$15k-$24.9k'),
        (3, '$25k-$34.9k'),
        (4, '$35k-$49.9k'),
        (5, '$50k or more'),
    )
    household_income = models.PositiveSmallIntegerField(choices=INCOME)

    BOOLEAN = ((1, 'Yes'), (0, 'No'))
    health_insurance = models.PositiveSmallIntegerField(choices=BOOLEAN)

    # Demographic Factors
    AGE = ((4, '<55'),(3, '55-64'),(2, '65-75'),(1, '75+'),)
    age = models.PositiveSmallIntegerField(choices=AGE)

    SEX = ((1, 'Female'),(2, 'Male'),(1, 'Other'),)
    sex = models.PositiveSmallIntegerField(choices=SEX)

    RACE = (
        (5, 'Non-Hispanic White'),
        (2, 'Non-Hispanic Black'),
        (1, 'Hispanic'),
        (4, 'Asian/Pacific Islander'),
        (3, 'Other'),
    )
    race = models.PositiveSmallIntegerField(choices=RACE, verbose_name="Race/Ethnicity")

    MARITAL = (
        (1, 'Living Alone'),
        (2, 'Married or Living with SO'),
    )
    marital_status = models.PositiveSmallIntegerField(choices=MARITAL)

    # Socioeconomic Factors
    EDUCATION = (
        (1, '<High School'),
        (1, 'Some High School'),
        (2, 'High School Grad or GED'),
        (2, 'Some College'),
        (3, 'College or More'),
    )
    education_level = models.PositiveSmallIntegerField(choices=EDUCATION)

    EMPLOYMENT = (
        (3, 'Employed/Self-employed'),
        (1, 'Not employed'),
        (4, 'Retired'),
        (2, 'Not in the workforce'),
    )
    employment_status = models.PositiveSmallIntegerField(choices=EMPLOYMENT)

    # Lifestyle Factors
    BOOLEAN = ((1, 'Yes'), (0, 'No'))
    physical_activity = models.PositiveSmallIntegerField(choices=BOOLEAN)
    alcohol_drinking = models.PositiveSmallIntegerField(choices=BOOLEAN)
    smoking_activity = models.PositiveSmallIntegerField(choices=BOOLEAN)
    weight = models.IntegerField(verbose_name="Weight (kg)")
    height = models.IntegerField(verbose_name="Height (m)")

    # Health Factors
    HEALTH_STATUS = ((4, 'Excellent'),(3, 'Good'),(2, 'Fair'),(1, 'Poor'),)
    general_health_status = models.PositiveSmallIntegerField(choices=HEALTH_STATUS)
    comorbidity = models.PositiveSmallIntegerField(choices=BOOLEAN, verbose_name="Other Health Conditions (Heart Attack, CHD, Stroke)")
    disability = models.PositiveSmallIntegerField(choices=BOOLEAN)

    other_info = models.TextField(default="")
    arrival_time = models.DateTimeField(default=timezone.now)

    # Result returned after survey
    crn_score = models.IntegerField(default=50)

    def body_mass_index(self):
        return (self.weight)/(self.height**2)

    def get_crn_score(self):
        """Calculated CRN likelihood score out of 100"""
        # self.crn_score = random.randrange(100)
        sum = (self.household_income + self.health_insurance + self.age +
              self.sex + self.race + self.marital_status + self.education_level +
              self.employment_status + self.physical_activity +
              self.alcohol_drinking + self.smoking_activity +
              self.general_health_status + self.comorbidity + self.disability)
        self.crn_score = (1-(sum/40)) * 100
        return self.crn_score

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
