import os
import chromadb
from joke_teller.crew import CreateJokeCrew
from shared.tracing import traceable
from crewai.utilities.paths import db_storage_path

os.environ["CREWAI_STORAGE_DIR"] = "/app/memory"

@traceable
def main():
    user = "valentine"

    while True:
        topic = input("Enter a topic for the joke: ")

        crew = CreateJokeCrew(user).crew()
        inputs = { "topic": topic }
        response = crew.kickoff(inputs=inputs)

        feedback = input("Do you like another joke? ")

        if feedback.lower() not in ["yes", "y"]:
            break

    # Connect to CrewAI's ChromaDB
    storage_path = db_storage_path()
    chroma_path = os.path.join(storage_path, "knowledge")

    if os.path.exists(chroma_path):
        client = chromadb.PersistentClient(path=chroma_path)
        collections = client.list_collections()

        print("ChromaDB Collections:")
        for collection in collections:
            print(f"  - {collection.name}: {collection.count()} documents")
    else:
        print("No ChromaDB storage found")


if __name__ == '__main__':
    main()
