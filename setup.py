import setuptools

with open("README.md", "r") as fh:
    logn_description = fh.read()

setuptools.setup(

        name="prefapp-core",
        version="0.0",
        author="prefapp",
        packages=setuptools.find_packages()
)
