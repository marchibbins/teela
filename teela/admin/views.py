from flask import Blueprint, render_template
from flask.ext.login import login_required

from teela.extensions import db
from teela.frontend.forms import MessageForm
from teela.frontend.models import Message


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@login_required
def index():
    """ Admin home, Message index. """
    messages = Message.query.all()
    return render_template('admin/index.html', messages=messages)


@admin.route('/message/<int:message_id>', methods=['GET', 'POST'])
@login_required
def message(message_id):
    """ Edit a Message. """
    message = Message.query.filter_by(id=message_id).first_or_404()
    form = MessageForm(obj=message)

    if form.validate_on_submit():
        form.populate_obj(message)
        db.session.add(message)
        db.session.commit()

    return render_template('admin/message.html', message=message, form=form)
