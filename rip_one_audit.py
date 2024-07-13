# rip one school audit pdf 

import audit_utils
import sys 
import tabula.io

# %% 

filepath = sys.argv[1]
school_name = filepath.replace("pdfs/", "").replace(".pdf", "")

# %% 

df_list = tabula.read_pdf(filepath, pages="all")

# %% 

n_pages = len(df_list)

for i in range(2, n_pages):
    df_page = df_list[i]
    audit_utils.clean_one_table(df_page).to_csv("outputs/" + school_name + str(i-1) + ".csv")


     


