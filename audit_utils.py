# utilities for cleaning audit tables and performing calculations

import pandas as pd 
import re 

# %% 

def _extract_area(room):

    pattern = re.compile("\\(.+\\)")
    match = pattern.search(room).group()

    return match.replace("(", "").replace(" SQM)", "")


def _extract_capacity(category):

    pattern = re.compile("\\(.+\\)")
    
    if ("Not Applicable" in category):
        cap = 0
    else:
        match = pattern.search(category).group()
        cap = match.replace("(", "").replace(")", "")

    return cap 

def _is_student_space(category) -> bool:

    pattern = re.compile("Student Space")
    return pattern.search(category) != None 

# %% 

def clean_one_table(df_page: pd.DataFrame) -> pd.DataFrame:
    
    top_row = df_page.columns.to_frame().T 

    df_page = pd.concat((top_row, df_page))
    df_page.reset_index(drop=True, inplace=True)
    df_page.columns = ["room", "category", "comment"]
    df_page.drop("comment", axis=1, inplace=True)

    df_page["area"] = df_page["room"].apply(_extract_area).astype(float)
    df_page["capacity"] = df_page["category"].apply(_extract_capacity).astype(int)
    df_page["student_space"] = df_page["category"].apply(_is_student_space)

    return df_page

# %% 











