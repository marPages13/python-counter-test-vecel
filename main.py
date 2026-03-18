from nicegui import app, ui

app = app()

app.on_startup(lambda: print('Visit your app on one of these URLs:', app.urls))

ui.label('Hello NiceGUI!')

ui.run()
