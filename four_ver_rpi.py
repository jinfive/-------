#-*-coding:utf-8-*-
from pynput import keyboard

from flask import Flask,send_file
from flask import request,render_template,abort, redirect, url_for,Response
import threading

import time
from datetime import datetime
from flask import Markup

import os
import random
import RPi.GPIO as GPIO
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib

# Import the ADS1x15 module.
import Adafruit_ADS1x15

# 모델 불러오기
loaded_model = joblib.load('decision_tree_model.pkl')
loaded_label_encoder = joblib.load('label_encoder.pkl')


adc1 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
GAIN = 1
switch1=6
switch2=19
switch3=20
led1=13
led2=26
led3=21
rel1=14
rel2=15
rel3=18
GPIO.setmode(GPIO.BCM)
GPIO.setup([switch1,switch2,switch3],GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup([led1,led2,led3,rel1,rel2,rel3],GPIO.OUT)

'''
 if not GPIO.input(switch1):
            GPIO.output(led1, GPIO.HIGH)
            GPIO.output(rel1, GPIO.HIGH)
        else :
            GPIO.output(rel1, GPIO.LOW)
            GPIO.output(led1, GPIO.LOW)
        
        if not GPIO.input(switch2):
            GPIO.output(led2, GPIO.HIGH)
            GPIO.output(rel2, GPIO.HIGH)
        else :
            GPIO.output(rel2, GPIO.LOW)
            GPIO.output(led2, GPIO.LOW)
        
        if not GPIO.input(switch3):
            GPIO.output(led3, GPIO.HIGH)
            GPIO.output(rel3, GPIO.HIGH)
        else :
            GPIO.output(led3, GPIO.LOW)
            GPIO.output(rel3, GPIO.LOW)
'''   

import random

# 초기 데이터 배열 생성 (길이 50의 랜덤 배열)
data1 = [20000 for _ in range(50)]
data2 = [20000 for _ in range(50)]
data3 = [20000 for _ in range(50)]

def add_data_and_get_average(data, new_value):
    # 첫 번째 요소를 제거하고
    data.pop(0)
    # 새로운 값을 마지막에 추가합니다.
    data.append(new_value)
    # 배열의 평균값을 계산합니다.
    average_value = sum(data) / len(data)
    return data, average_value
def transform_x_to_y(x):
    m = -0.3589
    b = 7541
    y = m * x + b
    return y


value1=20000
value2=20000
value3=20000
plug1_start=False
plug2_start=False
plug3_start=False
before_value1=20000
before_value2=20000
before_value3=20000
off_timer1=time.time()
off_timer2=time.time()
off_timer3=time.time()
error_cnt1=0
error_cnt2=0
error_cnt3=0
normal_cnt1=0
normal_cnt2=0
normal_cnt3=0
import threading
t1=time.time()
msg1='not used'
msg2='not used'
msg3='not used'
def predict_score():
    global value1,value2,value3,t1,plug1_start,plug2_start,plug3_start,msg1,msg2,msg3
    global t1
    while True:
            if time.time()-t1>2:
                
                print(msg1,msg2,msg3)
                if plug1_start and msg1!='error':
                    # 예측 예시1
                    sample_scores = np.array([value1]).reshape(-1, 1)
                    sample_pred = loaded_model.predict(sample_scores)
                    sample_pred_labels = loaded_label_encoder.inverse_transform(sample_pred)
                    msg1=sample_pred_labels[0]
                    print("Predicted devece : ", sample_pred_labels)
                if plug2_start and msg2!='error':
                    # 예측 예시1
                    sample_scores = np.array([value2]).reshape(-1, 1)
                    sample_pred = loaded_model.predict(sample_scores)
                    sample_pred_labels = loaded_label_encoder.inverse_transform(sample_pred)
                    msg2=sample_pred_labels[0]
                    print("Predicted devece : ", sample_pred_labels)
                if plug3_start and msg3!='error':
                    # 예측 예시1
                    sample_scores = np.array([value3]).reshape(-1, 1)
                    sample_pred = loaded_model.predict(sample_scores)
                    sample_pred_labels = loaded_label_encoder.inverse_transform(sample_pred)
                    msg3=sample_pred_labels[0]
                    print("Predicted devece : ", sample_pred_labels)        
                t1=time.time()
threading.Thread(target=predict_score,daemon=True).start()

values1 = [0]*4
def get_data():  
    global value1,value2,value3,t1,plug1_start,plug2_start,plug3_start,msg1,msg2,msg3
    global before_value1,before_value2,before_value3
    global off_timer1
    global off_timer2
    global off_timer3
    global error_cnt1
    global error_cnt2
    global error_cnt3
    global normal_cnt1
    global normal_cnt2,values1 
    global normal_cnt3,data1,data2,data3
    global adc1 
    global GAIN
    global switch1
    global switch2
    global switch3
    global led1
    global led2
    global led3
    global rel1
    global rel2
    global rel3
    try:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(rel1, GPIO.LOW)
                
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(rel2, GPIO.LOW)
                
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(rel3, GPIO.LOW)
        while True:
            for i in range(4):
                values1[i] = adc1.read_adc(i, gain=GAIN)
            #print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values1))
            time.sleep(0.01)
            #show graph
            if not GPIO.input(switch1):
                off_timer1=time.time()
                GPIO.output(led1, GPIO.HIGH)
                GPIO.output(rel1, GPIO.HIGH)
             
            if not GPIO.input(switch2):
                off_timer2=time.time()
                GPIO.output(led2, GPIO.HIGH)
                GPIO.output(rel2, GPIO.HIGH)
            if not GPIO.input(switch3):
                off_timer3=time.time()
                GPIO.output(led3, GPIO.HIGH)
                GPIO.output(rel3, GPIO.HIGH)
            if time.time()-off_timer1>30:
                print('off_1 not used')
                plug1_start=False
                data1 = [20000 for _ in range(50)]    
                value1=20000            
                GPIO.output(led1, GPIO.LOW)
                GPIO.output(rel1, GPIO.LOW)
                off_timer1=time.time()
                msg1='not used'
            if time.time()-off_timer2>30:
                print('off_2 not used')    
                msg2='not used'
                plug2_start=False
                data2 = [20000 for _ in range(50)]  
                value2=20000        
                GPIO.output(led2, GPIO.LOW)
                GPIO.output(rel2, GPIO.LOW)
                off_timer2=time.time()
            if time.time()-off_timer3>30:
                print('off_3 not used')
                msg3='not used'
                plug3_start=False
                data3 = [20000 for _ in range(50)]
                value3=20000
                GPIO.output(led3, GPIO.LOW)
                GPIO.output(rel3, GPIO.LOW)
                 
                off_timer3=time.time()
            
            if time.time()-off_timer1>10 and plug1_start:
                print('off_1 off device')
                msg1='not used'
                plug1_start=False
                data1 = [20000 for _ in range(50)]   
                value1=20000     
                GPIO.output(led1, GPIO.LOW)
                GPIO.output(rel1, GPIO.LOW)
            if time.time()-off_timer2>10 and plug2_start:
                print('off_2 off device ')
                plug2_start=False    
                msg2='not used'
                data2 = [20000 for _ in range(50)]   
                value2=20000
                GPIO.output(led2, GPIO.LOW)
                GPIO.output(rel2, GPIO.LOW)
            if time.time()-off_timer3>10 and plug3_start:
                print('off_3 off device')
                msg3='not used'
                plug3_start=False
                data3= [20000 for _ in range(50)]      
                value3=20000
                GPIO.output(led3, GPIO.LOW)
                GPIO.output(rel3, GPIO.LOW)
            ##########1111111111111111111111111111111111111111111111111111111111111  
            if(values1[0]<20000):
                off_timer1=time.time()
                new_value = values1[0]
                updated_data, value1 = add_data_and_get_average(data1, new_value)
                #with open('heater.txt','a') as f:
                    #f.write(f"{average_value}\n")
                print("Average Value of Updated Data1:", value1)
                normal_cnt1+=1
                if normal_cnt1>3:
                    #print(normal_cnt2,error_cnt2)
                    if error_cnt1>normal_cnt1*6:
                        print('error1')
                        msg1='error'
                        plug1_start=False
                        data1 = [20000 for _ in range(50)]
                        value1=20000
                        GPIO.output(led1, GPIO.LOW)
                        GPIO.output(rel1, GPIO.LOW)
                    normal_cnt1=0
                    error_cnt1=0
                if abs(before_value1-value1)<100:
                    plug1_start=True
                else :
                    plug1_start=False    
                before_value1=value1  
           
                # 예시 사용
                #watt= transform_x_to_y(value1)
                #print(watt)
            else:        
                if value1<20000:
                    error_cnt1+=1
            ##########22222222222222222222222222222222222222222222222222222
            if(values1[1]<20000):
                off_timer2=time.time()
                new_value = values1[1]
                updated_data, value2 = add_data_and_get_average(data2, new_value)
                #with open('heater.txt','a') as f:
                    #f.write(f"{average_value}\n")
                print("Average Value of Updated Data2:", value2)
                normal_cnt2+=1
                if normal_cnt2>3:
                    #print(normal_cnt2,error_cnt2)
                    if error_cnt2>normal_cnt2*6:
                        print('error2')
                        msg2='error'
                        value2=20000
                        plug2_start=False
                        data2 = [20000 for _ in range(50)]
                        GPIO.output(led2, GPIO.LOW)
                        GPIO.output(rel2, GPIO.LOW)
                    normal_cnt2=0
                    error_cnt2=0
                if abs(before_value2-value2)<100:
                    plug2_start=True
                else :
                    plug2_start=False
                before_value2=value2 
                # 예시 사용
                #watt= transform_x_to_y(value1)
                #print(watt)
            else:
                if value2<20000:
                    error_cnt2+=1
            ##########33333333333333333333333333333333333333333
            if(values1[2]<20000):
                off_timer3=time.time()
                new_value = values1[2]
                updated_data, value3 = add_data_and_get_average(data3, new_value)
                #with open('heater.txt','a') as f:
                    #f.write(f"{average_value}\n")
                print("Average Value of Updated Data3:", value3)
                normal_cnt3+=1
                if normal_cnt3>3:
                    #print(normal_cnt3,error_cnt3)
                    if error_cnt3>normal_cnt3*6:
                        print('error3')
                        msg3='error'
                        value3=20000
                        plug3_start=False
                        data3 = [20000 for _ in range(50)]
                        GPIO.output(led3, GPIO.LOW)
                        GPIO.output(rel3, GPIO.LOW)
                    normal_cnt3=0
                    error_cnt3=0
                if abs(before_value3-value3)<100:
                    plug3_start=True
                else :
                    plug3_start=False
                before_value3=value3 
            else:
                if value3<20000:
                    error_cnt3+=1
                # 예시 사용
                #watt= transform_x_to_y(value1)
                #print(watt)   

           
    except Exception as e:
        print(e)
        print('err')
        GPIO.cleanup()
threading.Thread(target=get_data,daemon=True).start()


time.sleep(5)

app = Flask(__name__)

@app.route('/read_data', methods=['GET', 'POST'])
def tag0():
    global msg1,msg2,msg3
    return {
        'plug1': msg1,        
        'plug2': msg2,
        'plug3': msg3
    }
    

graph_data1 = [20000 for _ in range(50)]
graph_data2 = [20000 for _ in range(50)]
graph_data3 = [20000 for _ in range(50)]
@app.route('/read_graph_data', methods=['GET', 'POST'])
def tag1():
    global graph_data1,values1,graph_data2,graph_data3,value1,value2,value3
    new_data1=values1[0]
    new_data2=values1[1]
    new_data3=values1[2]
    del graph_data1[0]
    del graph_data2[0]
    del graph_data3[0]
    
    # 새로운 항목 추가
    graph_data1.append(new_data1)
    graph_data2.append(new_data2)
    graph_data3.append(new_data3)

    #print(graph_data1)
    return {
       'graph_data1': graph_data1,
       'graph_data2': graph_data2,
       'graph_data3': graph_data3,
    }

@app.route("/")
def main():
    return render_template('main2.html')

@app.route('/main2.html')
def gohome():    
    return render_template("main2.html")



if __name__ == '__main__':
    app.run("0.0.0.0")

