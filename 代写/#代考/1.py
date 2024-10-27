import jieba.analyse
#准备语料
# corpus = "《知否知否应是绿肥红瘦》是由东阳正午阳光影视有限公司出品，侯鸿亮担任制片人，张开宙执导，曾璐、吴桐编剧，赵丽颖、冯绍峰领衔主演，朱一龙、施诗、张佳宁、曹翠芬、刘钧、刘琳、高露、王仁君、李依晓、王鹤润、张晓谦、李洪涛主演，王一楠、陈瑾特别出演的古代社会家庭题材电视剧"
corpus='经查证，山西高官均纷纷落网'

#textrank
keywords_textrank = jieba.analyse.textrank(corpus,withFlag=True)
print(keywords_textrank)
#['有限公司', '出品', '社会', '家庭', '制片人', '担任', '影视', '题材', '电视剧', '知否', '东阳', '出演', '执导']

#tf-idf
keywords_tfidf = jieba.analyse.extract_tags(corpus)
print(keywords_tfidf)
#['知否', '领衔主演', '刘钧', '刘琳', '侯鸿亮', '张晓谦', '王一楠', '张佳宁', '李依晓', '冯绍峰', '王鹤润', '施诗', '陈瑾', '赵丽颖', '吴桐', '朱一龙', '曹翠芬', '王仁君', '曾璐', '高露']