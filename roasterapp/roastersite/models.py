from django.db import models


class fileIdentifier(models.Model):
    uniqueIdentifier = models.CharField(max_length=50, primary_key=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.uniqueIdentifier)


class Employee(models.Model):
    # bad idenfier, could easily create conflict
    # lacks title, this app wouldnt work for gov or places where people with
    # contact details should be hear
    Identifier = models.ForeignKey(fileIdentifier, on_delete = models.CASCADE, related_name = "EmployeeByIdentifier")
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return f"firstname: {self.firstname} lastname: {self.lastname}"


class Shifts(models.Model):
    # what about a shift that violates rules already ?
    # starttime and endtime should be complete in %Y%m%d %I%
    Identifier=models.ForeignKey(fileIdentifier, on_delete=models.CASCADE, related_name = "ShiftsByIdentifier")
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    breaktime = models.IntegerField()
    
    # assignedEmployee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = 'EmployeeByShift', blank=True, null=True )


    def __str__(self):
        return f"startDate: {self.startDate} endDate: {self.endDate}"
