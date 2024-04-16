import pymongo

client = pymongo.MongoClient('mongodb+srv://staudachermatthew:3oy7jes9SD20j8iL@cluster1.jwepw3v.mongodb.net/')

db = client['Cluster1']
collection = db['sample_mflix']
print(collection)
client.close()