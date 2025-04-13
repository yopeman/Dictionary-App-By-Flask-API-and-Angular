from flask import Flask, jsonify, redirect, url_for
from flask_cors import CORS
from word import Word

app = Flask(__name__)
CORS(app)
w = Word()

@app.route('/')
def home():
	return redirect(url_for('get_words'))

@app.route('/word')
def get_words():
	return jsonify(w.get_words()), 201

@app.route('/word/<int:word_id>')
def get_word(word_id):
	return jsonify(w.get_word(word_id)), 201

@app.route('/to/amh/<eng>') # , methods=['POST'])
def to_amh(eng):
	return jsonify(w.find_amh(eng)), 201

@app.route('/to/eng/<amh>') # , methods=['POST'])
def to_eng(amh):
	return jsonify(w.find_eng(amh)), 201

@app.route('/add/<eng>/<amh>') # , methods=['POST'])
def add_word(eng, amh):
	if w.add_word(eng=eng, amh=amh):
		return jsonify({'success':'The new word are addad!'}),2001
	return jsonify({'error':'The word are not added!'}), 400

@app.route('/update/<int:word_id>/<eng>/<amh>') # , methods=['POST'])
def update_word(word_id, eng, amh):
	if w.update_word(word_id=word_id, eng=eng, amh=amh):
		return jsonify({'success':'The new word are updated!'}),2001
	return jsonify({'error':'The word are not updated!'}), 400

@app.route('/delete/<int:word_id>')
def delete_word(word_id):
	if w.delete_word(word_id):
		return jsonify({'success':'The word are deleted!'}), 2001
	return jsonify({'error':'The word are not deleted!'}), 400

@app.route('/clear')
def clear_word():
	if w.clear_word():
		return jsonify({'success':'The all words are cleared!'}), 2001
	return jsonify({'error':'The words are not cleared!'}), 400

if __name__ == '__main__':
	app.run(debug=True)
