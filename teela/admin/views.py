from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask.ext.login import login_required

from teela.example.forms import MessageForm
from teela.example.models import Message
from teela.extensions import db


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@login_required
def index():
    """ Admin home, Message index. """
    messages = Message.query.all()
    return render_template('admin/index.html', messages=messages)


@admin.route('/message/add', methods=['GET', 'POST'])
@login_required
def message_add():
    """ Create a new Message. """
    form = MessageForm()
    title = "Add message"

    if form.validate_on_submit():
        message = Message(text=form.text.data)
        db.session.add(message)
        db.session.commit()
        flash('Message created.', 'success')
        return redirect(url_for('admin.index'))

    return render_template('admin/message/add_edit.html', form=form, title=title)


@admin.route('/message/<int:message_id>', methods=['GET', 'POST'])
@login_required
def message_edit(message_id):
    """ Edit a Message. """
    message = Message.query.filter_by(id=message_id).first_or_404()
    form = MessageForm(obj=message)
    title = "Edit message"

    if form.validate_on_submit():
        form.populate_obj(message)
        db.session.add(message)
        db.session.commit()
        flash('Message updated.', 'success')

    return render_template('admin/message/add_edit.html', message=message, form=form, title=title)


@admin.route('/message/<int:message_id>/delete', methods=['GET', 'POST'])
@login_required
def message_delete(message_id):
    """ Delete a message. """
    message = Message.query.filter_by(id=message_id).first_or_404()

    if request.method == 'POST':
        db.session.delete(message)
        db.session.commit()
        flash('Message deleted.', 'success')
        return redirect(url_for('admin.index'))

    return render_template('admin/message/delete.html', message=message)
