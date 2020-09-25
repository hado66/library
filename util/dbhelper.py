from mysqlmapper.facade import MVCHolder

from library.settings import DATABASES

MVC_HOLDER = MVCHolder(
    DATABASES['default']["HOST"],
    DATABASES['default']["USER"],
    DATABASES['default']["PASSWORD"],
    DATABASES['default']["NAME"],
)
