# Citation

## SomeLang

```bibtex
@software{somelang2025,
  title = {SomeLang: Language Detection Library},
  author = {SomeAB},
  year = {2025},
  url = {https://github.com/SomeAB/somelang},
  version = {0.0.3}
}
```

## Training Datasets

The main dataset used to train SomeLang is `OpenLID-v2`. While other datasets such as the `OpenSubtitles 2024`, `hrenWaC v1`, `Mozilla-I10n`, `fiskmo`, `TEP v1 (farsi)` etc were used to fine tune data related to few specific languages, even further.

```bibtex
@inproceedings{burchell-etal-2023-open,
    title = "An Open Dataset and Model for Language Identification",
    author = "Burchell, Laurie  and
      Birch, Alexandra  and
      Bogoychev, Nikolay  and
      Heafield, Kenneth",
    editor = "Rogers, Anna  and
      Boyd-Graber, Jordan  and
      Okazaki, Naoaki",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-short.75",
    doi = "10.18653/v1/2023.acl-short.75",
    pages = "865--879",
    abstract = "Language identification (LID) is a fundamental step in many natural language processing pipelines. However, current LID systems are far from perfect, particularly on lower-resource languages. We present a LID model which achieves a macro-average F1 score of 0.93 and a false positive rate of 0.033{\%} across 201 languages, outperforming previous work. We achieve this by training on a curated dataset of monolingual data, which we audit manually to ensure reliability. We make both the model and the dataset available to the research community. Finally, we carry out detailed analysis into our model{'}s performance, both in comparison to existing open models and by language class.",
}
```

```bibtex
@inproceedings{lison-tiedemann-2016-opensubtitles2016,
    title = "{O}pen{S}ubtitles2016: Extracting Large Parallel Corpora from Movie and {TV} Subtitles",
    author = {Lison, Pierre  and
      Tiedemann, J{\"o}rg},
    editor = "Calzolari, Nicoletta  and
      Choukri, Khalid  and
      Declerck, Thierry  and
      Goggi, Sara  and
      Grobelnik, Marko  and
      Maegaard, Bente  and
      Mariani, Joseph  and
      Mazo, Helene  and
      Moreno, Asuncion  and
      Odijk, Jan  and
      Piperidis, Stelios",
    booktitle = "Proceedings of the Tenth International Conference on Language Resources and Evaluation ({LREC}'16)",
    month = may,
    year = "2016",
    address = "Portoro{\v{z}}, Slovenia",
    publisher = "European Language Resources Association (ELRA)",
    url = "https://aclanthology.org/L16-1147/",
    pages = "923--929",
    abstract = "We present a new major release of the OpenSubtitles collection of parallel corpora. The release is compiled from a large database of movie and TV subtitles and includes a total of 1689 bitexts spanning 2.6 billion sentences across 60 languages. The release also incorporates a number of enhancements in the preprocessing and alignment of the subtitles, such as the automatic correction of OCR errors and the use of meta-data to estimate the quality of each subtitle and score subtitle pairs."
}
```

```
@inproceedings{Tiedemann2012ParallelDT,
  title={Parallel Data, Tools and Interfaces in OPUS},
  author={J{\"o}rg Tiedemann},
  booktitle={International Conference on Language Resources and Evaluation},
  year={2012},
  url={https://api.semanticscholar.org/CorpusID:15453873}
}

```

```bibtex
@inproceedings{pilevar2011tep,
  title={TEP: Tehran English-Persian Parallel Corpus},
  author={M. T. Pilevar and H. Faili and A. H. Pilevar},
  booktitle={Proceedings of 12th International Conference on Intelligent Text Processing and Computational Linguistics (CICLing-2011)},
  year={2011}
}
```

## Original Inspiration (franc)

```bibtex
@software{wormer_franc,
  title = {franc: Detect the language of text},
  author = {Titus Wormer},
  url = {https://github.com/wooorm/franc}
}
```

SomeLang is inspired by franc, which is derived from guess-language (Python) by Kent S. Johnson, guesslanguage (C++) by Jacob R. Rideout, and Language::Guess (Perl) by Maciej Ceglowski.
