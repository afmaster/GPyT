from utils import google_search, openaai_tricks
import langid



def query_gpyt(query: str) -> str:
    """
    Function to search google and provide CHAT-GPT with uptodate data, based on "I'm lucky" function from Google.
    :param query: user input
    :return: open-AI response
    """
    lang = langid.classify(query)[0]
    html = google_search.search_google(query)

    if 'en' in lang:
        try:
            prompt = f"""
                    I want you to clarify the doubt {query}, based on your knowledge and the content of the website below:

                    Site content text: `{html}`
                    """
            text = openaai_tricks.create_completion(prompt)
        except Exception as err1:
            try:
                prompt = f"""
                        I want you to clarify the doubt `{query}`
                        """
                text = openaai_tricks.create_completion(prompt)
            except Exception as err2:
                text = f"Erro1: {err1}; Erro2: {err2}"
    else:
        try:
            prompt = f"""
                    Quero que você esclareça a dúvida `{query}`, com base no seu conhecimento e no conteúdo do site abaixo:
    
                    Texto do site: `{html}`
                    """
            text = openaai_tricks.create_completion(prompt)
        except Exception as err1:
            try:
                prompt = f"""
                        Quero que você esclareça a dúvida `{query}`
                        """
                text = openaai_tricks.create_completion(prompt)
            except Exception as err2:
                text = f"Erro1: {err1}; Erro2: {err2}"

    return text

if __name__ == "__name__":
    user_input = "Quantos nutricionistas tem registrados em Porto Alegre?"
    answer = query_gpyt(user_input)
    print(answer)
