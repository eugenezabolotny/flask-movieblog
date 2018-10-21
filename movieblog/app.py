from movieblog import run_app

app = run_app()


if __name__ == '__main__':
    from movieblog import settings

    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)
