import random
from io import BytesIO
from typing import Any

from qrcode import make
from qrcode.image.pil import PilImage

from providers.models import Provider


def set_debt(obj: Provider) -> Any:
    """
    Sets debt after debt reduction.
    """
    reduction_value = random.randint(100, 10000)
    obj.debt = max(obj.debt - reduction_value, 0)


def make_qr_code(value: str) -> PilImage:
    """
    Makes a qr code for the contacts of the provider
    """
    return make(value, box_size=10, border=1)


def convertPillToPng(image) -> bytes:
    """
    Convert PillImage to bytes(PNG)
    """
    with BytesIO() as f:
        image.save(f, format='PNG')
        return f.getvalue()
