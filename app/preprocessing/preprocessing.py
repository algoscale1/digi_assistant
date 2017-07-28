import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from nltk.corpus import stopwords


class Preprocessing:

    def __init__(self):
        pass

    @staticmethod
    def get_pos_tags(text):
        """

        :param text:
        :return:
        """

        sent_tokenize_list = sent_tokenize(text)

        # removing punctuations from sentence
        exclude = set(string.punctuation)
        sent_list = []
        for sent in sent_tokenize_list:
            sent_list.append(''.join(ch for ch in sent if ch not in exclude))

        # tokenizing words
        word_tokenized = []
        for sent in sent_list:
            word_tokenized.extend(word_tokenize(sent))

        # removing stopwords
        stop = set(stopwords.words('english'))
        word_tokens = [word.lower() for word in word_tokenized if word.lower() not in stop]

        # getting post tags from sentences
        pos_noun_tags = []
        pos_adj_tags = []
        pos_verb_tags = []
        for word, pos in nltk.pos_tag(word_tokens):
                    if pos in ['NN',"NNP", "NNS"]:
                        pos_noun_tags.append(word)
                    elif pos in ['JJ', 'JJR', 'JJS']:
                        pos_adj_tags.append(word)
                    elif pos in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                        pos_verb_tags.append(word)


        return pos_noun_tags, pos_adj_tags, pos_verb_tags








