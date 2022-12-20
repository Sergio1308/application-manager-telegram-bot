
class Application:
    def __init__(self, section, section_name, phone_number, location):
        self.section = section
        self.section_name = section_name
        self.phone_number = phone_number
        self.location = location

    def getSection(self):
        return self.section

    def setSection(self, section):
        self.section = section

    def getSectionName(self):
        return self.section_name

    def setSectionName(self, section_name):
        self.section_name = section_name

    def getPhoneNumber(self):
        return self.phone_number

    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def __str__(self):
        return f'section:{self.section} section_name:{self.section_name} ' \
               f'phone_number:{self.phone_number} location:{self.location} '
