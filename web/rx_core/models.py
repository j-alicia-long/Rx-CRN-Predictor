from django.db import models

import random #placeholder for CRN score

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    # middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    # # Financial Factors
    # INCOME = (
    #     (1, '<$15k'),
    #     (2, '$15k-$24.9k'),
    #     (3, '$25k-$34.9k'),
    #     (4, '$35k-$49.9k'),
    #     (5, '$50k or more'),
    # )
    # household_income = models.PositiveSmallIntegerField(choices=INCOME)
    #
    # health_insurance = models.TextChoices('Health Insurance', 'YES NO')
    #
    # # Demographic Factors
    # age = models.TextChoices('Age', '<55 55-64 65-75 75+')
    # sex = models.TextChoices('Sex', 'Male Female Other')
    # race = models.TextChoices('Race/Ethnicity', 'White Black Asian Hispanic Other')
    # marital_status = models.TextChoices('Marital Status', 'Single Married')
    #
    # # Socioeconomic Factors
    # EDUCATION = (
    #     (1, '<High School'),
    #     (2, 'Some High School'),
    #     (3, 'High School Grad or GED'),
    #     (4, 'Some College'),
    #     (5, 'College or More'),
    # )
    # education_level = models.PositiveSmallIntegerField(choices=EDUCATION)
    #
    # EMPLOYMENT = (
    #     (4, 'Employed/Self-employed'),
    #     (3, 'Not employed'),
    #     (2, 'Retired'),
    #     (1, 'Not in the workforce'),
    # )
    # employment_status = models.PositiveSmallIntegerField(choices=EMPLOYMENT)
    #
    # # Lifestyle Factors
    # physical_activity = models.TextChoices('Exercise', 'YES NO')
    # alcohol_drinking = models.TextChoices('Drinking', 'YES NO')
    # smoking_activity = models.TextChoices('Smoking', 'YES NO')
    # weight = models.IntegerField()
    # height = models.IntegerField()
    #
    # # Health Factors
    # general_health_status = models.TextChoices('General Health', 'EXCELLENT GOOD FAIR POOR')
    # comorbidities = models.TextChoices('Other Health Conditions', 'YES NO')
    # disability = models.TextChoices('Disability', 'YES NO')
    #
    #
    # def body_mass_index(self):
    #     return {self.weight}/({self.height}**2)

    crn_score = models.IntegerField()

    def get_crn_score(self):
        """Calculated CRN likelihood score out of 100"""
        self.crn_score = random.randrange(100)
        return self.crn_score

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
