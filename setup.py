from setuptools import setup

setup(name='markdown-djangostaticimage',
      version='0.1',
      description='Markdown extension: Add static tag to image source',
      url='https://bitbucket.org/melvinkcx/markdown-extension-django-static-image',
      author='Melvin Koh',
      author_email='melvinkcx@gmail.com',
      license='MIT',
      py_modules=['django_static_image'],
      keywords="django markdown static html text filter",
      test_suite='tests',
      tests_require=['markdown'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Filters',
          'Topic :: Text Processing :: Markup :: HTML',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      zip_safe=False)
