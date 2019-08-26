import datetime


# Simple class implementation


class User:
    """A member a friendBook, we will display the name and brithdate of the user."""

    def __init__(self, fullName, birthday):
        self.fullName = fullName
        self.birthday = birthday

        # Extracting the first and last names
        namePieces = fullName.split(" ")
        self.firstName = namePieces[0]
        self.lastName = namePieces[-1]

    def age(self):
        """Return the user's age in year."""
        today = datetime.date(2010, 6, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)  # data of birth
        ageInDays = (today - dob).days
        ageInYears = ageInDays / 365
        return int(ageInYears)


user = User("Dave oxa", "192822")
print(user.age())

# Displaying the docstring that uses """
# help(User)
