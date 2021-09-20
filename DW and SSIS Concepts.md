# Overview of Data Integration 

## Data Integration
Data Integration is a process in which heterogeneous data is **retreived and combined** as an incorporated form and structure which provides users with **unified view** of data.

#### Methods of Data Integration
1. Data Modeling
2. Data Profiling
3. Data Cleaning
4. Integrated Structure/ Unstructured Data
5. Data Merging, Migration & Replication
6. ETL/ ELT/ ETLT Design & Development
7. Data Warehousing
8. Legacy & 3rd Party Interfaces

### Different Tools for Integration Services
- Ab Initio
- Informatica
- SAP Data Services
- Oracle Data Integrator
- IBM InfoSphere DataStage
- Microsoft SQL Server Integration Services

## SQL Server Integration Services (SSIS)
- SQL Server Integration Services (SSIS) is a component of the Microsoft SQL Server database software that can be used to perform a broad range of data integration and data transformation tasks.
- It is a platform for building enterprise-level **data integration and transformation** and solutions.
- Integration Services can **extract and transform** data from wide variety of sources and then load it into one or more destinations.

### Keywords in SSIS
- Workflow
Workflow in SSIS provides facility to automate certain tasks and maintenance of SQL Server databases and updates to multidimensional analytical data.

- SSIS Package:
SSIS Package is an object that implements Integration Services to extract, transform and load data.
It consists of:
1. Connections
2. Control flow Elements (handles Workflow)
3. Data Flow Elements (handles Data Transformations)

- SSDT: SQL Server Data Tools
SQL Server Data Tools (SSDT) is a modern development tool for building SQL Server relational databases, databases in Azure SQL, Analysis Services (AS) data models, Integration Services (IS) packages, and Reporting Services (RS) reports.

- .dtsx = Data Transformation Services


## Technical Jargons in Data-driven Domain 

### Types of Data Systems
- **OLAP: Online Analytical Processing**  
*OLAP* systems are designed to **perform complex analysis** on the **historical data** for smarter decision making.

- **OLTP: Online Transaction Processing**  
*OLTP* systems are optized for processing a massive number of **transactions**, mostly in **real time**.  
[Reference](https://www.ibm.com/cloud/blog/olap-vs-oltp)

### Types of Data Sources
- **ODS: Operational Data Source**
    - An *ODS* is a *database* designed to *integrate data* from *multiple sources* of a system. 
    - ODS is used to pass the relevant data to *data warehouses* for *data mining* and *reporting*.
    -Data is never passed back to *operational systems/ databases* from ODS.

- **Data Warehouse**
    - *Data Warehouse* is the *central repository* of data *integrated* from one or more disparate sources used for *data analysis* and reporting. 
    - Major [approaches](#approaches-of-data-warehousing) to build data warehouses are;
        - ETL
        - ELT
        - ETLT   

#### Approaches of Data Warehousing
We shall discuss the approaches of Data Warehousing in this section. As we got introduced, there are mainly three approaches to build a DW. They are ETL, ELT and ETLT.   
In ETL (and ELT, ETLT as well);
- 'E' = **Extract**
    -*Data Extraction* is the process of extracting the relevant and useful data from any source for further processing. 
    - As we discussed earlier that DW's are built by integrating the data from various sources (including *ODS*), *extraction* is always the first process in every approach of Data Warehousing.

- 'T' = **Transform**
    - *Data Transformation* is the process of converting the primitive form of data/ attributes to the format which is suitable and efficient for the process of modeling and thus effective decision making.
    - Depending on the business requirements, thus various approaches of data warehousing, Data Engineers/ Architects can decide to *transform* source datasets within the *ODS* (before loading), within *DW* (after loading) or while in the intermediate *pipelines*.
    - e.g. Obtaining 'age' attribute from 'dob'

- 'L' = **Load**
    - *Loading* is the process of copying the data (extracted or transformed data) to a *destination system* like DW.  
[Reference](https://en.wikipedia.org/wiki/Data_warehouse#ETL-based_data_warehousing)
