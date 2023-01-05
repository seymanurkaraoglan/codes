from flask import Flask,request
from flask_restful import Api,Resource  #bize bazı kaynaklar sağlayacak

#Uygulamayı başlatıyoruz
app = Flask(__name__)
api = Api(app)


#nesne oluşturuyoruz
names = {"tim" : {"age" : 19, "gender": "male"},
        "bill" : {"age" : 70, "gender": "male"}}

Videos = {}
#yaptığımız apie ekleyeceğimiz fonksiyonu yazıyoruz
# class HelloWorld(Resource):
#     def get(self, name, test):
#         return {"name" : name, "test" : test}
#     def get(self, name):
#         return names[name]
#     def post(self):
#         return {"data" : "Posted"}

class Video(Resource):
    def get(self,video_id):
        return Videos[video_id]
    def put(self,video_id):
        print(request.form)
        return {}
#apie eklemek istediğimiz classı ve uzantıyı verdik.
# api.add_resource(HelloWorld,"/helloworld/<string:name>/<int:test>")
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)