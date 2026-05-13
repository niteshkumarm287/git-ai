# Security Policy

## Supported Versions

We actively support the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in git-ai, please follow these steps:

1. **Do not** open a public issue
2. Email security concerns to: security@example.com
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- **Response time**: Within 48 hours
- **Updates**: Every 5-7 days on progress
- **Disclosure**: Coordinated disclosure after fix is released

## Security Best Practices

When using git-ai:

- Keep your Gemini API key secure
- Don't commit sensitive data in your changes
- Review generated commit messages before confirming
- Use environment variables for configuration
- Keep dependencies updated

## Known Security Considerations

- git-ai executes shell commands - only use in trusted repositories
- Commit messages are sent to Gemini API - avoid staging files with secrets
- The tool has access to your git history and diff

Thank you for helping keep git-ai secure! 🔒
