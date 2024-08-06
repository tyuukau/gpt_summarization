import argparse
import os

from .utilities import read_file
from .summarizer import get_summarizer_with_limit
from .testing import mass_test_summarization


def run_summarization(
    file_dir: str, lang: str, word_count: int, verbose: bool
) -> None:
    """
    Runs summarization on a specified file.

    Args:
        file_dir (str): The path to the file to be summarized.
        lang (str): The language code for the summarization (e.g., 'en', 'sk', 'cz').
        word_count (int): The desired word count for the summary.
        verbose (bool): If True, provides detailed output.

    Returns:
        None: The function prints the summary and word count to the console.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file format or language is unsupported.
    """
    if not os.path.exists(file_dir):
        print(f"Error: The file {file_dir} does not exist.")
        return

    file_extension = os.path.splitext(file_dir)[1].lower()

    if file_extension in [".txt", ".pdf"]:
        text = read_file(file_dir)
    else:
        print(
            f"Error: Unsupported file format {file_extension}. Only .txt and .pdf are supported."
        )
        return

    if lang not in ["en", "sk", "cz"]:
        print("Error: Only the languages en, sk, and cz are supported.")
        return

    summarizer = get_summarizer_with_limit(language=lang)
    summary, final_word_count = summarizer.summarize(
        text, word_count, verbose
    )

    print("Summary:", summary)
    print("Word count:", final_word_count)


def run_mass_test(root_dir: str, test_settings: str, output_csv: str) -> None:
    """
    Runs mass summarization tests and writes results to a CSV file.

    Args:
        root_dir (str): The root directory containing the files to be summarized.
        test_settings (str): Path to the JSON file containing test settings.
        output_csv (str): Path to the output CSV file where results will be saved.

    Returns:
        None: The function writes results to the specified CSV file.

    Raises:
        Exception: Any exception raised by mass_test_summarization will be propagated.
    """
    mass_test_summarization(root_dir, test_settings, output_csv)


def main():
    parser = argparse.ArgumentParser(
        description="Summarize text or perform mass testing."
    )

    parser.add_argument(
        "--mode",
        choices=["run", "test"],
        required=True,
        help="Mode of operation: 'run' for summarization, 'test' for mass testing.",
    )

    # Arguments for 'run' mode
    parser.add_argument(
        "--file_dir", type=str, help="Directory of the file to summarize"
    )
    parser.add_argument(
        "--lang", type=str, default="en", help="Language of the file"
    )
    parser.add_argument(
        "--word_count", type=int, help="Desired word count for the summary"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Enable verbose output"
    )

    # Arguments for 'test' mode
    parser.add_argument(
        "--root_dir", type=str, help="Root directory containing files"
    )
    parser.add_argument(
        "--settings",
        type=str,
        help="Path to the JSON file containing test settings",
    )
    parser.add_argument(
        "--output_csv", type=str, help="Path to the output CSV file"
    )

    args = parser.parse_args()

    if args.mode == "run":
        if not args.file_dir or not args.word_count:
            parser.error(
                "For 'run' mode, --file_dir and --word_count are required."
            )
        run_summarization(
            args.file_dir, args.lang, args.word_count, args.verbose
        )
    elif args.mode == "test":
        if not args.root_dir or not args.settings or not args.output_csv:
            parser.error(
                "For 'test' mode, --root_dir, --settings, and --output_csv are required."
            )
        run_mass_test(args.root_dir, args.settings, args.output_csv)


if __name__ == "__main__":
    main()
