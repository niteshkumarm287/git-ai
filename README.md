# 🤖 git-ai

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> AI-powered Git commit message generator using Gemini

**git-ai** automates the creation of high-quality, conventional commit messages by analyzing your staged changes and recent commit history using Google's Gemini AI.

## ✨ Features

- 🎯 **Conventional Commits**: Automatically generates standardized commit messages
- 📝 **Context-Aware**: Analyzes both git diff and recent commit history
- 🎨 **Rich Terminal UI**: Beautiful, interactive output with Rich library
- 🚀 **One-Command Workflow**: Generate, review, commit, and push in one flow
- 🔒 **Safe**: Always shows generated message before committing
- ⚡ **Fast**: Lightweight CLI tool with minimal dependencies

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Git
- [Gemini CLI](https://github.com/google/generative-ai-python) configured with API key

### Setup

```bash
# Clone the repository
git clone https://github.com/niteshkumarm287/git-ai.git
cd git-ai

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make the script executable (optional)
chmod +x main.py
```

### Global Installation (Optional)

```bash
# Create an alias in your shell config (~/.bashrc, ~/.zshrc, etc.)
alias gcmp="python /path/to/git-ai/main.py"
```

## 🚀 Usage

### Basic Usage

```bash
# Stage your changes
git add .

# Run git-ai
python main.py
```

### Example Output

```
Generating commit message using Gemini...
╭─────────────────────────────────────── Generated Commit Message ────────────────────────────────────────╮
│ TITLE:                                                                                                  │
│ feat(core): add AI-powered commit message generation                                                   │
│                                                                                                         │
│ DESCRIPTION:                                                                                            │
│ Introduces an intelligent commit message generator that leverages Gemini AI to analyze staged changes  │
│ and recent commit history, producing contextually relevant conventional commit messages.               │
│                                                                                                         │
│ CHANGELOG:                                                                                              │
│ - Implements main CLI interface with rich terminal output                                              │
│ - Adds Gemini integration for AI-powered message generation                                            │
│ - Includes commit prompt template with conventional commit guidelines                                  │
│ - Provides automatic commit and push workflow with user confirmation                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Proceed with commit and push? (y/n):
```

## 🛠️ Configuration

### Prompt Customization

Edit `prompt/commit_prompt.txt` to customize the AI's behavior:

```
You are a senior software engineer.

Analyze the provided git diff and recent commit history.
...
```

### Environment Variables

```bash
# Set custom diff size limit (default: 12000 chars)
export GIT_AI_DIFF_LIMIT=15000
```

## 📋 How It Works

1. **Detects Changes**: Retrieves `git diff --cached` for staged changes
2. **Gathers Context**: Fetches recent commit history for consistency
3. **Generates Message**: Sends context to Gemini AI with structured prompt
4. **Interactive Review**: Displays generated message in a beautiful panel
5. **Commits & Pushes**: On confirmation, creates commit and pushes changes

## 🎯 Conventional Commits

git-ai follows the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`, `build`

## 🧪 Development

### Project Structure

```
git-ai/
├── main.py                 # Main CLI application
├── prompt/
│   └── commit_prompt.txt   # AI prompt template
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── LICENSE                # MIT License
└── README.md              # Documentation
```

### Code Quality

```bash
# Format code
black main.py

# Lint code
pylint main.py

# Type checking
mypy main.py
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes using git-ai 😉
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini](https://ai.google.dev/) for the AI model
- [Rich](https://github.com/Textualize/rich) for beautiful terminal formatting
- [Conventional Commits](https://www.conventionalcommits.org/) for the commit standard

## 📧 Support

- 🐛 [Report bugs](https://github.com/niteshkumarm287/git-ai/issues)
- 💡 [Request features](https://github.com/niteshkumarm287/git-ai/issues)
- 💬 [Ask questions](https://github.com/niteshkumarm287/git-ai/discussions)

---

<p align="center">Made with ❤️ by developers, for developers</p>