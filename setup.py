from setuptools import setup, find_packages

setup(name='wwu-ki_brainage',
      version='0.0.1',
      description="Predicting BrainAGE from 3d medical images using fastai v1",
      url="",
      author="Lukas Fisch",
      packages=find_packages(),
      install_requires=["fastai_scans @ git+git://github.com/renato145/fastai_scans.git#egg=fastai_scans",
                        "tqdm",
                        ],
      )