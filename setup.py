from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="git-ai",
    version="1.0.0",
    author="Nitesh Kumar M",
    author_email="kumarmnitesh@gmail.com",
    description="AI-powered Git commit message generator using Gemini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niteshkumarm287/git-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "rich>=15.0.0",
    ],
    entry_points={
        "console_scripts": [
            "git-ai=main:main",
        ],
    },
)
