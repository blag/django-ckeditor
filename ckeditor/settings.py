from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.functional import lazy


def url_reverse(pattern):
	return reverse(pattern)


lazy_reverse = lazy(reverse, str)


TIMESTAMP = 'D6HM'


DEFAULT_CONFIG = {
    'skin': 'moonocolor',
    'toolbar': 'Full',
    'height': 291,
    'width': 835,
    'autoUpdateElement': True,
    'filebrowserWindowWidth': 940,
    'filebrowserWindowHeight': 725,
    'filebrowserUploadUrl': lazy_reverse('ckeditor_upload'),
    'filebrowserBrowseUrl': lazy_reverse('ckeditor_browse'),
    'disableNativeSpellChecker': False,
    'allowedContent': True,
}


#: If CKEDITOR_DEBUG=True, uses the unminified version of files
CKEDITOR_DEBUG = getattr(settings, 'CKEDITOR_DEBUG', False)
MEDIA_ROOT = getattr(settings, 'CKEDITOR_MEDIA_ROOT', getattr(settings, 'MEDIA_ROOT', ''))

CONFIGS = getattr(settings, 'CKEDITOR_CONFIGS', None)

THUMBNAIL_SIZE = getattr(settings, 'CKEDITOR_THUMBNAIL_SIZE', (75, 75))
JQUERY_OVERRIDE_VAL = getattr(settings, 'CKEDITOR_JQUERY_OVERRIDE_VAL', True)
RESTRICT_BY_USER = getattr(settings, 'CKEDITOR_RESTRICT_BY_USER', False)
UPLOAD_PATH = getattr(settings, 'CKEDITOR_UPLOAD_PATH', None)
UPLOAD_PREFIX = getattr(settings, 'CKEDITOR_UPLOAD_PREFIX', None)
MEDIA_PREFIX = getattr(settings, 'CKEDITOR_MEDIA_PREFIX', settings.STATIC_URL)
PNG_TO_JPEG = getattr(settings, 'CKEDITOR_PNG_TO_JPEG', False)
