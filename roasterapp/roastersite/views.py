from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import fileIdentifier, Shifts, Employee
from .forms import uploadFileForm, resultForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import csv
from datetime import datetime
from .solver import solver

def validate_employee(filename):
    csvfile = open(f"{settings.MEDIA_ROOT}/{filename}",'r',newline='',encoding='utf-8-sig')
    reader, idx, invalidRows = csv.DictReader(csvfile) ,1, []
    for row in reader:
        if len(row) != 2:
            invalidRows.append(idx)
        idx += 1
    return invalidRows


def validate_shifts(filename):
    csvfile = open(f"{settings.MEDIA_ROOT}/{filename}",'r',newline='',encoding='utf-8-sig')
    reader, idx, invalidRows = csv.DictReader(csvfile) ,1, []
    for row in reader:
        if len(row) != 4:
            invalidRows.append(idx)
        else:
            try:
                datetime.strptime(row['Date'], "%d/%m/%Y")
                startHour = datetime.strptime(row['Start'], '%I:%M:%S %p')
                endHour = datetime.strptime(row['End'], '%I:%M:%S %p')
                int(row['Break'])

            except:
                invalidRows.append(idx)
        idx += 1
    return invalidRows


def populate_fileIdentifier(id):
    newEntry = fileIdentifier(uniqueIdentifier=id)
    newEntry.save()
    return newEntry

def populate_Employee(filename, newEntry):
    csvfile = open(f"{settings.MEDIA_ROOT}/{filename}",'r',newline='',encoding='utf-8-sig')
    reader = csv.DictReader(csvfile)
    for row in reader:
        e = Employee(Identifier=newEntry, firstname=row['First Name'], lastname=row['Last Name'])
        e.save()


def populate_Shift(filename, newEntry):
    csvfile = open(f"{settings.MEDIA_ROOT}/{filename}",'r',newline='',encoding='utf-8-sig')
    reader = csv.DictReader(csvfile)
    for row in reader:
        startTime = datetime.strptime(f"{row['Date']} {row['Start']}", "%d/%m/%Y %I:%M:%S %p")
        endTime = datetime.strptime(f"{row['Date']} {row['End']}", "%d/%m/%Y %I:%M:%S %p")
        if endTime<startTime:
            endTime=endTime.replace(day=endTime.day+1)
        brk = int(row['Break'])
        s = Shifts(Identifier=newEntry, startDate=startTime, endDate=endTime,breaktime=brk)
        s.save()


def populate_database(id, shiftFile, employeeFile):
    newEntry = populate_fileIdentifier(id)
    populate_Employee(employeeFile, newEntry)
    populate_Shift(shiftFile, newEntry)


def index(request):
    context = {}
    context["form"] = uploadFileForm
    context["resultForm"]= resultForm
    context["messages"] = {}
    context["messages"]["employeeFile"] = []
    context["messages"]["shiftFile"] = []
    context["messages"]["info"] = []

    if request.method == "POST":
        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uniqueIdentifier = form.cleaned_data['uniqueIdentifier']
            if fileIdentifier.objects.filter(uniqueIdentifier = uniqueIdentifier).exists():
                context["messages"] = ["Identifer already exists"]
                return render(request, 'welcome.html', context)
            else:
                fs = FileSystemStorage()
                shiftFile, shiftFile_filename = request.FILES['shiftFile'], f"{uniqueIdentifier}_shiftFile.csv"
                employeeFile, employeeFile_filename = request.FILES['employeeFile'], f"{uniqueIdentifier}_employeeFile.csv"
                fs.save(shiftFile_filename, shiftFile)
                fs.save(employeeFile_filename, employeeFile)
                context["messages"]["employeeFile"].extend(validate_employee(employeeFile_filename))
                context["messages"]["shiftFile"].extend(validate_shifts(shiftFile_filename))
                if not context["messages"]["employeeFile"] and not context["messages"]["shiftFile"]:
                    context["messages"]["info"].append("Files uploaded succesfully")
                    populate_database(uniqueIdentifier, shiftFile_filename,employeeFile_filename)
                    context["resultForm"]= resultForm(initial={"uniqueIdentifier":uniqueIdentifier})
                else:
                    fs.delete(shiftFile_filename)
                    fs.delete(employeeFile_filename)
        else:
            context["messages"]["info"].append(form.errors)
    return render(request, 'welcome.html', context)


def result(request):
    context = {}
    form = resultForm(request.POST)
    if form.is_valid():
        uniqueIdentifier = form.cleaned_data['uniqueIdentifier']
        result = solver(uniqueIdentifier)
        context["employeeShift"]=result
        return render(request, 'result.html', context)
