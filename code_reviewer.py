import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv()
# Set up the Gemini LLM (Large Language Model – basically the AI brain)
gemini_llm = LLM(
    model="gemini/gemini-1.5-pro-latest",  # This is a solid Gemini model for reasoning/code
    api_key=os.getenv("GEMINI_API_KEY"),   # Grabs your key from the env
    temperature=0.3                        # Low temp means more precise, less creative answers
)

# Agent 1: Code Analyzer – Spots errors and issues
analyzer = Agent(
    role="Code Analyzer",
    goal="Review the given code for syntax errors, logical bugs, and best practices violations.",
    backstory="You're a sharp-eyed debugger with years of experience spotting sneaky code issues.",
    llm=gemini_llm,
    verbose=True  # This prints out what the agent is thinking – helpful for us!
)

# Agent 2: Fix Suggester – Proposes corrections
suggester = Agent(
    role="Fix Suggester",
    goal="Suggest fixes and improvements for the identified code errors.",
    backstory="You're a helpful coder who loves refactoring messy code into clean masterpieces.",
    llm=gemini_llm,
    verbose=True
)

# Task 1: Analyze the code
analyze_task = Task(
    description="Thoroughly review the provided code snippet for any errors, bugs, or improvements. Be detailed.",
    expected_output="A report listing potential errors, their locations, and explanations.",
    agent=analyzer
)

# Task 2: Suggest fixes based on the analysis
suggest_task = Task(
    description="Using the analysis from the previous task, suggest specific code fixes and why they work.",
    expected_output="Rewritten code snippets with fixes, plus explanations.",
    agent=suggester
)

# Assemble the Crew (the team of agents)
crew = Crew(
    agents=[analyzer, suggester],
    tasks=[analyze_task, suggest_task],
    verbose=True  # Boolean: enable detailed output
)

# Example code to review (replace with your own buggy code!)
buggy_code = """
def add_numbers(a, b)
    return a + b  # Missing colon? Oops!
print(add_numbers(5, 'ten'))  # Type mismatch, heh
"""

# Run the crew with the input
result = crew.kickoff(inputs={"code_snippet": buggy_code})

# Print the final output
print("Final Review Result:")
print(result)