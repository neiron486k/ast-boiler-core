import io
from setuptools import setup
from setuptools import find_packages

with io.open("README.md", "r", encoding="utf8") as f:
    readme = f.read()

setup(
    name='nnt-content',
    version="1.0.2",
    author="Alex Astafev",
    author_email="efsneiron@gmail.com",
    description="core for flask",
    keywords="boiler, core, flask",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Framework :: Flask",
        "License :: MIT",
        "Programming Language :: Python :: 3.8"
    ],
    python_requires='>=3.6',
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
            "nnt = nntcontent.cli:cli",
        ],
    }
)
