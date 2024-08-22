from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(graph)
def breadth_first_search():
    search_queue = deque()
    search_queue += graph['you']
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print (person + ' is a mango seller!')
            return True
        else:
            search_queue += graph[person]
    return False

def person_is_seller(name):
    return name[-1] == 'm'
x = breadth_first_search()
print(x)
    
