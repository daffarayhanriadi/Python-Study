"""
maksud dari . disini adalah sains itu sendiri

kita dapat mengatur urutan/struktur dari packages menggunakan __init__.py

__init__.py disini menjelaskan bahwa matematika adalah anak dari sains
"""
# Main Package
# from . import matematika # sains.matematika.function()
# from . import fisika # sains.fisika.function()

# from .matematika import kali # sains.kali()

# Sub Package
from . import matematika
from . import fisika

# Hanya berfungsi jika menggunakan * saat melakukan import, namun penggunaan ini tidak disarankan
# __all__ = [
#     "matematika",
#     "fisika"
# ]