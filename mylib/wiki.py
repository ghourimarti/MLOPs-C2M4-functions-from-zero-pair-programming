import wikipedia


# build a function to return the summary of a wikipedia page
def wiki_summary(page: str) -> str:
    """
    Get the summary of a Wikipedia page.

    :param page: The title of the Wikipedia page
    :return: Summary of the page
    """
    try:
        summary = wikipedia.summary(page)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e}"
    except wikipedia.exceptions.PageError as e:
        return f"Page error: {e}"


# build a function which search wikipedia page for a match
def wiki_search(query: str) -> list:
    """
    Search Wikipedia for a query.

    :param query: The search query
    :return: List of search results
    """
    results = wikipedia.search(query)
    return results


# build a function to return the full text of a wikipedia page
def wiki_full_text(page: str) -> str:
    """
    Get the full text of a Wikipedia page.

    :param page: The title of the Wikipedia page
    :return: Full text of the page
    """
    try:
        page = wikipedia.page(page)
        return page.content
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e}"
    except wikipedia.exceptions.PageError as e:
        return f"Page error: {e}"


# build a function to return the title of a wikipedia page
def wiki_title(page: str) -> str:
    """
    Get the title of a Wikipedia page.

    :param page: The title of the Wikipedia page
    :return: Title of the page
    """
    try:
        page = wikipedia.page(page)
        return page.title
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e}"
    except wikipedia.exceptions.PageError as e:
        return f"Page error: {e}"


# build a function to return the url of a wikipedia page
def wiki_url(page: str) -> str:
    """
    Get the URL of a Wikipedia page.

    :param page: The title of the Wikipedia page
    :return: URL of the page
    """
    try:
        page = wikipedia.page(page)
        return page.url
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e}"
    except wikipedia.exceptions.PageError as e:
        return f"Page error: {e}"
