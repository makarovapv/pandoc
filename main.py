from panflute import *
from sys import stderr

headers = []


# заменяет все заголовки уровня 3 и ниже на верхний регистр
def header_level(element, document):
    if isinstance(element, Header) and element.level > 2:
        return Header(Str(stringify(element).upper()), level=element.level)


# делает жирным слово BOLD
def bold(document):
    document.replace_keyword("BOLD", Strong(Str("BOLD")))


# находит одинаковые заголовки и выдает предупреждение
def header_exists(element, document):
    if isinstance(element, Header):
        text = stringify(element)
        if text in headers:
            print("Повторные заголовки: " + text, file=stderr)
        else:
            headers.append(text)


if __name__ == "__main__":
    run_filters([header_exists, header_level], prepare=bold)
