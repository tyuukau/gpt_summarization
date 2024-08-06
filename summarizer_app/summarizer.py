from promptlayer import PromptLayer
import json
from math import floor
from dotenv import load_dotenv

from .prompt import (
    prompt,
    minus_word_prompt,
    add_word_prompt,
    system_prompt,
    prompt_cz,
    minus_word_prompt_cz,
    add_word_prompt_cz,
    system_prompt_cz,
    prompt_sk,
    minus_word_prompt_sk,
    add_word_prompt_sk,
    system_prompt_sk,
)

load_dotenv()


class SummarizerWithLimit:
    """
    A class that provides summarization functionality with word count limit.

    Args:
        prompt (str): The prompt template that will be used for generating the summarization.
        add_word_prompt (str): The prompt template for adding words to the summarization.
        minus_word_prompt (str): The prompt template for removing words from the summarization.
        system_prompt (str): The system prompt used for the chat-based completions.
        model (str): The name of the GPT model to be used for summarization. Default is "gpt-4o-mini".
        tolerance (float): The tolerance value used to calculate the word count limits. Default is 0.1.
        attempt_limit (int): The maximum number of attempts to generate a summarization within the word count limits. Default is 5.
    """

    def __init__(
        self,
        prompt: str = prompt,
        add_word_prompt: str = add_word_prompt,
        minus_word_prompt: str = minus_word_prompt,
        system_prompt: str = system_prompt,
        model: str = "gpt-4o-mini",
        tolerance: float = 0.1,
        attempt_limit: int = 5,
    ):
        _pl_client = PromptLayer()
        self._client = _pl_client.openai.OpenAI()
        if "{text}" in prompt:
            self._prompt = prompt
        else:
            raise ValueError("The prompt must contains `{text}`.")
        self._add_word_prompt = add_word_prompt
        self._minus_word_prompt = minus_word_prompt
        self._system_prompt = system_prompt
        self._model = model
        self._tolerance = tolerance
        self._attempt_limit = attempt_limit

    def _count_word(self, text: str) -> int:
        """
        Counts the number of words in the given text.

        Args:
            text (str): The input text.

        Returns:
            int: The number of words in the text.
        """
        words = text.split()
        return len(words)

    def _word_count_limits(self, word_count: int) -> tuple[int, int]:
        """
        Calculates the high and low limits for a given word count.

        Args:
            word_count (int): The desired word count.

        Returns:
            tuple[int, int]: A tuple containing the high and low limits for the word count.
        """
        tolerance = floor(word_count * 0.1)
        high_limit = word_count + tolerance
        low_limit = word_count - tolerance
        return high_limit, low_limit

    def _summarise_first_time(
        self, text: str, word_count: int
    ) -> tuple[str, int]:
        """
        Summarizes the given text using the GPT model for the first time.

        Args:
            text (str): The input text to be summarized.
            word_count (int): The desired word count of the summary.

        Returns:
            tuple[str, int]: A tuple containing the summary text and the actual word count of the summary.
        """
        completion = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {
                    "role": "system",
                    "content": self._system_prompt,
                },
                {
                    "role": "user",
                    "content": self._prompt.format(
                        text=text, word_count=word_count
                    ),
                },
            ],
            pl_tags=["summarization_wtih_count"],
            response_format={"type": "json_object"},
        )
        content = json.loads(completion.choices[0].message.content)
        summary = content["summary"]
        return summary, self._count_word(summary)

    def _add_word(
        self,
        text: str,
        previous_summarization: str,
        current_word_count: int,
        word_count: int,
        min_add_count: int,
        max_add_count: int,
    ) -> tuple[str, int]:
        """
        Adds words to the summarization and returns the updated summarization and word count.

        Args:
            text (str): The input text.
            previous_summarization (str): The previous summarization.
            current_word_count (int): The current word count.
            word_count (int): The desired word count.
            min_add_count (int): The minimum number of words to add.
            max_add_count (int): The maximum number of words to add.

        Returns:
            tuple[str, int]: A tuple containing the updated summarization and word count.
        """
        completion = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {
                    "role": "system",
                    "content": self._system_prompt,
                },
                {
                    "role": "user",
                    "content": self._add_word_prompt.format(
                        summary=previous_summarization,
                        current_word_count=current_word_count,
                        min_add_count=min_add_count,
                        max_add_count=max_add_count,
                        word_count=word_count,
                    ),
                },
            ],
            pl_tags=["summarization_wtih_count"],
            response_format={"type": "json_object"},
        )
        content = json.loads(completion.choices[0].message.content)
        summary = content["summary"]
        return summary, self._count_word(summary)

    def _minus_word(
        self,
        text: str,
        previous_summarization: str,
        current_word_count: int,
        word_count: int,
        min_minus_count: int,
        max_minus_count: int,
    ) -> tuple[str, int]:
        """
        Removes words to the summarization and returns the updated summarization and word count.

        Args:
            text (str): The input text.
            previous_summarization (str): The previous summarization.
            current_word_count (int): The current word count.
            word_count (int): The desired word count.
            min_minus_count (int): The minimum number of words to remove.
            max_minus_count (int): The maximum number of words to remove.

        Returns:
            tuple[str, int]: A tuple containing the updated summarization and word count.
        """
        completion = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {
                    "role": "system",
                    "content": self._system_prompt,
                },
                {
                    "role": "user",
                    "content": self._minus_word_prompt.format(
                        summary=previous_summarization,
                        current_word_count=current_word_count,
                        min_minus_count=min_minus_count,
                        max_minus_count=max_minus_count,
                        word_count=word_count,
                    ),
                },
            ],
            pl_tags=["minus_word_prompt"],
            response_format={"type": "json_object"},
        )
        content = json.loads(completion.choices[0].message.content)
        summary = content["summary"]
        return summary, self._count_word(summary)

    def _summarize_after(
        self, text: str, previous_summarization: str, word_count: int
    ) -> tuple[str, int]:
        """
        Update `previous_summarization` to reach the specified `word_count`.

        Args:
            text (str): The original text to summarize.
            previous_summarization (str): The previous summarization to append or remove words from.
            word_count (int): The desired word count of the resulting summarization.

        Returns:
            tuple[str, int]: A tuple containing the resulting summarization and its word count.
        """
        previous_word_count = self._count_word(previous_summarization)

        if previous_word_count < word_count:
            min_add_count = word_count - previous_word_count
            max_add_count = min_add_count + int(min_add_count * 0.05)
            summary, summary_wc = self._add_word(
                text,
                previous_summarization,
                previous_word_count,
                word_count,
                min_add_count,
                max_add_count,
            )
            return summary, summary_wc
        else:
            min_minus_count = previous_word_count - word_count
            max_minus_count = min_minus_count + int(min_minus_count * 0.05)
            summary, summary_wc = self._minus_word(
                text,
                previous_summarization,
                previous_word_count,
                word_count,
                min_minus_count,
                max_minus_count,
            )
            return summary, summary_wc

    def _summarize_in_loop(
        self, text: str, word_count: int, verbose: bool = False
    ) -> tuple[str, int]:
        """
        Summarizes the given text within a loop until the desired word count range is achieved.

        Args:
            text (str): The input text to be summarized.
            word_count (int): The desired word count of the summary.
            verbose (bool, optional): If True, prints the summary and word count at each attempt. Defaults to False.

        Returns:
            tuple[str, int]: A tuple containing the resulting summarization and its word count.
        """
        high, low = self._word_count_limits(word_count)
        summary, summary_wc = self._summarise_first_time(text, word_count)
        attempts = 1
        if verbose:
            print(f"Attempt {attempts}:\n")
            print(f"Summary: {summary}")
            print(f"Word count: {summary_wc}\n")
        while (attempts <= self._attempt_limit) and (
            not low < summary_wc < high
        ):
            summary, summary_wc = self._summarize_after(
                text, summary, word_count
            )
            attempts += 1
            if verbose:
                print(f"Attempt {attempts}:\n")
                print(f"Summary: {summary}")
                print(f"Word count: {summary_wc}\n")

        return summary, summary_wc

    def summarize(
        self, text: str, word_count: int, verbose: bool = False
    ) -> tuple[str, int]:
        """
        Summarizes the given text to the specified word count range.

        Args:
            text (str): The input text to be summarized.
            word_count (int): The desired word count of the summary.
            verbose (bool, optional): If True, additional information will be printed during the summarization process.
                Defaults to False.

        Returns:
            tuple[str, int]: A tuple containing the resulting summarization and its word count.
        """
        return self._summarize_in_loop(text, word_count, verbose)


def get_summarizer_with_limit(language: str) -> SummarizerWithLimit:
    """
    Returns an instance of SummarizerWithLimit configured for the given language.

    Args:
        language (str): The language code for the summarizer (e.g., 'en', 'cz', 'sk').

    Returns:
        SummarizerWithLimit: An instance of SummarizerWithLimit configured for the specified language.

    Raises:
        ValueError: If the language code is not supported.
    """
    match language:
        case "en":
            return SummarizerWithLimit()
        case "cz":
            return SummarizerWithLimit(
                prompt=prompt_cz,
                add_word_prompt=add_word_prompt_cz,
                minus_word_prompt=minus_word_prompt_cz,
                system_prompt=system_prompt_cz,
            )
        case "sk":
            return SummarizerWithLimit(
                prompt=prompt_sk,
                add_word_prompt=add_word_prompt_sk,
                minus_word_prompt=minus_word_prompt_sk,
                system_prompt=system_prompt_sk,
            )
        case _:
            raise ValueError(f"The language `{language}` is not supported.")
