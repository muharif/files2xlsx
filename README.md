## Introduction
Simple python script to combine multiple tab- or comma-separated files into an excel file. I'm writting it for personal use (especially to create supplementary data on papers) but it might be useful for others

## Requirement:
* Python (doesn't matter which version)
* [Pandas](https://pandas.pydata.org/)
* [Xlsxwriter Engine](http://xlsxwriter.readthedocs.io/)

## How to use:
1. With list of files written in a text file:
    tab-separated files:
    ```bash
    python files2xlsx.py files.txt tab newexcelfilename
    ```
    or
    comma-separated files:
    ```bash
    python files2xlsx.py files.txt csv newexcelfilename
    ```

2. Combine whole folder into an excel file:
    tab-separated files:
    ```bash
    python files2xlsx.py files2 tab newexcelfilename
    ```
    or
    comma-separated files:
    ```bash
    python files2xlsx.py files2 csv newexcelfilename
    ```
