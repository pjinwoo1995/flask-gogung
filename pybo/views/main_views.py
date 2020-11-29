from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def main():
    return render_template('main.html')

@bp.route('/01')
def page1():
    return render_template('page1.html')

@bp.route('/02')
def page2():
    return render_template('page2.html')

@bp.route('/03')
def page3():
    return render_template('page3.html')

@bp.route('/04')
def page4():
    return render_template('page4.html')

@bp.route('/05')
def page5():
    return render_template('page5.html')

@bp.route('/06')
def page6():
    return render_template('page6.html')

@bp.route('/07')
def page7():
    return render_template('page7.html')

@bp.route('/08')
def page8():
    return render_template('page8.html')