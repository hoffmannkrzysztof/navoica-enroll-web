from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from django.utils.translation import ugettext_lazy as _


class EdxAccount(ProviderAccount):
    def get_profile_url(self):
        if self.account.extra_data['profile_image']['has_image']:
            return self.account.extra_data['image_url_full']


class EdxProvider(OAuth2Provider):
    id = 'edx'
    name = _("Log in to Navoica.pl")
    account_class = EdxAccount

    def get_default_scope(self):
        return ['profile', 'email', 'permissions', 'default']

    def extract_uid(self, data):
        """Extract uid ('id') and ensure it's a str."""
        return str(data['username'])

    def extract_common_fields(self, data):
        return dict(
            email=data.get('email'),
            username=data.get('username'),
            name=data.get('name'),
            user_id=data.get('id'),
        )


provider_classes = [EdxProvider]
