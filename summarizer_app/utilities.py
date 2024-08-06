import re
import pymupdf


def filter_text(text):
    """
    Filters the input text to only include specific characters and normalizes whitespace.

    Args:
        text (str): The input text to be filtered.

    Returns:
        str: The filtered and normalized text.
    """
    pattern = pattern = (
        r'[a-zA-Z0-9 \u00C0-\u01BF\u1EA0-\u1EFF`~!@#$%^&*()_\-+=\[\]\n{}|\\;:\'",.<>/?§]+'
    )
    matches = re.findall(pattern, text)
    normalized_text = " ".join(matches)
    normalized_text = re.sub(r"\s+", " ", normalized_text.strip())

    return normalized_text


def read_file(file_path: str) -> str:
    """
    Reads the content of a PDF file and extracts the text.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF file as a string.
    """
    document = pymupdf.open(file_path)
    all_text = ""

    for _, page in enumerate(document):
        page_text = page.get_text("text")
        page_text = filter_text(page_text)
        all_text += " " + page_text

    return all_text
