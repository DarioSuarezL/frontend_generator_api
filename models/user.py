from tortoise import fields, models

class User(models.Model):
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)

    def __str__(self):
        return self.name + ' ' + self.email

    class Meta:
        table = 'users'