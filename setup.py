import setuptools


# to publish easily on PyPi 
with open("README.md", "r", encoding="utf-8") as fh: # the reame file is used as the long description
    long_description = fh.read()
    
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "linaber1"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "lina.berrayana@gmail.com"

setuptools.setup(
    name=f"{SRC_REPO}",
    version=__version__,
    author=f"{AUTHOR_USER_NAME}",
    author_email=f"{AUTHOR_EMAIL}",
    description="A package to summarize text for NLP app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)