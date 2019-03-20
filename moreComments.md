# How does the program work:
The program contains a "Welcome page" with two forms, one for uploading files and one for retriving results. The form prompts user to input files, and give a unique identifer. The Identifer is used for accessing the results. The file model goes like this:
class fileIdentifier(models.Model):
    uniqueIdentifier = models.CharField(max_length=50, primary_key=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.uniqueIdentifier)

When the files are uploaded it is stored in "media folder" with idenfier for empolyee and shift. The uniqueIdentifier is used by the user to access the results


# Notes on external optimizer:
Currently the UI prompts the user to insert files; and a unique indentifer to the file.
class fileIdentifier(models.Model):
    uniqueIdentifier = models.CharField(max_length=50, primary_key=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.uniqueIdentifier)
I ran out of time to make use of the 'prt cessed' field. This field was meants to indicate whether results are ready.
Several strategies I had in mind:
The Shift Model below:
class Shifts(models.Model):
    # what about a shift that violates rules already ?
    # starttime and endtime should be complete in %Y%m%d %I%
    Identifier=models.ForeignKey(fileIdentifier, on_delete=models.CASCADE, related_name = "ShiftsByIdentifier")
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    breaktime = models.IntegerField()

Would contain a forgienKey to Employee, and the external shedular would assign Employee to shifts, and once done, would set the "processed" flag to true. If user attempts to access the results while this flag is false, an approporate message can be displayed to user.

# what other things can be done.
Too many a brain storm:
1- adding API support.
2- Allowing user to modify uploaded files (and via rest).
3- Allowing login by employee which shows them their shifts.
4- More targerted shifts.csv file which includes potencially different costs by employee (perhaps different bids by contractors with optimizer minimizing the costs).
5- Better visualization for shifts.
