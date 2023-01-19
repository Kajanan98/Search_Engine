import json
import codecs
import random
import pandas as pd
import numpy as np

f = codecs.open('D:\DELL\OneDrive\Desktop\Assgnment\SearchEngine\search_engine_api\songs.json', 'w', encoding='utf-8')
df = pd.read_csv('D:\DELL\OneDrive\Desktop\Assgnment\SearchEngine\search_engine_api\180295F_Mini Project - Corpus.xlsx')

for i in range(df.shape[0]):
    # try:
        print(i)
        dict_ = {}
        dict_["பாடல் வரிகள்"] = df['Lyrics'][i]
        dict_["பாடகர்"] = df['Singers'][i]
        dict_["இசையமைப்பாளர்"] = df['Composer'][i]
        dict_["பாடலாசிரியர்"] = df['Lyricist'][i]
        dict_["திரைப்படம்"] = df['Album'][i]
        dict_["வருடம்"] = int(np.int64(df['Year'][i]))
        dict_["உருவகம்_1"] = df['metaphor_1'][i]
        dict_["மூல_களம்_1"] = df['source_domain_1'][i]
        dict_["இலக்கு_களம்_1"] = df['target_domain_1'][i]
        dict_["விளக்கம்_1"] = df['interpretation_1'][i]
        dict_["உருவகம்_2"] = df['metaphor_2'][i]
        dict_["மூல_களம்_2"] = df['source_domain_2'][i]
        dict_["இலக்கு_களம்_2"] = df['target_domain_2'][i]
        dict_["விளக்கம்_2"] = df['interpretation_2'][i]
        dict_["உருவகம்_3"] = df['metaphor_3'][i]
        dict_["மூல_களம்_3"] = df['source_domain_3'][i]
        dict_["இலக்கு_களம்_3"] = df['target_domain_3'][i]
        dict_["விளக்கம்_3"] = df['interpretation_3'][i]


        f.write('{ "index" : { "_index" : "tamil_songs_index", "_type" : "metaphor", "_id" :' + str(i) + ' } }\n')
        json.dump(dict_, f, ensure_ascii=False)
        f.write('\n')
        i += 1