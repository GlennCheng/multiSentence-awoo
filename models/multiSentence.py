from collections import Counter, namedtuple
import numpy as np


##
# for calculate Diversity
def __diversity(Pi, P, cluster, k=3):
    s = 0
    for j in range(1, k, 1):
        if not (Pi in P and Pi in cluster[j]):
            s = s + 1
    return s / len(P)


##
# for calculate Coverage
def __coverage(Pi, P):
    TWIDF = 1
    s = 0
    if Pi in P:
        s = s + TWIDF
    return s / len(P)


##
# for calculate Fluency
def __fluency(Pi, P, N=3):
    s = 0
    for i in range(1, len(P), 1):
        probabilityPitem = 0.7
        s = s + np.math.log(probabilityPitem)
    return s / N


##
# for calculate w'
def __w1(Pi, Pj, P, custer):
    sigma = 0
    fPi = 0
    fPj = 0

    for list in custer:
        fPi = fPi + list.count(Pi)
        fPj = fPj + list.count(Pj)

    for P in custer:
        if Pi in P and Pj in P:
            sigma = sigma + 1 / (abs(P.index(Pi) - P.index(Pj)))

    return (fPi + fPj) / sigma


##
# for calculate w''
def __w2(Pi, Pj, P, custer):
    fPi = 0
    fPj = 0

    for list in custer:
        fPi = fPi + list.count(Pi)
        fPj = fPj + list.count(Pj)

    if Pi in P and Pj in P:
        d = abs(P.index(Pi) - P.index(Pj))

    return (fPi * fPj) / d * d


##
# for calculate w'''
def __w3(Pi, Pj, P, custer):
    return __w1(Pi, Pj, P, custer) / __w2(Pi, Pj, P, custer)


##
# for calculate W
def __W(Pi, Pi2, P, custer):
    sigma = 0
    for i in range(1, len(P) - 1, 1):
        sigma = sigma + __w3(Pi, Pi2, P, custer)

    return sigma


##
# for calculate score
def score(Pi: str, Pi2: str, P: list, custer: np.array):
    return __W(Pi, Pi2, P, custer) / (len(P) * __fluency(Pi, P) * __coverage(Pi, P) * __diversity(Pi, P, custer))


def __word_feats(words):
    return dict.fromkeys(words.split(), True)


##
# for calculate n-gram
def __ngram(documents, N=3):
    ngram_prediction = dict()
    total_grams = list()
    words = list()
    Word = namedtuple('Word', ['word', 'prob'])

    for doc in documents:
        print(doc)
        split_words = ['<s>', doc, '</s>']
        # 計算分子
        [total_grams.append(tuple(split_words[i:i + N])) for i in range(len(split_words) - N + 1)]
        # 計算分母
        [words.append(tuple(split_words[i:i + N - 1])) for i in range(len(split_words) - N + 2)]

    total_word_counter = Counter(total_grams)
    word_counter = Counter(words)

    for key in total_word_counter:
        word = ''.join(key[:N - 1])
        if word not in ngram_prediction:
            ngram_prediction.update({word: set()})

        next_word_prob = total_word_counter[key] / word_counter[key[:N - 1]]
        w = Word(key[-1], '{:.3g}'.format(next_word_prob))
        ngram_prediction[word].add(w)

    return ngram_prediction

# if __name__ == "__main__":
#     tri_prediction = __ngram(P, N=3)
#     for word, ng in tri_prediction.items():
#         tri_prediction[word] = sorted(ng, key=lambda x: x.prob, reverse=True)
#
#     print(tri_prediction)
#
#     print(__ngram(P))
#
#     D = __diversity('Finally', P, cluster)
#
#     print(D)
#
#     print(score('Finally', 'here', P, cluster))
