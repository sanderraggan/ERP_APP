class Expense():
    def __init__(self,tittel,dato,totalsum,mva,kvittering):
        self.tittel = tittel
        self.dato = dato
        self.totalsum = totalsum
        self.mva = mva
        self.kvittering = kvittering
        self.status = "Til behandling"

    def get_sum(self):
        return self.totalsum
