import pandas as pd
import wikipedia as wp

def get_origin_table(page_title):
    html = wp.page(page_title).html().encode("UTF-8")  #"List_of_video_games_considered_the_best"
    wikipage_tables=pd.read_html(html)
    for table in wikipage_tables:
        ##TODO: check which table
        pass
    return tbody_tag



html = wp.page("alireza mirshafian").html().encode("UTF-8")  #"List_of_video_games_considered_the_best"
wikipage_tables=pd.read_html(html)
print(len(wikipage_tables))
try: 
    df = pd.read_html(html)[2]  # Try 2nd table first as most pages contain contents table first
except IndexError:
    df = pd.read_html(html)[1]
print(df)