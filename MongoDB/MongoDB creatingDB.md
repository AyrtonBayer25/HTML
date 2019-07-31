use classDB

db.classroom.insert({name: 'Mariah', age: 23, favorite_python_library: 'Seaborn', hobbies: ['Coding', 'Reading', 'Running']})
db.classroom.insert({name: 'Ricky', age: 34, favorite_python_library: 'Matplotlib', hobbies: ['Not Coding', 'Not Reading', 'Not Running', 'Guitar']})
db.classroom.insert({name: 'Srikanth', age: 28, favorite_python_library: 'Pandas', hobbies: ['Netflix', 'Guitar', 'Traveling']})

db.classroom.find({age: 23}).pretty()