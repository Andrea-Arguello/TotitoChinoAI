import socketio, signal, sys
import ai_totito as myai

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
    print('Connected: \n\tusername:', username, '\n\ttournament:', tid, '\n\tserver:', tserver)


@sio.event
def disconnect():
    print('Disconnected from server')

@sio.on('ok_signin')
def ok_signin():
    print('Successfully signed in!')

@sio.on('ready')
def ready(data):
    print('data of ready received:', data)

    # AI logic
  
    sio.emit('play', {
    'tournament_id': tid,
    'player_turn_id': data['player_turn_id'],
    'game_id': data['game_id'],
    'movement': myai.minmax(data['board']) })

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



