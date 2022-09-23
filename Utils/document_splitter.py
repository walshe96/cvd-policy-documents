from __future__ import annotations
import nltk
from nltk.tokenize import sent_tokenize
import re

nltk.download('punkt')

"""
Functions used as part of the document processing pipeline to 
split a document into paragraphs and sentences
"""


def paragraph_splitter(document: str) -> list[str]:
    """
    Simple paragraph splitting
    :param document: Text of the full document
    :return: List of paragraphs
    """

    if document:
        # Replace the carriage return characters in the document
        document = document.replace("\r", "")

        # Replace any sequences of more than two newline characters
        document = re.sub(r'\n\n+', '\n\n', document)

        # Split over double newlines and return
        paragraphs = [x.strip() for x in document.split("\n\n")]
        return paragraphs
    else:
        []


def sentence_splitter(paragraph: str) -> list[str]:
    """
    Simple sentence splitting
    :param paragraph: Text of a paragraph
    :return: List of sentences
    """
    if paragraph:
        sentences = sent_tokenize(paragraph)
        return sentences
    else:
        return []


def document_splitter(document: str) -> list[list[str]]:
    """
    Simple document splitting into paragraphs and sentences
    :param document: Text of a full document
    :return: List paragraphs containing a list of sentences
    """

    # Split into paragraphs
    paragraphs: list[str] = paragraph_splitter(document)

    # Split each paragraph into sentences
    content: list[list[str]] = [sentence_splitter(x) for x in paragraphs]

    return content
