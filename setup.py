import io
from setuptools import setup
from setuptools import find_packages

with io.open("README.md", "r", encoding="utf8") as f:
    readme = f.read()

setup(
    author="Alex Astafev",
    author_email="efsneiron@gmail.com",
    name='scrawny',
    version="1.0.0",
    description="skeleton for flask",
    keywords="skeleton, flask",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Framework :: Flask",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8"
    ],
    python_requires='>=3.8',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'flask',
        'python-dotenv',
        'flask-sqlalchemy',
        'Flask-MySQLdb',
        'Flask-Migrate'
    ],
    extras_require={"test": ["pytest", "coverage"]},
    entry_points={
        "console_scripts": [
            "scrawny = scrawny.cli.scrawny:cli",
        ],
    }
)
