from core.router import Router
from core.database import Database
from core.render import Render
from settings import DATABASE_PATH
import dataset
import datetime
import re

def init():
	Router.add_route('/', index)
	Router.add_route('/view', view)
	Router.add_route('/add', add)
	Router.add_route('/add_post', add_post)

db = dataset.connect('sqlite:///db.sqlite3')

def index(request):
	records = db['records'].find(order_by='-date')
	arr = []
	for el in records:
		arr.append({'id': el['id'], 'lid': el['lid'], 'date': el['date'], 'title': el['title']})
	print(arr)
	return Render.render_template('template.html', {'records': arr,})


def view(request):
	#record = db.select('records WHERE id=' + str(int(request['get']['p'][0])) + ' ORDER BY id DESC').run().fetchone()
	records = db['records']
	item = records.find_one(id=int(request['get']['p'][0]))
	return Render.render_template('item.html', { 'title': item['title'], 'content': item['content'], 'date': item['date'] })

def add(request):
	return Render.render_template('add.html')

def stripScript(s):
	return re.sub('\</?(.*)script(.*)/?\>', '', s)

def add_post(request):
	post = request['post']
	print(post)
	#db.insert_into('records').values((None, None, post['b\'name'][0], post['lid'][0], post['data'][0])).run()
	#records = db.select('records').run().fetch()
	db['records'].insert( dict(date=datetime.datetime.now(), title=stripScript(post['b\'name'][0]),
		lid=stripScript(post['lid'][0]), content=stripScript(post['data'][0]) )  )
	records = db['records'].find(order_by='-date')
	arr = []
	for el in records:
		arr.append({'id': el['id'], 'lid': el['lid'], 'date': el['date'], 'title': el['title']})
	return Render.render_template('template.html', {'records': arr,})
