from tortoise import fields, models
import uuid


class Meeting(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    title = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    users = fields.ManyToManyField(
        "models.User",
        related_name="meetings",
        through="user_meeting"
    )

    design = fields.ForeignKeyField(
        "models.Desing",
        related_name="meeting",
        unique=True,
    )

    def __str__(self):
        return self.title + " - " + self.id

    class Meta:
        table = "meetings"
