import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

        name="prefapp_core-prefapp-team",
        version="0.0",
        author="prefapp",
        packages=setuptools.find_packages(),
        python_requires='>=3.1',
        classifiers=[
	    "Programming Language :: Python :: 3",
        ]
)
