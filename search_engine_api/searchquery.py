from elasticsearch import Elasticsearch
import json

def basic_search(query, year_order, fields, page, page_size, from_year, to_year):
    if(query is None ) : 
        body = {
            "query": {
                "query_string": {
                    "query": '',
                }
            }
        }
    elif(query == ''):
        body = {
            "query": {
                'bool': {
                    "must": [
                        {"match_all": {}},
                        {"range": {"year": {"gte": from_year, "lte": to_year}}}

                    ],
                },
            },
            "sort": [
                {
                    "year": {
                        "order": year_order 
                    }
                }
            ],
            "size": page_size,
            "from": (page)*page_size
        }
    else:
        body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": query,
                                "fields": fields
                            }
                        },
                        {
                            "range": {
                                "year": {
                                    "gte": from_year,
                                    "lte": to_year
                                }
                            }
                        }
                    ]
                }
            },
            "sort": [
                {
                    "year": {
                        "order": year_order
                    }
                }
            ],
            "size": page_size,
            "from": (page)*page_size
        }

    return body
    # q = {
        # "query": {
        #     "query_string": {
        #         "query": query,
        #     },
        #     "bool" : {
        #         "must_not" : {
        #             "range" : {
        #                 "year" : { "gte" : 2021, "lte" : 2023 }
        #             }
        #         },
        #     }
        # }
    # }
    # body = {
    #     'query': {
    #         'bool': {
    #             "must": {
    #                 "match_all": {}
    #             }
    #             # 'must': 
    #             #     {'range': {'year': {'gte': 2021, "lte": 2023}}}
    #             # ,
    #             # "filter": {
    #             #     "term" : { "album" : query }
    #             # },
    #         },
    #         # "query_string": {
    #         #     "analyze_wildcard": True,
    #         #     "query": query,
    #         #     "fields": ["album", "singers"]
    #         # }
            
    #     },
    #     "size": 100
    #     ,
    #     "sort": [
    #         {
    #             "year": {
    #                 "order": year_order #asc
    #             }
    #         }
    #     ]
    # }
    # body = json.dumps(body)
    # return body


INDEX = 'tamil_songs_index'
client = Elasticsearch(HOST="http://localhost", PORT=9200,
                       http_auth=('elastic', 'EMyoDwDL4UH=4GHQW5X='))


def search(query, year_order, fields, page, page_size, from_year, to_year):
    # result = client. (index=INDEX,body=standard_analyzer(query))
    # keywords = result ['tokens']['token']
    # print(keywords)

    # query_body= process(query)
    query_body = basic_search(query, year_order, fields, page, page_size, from_year, to_year)
    print('Making Basic Search ')
    res = client.search(index=INDEX, body=query_body)
    return res
