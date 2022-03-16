from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from v1 import db
from v1.models import PostEvent
from v1.posts.forms import EventsForm


posts = Blueprint('posts', __name__)


@posts.route('/account/new-event', methods=['GET', 'POST'])
@login_required
def newEvent():
    """
    create a new event
    """
    form = EventsForm()
    if form.validate_on_submit():
        event = PostEvent(title=form.title.data, eventType=form.eventType.data, description=form.description.data,
                          date=form.date.data, hour=form.hour.data, event=current_user)
        db.session.add(event)
        db.session.commit()
        flash('Your event has been created!', 'success')
        return redirect(url_for('users.account'))
    return render_template('new-event.html', title='New Event',
                           legend="Event Form", form=form)


@posts.route('/account/<int:post_id>')
def post(post_id):
    """
    route for when the artist wants to choose an exact
    event to update/delete
    """
    post = PostEvent.query.get_or_404(post_id)
    return render_template('event.html', title=post.title, post=post)


@posts.route('/account/<int:post_id>/update', methods=['GET', 'POST'])
def updatePost(post_id):
    """
    a route to update an specific event
    """
    post = PostEvent.query.get_or_404(post_id)
    if post.event != current_user:
        abort(403)
    form = EventsForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.eventType = form.eventType.data
        post.description = form.description.data
        post.date = form.date.data
        post.hour = form.hour.data
        db.session.commit()
        flash('Your event has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.eventType.data = post.eventType
        form.description.data = post.description
        form.date.data = post.date
        form.hour.data = post.hour
    return render_template('new-event.html', title='Update Event',
                           form=form, legend='Update Event')


@posts.route('/account/<int:post_id>/delete', methods=['POST'])
def deletePost(post_id):
    """
    a route to delete an event
    """
    post = PostEvent.query.get_or_404(post_id)
    if post.event != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your event has been deleted!', 'success')
    return redirect(url_for('users.account'))
