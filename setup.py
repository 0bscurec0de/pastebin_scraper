from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = [item for item in f.read().split('\n') if item]

setup(name='pastebin_scraper',
      version='0.1.0',
      description='Pastebin\'s Scraping API Handler',
      url='https://github.com/0bscurec0de/pastebin_scraper.git',
      author='Felipe Duarte',
      author_email='efelipe.duartep@gmail.com',
      license='Apache',
      packages=['pastebin_scraper'],
      install_requires=requirements,
      zip_safe=False)
