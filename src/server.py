from flask import Flask, render_template, request
linkShort = Flask(__name__)

@linkShort.route('/', methods=['GET', 'POST'])
def short():
	if request.method == 'GET':
		return render_template('main.html')
	else:
		dic = {}
		dic['name'] = request.form['name']
		dic['mob'] = request.form['Mb.no']
		dic['atm'] = request.form['option']
		# lists = ['Ram', 'Shyam']
		lists = []
		lists.append('Ram')
		lists.append('Shyam')
		print (lists)
		return render_template( 'result.html', dic = dic , lists = lists)	

if __name__ == '__main__':
	linkShort.run()