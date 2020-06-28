from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mkdocs-bibtex-pandoc",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="An MkDocs plugin that enables managing citations with BibTex, using Pandoc as a backend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="mkdocs python markdown bibtex pandoc",
    url="https://github.com/alexvoronov/mkdocs-bibtex",
    author="Shyam Dwaraknath, Alexey Voronov",
    author_email="shyamd@lbl.gov",
    license="BSD-3-Clause-LBNL",
    python_requires=">=3.7",
    install_requires=["mkdocs>=1", "markdown>=3.1.1", "pypandoc>=1.5"],
    tests_require=["pytest"],
    packages=find_packages(),
    entry_points={"mkdocs.plugins": ["bibtex-pandoc = mkdocs_bibtex.plugin:BibTexPlugin"]},
)
