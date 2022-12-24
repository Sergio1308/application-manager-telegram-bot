from aiogram.types.location import Location


class Application:
    """
    A class that represents the object model of a table from the database from which python object is created.
    This class describes table columns and contains getters, setters methods.
    """
    def __init__(self, section: str, section_name: str, phone_number: str, location: Location) -> None:
        self.section = section
        self.section_name = section_name
        self.phone_number = phone_number
        self.location = location

    def getSection(self) -> str:
        return self.section

    def setSection(self, section: str):
        self.section = section

    def getSectionName(self) -> str:
        return self.section_name

    def setSectionName(self, section_name: str):
        self.section_name = section_name

    def getPhoneNumber(self) -> str:
        return self.phone_number

    def setPhoneNumber(self, phone_number: str):
        self.phone_number = phone_number

    def getLocation(self) -> Location:
        return self.location

    def setLocation(self, location: Location):
        self.location = location

    def __str__(self) -> str:
        return f'section:{self.section} section_name:{self.section_name} ' \
               f'phone_number:{self.phone_number} location:{self.location} '
