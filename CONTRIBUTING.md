# Contributing to git-ai

Thank you for your interest in contributing to git-ai! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/niteshkumarm287/git-ai.git
   cd git-ai
   ```
3. **Set up development environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 🔧 Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Test your changes**:
   ```bash
   python main.py
   ```

4. **Commit your changes** (use git-ai if you want! 😉):
   ```bash
   git add .
   python main.py
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

## 📝 Coding Standards

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Handle errors gracefully

### Code Formatting

We use `black` for code formatting:

```bash
pip install black
black main.py
```

## 🧪 Testing

- Test your changes manually with various git scenarios
- Ensure no regressions in existing functionality
- Test edge cases (no changes, large diffs, etc.)

## 📋 Pull Request Guidelines

- **Title**: Use conventional commit format (e.g., `feat: add new feature`)
- **Description**: Clearly describe what changes you made and why
- **Link issues**: Reference any related issues
- **Keep it focused**: One feature/fix per PR
- **Update docs**: Update README.md if needed

## 🐛 Bug Reports

When reporting bugs, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages or logs

## 💡 Feature Requests

We welcome feature requests! Please:

- Check if it already exists
- Clearly describe the feature and use case
- Explain why it would be useful

## 📜 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Assume good intentions

## 🙏 Questions?

Feel free to open an issue for questions or discussions.

Thank you for contributing! 🎉
