

# Importing flask module For Webpage

import os
from time import sleep
from flask import Flask, render_template, request, redirect, url_for, session,flash,Markup,jsonify
from math import log
from DQN import *

import pandas as pd

Toggle = False


app = Flask(__name__)
socketio = SocketIO(app)

SCOREBOARD = []

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_worlds() function.
def start():
    return render_template('index.html',SCOREBOARD = SCOREBOARD)




KILLS,GENERATIONS = 0,0

STATE = []
LIVES = 0
    #print('Pulse Recieved')
    

@app.route('/data', methods=['GET', 'POST'])

def receive_variables():
    global STATE,Toggle,LIVES,KILLS,GENERATIONS
    DATA = request.get_json()
    LOC = DATA['Arr']
    KILLS = DATA['kills']
    GENERATIONS = DATA['gen']
    # print(LOC)
    #CLEANING UP THE VALUES
    X = [int(x[0]) for x in LOC]
    Y = [int(y[1]) for y in LOC]
    FIRE =  LOC[-1][-2] 
    LIVES = LOC[-1][-1]
    STATE = X+Y+[FIRE]
    Toggle = False
    result = {'message': 'Variables received by Flask', 'data': LOC}
    return jsonify(result)
    #NOW OUR  STATE WILL BE : X1,X2,...XPlayer,Y1,Y2...YPlayer,FIRE, total 15 values
    #We use lives to denote the END STATE (LIVES = 6)
    #X = [0,30]
    #Y = [0,116]
    #FIRE = {0,1}
    #DEFEATED ALIENS AND ALIENS WITH Y < 0 WILL DEFAULT TO 0,0
    
    #OUR ACTIONS ARE LEFT,RIGHT and FIRE
    #OUR REWARD FUNCTION WILL BE = min(1,-log10(2*MEAN DISTANCE/30))



SCOREBOARD = []

@socketio.on('Init')

def loc():
    global STATE,Toggle,LIVES,SCOREBOARD
    loss = []
    action_space = 3
    state_space = 15
    max_steps = 100
    episode = 100
    agent = Agent(state_space, action_space)
    for e in range(episode):
        emit('RESET')
        Pulse([0,0,0,0])
        
        emit("FETCH")
        Toggle = True
        sleep(0.5)
        if not Toggle:
            sleep(2)
        Toggle = False
        state = np.array(STATE)
        state = np.reshape(state, [1, state_space])
        #print(">>>",state)
        score = 0
        for i in range(max_steps):
            # print('e:',e,'i',i)
            action = agent.act(state)
            Pulse(ACTIONS[action])
            # sleep(0.125)
            Pulse([0,0,0,0])
            emit("FETCH")
            Toggle = True
            sleep(0.25)
            if not Toggle:
                sleep(0.5)
            Toggle = False
            
            #reward, next_state, done = env.step(action)
            done = True if LIVES >=6 else False
            mean = weight_Mean(STATE[:6],STATE[6:12])/15
            if mean!=0:
                reward = min(1,-1*log(abs(mean),10))
            else:
                reward = 1
            print(mean,reward)
            next_state = np.array(STATE)
            next_state = np.reshape(next_state, [1, state_space])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            agent.replay()
            score += reward
            if done:
                score -=20
                print("episode: {}/{}, score: {}".format(e, episode, score))
                break
        loss.append(score)
        csvdata = {
            'Episode':e,
            'score':score/i,
            'kills':KILLS,
            'Generations':GENERATIONS        }
        df = pd.DataFrame(csvdata, index=[0])
        df.to_csv('out.csv', mode='a', index=False, header=False)
    
    
    
    
    
    
    
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    socketio.run(app,debug = True)