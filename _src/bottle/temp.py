# _*_coding:utf-8_*_
from bottle import route, run, get, post, delete, template, request, static_file

animals = [{'name': 'Ellie', 'type': 'Elephant'},
           {'name': 'Zed', 'type': 'Zebra'},
           {'name': 'JumpJump', 'type': 'tiger'}]


@get('/animal')
def get_all():
    return {'animal': animals}


@get('/animal/<name>')
def get_one(name):
    the_animal = [animal for animal in animals if animal['name'] == name]
    return {'animal': the_animal[0]}  # 为什么一定要dict呢？


@post('/animal')
def add_one():
    new_animal = {'name': request.json.get('name'),
                  'type': request.json.get('type')}
    animals.append(new_animal)
    return {'animal': animals}


@delete('/animal/<name>')
def remove_one(name):
    the_animal = [animal for animal in animals if animal['name'] == name]
    animals.remove(the_animal[0])
    return {'animal': animals}


@route('/')
def page():
    return template('page1', name='cai')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

if __name__ == '__main__':
    run(debug=True, reloader=True)
