from django.conf import settings
from django.utils.encoding import force_unicode
from picklefield.fields import _ObjectWrapper, PickledObject, PickledObjectField, dbsafe_encode, dbsafe_decode
from rest_framework.relations import HyperlinkedIdentityField, ManyRelatedField, HyperlinkedRelatedField
from rest_framework.reverse import reverse
from SimpleAES import SimpleAES


class DeploymentURLField(HyperlinkedIdentityField):
    def field_to_native(self, obj, field_name):
        request = self.context.get('request', None)
        format = self.context.get('format', None)
        view_name = self.view_name or self.parent.opts.view_name
        kwargs = {'name': obj.project.name, 'env_name': obj.env.name}
        return reverse(view_name, kwargs=kwargs, request=request, format=format)


class PairsField(ManyRelatedField):
    def field_to_native(self, obj, field_name):
        value = getattr(obj, field_name)
        items = {}
        [items.update(self.to_native(item)) for item in value.all()]
        return items

    def to_native(self, value):
        return {value.key: value.value}


class SlugHyperlinkedRelatedField(HyperlinkedRelatedField):
    slug_field = 'name'


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


