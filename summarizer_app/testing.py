import os
import csv
import json
from tqdm import tqdm

from .utilities import read_file
from .summarizer import get_summarizer_with_limit


def count_word(text: str) -> int:
    words = text.split()
    return len(words)


def read_settings_from_json(json_file):
    with open(json_file, "r") as file:
        return json.load(file)


def process_file(file_path) -> tuple[str, int]:
    # Read and summarize the file
    text = read_file(file_path)
    original_word_count = count_word(text)
    return text, original_word_count


def summarize_file(text, lang, word_count, verbose) -> tuple[str, int]:
    # Read and summarize the file
    summarizer = get_summarizer_with_limit(language=lang)
    summary, final_word_count = summarizer.summarize(
        text, word_count, verbose
    )
    return summary, final_word_count


def mass_test_summarization(root_dir, test_settings, output_csv):
    results = []

    # Read settings from the JSON file
    test_settings = read_settings_from_json(test_settings)

    # Iterate through each file and its settings
    for file_name, settings in tqdm(test_settings.items()):
        file_path = os.path.join(root_dir, file_name)

        if not os.path.isfile(file_path):
            print(f"Warning: File '{file_name}' does not exist.")
            continue

        # Extract the language from the filename
        lang = file_name.split("_")[0]
        if lang not in ["en", "cz", "sk"]:
            print(
                f"Warning: Unsupported language '{lang}' for file '{file_name}'."
            )
            continue

        try:
            text, original_word_count = process_file(file_path)
        except Exception as e:
            print(f"Error processing file '{file_name}': {e}")
            continue

        for desired_word_count in tqdm(settings["desired_word_count"]):
            try:
                summary, final_word_count = summarize_file(
                    text, lang, desired_word_count, verbose=False
                )
                results.append(
                    {
                        "file": file_name,
                        "lang": lang,
                        "original_word_count": original_word_count,
                        "desired_word_count": desired_word_count,
                        "word_count": final_word_count,
                        "summarisation": summary,
                    }
                )
            except Exception as e:
                print(
                    f"Error summarizing file '{file_name}' with word count {desired_word_count}: {e}"
                )
                continue

    # Write results to CSV
    with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "file",
                "lang",
                "original_word_count",
                "desired_word_count",
                "word_count",
                "summarisation",
            ],
        )
        writer.writeheader()
        writer.writerows(results)
