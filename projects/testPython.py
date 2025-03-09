projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    },
    {
        'id': '4',
        'title': 'Jan\'s special project',
        'description': 'Top Secret bananas'
    }
]


for i in projectsList:
    if i['id'] == '1':
        print(i)

print (projectsList[1])
print (projectsList[1]['title'])
