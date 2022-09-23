from __future__ import annotations
from document_splitter import document_splitter, paragraph_splitter
import spacy

"""
Functions used to perform inference, either classification or NER over a document
"""


def load_model(model_path: str):
    """
    Loads a spacy model from the path
    :param model_path: File path
    :return:
    """

    model = spacy.load(model_path)
    return model


def inference_over_text(model, text: str):
    """
    Perform interence
    :param model: Model to perform over the text
    :param text: Text (either paragraph or sentence)
    :return: spaCy doc for the paragraph
    """

    doc = model(text)
    return doc


def classify_all_paragraphs(model, document: str) -> list:
    """
    Perform inference over the paragraphs of a document
    :param model:
    :param document:
    :return: List of spaCy docs for each paragraph
    """

    paragraphs: list[str] = paragraph_splitter(document)

    docs = [inference_over_text(model, x) for x in paragraphs]

    return docs


def ner_all_sentences(model, document: str) -> list[list]:
    """
    Perform NER over the sentences of a document
    :param model:
    :param document:
    :return: List of lists of spaCy docs
    """

    content: list[list[str]] = document_splitter(document)

    docs = [[model(sentence) for sentence in paragraph] for paragraph in content]

    return docs
