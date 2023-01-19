import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from searchquery import search
from elasticsearch_dsl import Index

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def index():
    return "Welcome to python server"


@app.route('/search', methods=['POST'])
@cross_origin()
def hello_world():
    print(json.loads(request.data))
    query = json.loads(request.data)['query']
    year_order = json.loads(request.data)['year_order']
    fields = json.loads(request.data)['fields']
    page = json.loads(request.data)['page']
    page_size = json.loads(request.data)['page_size']
    from_year = json.loads(request.data)['from_year']
    to_year = json.loads(request.data)['to_year']
    res = search(query, year_order, fields, page, page_size, from_year, to_year)
    hits = res['hits']['hits']
    time = res['took']
    # aggs = res['aggregations']
    num_results = res['hits']['total']['value']

    return jsonify({'query': query, 'year_order': year_order, "fields": fields, "page":page, "page_size":page_size, 'hits': hits, 'num_results': num_results, 'time': time})


if __name__ == '__main__':
    app.run()
