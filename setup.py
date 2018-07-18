from setuptools import setup


VERSION = "1.0"


with open('README.md') as fobj:
    long_description = fobj.read().strip()


if __name__ == "__main__":
    setup(
        name="Snape",
        version=VERSION,
        author="Kai Xia",
        author_email="xiaket@gmail.com",
        url="https://github.com/xiaket/Snape",
        description="Minimalism snippet manager",
        long_description=long_description,
        py_modules=['Snape'],
        entry_points={
            'Snape': ['Snape = Snape:main']
        },
        keywords=['snippet manager', 'snippets'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Topic :: Utilities',
        ],
    )
