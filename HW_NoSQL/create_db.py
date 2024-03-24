from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sudorenkoroma:sudorenkoroma@cluster0.vcn7idw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.db02

# Send a ping to confirm a successful connection
try:
    db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
        {
        "name": 'barsik',
        "age": 3,
        "features": ['ходить в капці', 'дає себе гладити', 'рудий'],
        }
    ]
)
    print("Successfuly")
except Exception as e:
    print(e)
