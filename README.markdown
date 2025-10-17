# Agentic_AI - Code Review Superhero 🦸‍♂️

**Agentic_AI** is your go-to for squashing code bugs! Using [CrewAI](https://github.com/joaomdmoura/crewAI) and Google's [Gemini API](https://aistudio.google.com/), our AI agents review code, catch errors, and suggest fixes. Built in VS Code with Python 🐍, it’s perfect for dodging those “forgot a colon” or “int + string = oops” moments. *Infinite loop of ‘23? Never again, bro.* 😜

## Getting Started

### Prerequisites
- Python 3.8+ ([python.org](https://www.python.org/downloads/))
- VS Code ([code.visualstudio.com](https://code.visualstudio.com/))
- Gemini API Key ([Google AI Studio](https://aistudio.google.com/app/apikey))
- Git ([git-scm.com](https://git-scm.com/))

### Setup
1. **Clone Repo**  
   ```bash
   git clone https://github.com/VedantMore2006/Agentic_AI.git
   cd Agentic_AI
   ```

2. **Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install crewai crewai[tools] python-dotenv
   ```

4. **Add Gemini API Key**  
   Create `.env` file:  
   ```bash
   touch .env  # Linux/Mac
   echo GEMINI_API_KEY=your-api-key-here > .env
   ```

5. **Run It**  
   ```bash
   python code_reviewer.py
   ```

## How It Works
- **Analyzer Agent**: Spots errors like missing colons or type mismatches.
- **Suggester Agent**: Drops fixes with explanations, like a chill mentor.

**Example**:  
Buggy code:  
```python
def add_numbers(a, b)
    return a + b
print(add_numbers(5, 'ten'))
```  
Output:  
- Analyzer: “Missing colon in def, and int + string = TypeError!”  
- Suggester: “Add `:`, convert ‘ten’ to int or check types.”

## Contributing
Got ideas? Fork, tweak, and send a pull request. Let’s make it epic! 🚀

## Troubleshooting
- **API Key Error**: Check `.env` or `echo $GEMINI_API_KEY`.
- **Module Not Found**: Ensure virtual env is active, deps installed.
- **Stuck?** Hit me on GitHub issues. We’re debug pros!

## License
MIT License—use, share, remix, just shout out the repo. Built by Vedant More, fueled by bugs and no sleep. 😎