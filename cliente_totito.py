import socketio, signal, sys

sio = socketio.Client()

username = sys.argv[1]
tid = sys.argv[2]
tserver = sys.argv[3]

# Client for totito project

@sio.event
def connect():
    sio.emit('signin', {
    'user_name': username,
    'tournament_id': tid,
    'user_role': 'player'})
    print('Connected as ', username, ' to tournament ', tid, ' on server ', tserver)


@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.on('ok_signin')
def ok_signin():
    print('Successfully signed in!')

@sio.on('ready')
def ready(data):
    print('data of ready received', data)

@sio.on('finish')
def finish(data):
    print('tournament is over', data)
    
sio.connect(tserver)
try:
    sio.wait()

except KeyboardInterrupt as error:
    #sio.emit('asr', {"command":"disconnect"})

    sio.disconnect()
    print("sio.connected:%s" % sio.connected)



