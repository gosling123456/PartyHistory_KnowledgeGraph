import flask

app = flask.Flask(__name__)

@app.route('/data')
def stream_data():
    data = "主要介绍了 Flask 框架 响应、调度方法和蓝图操作，结合实例形式分析了 Flask 框架中 响应、调度方法和蓝图相关功能、使用方法及操作注意事项，需要的朋友可以"

    return flask.jsonify({'data': data})

@app.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run()
