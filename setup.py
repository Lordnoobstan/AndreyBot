import setuptools

setuptools.setup(
    name="AndreyBot",
    version="1.0.0",
    author="Lordnoobstan, GestaIt",
    description="A funny conversation bot that generates sentences using a Markov chain",
    url="https://github.com/Lordnoobstan/AndreyBot",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=["Markovify", "discord"],
)
