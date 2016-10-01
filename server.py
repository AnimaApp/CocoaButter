from flask_mongoengine import MongoEngine
import os
from auth import requires_auth
from flask import Flask, request, jsonify, render_template
from model import PluginException


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host': os.environ.get('MONGODB_URI')}
MongoEngine(app)


@app.route("/")
@requires_auth
def route_home():
    exceptions = PluginException.objects.order_by('-created_at')
    return render_template('index.html', exceptions=exceptions)


@app.route("/exceptions/", methods=['GET', 'POST'])
@requires_auth
def route_exceptions():

    if request.method == 'POST':

        message = request.json.get('message')
        stacktrace = request.json.get('stacktrace')
        page = request.json.get('page')
        exception = PluginException(message=message, stacktrace=stacktrace, page=page)
        exception.save()
        return jsonify(exception.to_dict())

    else:

        exceptions = PluginException.objects.order_by('-created_at')
        return jsonify(results=[exception.to_dict() for exception in exceptions])


if __name__ == "__main__":

    debug = 'DYNO' not in os.environ
    port = os.environ.get("PORT", "5007")
    app.run(host="0.0.0.0", port=int(port), use_reloader=False, debug=debug)