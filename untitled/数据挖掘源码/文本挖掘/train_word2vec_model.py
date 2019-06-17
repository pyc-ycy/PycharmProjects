# !/usr/bin/env python3.7
# encoding: utf-8
# site:D:\users\lenovo\PycharmProjects\untitled
# Time : 2019/6/6 16:42 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PycharmProjects
# File : train_word2vec_model.py 
# @oftware: PyCharm


import logging
import os
import sys
import multiprocessing

# import wiki as wiki
#
# wiki.zh.text.model wiki.zh.text.vector
from gensim.models import Word2Vec
from gensim.models.deprecated.word2vec import PathLineSentences
# from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        print(globals()['__doc__'] % locals())
        sys.exit(1)
    input_dir, outp1, outp2 = sys.argv[1:4]

    model = Word2Vec(PathLineSentences(input_dir),
                     size=256, window=10, min_count=5,
                     workers=multiprocessing.cpu_count(), iter=10)  # 向量维度是4256维，迭代10次

    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)