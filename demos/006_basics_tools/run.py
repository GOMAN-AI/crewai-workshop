from joke_teller.crew import CreateJokeCrew
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

if __name__ == '__main__':
    website = input("Enter a website for the joke: ")
    while not is_valid_url(website):
        print("Please enter a valid URL (e.g., https://example.com)")
        website = input("Enter a website for the joke: ")

    crew = CreateJokeCrew().crew()
    inputs = { "website": website }
    result = crew.kickoff(inputs=inputs)
