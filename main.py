from website import create_app  # we can do it because we put __init__ inside website and it is a python package
app = create_app()


if __name__ == '__main__': #only if we run this file it will be executed
    app.run(debug=True) # it will run our application
    #debug=True means, that every time we make changes it will rerun the server