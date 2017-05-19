from setuptools import setup


setup(
    name="slackmojify",
    packages=["slackmojify"],
    version="0.1",
    description="Create emojis so that they can be uploaded to Slack.",
    url="https://github.com/sgp715/slackmojify",
    install_requires=["pillow","imageio"],
    author="Sebastian Perez",
    author_email="7sebastianperez@gmail.com",
    license="MIT",
    keywords=["slack", "emoji"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Anyone',
        'License :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    zip_safe=False
)
