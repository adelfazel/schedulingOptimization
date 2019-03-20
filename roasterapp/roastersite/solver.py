from  .models import fileIdentifier, Employee, Shifts
from datetime import datetime

def assignToEmployee(employee, shift, employeeShift):
    if not employeeShift[employee]:
        employeeShift[employee].append(shift)
        return True
    exisitingShifts = employeeShift[employee] # imposing rules one by one
    lastShift = exisitingShifts[-1]
    startOfNewShift = shift.startDate
    endOfLastShift = lastShift.endDate
    diff = startOfNewShift - endOfLastShift
    days, seconds = diff.days, diff.seconds
    diffInHours = seconds/3600+days*24
    if startOfNewShift.day == endOfLastShift.day or diffInHours<10:
        return False
    numShiftsIn7Days = 0
    for s in exisitingShifts:
        if startOfNewShift.day - s.endDate.day < 7:
            numShiftsIn7Days+=1
    if numShiftsIn7Days>=5:
        return False
    employeeShift[employee].append(shift)
    return True



def solver(identifer):
    IdToProcess = fileIdentifier.objects.filter(uniqueIdentifier=identifer).first()
    Employees = list(IdToProcess.EmployeeByIdentifier.all())
    shifts = list(IdToProcess.ShiftsByIdentifier.all())
    employeeShift = {}
    for e in Employees:
        employeeShift[e] = []
    for s in shifts:
        for e in Employees:
            if assignToEmployee(e, s, employeeShift):
                break
    return employeeShift
