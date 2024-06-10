from djongo import models


class BaseModel:
    _id = models.ObjectIdField(primary_key=True)

    @property
    def id(self):
        return self._id