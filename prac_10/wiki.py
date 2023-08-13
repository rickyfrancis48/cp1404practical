import wikipedia

search_request = " "
while search_request != "":
    search_request = input("What would you like to search: ")
    search_result = wikipedia.search(search_request)
    print(search_result)
    suggestion = wikipedia.suggest(search_result)
    print(suggestion)
    print(wikipedia.page(search_result))

