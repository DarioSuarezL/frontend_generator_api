from tortoise import fields, models
import uuid

class Desing(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    data = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return "Desing ID:" + self.id

    class Meta:
        table = "desings"
