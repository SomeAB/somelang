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

## Training Dataset (OpenLID-v2)

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

## Original Inspiration (franc)

```bibtex
@software{wormer_franc,
  title = {franc: Detect the language of text},
  author = {Titus Wormer},
  url = {https://github.com/wooorm/franc}
}
```

SomeLang is inspired by franc, which is derived from guess-language (Python) by Kent S. Johnson, guesslanguage (C++) by Jacob R. Rideout, and Language::Guess (Perl) by Maciej Ceglowski.
