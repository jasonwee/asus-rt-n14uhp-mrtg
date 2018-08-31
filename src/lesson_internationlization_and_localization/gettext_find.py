import gettext

catalogs = gettext.find('example', 'locale', all=True)
print('Catalogs:', catalogs)

