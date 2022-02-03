from setuptools import find_packages, setup


with open('README.md', 'r') as f:
        long_description = f.read()

        setup(
            name = 'pgbackup',
            version = '0.1.0',
            author = 'Andrii Yaremenko'
            author_email = 'iriver87@example.com',
            description = 'Utility to make backup of the PostgreSQL database',
            long_description = long_description,
            long_description_content_type = 'text/markdown',
            url = 'https://github.com/du4ok/pgbackup',
            packages = find_packages('src')
             )
