class StoreHardware():
    def __init__(self, org_type, price, quantity):
        self.org_type = org_type
        self.price = price
        self.quantity = quantity


class Hardware():
    def __init__(self, print_volume, toner_volume):
        self.print_volume = print_volume
        self.toner_volume = toner_volume


class Printer(Hardware):
    def __init__(self, print_volume, toner_volume, speed_print):
        Hardware.__init__(self, print_volume, toner_volume)
        self.speed_print = speed_print


class Scanner(Hardware):
    def __init__(self, print_volume, toner_volume, speed_scan):
        Hardware.__init__(self, print_volume, toner_volume)
        self.speed_scan = speed_scan


class Xerox(Hardware):
    def __init__(self, print_volume, toner_volume, speed_copy):
        Hardware.__init__(self, print_volume, toner_volume)
        self.speed_copy = speed_copy