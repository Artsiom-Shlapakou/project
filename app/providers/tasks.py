import random
from config.celery import app
from celery import shared_task
from django.db.models import F
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives

from providers.models import Provider
from providers.utils import set_debt, convertPillToPng, make_qr_code

@app.task
def reduce_debt():
    objects_with_debt = Provider.objects.filter(debt_gt=0)
    [set_debt(obj) for obj in objects_with_debt]
    Provider.objects.bulk_update(objects_with_debt, ["debt"])


@app.task
def increase_debt():
    increasion_value = random.randint(5, 500)
    # This condition is True for objects exlude Factory because Factoty cannot have a debt
    Provider.objects.filter(provider__isnull=False).update(debt=F('debt') + increasion_value)


@shared_task(bind=True)
def send_qr_code_to_email(self, id):
    """
    Send The QR code to the employee's email
    """
    provider = Provider.objects.get(pk=id)
    contacts = provider.contacts
    tmp_contacts = f'Email:{contacts.email} Address: {contacts.address}'

    qr_code = make_qr_code(tmp_contacts)
    msg = EmailMultiAlternatives(
        subject=f'QR-code with {provider.name} contacts',
        to=request ["email"]
    )

    image = convertPillToPng(qr_code)
    img = MIMEImage(image)
    img.add_header('Content-ID', '<{name}>'.format(name='image'))
    img.add_header('Content-Disposition', 'inline', filename='qr-code.jpg')
    msg.attach(img)
    msg.send()
