Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Car Class
class Car :
    regNo = None
    color = None
    def __init__(self, regNo,  color) :
        self.regNo = regNo
        self.color = color
    def  getRegNo(self) :
        return self.regNo
    def  getColor(self) :
        return self.color
class AutomatedCarParker :
    totalNumberOfSlots = 0
    vsSize = 0
    vacantSlots = None
    occupiedSlots = None
    def initilizeVacantSlots(self) :
        self.vacantSlots = [0] * (self.totalNumberOfSlots)
        i = 0
        while (i < self.totalNumberOfSlots) :
            self.updateVacantSlots(i)
            i += 1
        self.minHeap()
    def initilizeOccupiedSlots(self) :
        self.occupiedSlots = [None] * (self.totalNumberOfSlots)
        i = 0
        while (i < self.totalNumberOfSlots) :
            self.occupiedSlots[i] = None
            i += 1
    def minHeap(self) :
        i = (int((self.vsSize - 1) / 2))
        while (i >= 0) :
            self.minHeapify(i)
            i -= 1
    def  isLeaf(self, pos) :
        if (pos >= int((self.vsSize - 1) / 2) and pos <= self.vsSize - 1) :
            return True
        return False
    def swap(self, fpos,  spos) :
        tmp = 0
        tmp = self.vacantSlots[fpos]
        self.vacantSlots[fpos] = self.vacantSlots[spos]
        self.vacantSlots[spos] = tmp
    def minHeapify(self, pos) :
        if (pos >= self.vsSize) :
            return
        if (not self.isLeaf(pos)) :
            if (self.vacantSlots[pos] > self.vacantSlots[(2 * pos) + 1] or self.vacantSlots[pos] > self.vacantSlots[(2 * pos) + 2]) :
                if (self.vacantSlots[(2 * pos) + 1] < self.vacantSlots[(2 * pos) + 2]) :
                    self.swap(pos, (2 * pos) + 1)
                    self.minHeapify((2 * pos) + 1)
                else :
                    self.swap(pos, (2 * pos) + 2)
                    self.minHeapify((2 * pos) + 2)
    def  getFirstVacantSlot(self) :
        if (self.vsSize == 0) :
            return -1
        slotNumber = self.vacantSlots[0]
        self.vacantSlots[0] = self.vacantSlots[self.vsSize - 1]
        self.vsSize -= 1
        self.minHeapify(0)
        return slotNumber
    def updateOccupiedSlots(self, slot,  car) :
        if (slot == -1) :
            return
        if (car == None) :
            self.updateVacantSlots(slot)
        self.occupiedSlots[slot] = car
    def  allotSlot(self, car) :
        allotedSlot = self.getFirstVacantSlot()
        self.updateOccupiedSlots(allotedSlot, car)
        return allotedSlot
    def createSlot(self, n) :
        self.totalNumberOfSlots = n
        self.initilizeVacantSlots()
        self.initilizeOccupiedSlots()
    def updateVacantSlots(self, element) :
        if (self.vsSize >= self.totalNumberOfSlots) :
            return
        self.vacantSlots[self.vsSize] = element
        current = self.vsSize
        while (self.vacantSlots[current] < self.vacantSlots[int((current - 1) / 2)]) :
            self.swap(current, int((current - 1) / 2))
            current = int((current - 1) / 2)
        self.vsSize += 1
    def displayStatus(self) :
        print("Slot No\tRegestration No\tColor")
        i = 0
        while (i < self.totalNumberOfSlots) :
            if (self.occupiedSlots[i] != None) :
                print(str(i + 1) + "\t" + self.occupiedSlots[i].getRegNo() + "\t" + self.occupiedSlots[i].getColor())
            i += 1
    def  getCarsOfColor(self, color) :
        res =  []
        i = 0
        while (i < self.totalNumberOfSlots) :
            if (self.occupiedSlots[i] != None and self.occupiedSlots[i].getColor().lower() == (color).lower()) :
                res.append(self.occupiedSlots[i].getRegNo())
            i += 1
        return res
    def  getSlotNumberOfCar(self, regNo) :
        i = 0
        while (i < self.totalNumberOfSlots) :
            if (self.occupiedSlots[i] != None and self.occupiedSlots[i].getRegNo().lower() == (regNo).lower()) :
                return i
            i += 1
        return -1
    def  getSlotsOfColor(self, color) :
        res =  []
        i = 0
        while (i < self.totalNumberOfSlots) :
            if (self.occupiedSlots[i] != None and self.occupiedSlots[i].getColor().lower() == (color).lower()) :
                res.append(i)
            i += 1
        return res
class Main :
    @staticmethod
    def main( arguments) :  Throws java.lang.Exception
        sc =  "Python-inputs"
        automatedCarParker = AutomatedCarParker()
        while (True) :
            input = input()
            args = input.split(" ")
            operation = args[0]
            if (operation=="create_parking_lot"):
                automatedCarParker.createSlot(int(args[1]))
                print("Created a parking slot with " + args[1] + " slots")
            elif(operation=="park"):
                regNo = args[1]
                color = args[2]
                car = Car(regNo, color)
                allotedSlot = automatedCarParker.allotSlot(car)
                if (allotedSlot == -1) :
                    print("Sorry! parking lot is full")
                print("Allocated slot number: " + str((allotedSlot + 1)))
            elif(operation=="leave"):
                slot = int(args[1]) - 1
                automatedCarParker.updateOccupiedSlots(slot, None)
                print("Slot number " + str((slot + 1)) + " is free")
            elif(operation=="status"):
                automatedCarParker.displayStatus()
            elif(operation=="registration_numbers_for_cars_with_colour"):
                res = automatedCarParker.getCarsOfColor(args[1])
                resLen = len(res)
                i = 0
                while (i < resLen - 1) :
                    print(res[i] + ", ", end ="")
                    i += 1
                if (resLen > 0) :
                    print(res[resLen - 1])
            elif(operation=="slot_number_for_registration_number"):
                resSlot = automatedCarParker.getSlotNumberOfCar(args[1])
                if (resSlot == -1) :
                    print("Not found")
                print(resSlot + 1)
            elif(operation=="slot_numbers_for_cars_with_colour"):
                resSlots = automatedCarParker.getSlotsOfColor(args[1])
                resSlotsLen = len(resSlots)
                i = 0
                while (i < resSlotsLen - 1) :
                    print(str((resSlots[i] + 1)) + ", ", end ="")
                    i += 1
                if (resSlotsLen > 0) :
                    print(resSlots[resSlotsLen - 1] + 1)
            else:
                print("command not found")
    

if __name__=="__main__":
    Main.main([])