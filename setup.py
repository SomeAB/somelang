from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Minimal setup to reserve the name on PyPI
setup(
    name="somelang",
    version="0.0.2",
    author="SomeAB",
    author_email="ssabs@protonmail.com",  # TODO: Replace with your actual email
    description="Language Detection Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SomeAB/somelang",  # Replace with your actual repo
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    keywords="language detection, nlp, text analysis, linguistics",
    project_urls={
        "Bug Reports": "https://github.com/SomeAB/somelang/issues",
        "Source": "https://github.com/SomeAB/somelang",
    },
)
