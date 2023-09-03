
from flask import request, redirect, url_for, flash, render_template

from werkzeug.security import generate_password_hash
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/token', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                pass
                
            except Exception as e:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return jsonify({"value":"hello Token"})