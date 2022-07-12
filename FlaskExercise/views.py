from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log:
        if log == 'info':
            app.logger.info('No errors')
        elif log == 'warning':
            app.logger.warning('warning occured')
        elif log == 'error':
            app.logger.error('an error occured')
        elif log == 'critical':
            app.logger.critical('critical error')
    return render_template(
        'index.html',
        log=log
    )
