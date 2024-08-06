# gpt_summarization

This Python application summarizes text from a file. It supports specifying the language of the text, the desired word count for the summary, and verbose output.

## Getting Started

Follow these steps to set up and run the application:

### 1. Create and Activate a Virtual Environment

1. Create a new virtual environment:

    ```bash
    python -m venv .venv
    ```

    Use Python 3.10 or above.

2. Activate the virtual environment:

    On Windows:

    ```bash
    .venv\Scripts\activate
    ```

    On macOS and Linux:

    ```bash
    source .venv/bin/activate
    ```

### 2. Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Provide a .env file with the following information

```bash
OPENAI_API_KEY=sk-proj-...
PROMPTLAYER_API_KEY=pl_...
```

Place the .env file at the top level of the repository, ensuring it is at the same level as the summarizer_app folder.

PromptLayer is a helpful tool used to log the prompts and their responses. Head over to [PromptLayer](https://promptlayer.com) to generate an API key.

## Run the application

Execute the summarizer app with the required arguments:

### Mode `run`

```bash
python -m summarizer_app --mode run --file_dir <path_to_file> [--lang <language_code>] --word_count <desired_word_count> [--verbose]
```

**Arguments:**

- `--file_dir`: Required. Directory of the file to summarize.
- `--lang`: Optional. Language of the file. Defaults to `en` (English).
- `--word_count`: Required. Desired word count for the summary.
- `--verbose`: Optional. Enable verbose output for more detailed information. Defaults to `False`.

### Mode `test`

```bash
python -m summarizer_app --mode test --root_dir <path_to_root_directory> --settings <path_to_settings_json> --output_csv <path_to_output_csv>
```

**Arguments:**

- `--root_dir`: Required. Root directory containing the files to be tested.
- `--settings`: Required. Path to the JSON file containing test settings, which should be a dictionary of file names and their corresponding desired word counts.
- `--output_csv`: Required. Path to the output CSV file where the results of the mass testing will be saved.

## Example Usage

### Usages of Mode `run`

To summarize a file example.txt in English with a desired word count of 300:

```bash
python -m summarizer_app --file_dir example.txt --word_count 300
```

To summarize a file example.txt in Czech with a desired word count of 500 and verbose output:

```bash
python -m summarizer_app --file_dir example.txt --lang cz --word_count 500 --verbose
```

### Usages of Mode `test`

```bash
python -m summarizer_app --mode test --root_dir ./data/documents --settings ./data/test_settings.json --output_csv ./data/results.csv
```

Example of `test_settings.json`:

```json
{
    "en_example_1.txt": [
        100,
        250,
        300
    ],
    "sk_example_2.txt": [
        150,
        200,
        250
    ]
}
```

## Planned

- Provide API: Develop and expose an API endpoint that allows external applications to interact with the summarizer functionality.
- Tune the Prompts: Adjust and test various prompt configurations to achieve better summaries across different types of documents.
