
from distutils.core import setup
setup(
  name = 'evaluation_framework',         # How you named your package folder (MyLib)
  packages = ['evaluation_framework'],   # Chose the same as "name"
  version = '01.3',      # Start with a small number and increase it with every change you make
  license='apache-2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Evaluation Framework for testing and comparing graph embedding techniques',   # Give a short description about your library
  author = 'Maria Angela Pellegrino',                   # Type in your name
  author_email = 'mariaangelapellegrino94@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/mariaangelapellegrino/Evaluation-Framework',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mariaangelapellegrino/Evaluation-Framework/archive/v_01.3.tar.gz',    # I explain this later on
  keywords = ['evaluation', 'graph-embedding', 'python', 'library', 'benchmark-framework', 'machine learning tasks', 'semantic tasks'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'scikit-learn',
          'scipy',
          'h5py'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',   # Again, pick a license
    'Programming Language :: Python :: 2.7',      #Specify which pyhton versions that you want to support
  ],
)
