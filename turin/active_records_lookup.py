from datetime import datetime, timedelta
authors = [
    {'id': 9, 'first_name':'John', 'last_name': 'Smith'},
    {"id": 2, "first_name": "Nancy", "last_name": "Brown"},
    {"id": 3, "first_name": "Alice", "last_name": "Brown"},
    {"id": 4, "first_name": "David", "last_name": "Johnson"},
    {"id": 9, "first_name": "Michael", "last_name": "Scott"},
    ]
    
articles = [
    {"id": 1, "title": "Python Basics", "author_id": 9, "created_at": datetime.now() - timedelta(days=2)},
    {"id": 2, "title": "Advanced Python", "author_id": 3, "created_at": datetime.now() - timedelta(days=6)},
    {"id": 3, "title": "Data Science 101", "author_id": 2, "created_at": datetime.now() - timedelta(days=1)},
    {"id": 4, "title": "Machine Learning", "author_id": 4, "created_at": datetime.now() - timedelta(days=4)},
]

author_id = next((author for author in authors if author['id'] == 9), None)
print(author_id)
print('-------------------')
author_last_name = [author for author in authors if author['last_name'] == 'Brown']
print(author_last_name)
print('-------------------')
first_author = next((author for author in authors if author['last_name'] == 'Brown'), None)
print(f'first_author with last name of Brown is {first_author}')

print('-------------------')
recent_articles = [article for article in articles if article["created_at"] >= datetime.now() - timedelta(days=5)]
print("Articles created in the last 5 days:", recent_articles)

print('-------------------')

nancy_brown = next((author for author in authors if author['last_name'] == 'Brown' and author['first_name'] == 'Nancy'), None)
print(f'Author matching nancy_brown is {nancy_brown}')

print('-------------------')
recent_articles = [article for article in articles if article["created_at"] >= datetime.now() - timedelta(days=5)]


recent_articles_with_authors = [
    {"title": article["title"], "author_last_name": next(author["last_name"] for author in authors if author["id"] == article["author_id"])}
    for article in recent_articles
]
print(recent_articles_with_authors)



