#!/usr/bin/env python3
"""
git-ai: AI-powered Git commit message generator

This tool analyzes staged git changes and generates conventional commit
messages using Google's Gemini AI.
"""
import subprocess
import sys
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.panel import Panel

__version__ = "1.0.0"
__author__ = "git-ai contributors"

console = Console()
BASE_DIR = Path(__file__).resolve().parent

def run_command(command: str) -> str:
    """Execute a shell command and return output.
    
    Args:
        command: Shell command to execute
        
    Returns:
        Command output stripped of whitespace
        
    Raises:
        SystemExit: If command fails
    """
    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        console.print(f"[red]Error:[/red] {result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def get_git_diff() -> str:
    """Get staged git changes."""
    return run_command("git diff --cached")

def get_recent_commits() -> str:
    """Get last 5 commits for context."""
    return run_command("git log --oneline -5")

def load_prompt(diff: str, commits: str) -> str:
    """Load and format the AI prompt template.
    
    Args:
        diff: Git diff output
        commits: Recent commit history
        
    Returns:
        Formatted prompt string
    """
    prompt_path = BASE_DIR / "prompt" / "commit_prompt.txt"
    template = prompt_path.read_text()
    
    return template.format(
        recent_commits=commits,
        git_diff=diff[:12000],
    )

def ask_gemini(prompt: str) -> str:
    """Query Gemini AI with the prompt.
    
    Args:
        prompt: Formatted prompt to send to Gemini
        
    Returns:
        AI-generated commit message
        
    Raises:
        SystemExit: If Gemini CLI fails
    """
    result = subprocess.run(
        ["gemini", "-p", prompt],
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        console.print(f"[red]Error:[/red] {result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def extract_title(response: str) -> str:
    """Extract commit title from AI response.
    
    Args:
        response: Full AI response text
        
    Returns:
        Extracted title or default fallback
    """
    for line in response.splitlines():
        if line.startswith("TITLE:"):
            continue
        if line.strip():
            return line.strip()
    
    return "chore: update changes"

def create_commit(message: str) -> None:
    """Create git commit with generated message.
    
    Args:
        message: Commit message to use
    """
    commit_msg_file = Path(".git/AI_COMMIT_MSG")
    commit_msg_file.write_text(message)
    run_command("git commit -F .git/AI_COMMIT_MSG")

def push_changes() -> None:
    """Push committed changes to remote."""
    run_command("git push")

def main() -> None:
    """Main application entry point."""
    try:
        diff = get_git_diff()
        if not diff:
            console.print("[yellow]No staged changes found.[/yellow]")
            console.print("[dim]Tip: Use 'git add' to stage changes first[/dim]")
            return

        console.print("[cyan]Generating commit message using Gemini...[/cyan]")
        commits = get_recent_commits()
        prompt = load_prompt(diff, commits)
        response = ask_gemini(prompt)
        
        console.print(
            Panel(
                response,
                title="Generated Commit Message",
                border_style="green",
            )
        )
        
        confirm = input("\nProceed with commit and push? (y/n): ")
        if confirm.lower() != "y":
            console.print("[red]Aborted.[/red]")
            return
            
        create_commit(response)
        console.print("[green]✓ Commit created successfully.[/green]")
        
        push_changes()
        console.print("[bold green]✓ Changes pushed successfully 🚀[/bold green]")
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()