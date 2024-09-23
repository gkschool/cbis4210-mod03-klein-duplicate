from flask import Flask, render_template
import os

def create_app():
    flask_app = Flask(__name__, template_folder='app/templates')

    @flask_app.route('/')
    def index():
        return render_template('index.html')

    @flask_app.route('/about')
    def about():
        return render_template('about.html')

    @flask_app.route('/products')
    def products():
        return render_template('products.html')

    @flask_app.route('/contact')
    def contact():
        return render_template('contact.html')

    @flask_app.route('/services')
    def services():
        return render_template('services.html')

    @flask_app.errorhandler(404)
    def page_not_found(_):
        print("Template folder:", flask_app.template_folder)
        print("Templates:", os.listdir(flask_app.template_folder))
        return render_template('404.html'), 404

    return flask_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)