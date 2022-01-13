# My Interview Preparation

## Experience in Software Development?

### ASP.NET (5-6 out of 10)
- ***Using ASP.NET*** 
    - [Entity Framework](https://www.c-sharpcorner.com/UploadFile/ff2f08/identifying-entity-framework-development-approaches/)
        - **Database First**
            Design and Build Database (SQL) --> Connect to Model --> Map with Classes --> Controller
        - Model First
            Create Database Schema (Visual Modelling) --> Controller 
        - Code First
            Create Model with Data Annotations (Model) --> Database Migration --> Controller

### Python 
- Python Programming - Intermediate Level (6-7 out of 10)
- Libraries:
    - pandas
    - pyodbc
    - requests (Authorization using: API key, OAuth)

### SQL (7-8 out of 10)
- DDL, DML, DCL
- Stored Procedures
- Cursors

### All projects so far
- ***With Embedded Programming***
    1. Emergency Vehicles Assistance Aid (EA+)
        - 

    2. Home Automation 
        -

    3. Obstacle Detection and Collision Avoidance 
        -

    4. RFID based Attendance System
        -
- ***Using ASP.NET***             
    5. Time Conceirge
        - **WHY:** In the pre-Covid19 era, arranging the conferences and meetings to address your team was a formal stretch. More than one teams would need to share the conference halls. Thus, booking time slots for meeting rooms across the campus was quite time consuming and effort leading stuff. Hence, I decided to build a platform where employees across the campus could reserve time slots for conference rooms according to their requirements easily, so that more time could be spent at contributing to the team and performing at the work more productively.
        - **HOW:**
        - I have built this web application using ASP.NET framework built on .NET programming language
        - Hereby, I used the MVC design pattern
        - and implemented the approaches of Entity framework. 
        - Through this project, I learnt the implementation - of building web applications.
            1. Database First 
            2. Migration with Code First
        of building web applications.    
        - **WHAT:** 
            - I built an web application for the use of three types of different users of organization i.e. Db Administrators, Corporate Employees and Facility supervisors.  
            - Using this application Db Admins would provide accounts to other roles and also maintain/ update any changes to the facilities like incorporation of new locations, campus etc. 
            - Employees can search and reserve the meeting halls at the required timings while facility supervisors can schedule maintenance windows for the meeting rooms making it unavailable for reserve during particular durations. 
            - Through this project, I learnt the implementation of **Database First** and **Code First** approach of building web applications. 

    
    *6. Data Logger
        /* PARTS:
         *  0. Run old project on Visual Studio and Arduino
         *  1. ESP8266 - Hardware design
         *  2. Arduino IDE - Programming
         *  3. SQL Database Design
         *  4. ASP.NET/ REST
         *      4.1 Web application Implementation
         *      4.2 Load data to Db using webapp on localhost
         *      4.3 Host webapp on IIS Manager
         *      4.4 Load data through IIS hosted webapp
         */
        - Data Transmission using Query Strings
        - used REST framework for data transfer 
        - **WHY:** Today, industrial automations and use of IoT sensors is driving all the sectors. If we are enabled to analyze the periodic working and hidden patterns followed by them we can anticipate the fluctuations which can harm the large system and take necessary steps proactively to avoid the damage.
        - **HOW:** I have good understanding sensors and interfacing. Thus, I used ESP8266 NodeMCU to transmit data over localhost through REST requests using web platform built over ASP.NET framework.
        - **WHAT:** 


- ***Data Science Projects with Pandas and Scikit Learn***
    /*
    7. Absenteeism Analytics
        - **WHY:** 
        - **HOW:**
        - **WHAT:**
    */

    8. Valuable Customers Segmentation
        - **WHY:** You must have heard about 80/20 principle. It says, "80 percent of your results are determined by 20 percent of your efforts". And this principle is applicable in various sectors like investments, project management etc. So, based on this principle one of the retailer is interested to identify the most profitable customers from their customer base so they can earn more profits by targetting these customers.
        - **HOW:** After analysing the available datasets, I decided to solve this problem with Machine Learning approach. 
        - **WHAT:** 
            - After successfully defining the problem, I have performed Data Analysis, Data Exploration and Features Transformation. 
            - Thus, I have used Ms Excel, Python programming, libraries like Pandas and Scikit Learn so far.
            - One of my achievement in this project is, I have identified all the data issues present in dataset and currently working on training Regression models to filter most profitable customers.

    9. Building Data Pipelines
        - **WHY:** While the Data Science domain is witnessing the highest demand from businesses, the most important aspect is to provide the sufficient amount and variety of quality data for the processing. In normal scenario, its not always possible to get large amount of data from the single source. Thus, its necessary to build data pipelines which can import (and export) data to the primary system from disparate sources.  
        - **HOW:** I have used python libraries like requests to request required data from various data sources like API data sources like Yelp and Spotify. I have implemented API key and OAuth authorization practices for the same. Further, pyodbc was used to connect to the SQL database and load data in the databases.  
        - **WHAT:** 
            0. Database Design
                0.1 Analysed the incoming data fields from flat-files, operational databases and API data sources.
                0.2 Designed and created SQL database with compatible data types to ensure consistency with the incoming data
            1. Extract
                1.1 Extract data from **flat-files**
                1.2 Extract data from existing **SQL Databases**
                1.3 Extract data from **API data sources** using **API key Authorization**
                1.4 Extract data from **API data sources** using **OAuth Authorization**
            2. Transform
                1.1 Convert datatypes of incoming data fields in target database table compatible types
            3. Load
                3.1 Establish connection with Db
                3.2 Load data using connection object
                3.3 Commit and close connection