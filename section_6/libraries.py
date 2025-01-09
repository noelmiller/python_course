
# libraries include both packages and modules
# to import items from a library, you use the import keyword

from library import helper

helper.helper()

# You can also import a package from a library

from library.package import internet, website

internet.connect()
website.load("google.com")
