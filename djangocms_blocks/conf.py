# -*- coding: utf-8 -*-

from appconf import AppConf

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _


class Djangocms_blocksConf(AppConf):
    pass

    class Meta:
        prefix = 'djangocms_blocks'