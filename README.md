# Analysis and Visualization of Women in the Workforce

## Objective:

Analyze and visualize women’s participation in the workplace. Examining trends over time and identifying factors that contribute to these changes.

## Tools and Technologies:

Pandas, Matplotlib, SQLite, Plotly, Jupyter Notebook.

## Goals aka questions to answer:

- Evolution of women's labor force participation rates
- Compare wage gaps between men and women
- Analyze female representation in leadership positions
- Plot gender distribution in STEM fields
- Impact of family responsibilities on career progression

## Features:

- Loading Data:
  - Read Two Data Files: Load employment and labor data from US Department of Labor(CSV) and Unesco (CSV).
  - Set up a local database and read data in with SQLite
- Data Cleaning and Merging
  - Clean datasets using Pandas (handling missing values, correcting data types).
  - Perform a SQL join with your data sets using sql
- Visualize your data
  - 3 visualizations to display the data.
- Best Practices
  - Utilize a virtual environment and include instructions in your README on how the user should set one up
  - Annotate your code with markdown cells in Jupyter Notebook, write clear code comments, and have a well-written README.md.
  - Tidy up your notebook, and make sure you don’t have any empty cells or incomplete cells that don’t do anything.
  - Make sure it’s all functional before your final github commit.

## How to Run on your Machine

1. Clone Repository
2. After you have cloned the repo to your machine, navigate to the project folder in GitBash/Terminal.
3. Create a virtual environment in the project folder. python3 -m venv venv 1
4. Activate the virtual environment. source venv/bin/activate
5. Install the required packages. pip install -r requirements.txt
6. When you are done working on your repo, deactivate the virtual environment. deactivate
