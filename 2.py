# Importación librerias
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# Credenciales
ckey = "W4AgF66h1bM4u9f9VwO0MaNeg"
csecret = "8M1L0RE7Sssav2KRDzdWTJsu0VQJiQj3az2mxwmr59FTDSGf2p"
atoken = "301140584-XiiZWps5D4Qol0C7iJIK8lib3HvJ5LJDGaCKpuXW"
asecret = "yW4vQynMPMDUn3l1Gh8DDwXlrX43reetlfsN6avzGP7BQ"

#


class listener(StreamListener):

    def on_data(self, data):
        archiTweet = json.loads(data)
        try:

            archiTweet["_id"] = str(archiTweet['id'])
            doc = db.save(archiTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

# Conexión con couchdb
server = couchdb.Server('http://admin:admin@localhost:5984/')
try:
    db = server.create('olimpiccities')
except:
    db = server('olimpiccities')

# Busqueda de twweet por Track
twitterStream.filter(track=['juegos olimpicos', 'Tokio'])
