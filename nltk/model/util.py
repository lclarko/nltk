# Natural Language Toolkit: Language Model Unit Tests
#
# Copyright (C) 2001-2016 NLTK Project
# Author: Ilia Kurenkov <ilia.kurenkov@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

from nltk.util import ngrams, everygrams, pad_sequence

NEG_INF = float("-inf")
POS_INF = float("inf")

NGRAMS_KWARGS = {
    "pad_left": True,
    "pad_right": True,
    "left_pad_symbol": "<s>",
    "right_pad_symbol": "</s>"
}


def padded_everygrams(sequence, order, **padding_kwargs):
    """Pads sequence *before* generating everygrams, not during."""
    padded = list(pad_sequence(sequence, order, **padding_kwargs))
    return everygrams(padded, max_len=order)


def default_ngrams(order, only_ngrams=False):
    """Provides defaults for nltk.util.ngrams"""

    def to_ngrams(sequence):
        """Wrapper around util.ngrams with usefull options saved during initialization.

        :param sequence: same as nltk.util.ngrams
        :type sequence: any iterable
        """
        if only_ngrams:
            return ngrams(sequence, order, **NGRAMS_KWARGS)

        return padded_everygrams(sequence, order, **NGRAMS_KWARGS)

    return to_ngrams


def mask_oov_words_in_corpus(corpus, ngram_vocab):
    """Replace all out-of-vocabulary words in a corpus label for unknowns."""
    return [ngram_vocab.lookup(sent) for sent in corpus]
