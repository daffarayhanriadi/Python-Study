"""
maksud dari . disini adalah matematika itu sendiri

Digunakan agar matematika dapat melakukan import

__init__.py disini menjelaskan bahwa basic dan scientific adalah anak dari matematika
"""

from . import basic # sains.matematika.basic.function()
from . import scientific # sains.matematika.basic.function()

from .basic import tambah, kali # sains.matematika.function()
from .scientific import pangkat # sains.scientific.function()

