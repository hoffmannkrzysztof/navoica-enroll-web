from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from localflavor.pl.pl_administrativeunits import ADMINISTRATIVE_UNIT_CHOICES
from localflavor.pl.pl_voivodeships import VOIVODESHIP_CHOICES


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class UserRegistrationCourse(models.Model):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    gender = models.CharField(_("Gender"), choices=[
        ('M', _('Male')),
        ('F', _('Female')),
    ], max_length=1)
    pesel = models.CharField(_("Pesel"), max_length=11, help_text=_(
        "For people who do not have a PESEL number, type in NONE."))
    age = models.SmallIntegerField(_("Age"), default=18, help_text=_(
        "Enter your age when joining the project"))
    education = models.CharField(_("Education"), max_length=1,
                                 choices=[
                                     ('1', 'podstawowe'),
                                     ('2', 'gimnazjalne'),
                                     ('3', 'policealne'),
                                     ('4', 'pomaturalne'),
                                     ('5', 'wyższe I stopnia licencjat'),
                                     ('6', 'wyższe I stopnia inżynier'),
                                     ('7', 'wyższe II stopnia'),
                                     ('8', 'doktorat'),
                                 ]
                                 )
    street = models.CharField(_("Street"), max_length=300,
                              help_text=_("Enter the address correspondence."))
    street_no = models.CharField(_("Street no"), max_length=10,
                                 help_text=_("May contain letters"))
    street_building_no = models.CharField(_("Building no"), max_length=10,
                                          help_text=_("May contain letters"))
    postal_code = models.CharField(_("Postal code"), max_length=6)
    city = models.CharField(_("City"), max_length=30)
    voivodeship = models.CharField(_("Voivodeship"), max_length=30,
                                   choices=VOIVODESHIP_CHOICES)
    county = models.CharField(_("County"), max_length=30,
                              choices=ADMINISTRATIVE_UNIT_CHOICES)
    commune = models.CharField(_("Commune"), max_length=30)
    phone = models.CharField(_("Phone"), max_length=30, help_text=_(
        "Provide the contact telephone number."))
    email = models.CharField(_("E-mail"), max_length=30,
                             help_text=_("Enter the address mail for contact."))
    start_project_date = models.DateField(_("Start project date"),
                                          default=timezone.now)
    end_project_date = models.DateField(_("End project date"),
                                        default=timezone.now)
    start_support_date = models.DateField(_("Start support date"),
                                          default=timezone.now)
    status = models.CharField(_("Status"), max_length=1,
                              choices=[
                                  ('e', 'Unemployment'),
                                  ('n', 'No working'),
                                  ('w', 'Working'),
                              ]
                              )
    profession = models.CharField(_("Profession"), max_length=1000)
    work_name = models.CharField(_("Work name"), max_length=1000, help_text=_(
        "Abbreviations not allowed, full name of the institution"))
    origin = models.CharField(_("Origin"), max_length=1,
                              choices=[
                                  ('y', _("Yes")),
                                  ('n', _("No")),
                                  ('r', _("Refusal"))

                              ]
                              )
    homeless = models.CharField(_("Homeless"), max_length=1, choices=[
        ('y', _("Yes")),
        ('n', _("No")),
        ('r', _("Refusal"))

    ])
    disabled_person = models.CharField(_("Disabled person"), max_length=1,
                                       choices=[
                                           ('y', _("Yes")),
                                           ('n', _("No")),
                                           ('r', _("Refusal"))

                                       ])
    social_disadvantage = models.CharField(_("Social disadvantage"),
                                           max_length=1, choices=[
            ('y', _("Yes")),
            ('n', _("No")),
            ('r', _("Refusal"))

        ])

    course_id = models.CharField(max_length=1000)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {} {}".format(self.course_id, self.user.first_name,
                                  self.user.last_name)

    class Meta:
        verbose_name = _("Registration for course")
        verbose_name_plural = _("Registrations for course")
