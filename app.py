from flask import Flask
from views import main_views
from sqlalchemy import create_engine, text

app = Flask(__name__)

app.config.from_pyfile('config.py')

# database = create_engine(app.config['DB_URL'], encoding= 'utf-8')
database_url_with_charset = app.config['DB_URL']
# database_url_with_charset = app.config['DB_URL'] + '?charset=utf8mb3'
database = create_engine(database_url_with_charset)
app.database = database

app.register_blueprint(main_views.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3121, debug=True)