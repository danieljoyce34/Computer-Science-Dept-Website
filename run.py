#!../csc_env/bin/python
from app import app
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain('server.crt', 'server.key')

app.run(debug=True, ssl_context=context)
# host='0.0.0.0'
