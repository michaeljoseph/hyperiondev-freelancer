import sys

from eyesbeen import validate_isbn


if len(sys.argv) < 2:
    # https://stackoverflow.com/questions/602846/how-can-i-access-the-current-executing-module-or-class-name-in-python
    package_name = vars(sys.modules[__name__])['__package__']
    sys.exit(f"Usage: {package_name} ISBN")

print(validate_isbn(sys.argv[1]))