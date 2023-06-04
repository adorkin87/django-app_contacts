from .models import Requisites, Phones, OtherContacts


class Contacts:
    @staticmethod
    def get_contacts() -> dict:
        return {
            "requisites": Contacts.__get_requisites(),
            "phones": Contacts.__get_phones(),
            "other_contacts": Contacts.__get_other_contacts()
        }

    @staticmethod
    def __get_requisites() -> dict:
        requisites = {}
        query = Requisites.objects.select_related('company').all().in_bulk()
        for requisite in query.values():
            if 'company' not in requisites:
                requisites['company'] = requisite.company.name
            requisites[requisite.name] = requisite.value
        return requisites

    @staticmethod
    def __get_phones() -> dict:
        phones = {}
        for phone in Phones.objects.all():
            if phone.type == 'phone':
                if phone.type not in phones:
                    phones[phone.type] = []
                phones[phone.type].append({'phone': phone.phone,
                                           'call_tracking': phone.call_tracking,
                                           'call_tracking_class': phone.call_tracking_class})
            else:
                phones[phone.type] = phone.phone
        return phones

    @staticmethod
    def __get_other_contacts() -> dict:
        other_contacts = {}
        for contact in OtherContacts.objects.all():
            other_contacts[contact.type] = contact.contact
        return other_contacts
