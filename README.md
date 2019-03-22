# Comments (This is displayed to user)
Results for optimization

        Frank White
            Starting at 18/06/2018 05:00:00 till 18/06/2018 13:30:00
            Starting at 19/06/2018 05:00:00 till 19/06/2018 13:30:00
            Starting at 20/06/2018 05:00:00 till 20/06/2018 13:30:00
            Starting at 21/06/2018 05:00:00 till 21/06/2018 13:30:00
            Starting at 22/06/2018 05:00:00 till 22/06/2018 13:30:00
        Sally Brown
            Starting at 18/06/2018 05:00:00 till 18/06/2018 13:30:00
            Starting at 19/06/2018 05:00:00 till 19/06/2018 13:30:00
            Starting at 20/06/2018 05:00:00 till 20/06/2018 13:30:00
            Starting at 21/06/2018 05:00:00 till 21/06/2018 13:30:00
            Starting at 22/06/2018 05:00:00 till 22/06/2018 13:30:00
        Dylan Purple
            Starting at 18/06/2018 05:00:00 till 18/06/2018 13:30:00
            Starting at 19/06/2018 05:00:00 till 19/06/2018 13:30:00
            Starting at 20/06/2018 05:00:00 till 20/06/2018 13:30:00
            Starting at 21/06/2018 05:00:00 till 21/06/2018 13:30:00
            Starting at 22/06/2018 05:00:00 till 22/06/2018 13:30:00
        Tom Yellow
            Starting at 18/06/2018 13:00:00 till 18/06/2018 21:30:00
            Starting at 19/06/2018 13:00:00 till 19/06/2018 21:30:00
            Starting at 20/06/2018 13:00:00 till 20/06/2018 21:30:00
            Starting at 21/06/2018 13:00:00 till 21/06/2018 21:30:00
            Starting at 22/06/2018 13:00:00 till 22/06/2018 21:30:00
        Andrew Blue
            Starting at 18/06/2018 13:00:00 till 18/06/2018 21:30:00
            Starting at 19/06/2018 13:00:00 till 19/06/2018 21:30:00
            Starting at 20/06/2018 13:00:00 till 20/06/2018 21:30:00
            Starting at 21/06/2018 13:00:00 till 21/06/2018 21:30:00
            Starting at 22/06/2018 13:00:00 till 22/06/2018 21:30:00
        Sarah Black
            Starting at 18/06/2018 13:00:00 till 18/06/2018 21:30:00
            Starting at 19/06/2018 13:00:00 till 19/06/2018 21:30:00
            Starting at 20/06/2018 13:00:00 till 20/06/2018 21:30:00
            Starting at 21/06/2018 13:00:00 till 21/06/2018 21:30:00
            Starting at 22/06/2018 13:00:00 till 22/06/2018 21:30:00
        Paul Red
            Starting at 18/06/2018 21:00:00 till 19/06/2018 05:30:00
            Starting at 20/06/2018 21:00:00 till 21/06/2018 05:30:00
            Starting at 22/06/2018 21:00:00 till 23/06/2018 05:30:00
            Starting at 24/06/2018 05:00:00 till 24/06/2018 13:30:00
        Steven Green
            Starting at 18/06/2018 21:00:00 till 19/06/2018 05:30:00
            Starting at 20/06/2018 21:00:00 till 21/06/2018 05:30:00
            Starting at 22/06/2018 21:00:00 till 23/06/2018 05:30:00
            Starting at 24/06/2018 05:00:00 till 24/06/2018 13:30:00
        David Orange
            Starting at 19/06/2018 21:00:00 till 20/06/2018 05:30:00
            Starting at 21/06/2018 21:00:00 till 22/06/2018 05:30:00
            Starting at 23/06/2018 05:00:00 till 23/06/2018 13:30:00
            Starting at 24/06/2018 05:00:00 till 24/06/2018 13:30:00
        Rachel Cyan Can
            Starting at 19/06/2018 21:00:00 till 20/06/2018 05:30:00
            Starting at 21/06/2018 21:00:00 till 22/06/2018 05:30:00
            Starting at 23/06/2018 05:00:00 till 23/06/2018 13:30:00
            Starting at 24/06/2018 13:00:00 till 24/06/2018 21:30:00
        John Magenta-Rose
            Starting at 23/06/2018 05:00:00 till 23/06/2018 13:30:00
            Starting at 24/06/2018 13:00:00 till 24/06/2018 21:30:00
        Ashley Teal
            Starting at 23/06/2018 13:00:00 till 23/06/2018 21:30:00
            Starting at 24/06/2018 13:00:00 till 24/06/2018 21:30:00
        Emily Grey
            Starting at 23/06/2018 13:00:00 till 23/06/2018 21:30:00
            Starting at 24/06/2018 21:00:00 till 25/06/2018 05:30:00

Back 

# Comments
# related to csv files
The employee file does not contain sufficient identifers and links to contact details. They don't have titles either. I can see in some applications they can pose problems.
# Comment on shifts:
My program does not check whether a single shift is strictly viable, that is exceeds legal limits in itself. 
Shifts are given in format of date, start and end date and breaktime is not specified either. Better way is to specify startdate and end date as full dates, I assumed if start is 9pm and end is 5am, it is a nightshift. But it could be a simple mistake. 
# Other assumptions
The scheduling task does at all attempt to make things 'fair'. That is not a design consideration. Nor it takes into account the potencial for penalty rates if there some shifts cannot be taken by any employee. 
Shifts are assumed not to be breable into multiple sub-shifts. That is one big assumption. 
# Time ran out! Things I wish I had time to do
The delivrable does not include rest api support. I have similar project in this repo called "sqlalchemytest" which is written in flask and supports rest api. 
# I did not ask any questions regarding my assumptions. :( Time ran out




### Instructions

For this challenge, we are looking for you to create the backend for a a simple rostering application. This application would be used for creating, editing and deleting both employees and shifts, and for managing the assignment and re-assignment of shifts to employees. It may also call out to an optimisation engine to assign all the shifts to employees in a least cost way. The tool may be used by a company that has one or multiple locations which need to be managed.

An example use for this application could be for a small business that works 24/7 to manage the shifts of it's employees to make sure everyone gets adequate days off and doesn't get shifts which are directly back-to-back (eg working on a night shift followed by a morning shift the next day).

We're providing you with two mock data csv files which are typical of the type of data collected directly from clients:

- Employees: The people who are being rostered
- Shifts: These are the bits of work assigned to employees.

The minimum set of rules that the external algorithm would consider are:
- Minimum of 10hr overnight rest
- Maximum of 5 days working out of 7 any rolling 7 day window
- Maximum of 5 days working in a row

### Challenge

The amount of time you spend on this exercise is up to you, and there are several activities you could consider depending on your strengths:

- (Required) Create a database schema for the application.
- Write code for reading and validating the clients csv files into the database.
- Design and/or implement a web API which could be used for communication between the web app's server and client. For example, endpoints for the manual interactions with the data.
- Develop some questions (for the rosterer) that support further requirements that you might need in order to more fully specify such an application.
- Design and/or implement a pattern for calling an external process where a mathematical algorithm can run (these can sometimes run for many minutes)
- Design and/or implement a pattern for validating shifts and returning or storing warnings

Note that this exercise does not include the writing of the mathematical algorithm for optimal assignment.

If any of the requirements are unclear feel free to send through questions for clarification or make assumptions - we are not trying to test you on your knowledge of rostering.

### Deliverables

What you deliver is up to you, some suggestions based on our current practices are:

- Python 3
- Django
- Postgresql
- Pseudo-code
- Diagrams (e.g. UML)
- Notes on assumptions or next steps you would take

Please create your solution in a fork off this repo. When you're ready to share your solution with us, email a link to your recruiter or Biarri contact.

On completion, if there are additional things you think you could have done better/did not have enough time to complete, feel free to compile a quick list and bring it to the technical interview to help remind yourself during the discussion.


