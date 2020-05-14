from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Div, Fieldset, HTML, Layout, \
    Submit
from django.conf import settings
from django.contrib.auth import forms, get_user_model
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.exceptions import ValidationError
from django.forms import BooleanField, EmailField, ModelForm, TextInput
from django.utils.translation import ugettext_lazy as _
from localflavor.pl.forms import PLPESELField, PLPostalCodeField

from .models import UserRegistrationCourse

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class UserRegistrationCourseFormBase(ModelForm):
    pesel = PLPESELField(max_length=11, label=_("PESEL"),
                         widget=TextInput(attrs={'type': 'number'}))
    postal_code = PLPostalCodeField(label=_("Postal code"))
    email = EmailField(label=_("E-mail address"))

    statement1 = BooleanField(required=True)
    statement2 = BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserRegistrationCourseFormBase, self).__init__(*args, **kwargs)

        self.fields['statement1'].label = _(
            "I agree with the project participant's declaration. <a href='{url}'>PDF</a>").format(
            url=
            static(settings.STATEMENT1_PDF))

        self.fields['statement2'].label = _(
            "I consent to the processing of my personal data to participate in the project. <a href='{url}'>PDF</a>").format(
            url=
            static(settings.STATEMENT2_PDF))

        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Fieldset(
                '',
                HTML('<p class="h4 mt-5">{}</p><hr/>'.format(
                    _("Participant details"))),
                Div(
                    Div('first_name',
                        css_class="col-md-6 mb-3"
                        ),
                    Div(
                        'last_name',
                        css_class="col-md-6 mb-3"
                    ),
                    css_class="row"
                ),
                Div(
                    Div('gender',
                        css_class="col-md-4 mb-4"
                        ),
                    Div(
                        'pesel',
                        css_class="col-md-6 mb-4"
                    ),
                    Div(
                        'age',
                        css_class="col-md-2 mb-2"
                    ),
                    css_class="row"
                ),
                'education',
                HTML('<p class="h4 mt-5">{}</p><hr/>'.format(
                    _("Contact details"))),
                Div(
                    Div('street',
                        css_class="col-md-6 mb-4"
                        ),
                    Div('street_no',
                        css_class="col-md-2 mb-2"
                        ),
                    Div(
                        'street_building_no',
                        css_class="col-md-2 mb-2"
                    ),
                    Div(
                        'postal_code',
                        css_class="col-md-2 mb-2"
                    ),
                    css_class="row"
                ),

                Div(
                    Div('city',
                        css_class="col-md-3 mb-3"
                        ),
                    Div(
                        'voivodeship',
                        css_class="col-md-3 mb-3"
                    ),
                    Div(
                        'county',
                        css_class="col-md-3 mb-3"
                    ),
                    Div(
                        'commune',
                        css_class="col-md-3 mb-3"
                    ),
                    css_class="row"
                ),

                Div(
                    Div('phone',
                        css_class="col-md-6 mb-3"
                        ),
                    Div(
                        'email',
                        css_class="col-md-6 mb-3"
                    ),
                    css_class="row"
                ),
                HTML('<p class="h4 mt-5">{}</p><hr/>'.format(
                    _("Details and type of support"))),
                Div(
                    Div('start_project_date',
                        css_class="col-md-4 mb-4"
                        ),
                    Div(
                        'end_project_date',
                        css_class="col-md-4 mb-4"
                    ),
                    Div(
                        'start_support_date',
                        css_class="col-md-4 mb-4"
                    ),
                    css_class="row"
                ),

                Div(
                    Div('status',
                        css_class="col-md-4 mb-4"
                        ),
                    Div(
                        'profession',
                        css_class="col-md-4 mb-4"
                    ),
                    Div(
                        'work_name',
                        css_class="col-md-4 mb-4"
                    ),
                    css_class="row"
                ),

                Div(
                    Div('origin',
                        css_class="col-md-3 mb-3"
                        ),
                    Div(
                        'homeless',
                        css_class="col-md-3 mb-3"
                    ),
                    Div(
                        'disabled_person',
                        css_class="col-md-3 mb-3"
                    ),
                    Div(
                        'social_disadvantage',
                        css_class="col-md-3 mb-3"
                    ),
                    css_class="row"
                ),

            ),
            HTML("<hr/>"),

            'statement1', 'statement2',

            HTML("<hr/>"),
            ButtonHolder(
                Submit('submit',
                       _("Send the form and register me for the course"),
                       css_class='button white w-100')
            ),
            HTML("<br/>"),
        )

    class Meta:
        model = UserRegistrationCourse
        exclude = ('user', 'course_id')


class UserRegistrationCourseForm(UserRegistrationCourseFormBase):
    pass


class UserRegistrationCourseEnglishForm(UserRegistrationCourseFormBase
                                        ):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationCourseEnglishForm, self).__init__(*args, **kwargs)
        self.fields['pesel'].required = False
        self.fields['voivodeship'].required = False
        self.fields['county'].required = False
        self.fields['commune'].required = False
