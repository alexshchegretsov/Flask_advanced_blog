from flask_blog.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=0)
