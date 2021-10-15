import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devlist",
    version="0.0.1",
    author="HazemMeqdad",
    author_email="hazemmeqdad@gmail.com",
    description="package that gets information about devlist profile and other info from the Dev List API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HazemMeqdad/devlist",
    project_urls={
        "Bug Tracker": "https://github.com/HazemMeqdad/devlist/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["devlist"],
    python_requires=">=3.6",
)