from flask import render_template, Markup, request, jsonify

from top.utils import log_me
from top import offers
from top import top


@log_me
@top.route('/')
def index():
    products = offers.read_offers()

    return render_template("app-top.html", product_dict=products)


