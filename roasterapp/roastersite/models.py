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
    Identifier = models.ForeignKey(fileIdentifier, on_delete = models.CASCADE, related_name = "EmployeeByIdentifier")
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    class Meta:
        unique_together = ('firstname', 'lastname', 'Identifier')

    def __str__(self):
        return f"firstname: {self.firstname} lastname: {self.lastname}"


class Shifts(models.Model):
    Identifier=models.ForeignKey(fileIdentifier, on_delete=models.CASCADE, related_name = "ShiftsByIdentifier")
    startDate = models.DateField()
    endDate = models.DateField()
    breaktime = models.IntegerField()

    def __str__(self):
        return f"day: {self.day} startTime: {self.startTime} endTime: {self.breaktime}"


class result(models.Model):
    Identifier = models.ForeignKey(fileIdentifier, on_delete = models.CASCADE, related_name = "ResultByIdentifier")
    Employee = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name = "ResultByEmployee")
    Shifts = models.ForeignKey(Shifts, on_delete = models.CASCADE, related_name = "ResultByIdentifier")
    def __str__(self):
        return f"Identifier: {self.Identifier} Employee: {self.Employee} Shifts: {self.Shifts}"
