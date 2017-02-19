from django.db import models


class Recipe(models.Model):
    SKILL_LEVELS = (
        ('N', 'Novice'),
        ('B', 'Beginner'),
        ('E', 'Experienced'),
        ('M', 'Master'),
    )
    STAR_RATINGS = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=250)
    preparation_time = models.CharField(max_length=10)
    cooking_time = models.CharField(max_length=10)
    serves = models.SmallIntegerField()
    freezable = models.CharField(max_length=10)
    skill_level = models.CharField(max_length=1, choices=SKILL_LEVELS)
    star_rating = models.SmallIntegerField(default=0, choices=STAR_RATINGS)
    main_image = models.FileField(null=True, blank=True)
    # serialized fields:
    ingredients = models.TextField(default='#First ingredient.\n#Second ingredient.')
    instructions = models.TextField(default='#1 First instruction\n#2 Second instruction. (fig. A)')
    image_a = models.FileField(null=True, blank=True)
    image_b = models.FileField(null=True, blank=True)
    image_c = models.FileField(null=True, blank=True)
