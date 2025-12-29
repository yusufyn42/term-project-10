Event Registration and Check-In Platform 

This project is a terminal-based event management system that allows organizers to create events, register attendees, handle ticketing, manage waitlists, process check-ins, and generate reports.  
The goal is to maintain event data in a persistent format and simulate a lightweight event workflow.



 Project Objectives
- Create and manage events and sessions
- Register attendees and authenticate login
- Process ticket sales with capacity limits & waitlist handling
- Support ticket cancellation and transfers
- Generate check-in records and printable badges
- Store all data using JSON persistence
- Provide basic reporting and analytics



 Modules Overview

- events.py                  Event creation & management
- attendees.py      Attendee registration & authentication
- registration.py   Ticketing, waitlist, cancellation, transfer, revenue
- checkin.py        On-site check-in & badge generation
- storage.py        JSON persistence, state saving & backup
- reports.py        Attendance, revenue and session analytics
- main.py           Main entry point 
