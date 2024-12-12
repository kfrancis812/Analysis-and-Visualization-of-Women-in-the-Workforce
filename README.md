# Analysis and Visualization of Women in the Workforce

## Objective:

Analyze and visualize women’s participation in the workplace. Examining trends over time and identifying factors that contribute to these changes.

## Goals aka questions to answer:

- Evolution of women's labor force participation rates
- Compare wage gaps between men and women
- Analyze female representation in leadership positions
- Plot gender distribution in STEM fields
- Impact of family responsibilities on career progression

## Tools and Technologies:

Pandas, Matplotlib, SQLite, Plotly, Jupyter Notebook.

## Features:

- Loading Data:
  - Read Two Data Files: Load employment and labor data.
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
3. Create a virtual environment in the project folder. `python3 -m venv venv `
4. Activate the virtual environment. `source venv/bin/activate`
5. Install the required packages. `pip install -r requirements.txt`
   When you are done working on your repo, deactivate the virtual environment. `deactivate`
6. In the terminal run `jupyter notebook`
   This will open your browser. Then open each of the notebooks and run in the following order to clean the data and create the database. In Juptyer Notebook, once the file is open, click the play button at the top to run.
   1. `/clean_data_gender_wage_gap_oecd.ipynb`
   2. `/clean_data_female_labor_force_participation_rates.ipynb`
   3. `/clean_data_continents.ipynb`
7. Then run the `/analysis.ipynb` notebook to create the data visualizations.

If you run into any issues, you can also view the notebook in a IDE with the juypter notebook extension: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
