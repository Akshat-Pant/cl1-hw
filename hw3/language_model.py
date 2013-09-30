from math import log, exp
from collections import defaultdict

from numpy import mean

import nltk
from nltk import FreqDist
from nltk.util import bigrams

kLM_ORDER = 2
kUNK_CUTOFF = 3
kNEG_INF = -1e6

kSTART = "<s>"
kEND = "</s>"



class BigramLanguageModel:

    def __init__(self, unk_cutoff, jm_lambda=0.5, dirichlet_alpha=0.1,
                 katz_cutoff=5, kn_discount=0.1, py_a=0.1, py_b=0.1):
        self._unk_cutoff = unk_cutoff
        self._jm_lambda = 0.5
        self._vocab_final = False

    def train_seen(self, word, count=1):
        """
        Tells the language model that a word has been seen @count times.  This
        will be used to build the final vocabulary.
        """
        assert not self._vocab_final, \
            "Trying to add new words to finalized vocab"

        None

    def vocab_lookup(self, word):
        """
        Given a word, provides a vocabulary representation.  Words under the
        cutoff threshold shold have the same value.  All words with counts
        greater than or equal to the cutoff should be unique and consistent.
        """
        assert self._vocab_final, \
            "Vocab must be finalized before looking up words"

        return -1

    def finalize(self):
        """
        Fixes the vocabulary as static, prevents keeping additional vocab from
        being added
        """
        self._vocab_final = True

    def censor(self, sentence):
        """
        Given a sentence, yields a sentence suitable for training or testing.
        Prefix the sentence with <s>, replace words not in the vocabulary with
        <UNK>, and end the sentence with </s>.
        """
        yield self.vocab_lookup(kSTART)
        for ii in sentence:
            yield self.vocab_lookup(ii)
        yield self.vocab_lookup(kEND)

    def mle(self, context, word):
        """
        Return the log MLE estimate of a word given a context.
        """

        return 0.0

    def laplace(self, context, word):
        """
        Return the log MLE estimate of a word given a context.
        """

        return 0.0

    def dirichlet(self, context, word):
        """
        Return the log Jelinek-Mercer estimate of a word given a context;
        interpolates context probability with the overall corpus probability.
        """

        return 0.0

    def jelinek_mercer(self, context, word):
        """
        Return the log Jelinek-Mercer estimate of a word given a context;
        interpolates context probability with the overall corpus probability.
        """

        return 0.0

    def add_train(self, sentence):
        """
        Add the counts associated with a sentence.
        """

        # You'll need to complete this function, but here's a line of code that
        # will hopefully get you started.
        for context, word in bigrams(self.censor(sentence)):
            None

    def perplexity(self, sentence, method):
        try:
            return exp(-1.0 * mean([method(context, word) for context, word \
                                        in bigrams(self.censor(sentence))]))
        except OverflowError:
            return kNEG_INF

if __name__ == "__main__":
    lm = BigramLanguageModel(kUNK_CUTOFF)

    for ii in nltk.corpus.brown.words():
        lm.train_seen(ii)

    lm.finalize()

    for ii in nltk.corpus.brown.sentences():
        lm.add_train(ii)

    for ii in nltk.corpus.treebank.sents():
        scores = (lm.perplexity(ii, lm.mle),
                  lm.perplexity(ii, lm.laplace),
                  lm.perplexity(ii, lm.dirichlet))
        print(scores, " ".join(ii))