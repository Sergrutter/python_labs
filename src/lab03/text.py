import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Приводит текст к стандарту"""

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    text = re.sub(r'[\t\r\n]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова"""

    return re.findall(r'\w+(?:-\w+)*', text, flags=re.UNICODE)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоту слов"""

    freq = {}

    for word in tokens:
        freq[word] = freq.get(word, 0) + 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает N самых частых слов"""

    if n <= 0:
        return []

    items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

    return items[:n]


assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"
assert normalize("Hello\r\nWorld") == "hello world"
assert normalize("  двойные   пробелы  ") == "двойные пробелы"

assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]
assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

freq = count_freq(["a", "b", "a", "c", "b", "a"])
assert freq == {"a": 3, "b": 2, "c": 1}
assert top_n(freq, 2) == [("a", 3), ("b", 2)]

freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]