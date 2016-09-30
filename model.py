import datetime
from mongoengine import Document, DateTimeField, BooleanField, StringField


class BaseDocument(Document):

    meta = {'allow_inheritance': True,
            'abstract': True}

    created_at = DateTimeField()
    updated_at = DateTimeField(default=datetime.datetime.utcnow)
    is_deleted = BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
        return super(BaseDocument, self).save(*args, **kwargs)

    def to_dict(self):
        dic = self.to_mongo().to_dict()
        dic.pop('_cls')
        dic['id'] = str(dic.pop('_id'))
        return dic


class PluginException(BaseDocument):

    message = StringField()
    stacktrace = StringField()
    document= StringField()