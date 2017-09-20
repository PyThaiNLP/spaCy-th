# coding: utf8
from __future__ import unicode_literals, print_function

from os import path

from ..language import Language, BaseDefaults
from ..attrs import LANG
from ..tokenizer import Tokenizer
from ..tokens import Doc
from .language_data import *
class ThaiTokenizer(object):
    def __init__(self, cls, nlp=None):
        self.vocab = nlp.vocab if nlp is not None else cls.create_vocab(nlp)
        try:
            from pythainlp.tokenize import word_tokenize
        except ImportError:
            raise ImportError("The Thai tokenizer requires the PyThaiNLP library: "
                              "https://github.com/wannaphongcom/pythainlp/")
        self.tokenizer = word_tokenize

    def __call__(self, text):
        words = [x for x in self.tokenizer(text)]
        return Doc(self.vocab, words=words, spaces=[False]*len(words))

class ThaiDefaults(BaseDefaults):
	lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
	lex_attr_getters[LANG] = lambda text: 'th'
	tokenizer_exceptions = TOKENIZER_EXCEPTIONS
	tag_map = TAG_MAP
	stop_words = STOP_WORDS
	@classmethod
	def create_tokenizer(cls, nlp=None):
		return ThaiTokenizer(cls, nlp)

class Thai(Language):
	lang = 'th'
	Defaults = ThaiDefaults
	def make_doc(self, text):
		words = self.tokenizer(text)
		return Doc(self.vocab, words=words, spaces=[False]*len(words))