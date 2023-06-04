from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Companies(SingletonModel):
    name = models.CharField(max_length=100, verbose_name='Company')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Requisites(models.Model):
    company = models.ForeignKey(to=Companies, on_delete=models.PROTECT, related_name='requisites')
    name = models.CharField(max_length=50, verbose_name='Name')
    value = models.CharField(max_length=100, verbose_name='Value')
    active = models.BooleanField(db_index=True, default=False, verbose_name='Active')

    class Meta:
        verbose_name_plural = 'Requisites'


class Phones(models.Model):
    type_phones = (
        ('phone', 'phone'),
        ('wa', 'whatsapp'),
        ('tg', 'telegram'),
    )

    company = models.ForeignKey(to=Companies, on_delete=models.PROTECT, related_name='phones')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    type = models.CharField(max_length=10, choices=type_phones, verbose_name='Type phone')
    call_tracking = models.BooleanField(null=True, blank=True, default=False, verbose_name='Call tracking')
    call_tracking_class = models.CharField(max_length=20, null=True, blank=True, verbose_name='Class for call tracking')
    active = models.BooleanField(db_index=True, default=False, verbose_name='Active')

    class Meta:
        verbose_name_plural = 'Phones'


class OtherContacts(models.Model):
    type_contact = (
        ('mail', 'mail'),
        ('insta', 'instagram'),
        ('vk', 'vk'),
        ('ok', 'ok')
    )

    company = models.ForeignKey(to=Companies, on_delete=models.PROTECT, related_name='other_contacts')
    contact = models.CharField(max_length=50, verbose_name='Contact')
    type = models.CharField(max_length=15, choices=type_contact, verbose_name='Type contact')
    active = models.BooleanField(db_index=True, default=False, verbose_name='Active')

    class Meta:
        verbose_name_plural = 'Other contacts'
