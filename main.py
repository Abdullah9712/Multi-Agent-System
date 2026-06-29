from agents.research_agent import ResearchAgent
from agents.cleaning_agent import CleaningAgent
from agents.formatting_agent import FormattingAgent


def main():

    query = input("\nEnter your topic: ")

    print("\n=== Research Agent ===")
    ResearchAgent().run(query)

    print("\n=== Cleaning Agent ===")
    CleaningAgent().run()

    print("\n=== Formatting Agent ===")
    result = FormattingAgent().run()

    print("\n=== FINAL OUTPUT ===")
    print(result)


if __name__ == "__main__":
    main()