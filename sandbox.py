# from collections import defaultdict

# wikipron_dict = {}

# with open("wikipron/eng_latn_us_broad_filtered.tsv") as f:
#     for line in f:
#         word, transcription = line.strip().split('\t')
#         wikipron_dict[word] = transcription

# forms = defaultdict(lambda: set())
# with open("task0-data/split-by-lemma/grapheme/eng.trn") as f:
#     for line in f:
#         lemma, form, _ = line.split('\t')
#         forms[lemma].add(form)

# n_full_paradigms = 0
# n_empty_paradigms = 0
# n_partial_paradigms = 0
# n_lemmas_only = 0
# n_forms_only = 0
# for lemma in forms:
#     forms_found = forms[lemma].intersection(wikipron_dict.keys())
#     if lemma in wikipron_dict:
#         if len(forms_found) == 0:
#             n_lemmas_only += 1
#         elif len(forms_found) == len(forms[lemma]):
#             n_full_paradigms += 1
#         else:
#             n_partial_paradigms += 1
#     else:
#         if len(forms_found) == 0:
#             n_empty_paradigms += 1
#         else:
#             n_forms_only += 1

# print(f"Full paradigms: {n_full_paradigms}")
# print(f"Lemma and partial forms: {n_partial_paradigms}")
# print(f"Lemma but no forms: {n_lemmas_only}")
# print(f"Forms but no lemma: {n_forms_only}")
# print(f"Neither lemma nor forms: {n_empty_paradigms}")
# print(f"Total paradigms: {len(forms)}")

# import random
# from collections import defaultdict
# sample_size = 404
# random.seed(0)

# fout = open("task0-data/split-by-lemma/grapheme/eng-verysmall-1.trn", "w+")

# paradigms = defaultdict(list)
# with open("task0-data/split-by-lemma/grapheme/eng.trn") as f:
#     lines = f.readlines()
#     sample_lines = random.sample(lines, sample_size)
    # for line in f:
    #     lemma, form, tags = line.strip().split()
    #     paradigms[lemma].append(line)

# lemmas = list(paradigms.keys())
# random.shuffle(lemmas)

# sample_lines = []
# for lemma in lemmas:
#     for line in paradigms[lemma]:
#         sample_lines.append(line)
#     if len(sample_lines) >= sample_size:
#         break

# for line in sample_lines:
#     fout.write(line)

# fout.close()

# import os

# files = list(set([x[:3] for x in os.listdir("task0-data/original")]))
# print('\n'.join(files))

#import random
#random.seed(0)

#fout = open("task0-data/split-by-lemma/grapheme/ceb-shuffled.trn", "w+")

#with open("task0-data/split-by-lemma/grapheme/ceb.trn") as f:
#    lines = f.readlines()

#random.shuffle(lines)
#for line in lines:
#    fout.write(line)

#fout.close()


# for lang in 'aka', 'ang', 'ast', 'aze', 'azg', 'bak', 'ben', 'bod', 'cat', 'ceb', 'cly', 'cpa', 'cre', 'crh', \
#  'ctp', 'czn', 'dak', 'dan', 'deu', 'dje', 'eng', 'est', 'evn', 'fas', 'fin', 'frm', 'frr', 'fur', 'gaa', 'glg', \
#  'gmh', 'gml', 'gsw', 'hil', 'hin', 'isl', 'izh', 'kan', 'kaz', 'kir', 'kjh', 'kon', 'kpv', 'krl', 'lin', \
#  'liv', 'lld', 'lud', 'lug', 'mao', 'mdf', 'mhr', 'mlg', 'mlt', 'mwf', 'myv', 'nld', 'nno', 'nob', 'nya', \
#  'olo', 'ood', 'orm', 'ote', 'otm', 'pei', 'pus', 'san', 'sme', 'sna', 'sot', 'swa', 'swe', 'syc', 'tel', \
#  'tgk', 'tgl', 'tuk', 'udm', 'uig', 'urd', 'uzb', 'vec', 'vep', 'vot', 'vro', 'xno', 'xty', 'zpv', 'zul':
# for lang in 'ben', 'ceb', 'hin', 'kaz', 'kir', 'mlt', 'orm', 'sna', 'swa', 'tgk', 'tgl', 'zul':
#     lemmas = []
#     ff = open(f"task0-data/split-by-lemma/grapheme/{lang}.hall.trn", "w+")

#     with open(f"task0-data/split-by-lemma/grapheme/{lang}.trn") as f:
#         for line in f:
#             lemma, form, tags = line.strip().split('\t')
#             if lemma not in lemmas:
#                 ff.write(f"{lemma}\t{lemma}\tCOPY\n")
#                 lemmas.append(lemma)
#             ff.write(line)

#     with open(f"task0-data/split-by-lemma/grapheme/{lang}.hall") as f:
#         for line in f:
#             lemma, form, tags = line.strip().split('\t')
#             if lemma not in lemmas:
#                 ff.write(f"{lemma}\t{lemma}\tCOPY\n")
#                 lemmas.append(lemma)
#             ff.write(line)

#     ff.close()

# from collections import Counter, defaultdict
# import math

# lang = 'kaz'

# wordlist = []
# start = "<s>"
# stop = "</s>"
# alphabet = set()
# with open(f"task0-data/split-by-lemma/grapheme/{lang}.trn") as f:
#     for line in f:
#         lemma, form, tags = line.strip().split('\t')
#         wordlist += [[start] + list(lemma) + [stop], [start] + list(form) + [stop]]
#         alphabet.update(list(lemma))
#         alphabet.update(list(form))

# alphabet.add(stop)
# bigram_probs = defaultdict(Counter)

# for word in wordlist:
#     for i in range(len(word)-1):
#         bigram_probs[word[i]][word[i+1]] += 1

# for token in bigram_probs:
#     normalizer = sum(bigram_probs[token].values())
#     for next_token in alphabet:
#         bigram_probs[token][next_token] = (bigram_probs[token][next_token] + 1) / (normalizer + 1)

# def score(word):
#     logprob = math.log(bigram_probs[start][word[0]])
#     for i in range(len(word)-1):
#         logprob += math.log(bigram_probs[word[i]][word[i+1]])
#     logprob += math.log(bigram_probs[word[-1]][stop])
#     return logprob

# d = Counter()
# with open(f"task0-data/split-by-lemma/grapheme/{lang}.hall") as f:
#     for line in f:
#         lemma, form, tags = line.strip().split('\t')
#         d[(lemma, form, tags)] = score(lemma) + score(form)

# print(d.most_common(1000))

# import shutil
# import os

# for family in os.listdir("LemmaSplitting/data"):
#     langs = set([os.path.splitext(filename)[0] for filename in os.listdir(f"LemmaSplitting/data/{family}")])
#     for lang in langs.intersection(['ben', 'ceb', 'hin', 'kaz', 'kir', 'mlt', 'orm', 'sna', 'swa', 'tgk', 'tgl', 'zul']):
#         shutil.copy(f"task0-data/split-by-lemma/grapheme/{lang}.hall.trn", f"LemmaSplitting/data/{family}/{lang}.hall.trn")

# for lang in ['ben', 'ceb', 'hin', 'kaz', 'kir', 'mlt', 'orm', 'sna', 'swa', 'tgk', 'tgl', 'zul']:
#     ff = open(f"LemmaSplitting/data_NN_TSV/{lang}.trn.tsv", "w+")
#     with open(f"LemmaSplitting/data_LEMMA_TSV/{lang}.hall.trn.tsv") as f:
#         for line in f:
#             i_tags, o = line.strip().split('\t')
#             i, tags = i_tags.split('$,')
#             ff.write(f"{i}(,{i}(,{o},),),$,{tags}\t{o}\n")
#     ff.close()
#     ff = open(f"LemmaSplitting/data_NN_TSV/{lang}.tst.tsv", "w+")
#     with open(f"LemmaSplitting/data_LEMMA_TSV/{lang}.tst.tsv") as f:
#         for line in f:
#             i_tags, o = line.strip().split('\t')
#             i, tags = i_tags.split('$,')
#             ff.write(f"{i}(,{i}(,{o},),),$,{tags}\t{o}\n")
#     ff.close()

# import re

# lang = "orm"
# with open(f"LemmaSplitting/data_NN_TSV/{lang}.tst.tsv") as f:
#     for line in f:
#         i_tags, o = line.strip().split('\t')
#         i, tags = i_tags.split('$,')
#         inp = "".join(i.split(','))
#         lemma, nn_lemma, nn_form = re.split('\(|\)|\*\(|\)', inp)[:3]
#         form = "".join(o.split(','))
#         tags = ";".join(tags.split(','))

#         print(f"{lemma}\t{tags}\t{form}\t{nn_lemma}\t{nn_form}")

# import os

# def get_langs_and_paths(data_dir='', use_hall=False):
#     """
#     Return a list of the languages, and a dictionary of tuples: {lang: (train_path,dev_path,test_paht)}.
#     :param data_dir:
#     :return:
#     """
#     develop_paths = {}
#     surprise_paths = {}
#     test_paths = {}
#     lang2family = {} # a dictionary that indicates the family of every language

#     for family in os.listdir(data_dir):
#         for filename in os.listdir(os.path.join(data_dir, family)):
#             lang, ext = os.path.splitext(filename)
#             filename = os.path.join(family,filename)
#             hall_file = False
#             if lang.endswith('.hall'):
#                 lang = lang[:-5]
#                 hall_file = True
#             if ext=='.trn':
#                 if hall_file == use_hall:
#                     develop_paths[lang] = filename
#             elif ext=='.dev':
#                 surprise_paths[lang] = filename
#             elif ext=='.tst':
#                 test_paths[lang] = filename
#             family_name = os.path.split(family)[1]
#             if lang not in lang2family: lang2family[lang] = family_name

#     langs = lang2family.keys()
#     if use_hall: langs = develop_paths.keys() # not all languages have hall data
#     files_paths = {k:(develop_paths[k],surprise_paths[k],test_paths[k]) for k in langs}
#     return langs, files_paths, lang2family

# vocab = set()
# l, fp, l2f = get_langs_and_paths('../LemmaSplitting/data')
# for lang in l:
#     for fname in fp[lang]:
#         with open(f"../LemmaSplitting/data/{fname}") as f:
#             for line in f:
#                 vocab.update(list(line))

# print(vocab)
# print('x' in vocab)
# print('#' in vocab)
# print('&' in vocab)


# import random
# from collections import defaultdict

# alphabet = set()

# with open("LemmaSplitting/data/germanic/eng.tst") as f:
#     for line in f:
#         lemma, form, tags = line.strip().split('\t')
#         alphabet.update(list(lemma) + list(form))

# paradigms = defaultdict(list)
# with open("LemmaSplitting/data/germanic/eng.trn") as f:
#     for line in f:
#         lemma, form, tags = line.strip().split('\t')
#         if len(set(list(lemma)).difference(alphabet)) > 0 and len(set(list(form)).difference(alphabet)) > 0:
#             continue
#         paradigms[lemma].append((form, tags))

# random.seed(0)

# train_small = []

# items = list(paradigms.items())
# random.shuffle(items)

# for paradigm in items:
#     lemma = paradigm[0]
#     for cell in paradigm[1]:
#         form, tags = cell
#         train_small.append(f"{lemma}\t{form}\t{tags}")
#     if len(train_small) >= 5053:
#         break

# with open("LemmaSplitting/data/germanic/erl.trn", "w+") as f:
#     for line in train_small:
#         f.write(f'{line}\n')

# key = 'elr-baseline2'

# with open(f'task0-data/split-by-lemma/grapheme/{key}.tst') as f:
#     input_lines = f.readlines()

# with open(f'neural-transducer/checkpoints/sigmorphon20-lemma/grapheme/transformer/dropout0.3/{key}.decode.test.tsv') as f:
#     output_lines = f.readlines()[1:]

# with open("tmp.txt", "w") as f:
#     for l1, l2 in zip(input_lines, output_lines):
#         score = int(l2.split('\t')[-1])
#         if score:
#             f.write(f"{l1.strip()}\t{''.join(l2.split(' '))}")

# lang = 'elr'
# c = 0
# for lang in 'ben', 'ceb', 'hin', 'kaz', 'kir', 'mlt', 'orm', 'sna', 'swa', 'tgk', 'tgl', 'zul':
#     lemmas = []
#     with open(f'task0-data/split-by-lemma/grapheme/{lang}.trn') as f:
#         for line in f:
#             lemmas.append(line.split('\t')[0])

#     print(lang, len(lemmas) / len(set(lemmas)))
#     c += len(lemmas) / len(set(lemmas))
#     # print(len(set(lemmas)))

# print(c/12)

with open('task0-data/split-by-lemma/grapheme/elr.tst') as f:
    for line in f:
        lemma, form, tags = line.strip().split('\t')
        if form.endswith('ing') and tags.endswith('PST'):
            print(line)
