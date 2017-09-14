from flask import Blueprint, render_template, request
from helpers import object_list
from models import Entry, Tag

entries = Blueprint('entries', __name__, template_folder='templates')


def entry_list(template, query, **context):
    search = request.args.get('q')
    if search:
        query = query.filter((Entry.body.contains(search)) | (Entry.title.contains(search)))
    return object_list(template, query, **context)


@entries.route('/')
def index():
    entries = Entry.query.order_by(Entry.created_timestamp.desc()).filter((Entry.status == Entry.STATUS_PUBLIC))
    return entry_list('entries/index.html', entries)


@entries.route('/tags/')
def tag_index():
    tags = Tag.query.order_by(Tag.name)
    return object_list('entries/tag_index.html', tags)


@entries.route('/tags/<slug>/')
def tag_details(slug):
    slugs = slug.split('+')
    tags = Tag.query.filter(Tag.slug.in_(slugs)).all()
    print tags
    entry_slugs = []
    tag_names = []
    for tag in tags:
        tag_names.append(tag.name.title())
        for entry in tag.entries:
            if entry.slug not in entry_slugs:
                entry_slugs.append(entry.slug)
    entries = Entry.query.filter(Entry.slug.in_(entry_slugs)).order_by(Entry.created_timestamp.asc())
    print entry_slugs
    if len(tags) == 1:
        return entry_list('entries/tag_detail.html', entries, tag=tag_names[0])
    else:
        return entry_list('entries/tag_detail.html', entries, tags=tag_names)


@entries.route('/<slug>/')
def details(slug):
    entry = Entry.query.filter(Entry.slug == slug).first_or_404()
    return render_template('entries/detail.html', entry=entry)
