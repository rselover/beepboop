from ingest import ingest

def test_ingest():
    url='https://gist.githubusercontent.com/rselover/a82f17ec1a97538080940248880597fe/raw/69c797301be90b135eccc00d2015a28edc630b95/weston.json'
    df=ingest(url)
    assert df.shape[0]==4336
    