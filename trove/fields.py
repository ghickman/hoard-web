from django.conf import settings
from django.utils.encoding import force_unicode
from picklefield.fields import _ObjectWrapper, PickledObject, PickledObjectField, dbsafe_encode, dbsafe_decode
from SimpleAES import SimpleAES


# TODO: Update when this gets updated https://github.com/gintas/django-picklefield/pull/4


aes = SimpleAES(settings.SECRET_KEY)


def dbsafe_encode_aes(value, *args, **kwargs):
    pickled = dbsafe_encode(value, *args, **kwargs)
    return PickledObject(aes.base64_encrypt(pickled))


def dbsafe_decode_aes(value, *args, **kwargs):
    return dbsafe_decode(aes.base64_decrypt(value), *args, **kwargs)


class AESPickledObjectField(PickledObjectField):
    def get_db_prep_value(self, value, connection=None, prepared=False):
        if value is not None and not isinstance(value, PickledObject):
            value = force_unicode(dbsafe_encode_aes(value, self.compress, self.protocol))
        return value

    def to_python(self, value):
        if value is not None:
            try:
                value = dbsafe_decode_aes(value, self.compress)
            except:
                if isinstance(value, PickledObject):
                    raise
            else:
                if isinstance(value, _ObjectWrapper):
                    return value._obj
        return value


