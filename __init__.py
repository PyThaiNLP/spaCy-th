# coding: utf8
from __future__ import unicode_literals, print_function

from os import path

from ..language import Language
from ..attrs import LANG

from .language_data import *


class Thai(Language):
    lang = 'th'

    class Defaults(Language.Defaults):
        lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
        lex_attr_getters[LANG] = lambda text: 'th'

        tokenizer_exceptions = TOKENIZER_EXCEPTIONS
        #tag_map = TAG_MAP
        stop_words = STOP_WORDS