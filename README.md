# Detailed Description of the Software

## 1. Overview
A web/server-based application designed for course booking and management.
Built with Django for backend and React for frontend.


## 2. Booking System
Manages 12 spots across three daily time slots.
Features real-time availability checking, advanced booking, and recurring reservation capabilities.


## 3. Access Control
Uses profile/username and password-based login system.
Different access levels for administrators, instructors, and maintenance staff.


## 4. Participant Management
Participant profiles with essential details.
Digital/manual check-in system for attendance tracking.


## 5. Maintenance and Administration Tools
Capabilities for booking management including rescheduling and canceling.
System configuration tools for various settings.


## 6. Notifications and Reminders
Primary method through emails, with minimal usage.
Customizable content and scheduling by the Academy team.


## 7. Reporting and Documentation
Reporting on occupancy rates, participant attendance, and course completion.
Exportable data in formats like CSV or Excel.


## 8. User Interface
Clean and minimalistic design.
Basic web accessibility features.


## 9. Technical Specifications
Scalable up to 500 participants at a single location.
Hosted on the company server.


## 10. Security and Compliance
Standard security measures including data encryption.
Compliance with relevant data protection laws.


## 11. Future Enhancements
Potential for additional authentication methods and notification channels.
Scalability to multiple locations.


--------------------

# Open Questions

## 1. Recurring Reservations
Setup: How should users set up recurring bookings? What options should be available for frequency (e.g., daily, weekly, monthly)?
Limitations: Are there any restrictions on the duration or frequency of recurring bookings (e.g., a maximum number of weeks or a limit on consecutive bookings)?

## 2. Conflict Resolution
Strategies: What specific conflict resolution strategies are preferred? Options could include first-come-first-serve, manual intervention by administrators, or automatic rescheduling suggestions.
User Notification: How should users be informed about conflicts? What options should they have for resolving these conflicts?

## 3. Participant Management
Profile Information: What detailed information should be included in participant profiles? This might include personal details, contact information, booking history, and any special requirements.
Attendance Tracking: What method should be used for tracking attendance? Options could include digital check-in, manual entry, or integration with access control systems.

## 4. Waiting List Management
Prioritization: How should the waiting list be prioritized? This could be based on first-come-first-served, participant status (e.g., regular vs. new participants), or other criteria.
Notification and Enrollment: How should participants on the waiting list be notified when a spot becomes available? Should enrollment be automatic or require confirmation?

## 5. Reporting and Documentation
Report Types: What specific reports are needed (e.g., attendance reports, financial reports, utilization statistics)?
Export Formats: In what formats should data be exportable? Common formats include CSV, Excel, and PDF. Are there any specific layout or data requirements for these reports?

## 6. Integration with Other Systems
System Types: What types of systems or databases does the application need to integrate with? This might include CRM systems, financial software, or external databases.
Integration Requirements: What specific data needs to be shared between systems? This will help determine the complexity of the integration.

## 7. Security Considerations
Security Standards: Are there specific industry standards or regulatory requirements that the system must adhere to (e.g., GDPR for data protection)?
Data Protection: What measures are required to protect sensitive data, both in transit and at rest?




# Tech stack 
 - Backend: Django , PostgreSQL, Docker (?) 
 - Front-end : React


# 14.12 

Eliminated the Person abstract base class in favor of individual attributes in Participant and Lecturer models.

Implemented and updated models: UserMaster, Course, Participant, RoomResource, and Lecturer.

Ensured models are aligned with new specifications, adding fields like location, platform, category, costs, and period of stay.

Created a custom management command script to seed the database with initial test data.

Resolved database migration issues by setting default values for new fields.

Configured Git for the project and set up the connection to the existing GitHub repository.

Addressed git push issues by setting up a new repo.


# 18.12: 

## Database Population: 
Created and emplemented a python script to populate with dummy entries the data base so it can be tested.

## Admin Interface Customization: 
We created custom admin classes for models like Participant, Lecturer, UserMaster, Course, and RoomResource, enabling detailed data display in the Django admin.

## Database View:
Developed a view function display_database to render data from all models on a webpage.

## Template Creation: 
Prepared a display_database.html template for presenting database contents in a web-friendly format.

## URL Configuration: 
Updated urls.py to include paths for the new database display view and the home page.

## Error Resolution: 
Addressed various issues, including template not found errors and admin registration conflicts. 


# 20.12: 

## Refining  the representation of the existing models : 
clearing up the representation of data in front-end and correcting some models' logic


