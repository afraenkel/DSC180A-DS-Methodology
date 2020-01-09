Assignments: Introduction
=========================

The three 'major' assignments for the first quarter of the Capstone serve to

-   Force a close reading of narrowly focused background material (#1)

-   Go through a semi-guided exploratory data analysis and data assessment

-   Through replicating an existing result, understand how to draw a rigorous conclusion in an area (e.g. use a specific statistical tool) and critically view the conclusion.

Each assignment will consist of a coding component (data processing, computation of statistics, model building, etc) and a written component (whose supported data should be automatically generated from the coding components.

These assignments will not only serve to introduce students to a domain and way of thinking, but will also naturally raise questions about existing methodology, shortcomings and possible improvements to the existing approach.

The coding components will be structured to encourage code reuse and extension to future projects in the domain (done in 180B).

Assignment #1: The Data
=======================

In this assignment, you will:

1.  Write a survey of the data and the context in which it was created (report).

2.  Describe and justify the data ingestion process in part 3 (report).

3.  Develop code for ingesting and storing the data for later use (code).

* * * * *

### Part 1

Introduce the problem being investigated and describe the data being used to approach the problem.

Address the appropriateness of the data design and collection:

-   Why is the data is appropriate to address the problem? 

-   What are the potential shortcomings of the data for addressing the problem? 

-   What data have been used to address this problem in the past? (Historical context)

Summarize relevant details of the data generating process, describing the population that the data represents, whether that population is relevant to the question at hand, while addressing possible questions of data reliability.

The material in this section should be informed by the listed background readings and the introduction/data explanation sections of the main paper.

### Part 2

Describe the data ingestion process. This description should: 

-   Specify from where the data originates, addressing legal issues pertaining to access.

-   Address any data privacy concerns and how your data pipeline handles them.

-   Lay out the schema and justify the decisions (what's the unit corresponding to an observation? What are the storage considerations?)

-   Address the applicability of the pipeline to similar data sources you might anticipate using (what might those be?).

### Part 3

In a private GitHub repository for your project, structured according to the methodology portion of the course, create a data ingestion pipeline for the result-replication project. The pipeline should:

-   Ingest data from a data source via an API, HTTP requests, or database connection. The data source should be specified as configuration.

-   Store the data according to your designed schema, taking care to appropriately type the data and implement the best storage design (e.g. relational vs NoSQL).

-   The stored data should be in a form most appropriate for assessment and cleaning (EDA).

Assignment #2: Cleaning and EDA
===============================

In this assignment you will:

1.  Statistically assess the quality of the data, justify the data-cleaning logic, and explain/analyze the features/statistics/target needed for the  replication (report).

2.  Develop and justify data cleaning (code).

* * * * *

### Part 1

Perform an initial EDA to statistically assess the quality of the data and its appropriateness for addressing the problem at hand, justifying data cleaning logic. This will likely address issues with accuracy, precision, and missingness of specific attributes, tying these issues to their possible impact over eventual results.

Statistically summarize the relevant, cleaned attributes and derived features (e.g. in univariate and bivariate analyses), paying particular attention to their relationship to target attributes.

### Part 2

Develop code to clean data (as defined and justified in Part 1), create the features for the replication, and compute the statistics for the report.

Assignment #3: Result Replication
=================================

In this assignment you will:

1.  Develop code to replicate the main result under consideration, using methodological best practices from class (code)

2.  Describe the experimental design and write a summary of the results with code-generated figures and tables (report)

### Part 1

Develop code that replicates the main result of question at hand. The replication should ingest data from the data ingestion/cleaning/feature pipeline and output data used in the report for analysis.

### Part 2

Write a summary of the results from the replication. This includes describing the technique/methodology behind the result, relevant details about how the technique was applied to the data, and an interpretation of the results. This should include an assessment of the shortcomings of the results and possible improvements.
