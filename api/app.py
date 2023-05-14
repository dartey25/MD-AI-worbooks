from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from models import code_search, ask_eur, summarize_doc

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/search', methods=['GET'])
@cross_origin()
def search():
   query = request.args.get('query')
   return jsonify(code_search(query))

@app.route('/eur', methods=['GET'])
@cross_origin()
def eur():
  query = request.args.get('query')
  chain = request.args.get('chain', 'map_reduce') 
  return jsonify(ask_eur(query=query, chain=chain))

@app.route('/summarize', methods=['GET'])
@cross_origin()
def summ():
  doc = request.args.get('doc', '1')
  chain = request.args.get('chain', 'map_reduce') 
  return jsonify(summarize_doc(doc=doc, chain=chain))

if __name__ == '__main__':
  app.run(debug=True)