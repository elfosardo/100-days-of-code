
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    ordered_list = []
    if request.method == 'POST' and 'list_to_order' in request.form:
        list_to_order = request.form.get('list_to_order').splitlines()
        ordered_list = order_list(list_to_order)
    return render_template("list_ordering.html",
                           ordered_list=ordered_list)


def order_list(list_to_order):
    list_to_order.sort()
    return list_to_order


if __name__ == '__main__':
    app.run()
