from tortoise import fields, models
import uuid


class Meeting(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    title = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    design = fields.TextField(default="")

    users = fields.ManyToManyField(
        "models.User", related_name="meetings", through="user_meeting"
    )

    owner = fields.ForeignKeyField("models.User", related_name="owned_meetings")

    def __str__(self):
        return self.title + " - " + self.id

    class Meta:
        table = "meetings"
