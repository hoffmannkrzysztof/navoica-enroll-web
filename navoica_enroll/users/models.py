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
    name = CharField(_("Name of User"), blank=True, null=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class UserRegistrationCourse(models.Model):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    gender = models.CharField(_("Gender"), choices=[
        ('M', _('Male')),
        ('F', _('Female')),
    ], max_length=1)
    pesel = models.CharField(_("PESEL"), null=True, blank=True, max_length=11,
                             help_text=_(
                                 "For people who do not have a PESEL number, type in NONE."))
    age = models.SmallIntegerField(_("Age"), default=18)
    education = models.CharField(_("Education"), max_length=1,
                                 choices=[
                                     ('1', _('Pre-primary')),
                                     ('2', _('Primary')),
                                     ('3', _('Secondary')),
                                     ('4', _('High school')),
                                     ('5', _('Higher'))
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
    voivodeship = models.CharField(_("Voivodeship"), max_length=30, null=True,
                                   blank=True,
                                   choices=sorted(VOIVODESHIP_CHOICES,
                                                  key=lambda x: x[1]))
    county = models.CharField(_("County"), max_length=30, null=True, blank=True,
                              choices=sorted(ADMINISTRATIVE_UNIT_CHOICES,
                                             key=lambda x: x[1]))
    commune = models.CharField(_("Commune"), max_length=30, null=True,
                               blank=True)

    country = models.CharField(_("Country"), max_length=30, null=True,
                               blank=True)

    phone = models.CharField(_("Phone"), max_length=30, help_text=_(
        "Provide the contact telephone number."))
    email = models.CharField(_("E-mail"), max_length=254,
                             help_text=_("Enter the address mail for contact."))
    start_project_date = models.DateField(_("Start project date"),
                                          default=timezone.now)
    end_project_date = models.DateField(_("End project date"),
                                        default=timezone.now)
    start_support_date = models.DateField(_("Start support date"),
                                          default=timezone.now)

    STATUSES = [
        _("Employed"),
        _("Registered unemployed"),
        _("Unregistered unemployed"),
        _("Unemployed, not looking for work")
    ]

    status = models.CharField(_("Status"), max_length=1000,
                              choices=[(t, t) for t in STATUSES]
                              )

    PROFESSIONS = [
        _("Vocational teacher"),
        _("General education teacher"),
        _("Kindergarten teacher"),
        _("Employee in higher education institution"),
        _("Labor market institution employee"),
        _("Health care worker"),
        _("Farmer"),
        _("Key employee in social assistance and integration institution"),
        _("Employee in family and foster care support institution"),
        _("Employee in social economy support center"),
        _("Employee in psychological and pedagogical counseling center"),
        _("Practical vocational instructor"),
        _("Other"),
    ]

    profession = models.CharField(_("Profession"), max_length=1000,
                                  choices=[(t, t) for t in
                                           PROFESSIONS])

    work_name = models.CharField(_("Job title"), max_length=1000, help_text=_(
        "Abbreviations not allowed, full name of the institution"))
    origin = models.CharField(_("Migrant / ethnic minority"), max_length=1,
                              choices=[
                                  ('y', _("Yes")),
                                  ('n', _("No")),
                                  ('r', _("Prefer not to tell"))

                              ]
                              )
    homeless = models.CharField(_("Homeless"), max_length=1, choices=[
        ('y', _("Yes")),
        ('n', _("No")),
        ('r', _("Prefer not to tell"))

    ])
    disabled_person = models.CharField(_("Disabled person"), max_length=1,
                                       choices=[
                                           ('y', _("Yes")),
                                           ('n', _("No")),
                                           ('r', _("Prefer not to tell"))

                                       ])
    social_disadvantage = models.CharField(_("Socially disadvantaged"),
                                           max_length=1, choices=[
            ('y', _("Yes")),
            ('n', _("No")),
            ('r', _("Prefer not to tell"))

        ])

    course_id = models.CharField(max_length=1000)
    language_code = models.CharField(max_length=1000)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {} {}".format(self.course_id, self.user.first_name,
                                  self.user.last_name)

    class Meta:
        verbose_name = _("Registration for course")
        verbose_name_plural = _("Registrations for course")
