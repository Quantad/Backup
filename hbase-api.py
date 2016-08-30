import happybase as hb
from datetime import datetime

def insert_data(data):
    connection = hb.Connection('localhost')
    table = connection.table('spectrum')
    batch = table.batch(batch_size=2)
    batch.put(datetime.now().isoformat(), data)
    batch.send()


data = [{'location:lat':'61', 'location:lon':'139', 'frequency:psd':'477'},
        {'location:lat':'63', 'location:lon':'140', 'frequency:psd':'696'},
        {'location:lat':'64', 'location:lon':'129', 'frequency:psd':'227'},
        {'location:lat':'68', 'location:lon':'128', 'frequency:psd':'646'},
        {'location:lat':'71', 'location:lon':'140', 'frequency:psd':'606'},
        {'location:lat':'73', 'location:lon':'141', 'frequency:psd':'791'},
        {'location:lat':'75', 'location:lon':'128', 'frequency:psd':'783'}]


for item in data:
    insert_data(item)