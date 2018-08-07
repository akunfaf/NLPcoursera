#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def download_github_code(path):
    filename = path.rsplit("/")[-1]
    os.system("wget https://raw.githubusercontent.com/hse-aml/intro-to-dl/master/{} -O {}".format(path, filename))

def setup_common():
    #os.system("pip install tqdm")
    #os.system("pip install --upgrade Keras==2.0.6")  # latest version breaks callbacks
    #download_github_code("keras_utils.py")
    #download_github_code("grading.py")
    #download_github_code("download_utils.py")
    download_github_code("contohHitung.py")

def getDatasetWeek3(){
	import download_utils
	download_utils.sequential_downloader(
        "week3",
        [
            "train.tsv",
            "validation.tsv",
            "test.tsv",
            "test_embeddings.tsv",
        ],
        "data",
        force=force
    )
}