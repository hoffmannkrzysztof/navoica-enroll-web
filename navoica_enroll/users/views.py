import requests
from allauth.socialaccount.models import SocialToken
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.views.generic.edit import FormView

from .forms import UserRegistrationCourseForm

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


@method_decorator(login_required, name='dispatch')
class UserRegistrationCourseView(FormView):
    template_name = 'users/form_registration.html'
    form_class = UserRegistrationCourseForm
    success_url = '/thanks/'
    token = None
    course_info = None

    def dispatch(self, request, *args, **kwargs):
        social_token = SocialToken.objects.filter(
            account__user=self.request.user,
            account__provider='edx')

        self.token = social_token[0].token

        headers = {
            "Authorization": "Bearer " + self.token
        }

        response = requests.get(
            "{}{}{}".format(
                settings.NAVOICA_URL,
                "/api/courses/v1/courses/",
                self.kwargs['course_id']
            ),
            headers=headers)

        if response.status_code != 200:
            raise Http404(_("Course does not exist"))

        self.course_info = response.json()

        response = requests.get(
            "{}{}{}".format(
                settings.NAVOICA_URL,
                "/api/enrollment/v1/enrollment/",
                self.kwargs['course_id']
            ),
            headers=headers)

        self.success_url = "{}/courses/{}".format(
            settings.NAVOICA_URL,
            self.course_info['course_id']
        )

        course_enrollment = response.text
        if course_enrollment != "":
            raise Http404(_("Already enrollment for this course"))

        return super(UserRegistrationCourseView, self).dispatch(request, *args,
                                                                **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_info'] = self.course_info
        return context

    def form_valid(self, form):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        requests.post(
            "{}{}".format(
                settings.NAVOICA_URL,
                "/api/enrollment/v1/enrollment",
            ),
            json={
                "course_details": {"course_id": self.course_info['course_id']}},
            headers=headers)

        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.course_id = self.course_info['course_id']
        obj.save()

        return super().form_valid(form)
