from __future__ import annotations
import os
import spacy
from spacy.tokens import DocBin
import numpy as np

"""
Functions used to split a dataset into folds to be used with 
k-fold cross-validation.
"""


def create_sub_folders(num_folds: int, ignore_error_exists: bool = True) -> list:
    """
    Create the desired subfolders for each
    of the folds
    :param num_folds: Number of folds to create
    :param ignore_error_exists:
    :return paths: Names of the folders
    """

    paths: list = ["fold_{}".format(x) for x in range(1, num_folds + 1)]

    for path in paths:
        try:
            os.mkdir(path)
        except FileExistsError as e:
            if ignore_error_exists:
                print("Warning: {}".format(e))
                continue
            else:
                raise FileExistsError

    return paths


def load_docbin_as_docs(filename: str):
    """
    Load in a spaCy docBin and convert to docs
    :param filename:
    :return: List of docs, Attributes of the docBin
    """

    nlp = spacy.blank("en")
    doc_bin = DocBin()
    doc_bin.from_disk(filename)

    return list(doc_bin.get_docs(nlp.vocab)), doc_bin.attrs


def save_train_test_docs(path: str, attributes, train_docs, test_docs):
    """
    :param path: Location to save the data into
    :param attributes: Attributes of the doc bin
    :param train_docs: Train split
    :param test_docs: Test split
    :return: None
    """

    # Convert to docBins
    train_doc_bin = DocBin(attrs=attributes)
    test_doc_bin = DocBin(attrs=attributes)

    # Add the docs
    _ = [train_doc_bin.add(x) for x in train_docs]
    _ = [test_doc_bin.add(x) for x in test_docs]

    # Save the files
    train_doc_bin.to_disk("{}/train.spacy".format(path))
    test_doc_bin.to_disk("{}/test.spacy".format(path))


def generate_folds(filename: str, num_folds: int):
    """
    Load in a .spacy file, create the required folds, and
    save into respective folders.

    :param filename: Input file
    :param num_folds: Number of folds to create
    :return: None
    """

    # Restrictions on inputs
    assert 1 <= num_folds <= 10, "Valid number of folds must be between, or equal to, 1 and 10"
    assert ".spacy" in filename, "Provide a valid .spacy"

    # Load in the desired file
    docs, attributes = load_docbin_as_docs(filename)

    # Generate the desired sub-folder
    folder_paths: list = create_sub_folders(num_folds)

    # Split the docs into folds
    folds: np.ndarray = np.array(np.array_split(np.array(docs, dtype=object), num_folds), dtype=object)

    # Save the desired train and test folds
    for i in range(num_folds):
        # Create the mask to select between train and test
        mask = np.ones(len(folds), dtype=bool)
        mask[i] = False

        train_docs = np.concatenate(folds[mask])
        test_docs = np.concatenate(folds[np.invert(mask)])

        save_train_test_docs(folder_paths[i], attributes, train_docs, test_docs)


if __name__ == "__main__":
    generate_folds("dataset_classification.spacy", 10)
