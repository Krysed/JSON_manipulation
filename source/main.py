"""Main script running the app"""
import app
import factories
import json_creator


if __name__ == "__main__":

    instance = app.app()
    instance.start_app()

    exit()
