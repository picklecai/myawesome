# _*_coding:utf-8_*_
from bottle import route, run, template, static_file


@route('/')
def page():
    return template('page1', name='cai')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

if __name__ == '__main__':
    run(debug=True, reloader=True)
