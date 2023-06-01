from re import findall


class NameTooShortOrTooLongError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass

MIN_LEN = 4
MAX_LEN = 30
VALID_DOMAINS = ["bg", "net", "org", "com"]

pattern_name = r'\w+'

email = input()
while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email can contain only one @ symbol!")
    if len(email.split("@")[0]) < MIN_LEN or len(email.split("@")[0]) > MAX_LEN:
        raise NameTooShortOrTooLongError("Name must be 5-30 characters long!")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @ symbol!")
    if findall(pattern_name, email)[0] != email.split("@")[0]:
        raise InvalidNameError("Name accepts only letters, digits and underscores.")
    if email.split(".")[1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net .")

    print("Email is valid")
    email = input()
