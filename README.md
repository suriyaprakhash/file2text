# file2text

1. [Introduction](#introduction)
2. [Pre requisite](#pre-requisite)
3. [Local setup](#local-setup)
4. [Contribution](#contribution)
5. [Miscellaneous Details](#miscellaneous-details)
6. [Release](#release)

## Introduction

This project converts the <i>pdf/jpg/img</i> files to readable text format. This project uses [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and [Poppler](http://blog.alivate.com.au/poppler-windows/) librires to achieve it.

## Pre requisite

- [Python](https://www.python.org/downloads/windows/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- [Poppler](http://blog.alivate.com.au/poppler-windows/)

## Local setup

1. Install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) into the machine and provide the <b>exe</b> location in [config.ini](resources/config.ini)
2. Download and unzip [Poppler](http://blog.alivate.com.au/poppler-windows/) and place it in the [lib](lib)

### Dependency installation  

Use the following command to install the [Pipfile](Pipfile) dependencies,

```cmd
pipenv install
```

### Run

1. Place the source files in the [source directory](resources/config.ini)
2. If the file type is pdf, it gets converted to [jpg](resources/config.ini) before it gets converted to text
3. The [output text file](resources/config.ini) will have the text of individual pages of pdf or an image
from the <b>src</b> to the <b>dest</b>

The following command executes the program, make user that the <b>python</b> is pointing to the correct <b>virtualenv</b>

```cmd
${user.home}\file2text-{generated}\Scripts\python.exe C:/Suriya/ws/Python/ocr/main.py
```

## Contribution

## Miscellaneous Details

## Release


