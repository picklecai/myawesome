from bottle import get,run


@get("/")
def hello():
    return "hello"
run(host="0.0.0.0", port=8080,server="tornado")