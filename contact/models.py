from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    """
    Contacts model, which stores contact information.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def get_contact_full_name(self):
        """
        Returns contact full name.
        """
        return f"{self.first_name} {self.last_name}"


class ContactNumber(models.Model):
    """
    Contact number model, which stores contact numbers.
    """
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='contact_numbers')
    LABELS = (
        ('home', 'Home'),
        ('work', 'Work'),
        ('mobile', 'Mobile'),
        ('other', 'Other'),
    )
    label = models.CharField(max_length=16, choices=LABELS, default='other')
    number = PhoneNumberField()
