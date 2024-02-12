from career.search import search,search_api
from career.filter import Filter
from career.storage import DBStorage
import html



result_template1 = """
<p class="career1" encode="UTF-8" style="color:#581B98;">{rank}: {link}</p> 
<a class="career3"  encode="UTF-8" style="color:#581B98;" href="{link}">{title}</a>
<p class="career2" encode="UTF-8" style="color:#581B98;">{snippet}</p><br/>

"""
def run_search(query):
    results = search(query)
    print(results)
    fi = Filter(results)
    results = fi.filter()
    rendered = ''
    results["snippet"] = results["snippet"].apply(lambda x: html.escape(x))
    for index, row in results.iterrows():
        rendered += result_template1.format(**row)
    return rendered
