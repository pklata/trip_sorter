from flask import Flask


def create_app(name):
    app = Flask(name)

    @app.route('/trip_sorter', methods=['POST'])
    def trip_sorter():
        return ''

    return app


if __name__ == '__main__':
    app = create_app(__name__)
    app.run(debug=True)
