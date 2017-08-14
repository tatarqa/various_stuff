#BIG MESS
#runtime: python27
#api_version: 1
#threadsafe: true

# [START handlers]
#handlers:
#- url: /static
#  static_dir: static
#- url: /.*
#  script: main.app
#libraries:
#- name: MySQLdb
#  version: "latest"
#- name: ssl
#  version: 2.7
# [END handlers]

#env_variables:
#    CLOUDSQL_CONNECTION_NAME: xxxx
#    CLOUDSQL_USER: xxxx
#    CLOUDSQL_PASSWORD: xxx


import logging
import os
from flask import *
from werkzeug import *
from google.appengine.ext import blobstore
import MySQLdb




app = Flask(__name__)

CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')


def connect_to_cloudsql():
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD)

    # If the unix socket is unavailable, then try to connect using TCP. This
    # will work if you're running a local MySQL server or using the Cloud SQL
    # proxy, for example:
    #
    #   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    #
    else:
        db = MySQLdb.connect(
            host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD)

    return db

@app.route('/')
def home():
	dd="Hello"
	return ("<meta http-equiv='refresh' content='1;url=/upload' />"+dd)

@app.route('/form')
def form():
	db = connect_to_cloudsql()
	cursor = db.cursor()
	cursor.execute('SHOW VARIABLES')
	for r in cursor.fetchall():
		response.write('{}\n'.format(r))
	return render_template(
		'form.html',
		data=[{'name':'US-ASCII'}, {'name':'ISO_8859-1:1987'}, {'name':'ISO_8859-2:1987'}, {'name':'ISO_8859-3:1988'}, {'name':'ISO_8859-4:1988'}, {'name':'ISO_8859-5:1988'}, {'name':'ISO_8859-6:1987'}, {'name':'ISO_8859-7:1987'}, {'name':'ISO_8859-8:1988'}, {'name':'ISO_8859-9:1989'}, {'name':'ISO-8859-10'}, {'name':'ISO_6937-2-add'}, {'name':'JIS_X0201'}, {'name':'JIS_Encoding'}, {'name':'Shift_JIS'}, {'name':'Extended_UNIX_Code_Packed_Format_for_Japanese'}, {'name':'Extended_UNIX_Code_Fixed_Width_for_Japanese'}, {'name':'BS_4730'}, {'name':'SEN_850200_C'}, {'name':'IT'}, {'name':'ES'}, {'name':'DIN_66003'}, {'name':'NS_4551-1'}, {'name':'NF_Z_62-010'}, {'name':'ISO-10646-UTF-1'}, {'name':'ISO_646.basic:1983'}, {'name':'INVARIANT'}, {'name':'ISO_646.irv:1983'}, {'name':'NATS-SEFI'}, {'name':'NATS-SEFI-ADD'}, {'name':'NATS-DANO'}, {'name':'NATS-DANO-ADD'}, {'name':'SEN_850200_B'}, {'name':'KS_C_5601-1987'}, {'name':'ISO-2022-KR'}, {'name':'EUC-KR'}, {'name':'ISO-2022-JP'}, {'name':'ISO-2022-JP-2'}, {'name':'JIS_C6220-1969-jp'}, {'name':'JIS_C6220-1969-ro'}, {'name':'PT'}, {'name':'greek7-old'}, {'name':'latin-greek'}, {'name':'NF_Z_62-010_(1973)'}, {'name':'Latin-greek-1'}, {'name':'ISO_5427'}, {'name':'JIS_C6226-1978'}, {'name':'BS_viewdata'}, {'name':'INIS'}, {'name':'INIS-8'}, {'name':'INIS-cyrillic'}, {'name':'ISO_5427:1981'}, {'name':'ISO_5428:1980'}, {'name':'GB_1988-80'}, {'name':'GB_2312-80'}, {'name':'NS_4551-2'}, {'name':'videotex-suppl'}, {'name':'PT2'}, {'name':'ES2'}, {'name':'MSZ_7795.3'}, {'name':'JIS_C6226-1983'}, {'name':'greek7'}, {'name':'ASMO_449'}, {'name':'iso-ir-90'}, {'name':'JIS_C6229-1984-a'}, {'name':'JIS_C6229-1984-b'}, {'name':'JIS_C6229-1984-b-add'}, {'name':'JIS_C6229-1984-hand'}, {'name':'JIS_C6229-1984-hand-add'}, {'name':'JIS_C6229-1984-kana'}, {'name':'ISO_2033-1983'}, {'name':'ANSI_X3.110-1983'}, {'name':'T.61-7bit'}, {'name':'T.61-8bit'}, {'name':'ECMA-cyrillic'}, {'name':'CSA_Z243.4-1985-1'}, {'name':'CSA_Z243.4-1985-2'}, {'name':'CSA_Z243.4-1985-gr'}, {'name':'ISO_8859-6-E'}, {'name':'ISO_8859-6-I'}, {'name':'T.101-G2'}, {'name':'ISO_8859-8-E'}, {'name':'ISO_8859-8-I'}, {'name':'CSN_369103'}, {'name':'JUS_I.B1.002'}, {'name':'IEC_P27-1'}, {'name':'JUS_I.B1.003-serb'}, {'name':'JUS_I.B1.003-mac'}, {'name':'greek-ccitt'}, {'name':'NC_NC00-10:81'}, {'name':'ISO_6937-2-25'}, {'name':'GOST_19768-74'}, {'name':'ISO_8859-supp'}, {'name':'ISO_10367-box'}, {'name':'latin-lap'}, {'name':'JIS_X0212-1990'}, {'name':'DS_2089'}, {'name':'us-dk'}, {'name':'dk-us'}, {'name':'KSC5636'}, {'name':'UNICODE-1-1-UTF-7'}, {'name':'ISO-2022-CN'}, {'name':'ISO-2022-CN-EXT'}, {'name':'UTF-8'}, {'name':'ISO-8859-13'}, {'name':'ISO-8859-14'}, {'name':'ISO-8859-15'}, {'name':'ISO-8859-16'}, {'name':'GBK'}, {'name':'GB18030'}, {'name':'OSD_EBCDIC_DF04_15'}, {'name':'OSD_EBCDIC_DF03_IRV'}, {'name':'OSD_EBCDIC_DF04_1'}, {'name':'ISO-11548-1'}, {'name':'KZ-1048'}, {'name':'ISO-10646-UCS-2'}, {'name':'ISO-10646-UCS-4'}, {'name':'ISO-10646-UCS-Basic'}, {'name':'ISO-10646-Unicode-Latin1'}, {'name':'ISO-10646-J-1'}, {'name':'ISO-Unicode-IBM-1261'}, {'name':'ISO-Unicode-IBM-1268'}, {'name':'ISO-Unicode-IBM-1276'}, {'name':'ISO-Unicode-IBM-1264'}, {'name':'ISO-Unicode-IBM-1265'}, {'name':'UNICODE-1-1'}, {'name':'SCSU'}, {'name':'UTF-7'}, {'name':'UTF-16BE'}, {'name':'UTF-16LE'}, {'name':'UTF-16'}, {'name':'CESU-8'}, {'name':'UTF-32'}, {'name':'UTF-32BE'}, {'name':'UTF-32LE'}, {'name':'BOCU-1'}, {'name':'ISO-8859-1-Windows-3.0-Latin-1'}, {'name':'ISO-8859-1-Windows-3.1-Latin-1'}, {'name':'ISO-8859-2-Windows-Latin-2'}, {'name':'ISO-8859-9-Windows-Latin-5'}, {'name':'hp-roman8'}, {'name':'Adobe-Standard-Encoding'}, {'name':'Ventura-US'}, {'name':'Ventura-International'}, {'name':'DEC-MCS'}, {'name':'IBM850'}, {'name':'PC8-Danish-Norwegian'}, {'name':'IBM862'}, {'name':'PC8-Turkish'}, {'name':'IBM-Symbols'}, {'name':'IBM-Thai'}, {'name':'HP-Legal'}, {'name':'HP-Pi-font'}, {'name':'HP-Math8'}, {'name':'Adobe-Symbol-Encoding'}, {'name':'HP-DeskTop'}, {'name':'Ventura-Math'}, {'name':'Microsoft-Publishing'}, {'name':'Windows-31J'}, {'name':'GB2312'}, {'name':'Big5'}, {'name':'macintosh'}, {'name':'IBM037'}, {'name':'IBM038'}, {'name':'IBM273'}, {'name':'IBM274'}, {'name':'IBM275'}, {'name':'IBM277'}, {'name':'IBM278'}, {'name':'IBM280'}, {'name':'IBM281'}, {'name':'IBM284'}, {'name':'IBM285'}, {'name':'IBM290'}, {'name':'IBM297'}, {'name':'IBM420'}, {'name':'IBM423'}, {'name':'IBM424'}, {'name':'IBM437'}, {'name':'IBM500'}, {'name':'IBM851'}, {'name':'IBM852'}, {'name':'IBM855'}, {'name':'IBM857'}, {'name':'IBM860'}, {'name':'IBM861'}, {'name':'IBM863'}, {'name':'IBM864'}, {'name':'IBM865'}, {'name':'IBM868'}, {'name':'IBM869'}, {'name':'IBM870'}, {'name':'IBM871'}, {'name':'IBM880'}, {'name':'IBM891'}, {'name':'IBM903'}, {'name':'IBM904'}, {'name':'IBM905'}, {'name':'IBM918'}, {'name':'IBM1026'}, {'name':'EBCDIC-AT-DE'}, {'name':'EBCDIC-AT-DE-A'}, {'name':'EBCDIC-CA-FR'}, {'name':'EBCDIC-DK-NO'}, {'name':'EBCDIC-DK-NO-A'}, {'name':'EBCDIC-FI-SE'}, {'name':'EBCDIC-FI-SE-A'}, {'name':'EBCDIC-FR'}, {'name':'EBCDIC-IT'}, {'name':'EBCDIC-PT'}, {'name':'EBCDIC-ES'}, {'name':'EBCDIC-ES-A'}, {'name':'EBCDIC-ES-S'}, {'name':'EBCDIC-UK'}, {'name':'EBCDIC-US'}, {'name':'UNKNOWN-8BIT'}, {'name':'MNEMONIC'}, {'name':'MNEM'}, {'name':'VISCII'}, {'name':'VIQR'}, {'name':'KOI8-R'}, {'name':'HZ-GB-2312'}, {'name':'IBM866'}, {'name':'IBM775'}, {'name':'KOI8-U'}, {'name':'IBM00858'}, {'name':'IBM00924'}, {'name':'IBM01140'}, {'name':'IBM01141'}, {'name':'IBM01142'}, {'name':'IBM01143'}, {'name':'IBM01144'}, {'name':'IBM01145'}, {'name':'IBM01146'}, {'name':'IBM01147'}, {'name':'IBM01148'}, {'name':'IBM01149'}, {'name':'Big5-HKSCS'}, {'name':'IBM1047'}, {'name':'PTCP154'}, {'name':'Amiga-1251'}, {'name':'KOI7-switched'}, {'name':'BRF'}, {'name':'TSCII'}, {'name':'CP51932'}, {'name':'windows-874'}, {'name':'windows-1250'}, {'name':'windows-1251'}, {'name':'windows-1252'}, {'name':'windows-1253'}, {'name':'windows-1254'}, {'name':'windows-1255'}, {'name':'windows-1256'}, {'name':'windows-1257'}, {'name':'windows-1258'}, {'name':'TIS-620'}, {'name':'CP50220'}],
		xxxfewfe=response
		)

@app.route("/upload")
def upload():
	uploadUri = blobstore.create_upload_url('/submit', gs_bucket_name="fit-axis-2340")
	return render_template('form2.html', uploadUri=uploadUri)

@app.route("/submit", methods=['POST'])
def submit():
	if request.method == 'POST':
		f = request.files['file']
		header = f.headers['Content-Type']
		parsed_header = parse_options_header(header)
		blob_key = parsed_header[1]['blob-key']
		fPath="/uploads/"+blob_key
		return render_template('fileUploaded.html', bkey=blob_key)
	#{'name': 'file', 'headers': Headers([('Content-Type', 'message/external-body; blob-key="encoded_gs_file:cHl0Y2hvbi9mYWtlLUVmTkpBSUJsMGJoLVNNdVByZXh5dWc9PQ=="; access-type="X-AppEngine-BlobKey"'), ('Content-Disposition', 'form-data; name="file"; filename="apetit.css"')]), 'stream': <_io.BytesIO object at 0x04695C00>, 'filename': u'apetit.css'}
	#{'headers': Headers([('Content-Disposition', 'form-data; name="file"; filename="apetit.css"'), ('Content-Type', 'text/css')]), 'name': 'file', 'stream': <_io.BytesIO object at 0x036048A0>, 'filename': u'apetit.css'}


@app.route("/uploads/<bkey>")
def img(bkey):
	blob_info = blobstore.get(bkey)
	response = make_response(blob_info.open().read())
	response.headers['Content-Type'] = blob_info.content_type
	return response





@app.route('/submitted', methods=['POST'])

def submitted_form():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		site = request.form['site_url']
		comments = request.form['comments']
		chosenEnc =  request.form['encoding']

		return render_template(
			'submitted_form.html',
			filenameko=filename,
			name=name,
			email=email,
			site=site,
			comments=comments,
			chosenEnc=chosenEnc)
		# [END render_template]


@app.errorhandler(500)
def server_error(e):
	# Log the error and stacktrace.
	logging.exception('An error occurred during a request.')
	return 'An internal error occurred.', 500
# [END app]