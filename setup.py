from setuptools import setup, find_packages
import os

VERSION = '0.0.1'
DESCRIPTION = "Lc's python helper."

setup(
    name="lchelper",
    version=VERSION,
    author="Diselorya",
    # author_email="listorlc@hotmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md',encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['PyPDF2', 'pytesseract', 'pdfplumber', 'unicodedata', 'pangu', 'opencv-python'],
    keywords=['python', 'lchelper', 'diselorya'],
    # data_files=[('lchelper', ['lchelper/asdf.json'])],
    # entry_points={
    # 'console_scripts': [
    #     'lchelper = lchelper.main:main'
    # ]
    # },
    license="MIT",
    # url="",
    scripts=['lchelper/chineseLanguageHelper.py',
             'lchelper/ocrHelper.py',
             'lchelper/pathHelper.py',
             'lchelper/pdfHelper.py',
             'lchelper/stringHelper.py',
             'lchelper/terminalHelper.py',
             ],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)