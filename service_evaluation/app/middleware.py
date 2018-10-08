from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from social_django.middleware import SocialAuthExceptionMiddleware
from social_core.exceptions import SocialAuthBaseException, AuthCanceled
class RedirectSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if isinstance(exception, AuthCanceled):
            return HttpResponseRedirect(reverse('index'))
        else:
            raise exception
