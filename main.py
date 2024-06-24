# Entry point for your Flask application. It initialises the app and starts the server.

# from flask import Flask
# # from app.routes import init_routes # a function from `app.routes` that we'll create later to initialise our API routes

# app = Flask(__name__)

# # # initialise routes
# # init_routes(app) # initialise the routes for the application

# if __name__ == '__main__':
#     app.run(debug=True) # starts the server in debug mode, which provides helpful debugging information


from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # starts the server in debug mode, which provides helpful debugging information
