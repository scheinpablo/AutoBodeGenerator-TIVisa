import pyvisa as visa


class VisaManager:
    def __init__(self):
        self.list_of_instruments = []
        self.resource_manager = visa.ResourceManager()
        self.list_of_detailed_instruments = []

    def get_resource_manager(self):
        return self.resource_manager

    def get_list_of_visa_strings(self):
        self.list_of_instruments = []
        self.list_of_instruments = self.resource_manager.list_resources()
        return self.list_of_instruments

    def get_list_of_detailed_instruments(self):
        lst_inst = self.get_list_of_visa_strings()
        self.list_of_detailed_instruments = []
        for inst in lst_inst:
            instrument = Instrument(inst, self)
            self.list_of_detailed_instruments.append(instrument)
        return self.list_of_detailed_instruments

    def get_visa_from_idn(self, idnString):
        found = False
        for inst in self.list_of_detailed_instruments:
            if inst.idnString == idnString:
                found = True
                return inst.visa_string
        if not found:
            return None


class Instrument:
    def __init__(self, visa_string, visa_manager):
        self.visa_string = visa_string
        rm = visa_manager.get_resource_manager()
        inst = rm.open_resource(visa_string)
        self.idnString = inst.query('*IDN?')
