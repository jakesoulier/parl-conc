from common import *

def dfs(family_id, tree):
    if family_id == None:
        return
    family_t = Request_thread(f'{TOP_API_URL}/family/{family_id}')
    family_t.start()
    family_t.join()
    if("id" not in family_t.response):
        return
    family = Family(family_id, family_t.response)