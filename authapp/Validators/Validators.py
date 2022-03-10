from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _


def validate_image(image):
    if image:
        if image.size > 3 * 1024 * 1024:
            raise ValidationError(
            _("%(image)s isn*t "),
            params={'value': image},
            )
def validate_login_title(value):
    if not value.istitle():
        raise ValidationError(
            _("%(value)s isn*t Title"),
            params={'value': value},
        )



