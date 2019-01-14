import flask
import json
from flask import request
from flask_cors import *
import struct
import base64
import os
import random
from datetime import datetime
from urllib import request as url_request
from urllib import parse

app=flask.Flask(__name__,static_folder='.',static_url_path='')

CORS(app, supports_credentials=True)

import pymysql
import pymysql.cursors

from sklearn.cluster import KMeans

import numpy as np
# 对一个表中数据筛选出每小时的个数
def total_getoff_geton(datalist):
	datalist=list(datalist)
	target=[];
	for i in range(0,24):
		target.append(0)
	for item in datalist:
		# print(item)
		# item=list(item)
		try:
			hour=datetime.strptime(item[5],'%Y-%m-%d %H:%M:%S').hour
		except Exception as e:
			print('error')
		
		# print(hour)
		# hour=item[5].split(" ")[1].split(":")[0]
		if(0<int(hour)<=1):
			target[0]=target[0]+1
			# print(item[2]+","+item[1]+"^")
		elif(1<int(hour)<=2):
			target[1]=target[1]+1
			
		elif(2<int(hour)<=3):
			target[2]=target[2]+1
			
		elif(3<int(hour)<=4):
			target[3]=target[3]+1
			
		elif(4<int(hour)<=5):
			target[4]=target[4]+1
			
		elif(5<int(hour)<=6):
			target[5]=target[5]+1
			
		elif(6<int(hour)<=7):
			target[6]=target[6]+1
			
		elif(7<int(hour)<=8):
			target[7]=target[7]+1
			
		elif(8<int(hour)<=9):
			target[8]=target[8]+1
			
		elif(9<int(hour)<=10):
			target[9]=target[9]+1
			
		elif(10<int(hour)<=11):
			target[10]=target[10]+1
			
		elif(11<int(hour)<=12):
			target[11]=target[11]+1
			
		elif(12<int(hour)<=13):
			target[12]=target[12]+1
			
		elif(13<int(hour)<=14):
			target[13]=target[13]+1
			
		elif(14<int(hour)<=15):
			target[14]=target[14]+1
			
		elif(15<int(hour)<=16):
			target[15]=target[15]+1
			
		elif(16<int(hour)<=17):
			target[16]=target[16]+1
			
		elif(17<int(hour)<=18):
			target[17]=target[17]+1
			
		elif(18<int(hour)<=19):
			target[18]=target[18]+1
			
		elif(19<int(hour)<=20):
			target[19]=target[19]+1
			
		elif(20<int(hour)<=21):
			target[20]=target[20]+1
			
		elif(21<int(hour)<=22):
			target[21]=target[21]+1
			
		elif(22<int(hour)<=23):
			target[22]=target[22]+1
			
		else:
			target[23]=target[23]+1
	# print(target)
	return target;
# 热力图请求，返回每小时的坐标记录
def dog(num,item,target):
	tmp={"longi":float(item[2]),"lati":float(item[3])}
	if (num in target):
		target[num].append(tmp)
	else:
		target[num]=[]
		target[num].append(tmp)

def getCoordPerHour(datalist):
	datalist=list(datalist)
	target={};
	for item in datalist:
		try:
			hour=datetime.strptime(item[5],'%Y-%m-%d %H:%M:%S').hour
		except Exception as e:
			print('error')
		
		# print(hour)
		# hour=item[5].split(" ")[1].split(":")[0]
		if(0<int(hour)<=1):
			num=0
			dog(num,item,target)
			# print(item[2]+","+item[1]+"^")
		elif(1<int(hour)<=2):
			num=1
			dog(num,item,target)
			
		elif(2<int(hour)<=3):
			num=2
			dog(num,item,target)
			
		elif(3<int(hour)<=4):
			num=3
			dog(num,item,target)
			
		elif(4<int(hour)<=5):
			num=4
			dog(num,item,target)
			
		elif(5<int(hour)<=6):
			num=5
			dog(num,item,target)
			
		elif(6<int(hour)<=7):
			num=6
			dog(num,item,target)
			
		elif(7<int(hour)<=8):
			num=7
			dog(num,item,target)
			
		elif(8<int(hour)<=9):
			num=8
			dog(num,item,target)
			
		elif(9<int(hour)<=10):
			num=9
			dog(num,item,target)
			
		elif(10<int(hour)<=11):
			num=10
			dog(num,item,target)
			
		elif(11<int(hour)<=12):
			num=11
			dog(num,item,target)
			
		elif(12<int(hour)<=13):
			num=12
			dog(num,item,target)
			
		elif(13<int(hour)<=14):
			num=13
			dog(num,item,target)
			
		elif(14<int(hour)<=15):
			num=14
			dog(num,item,target)
			
		elif(15<int(hour)<=16):
			num=15
			dog(num,item,target)
			
		elif(16<int(hour)<=17):
			num=16
			dog(num,item,target)
			
		elif(17<int(hour)<=18):
			num=17
			dog(num,item,target)
			
		elif(18<int(hour)<=19):
			num=18
			dog(num,item,target)
			
		elif(19<int(hour)<=20):
			num=19
			dog(num,item,target)
			
		elif(20<int(hour)<=21):
			num=20
			dog(num,item,target)
			
		elif(21<int(hour)<=22):
			num=21
			dog(num,item,target)
			
		elif(22<int(hour)<=23):
			num=22
			dog(num,item,target)
			
		else:
			num=23
			dog(num,item,target)
	# print(target)
	return target;
def center_to_dic(centerlist):
	target=[]
	for item in centerlist:
		print("-------------")
		print(item)
		tmp={"longi":item[0],"lati":item[1]}
		target.append(tmp)
	return target

# 在generate的日期总共的点，筛选出在矩形选框中的记录
def record_in_rectge(records,lati_min,lati_max,longi_min,longi_max):
	mylist=[]
	# print(records)
	for item in records:
		if(item[3]>lati_min and item[3]<lati_max and item[2]>longi_min and item[2] <longi_max):
			mylist.append(item)
	# print('+=====================')
	# print(mylist)
	return mylist
POI_CENTERS=[]
# GETOFFDATA,存储getoff查询状态下，存储的数据，之后被record_in_rectge()调用，求出在矩形内的数据，然后再找请求时间段内所有数据，进行对比
GETOFFDATA=[]

def middle_and_geton(part_rec,day):
	conn=pymysql.Connect(host='127.0.0.1',user='root',passwd='',db='gps_taxi',port=3306,charset='utf8')
	conn.commit()
	cursor=conn.cursor()
	cursor.execute('select * from lake_getoff_middle_'+day)
	all__rec=cursor.fetchall()
	total={}
	print('part'+str(len(part_rec)))
	print('all'+str(len(all__rec)))
	for part in part_rec:
		for all_ in all__rec:

			if (part[1]==all_[1] and part[2]==all_[2] and part[3]==all_[3] and part[4]==all_[4] and part[5]==all_[5]):

				index=int(all_[0])
				end_index=index
				while index>0:
					if (all__rec[index][4]=='1'):
						if(all__rec[index-1][4]=='0'):
							start_index=index
						# target=all__rec[index]
							ele=[]
							vehicle_id=''
							for i in range(start_index,end_index+1):
								tmp={}
								vehicle_id=all__rec[i][1]
								tmp['longi']=all__rec[i][2]
								tmp['lati']=all__rec[i][3]
								tmp['state']=all__rec[i][4]
								tmp['speed_time']=all__rec[i][5]
								ele.append(tmp)
								# tmp.append([all__rec[i][2],all__rec[i][3],all__rec[i][5]])
							total[vehicle_id]=ele
						# res.append(target)
							break
					
					index=index-1
				break
			else:
				continue
	# print(total)
	return total
GETONDATA=[]
def middle_and_getoff(part_rec,day):
	conn=pymysql.Connect(host="127.0.0.1",port=3306,user="root",passwd="",db='gps_taxi',charset='utf8')
	conn.commit()
	cursor=conn.cursor()
	cursor.execute("select * from lake_geton_middle_"+day)
	all__rec=cursor.fetchall()
	total={}
	for part in part_rec:
		for all_ in all__rec:
			# print(all_)
			if(part[1]==all_[1] and all_[4]=='0' and all_[5]>part[5]) :
				index=int(all_[0])
				end_index=index
				while  index>0:
					if all__rec[index][4]=='1':
						if all__rec[index-1][4]=='0':
							start_index=index
							ele=[]
							vehicle_id=''
							for i in range(start_index,end_index+1):
								tmp={}
								vehicle_id=all__rec[i][1]
								tmp['longi']=all__rec[i][2]
								tmp['lati']=all__rec[i][3]
								tmp['state']=all__rec[i][4]
								tmp['speed_time']=all__rec[i][5]
								ele.append(tmp)
							total[vehicle_id]=ele
							break
					index=index-1
				break
			else:
				continue
	return total

def get_geton_point(allrecords):
	X=[]
	for key in iter(allrecords.keys()):
		value=allrecords[key]
		item=[value[0]['longi'],value[0]['lati']]
		X.append(item)
	return X

def get_getoff_point(allrecords):
	X=[]
	for key in iter(allrecords.keys()):
		value=allrecords[key]
		item=[value[-1]['longi'],value[-1]['lati']]
		X.append(item)
	return X

def cluster_data(allrecords,label):

# allrecords={"vehicle_id":[middle],"vehicle_id":[middle],...,"vehicle_id":[middle]}
# label=[2,1,3,1]
	newdic={}
	i=0
	for key in iter(allrecords.keys()):
		value=allrecords[key]
		tag=str(label[i])
		if tag in newdic:
			newdic[tag].append({key:value})
		else:
			newdic[tag]=[]
			newdic[tag].append({key:value})
		i+=1
	return newdic
def requestDB(sql):
	conn=pymysql.Connect(host='127.0.0.1',user='root',passwd='',db='gps_taxi',port=3306,charset='utf8')
	conn.commit()
	cursor=conn.cursor()
	cursor.execute(sql)
	res=cursor.fetchall()
	cursor.close()
	conn.close()
	return res;

def gpsToGaoDe(coords):
	coo=[]
	for item in coords:
		obj=[]
		obj.append(str(item[0]))
		obj.append(str(item[1]))
		print("=============")
		print(item)
		tmp=",".join(obj)
		coo.append(tmp)
	coords='|'.join(coo)  # coords='116.481499,39.990475|116.481499,39.990375' 参数的形式
	print(coords)
	key="200524690d0ee70cc6e0314701f542cb"
	url="http://restapi.amap.com/v3/assistant/coordinate/convert?locations={}&coordsys=gps&output=json&key={}".format(coords,key)
	req=url_request.urlopen(url);
	res=req.read().decode("utf-8")
	locations=json.loads(res)["locations"]

	new=[]
	for item in locations.split(";"):
		tmp=item.split(",")
		ele={"longi":float(tmp[0]),"lati":float(tmp[1])}
		new.append(ele)
	return new;

def poiRequest(coords):
	key="200524690d0ee70cc6e0314701f542cb"
	poi_total=[]
	for item in coords:
		longi=item["longi"]
		lati=item["lati"]
		target=["company","residential","market","school"]
		obj={}
		for ele in target:
			poi=parse.quote(ele)
			url='http://restapi.amap.com/v3/place/around?key={0}&location={1},{2}&city=hangzhou&output=json&radius=500&types={3}'.format(key,str(longi),str(lati),poi)
			req=url_request.urlopen(url)
			res=req.read().decode("utf-8")
			# print(res)
			res=json.loads(res)["count"]
			obj[ele]=res
		poi_total.append(obj)

	return poi_total


# OD模块中，generate按钮请求某天getoff的数据
@app.route('/getoffdata', methods=['GET'])
def getOffData():
	args=request.args
	# print(args.get("starttime"))
	start=args.get("start_time")
	end=args.get("end_time")
	day=start.split(" ")[0][-1]
	print(start)
	print(end)
	print(type(day))
	db = pymysql.Connect(host='127.0.0.1', user='root', passwd='', db='gps_taxi', port=3306, charset='utf8')
	db.commit()
	cursor = db.cursor()
	cursor.execute("select * from lake_getoff_"+day+" where speed_time > %s and speed_time < %s",[start,end])

	res=cursor.fetchall()
	global GETOFFDATA#将请求到的GETOFFDATA作为全局数据，以方便矩形选框筛选
	GETOFFDATA=list(res)
	print(len(GETOFFDATA))
	cursor.close()
	db.close()
	back=[]
	flag=True;
	for item in res:
		back.append({"longi":float(item[2]),"lati":float(item[3])})
	# print(back)
	# print(res)
	# for item in res:
	# 	if flag==True:
	# 		back+=str(item[2])+','+str(item[3])
	# 		flag=False
	# 	else:
	# 		back+='^'+str(item[2])+','+str(item[3])
	# print(values)
	
	getoff_data=json.dumps({"data":back})
	return getoff_data;

@app.route('/getondata',methods=['GET'])
def getOnData():
	args=request.args
	start=args.get("start_time")
	end=args.get("end_time")
	day=start.split(" ")[0][-1]
	print(start)
	print(end)
	try:
		db=pymysql.Connect(host='127.0.0.1',user='root',passwd='',db='gps_taxi',port=3306,charset='utf8')
		db.commit()
		cursor=db.cursor()
		cursor.execute("select * from lake_geton_"+day+" where speed_time>%s and speed_time<%s",[start,end])
		res=cursor.fetchall()
		global GETONDATA
		GETONDATA=list(res)
		cursor.close()
		db.close()
		back=[]
		for item in res:
			back.append({"longi":item[2],"lati":item[3]})

	except Exception as e:
		print("数据库请求 error")
	geton_data=json.dumps({"data":back})
	return geton_data


# getoff查询状态，寻找上车点进行聚类
@app.route('/getoffclusterdata', methods=['GET'])#url router funciton
def getoffClusterData():
	args=request.args
	north=args.get('north')
	south=args.get('south')
	west=args.get('west')
	east=args.get('east')
	day=args.get('day')
	print('north'+north)
	print('south'+south)
	print('day'+day)
	global GETOFFDATA
	print("GETOFFDATA"+str(len(GETOFFDATA)));
	# print(tmp)tmp是查看时间内的所有记录
	rectangle_list=record_in_rectge(GETOFFDATA,lati_min=south,lati_max=north,longi_min=west,longi_max=east)
	print('rectangle_list'+str(len(rectangle_list)))
	total=middle_and_geton(rectangle_list,day)
	
	X=get_geton_point(total)
	X=np.array(X)
	# label=KMeans(n_clusters=4,random_state=4).fit_predict(X)
	kmeans=KMeans(n_clusters=4,random_state=4).fit(X)
	label=kmeans.predict(X)
	center=kmeans.cluster_centers_
	global POI_CENTERS
	POI_CENTERS=center  #将聚类后的簇中心赋给全局变量，以便poi_info请求拿到

	centerdic=center_to_dic(center)
	clusterdata=cluster_data(total,label)
	clusterdata["center"]=centerdic
	print("++++++")
	print(center)

	return json.dumps(clusterdata)

@app.route('/poi_info',methods=["GET"])
def poiInfo():
	print("11111111111111111")
	global POI_CENTERS
	print(POI_CENTERS);
	gps_gaode=gpsToGaoDe(POI_CENTERS)
	poi_total=poiRequest(gps_gaode)
	poi_info={}
	poi_info['poi']=poi_total

	return json.dumps(poi_info)

@app.route('/getonclusterdata',methods=['GET'])
def getonClusterData():
	args=request.args
	north=args.get("north")
	south=args.get("south")
	west=args.get("west")
	east=args.get("east")
	day=args.get("day")
	print("GETON"+day)
	global GETONDATA
	print("GETONDATA"+str(len(GETONDATA)))
	rectangle_list=record_in_rectge(GETONDATA,lati_min=south,lati_max=north,longi_min=west,longi_max=east)
	print('rectangle_list'+str(len(rectangle_list)))
	total=middle_and_getoff(rectangle_list,day)
	X=get_getoff_point(total)
	X=np.array(X)
	kmeans=KMeans(n_clusters=4,random_state=4).fit(X)
	label=kmeans.predict(X)
	
	center=kmeans.cluster_centers_
	global POI_CENTERS
	POI_CENTERS=center

	centerdic=center_to_dic(center)
	clusterdata=cluster_data(total,label)
	clusterdata["center"]=centerdic

	return json.dumps(clusterdata)


# heatmap模块，生成散点图中的数据，返回一个list，length是24，每个值是每小时的出行数量
@app.route('/heatmap_scatterParagraph',methods=['GET'])
def scatterParagraph():
	args=request.args
	date=args.get('date')
	state=args.get('state') #state代表getoff或者geton
	day=datetime.strptime(date,'%Y-%m-%d').day
	state=state.lower()
	table='lake_'+state+'_'+str(day)
	data=requestDB('select * from '+table)
	target=getCoordPerHour(data)

	return json.dumps(target)




# 基本统计数据，第一个服务
@app.route('/line_pie',methods=['GET'])
def line_pie():
	args=request.args
	day=args.get('day')
	dic={"Monday":3,"Tuesday":4,"Wednesday":5,"Thursday":6,"Friday":7,"Saturday":1,"Sunday":2}
	day=dic.get(day)
	lake_getoff=requestDB('select * from lake_getoff_'+str(day))
	lake_geton=requestDB('select * from lake_geton_'+str(day))
	lake_getoff=total_getoff_geton(lake_getoff)
	lake_geton=total_getoff_geton(lake_geton)
	# print(lake_getoff)
	# print(lake_geton)
	getoff_dic={}
	for i in range(len(lake_getoff)):
		getoff_dic[i]=lake_getoff[i]
	geton_dic={}
	for j in range(len(lake_geton)):
		geton_dic[j]=lake_geton[j]
	target={}
	target['getoff']=[getoff_dic]
	target['geton']=[geton_dic]
	return json.dumps(target)

# 基本统计数据第二个服务
@app.route('/line_pie_2',methods=['GET'])
def line_pie_2():
	args=request.args
	value=args.get('value')
	dic={'Getoff':['lake_getoff_1','lake_getoff_2','lake_getoff_3','lake_getoff_4','lake_getoff_5','lake_getoff_6','lake_getoff_7']
		 ,'Geton':['lake_geton_1','lake_geton_2','lake_geton_3','lake_geton_4','lake_geton_5','lake_geton_6','lake_geton_7']
	    }
	total_days=dic.get(value)
	line2=[]
	for i in range(0,24):
		line2.append(0)
	pie2=[]
	for item in total_days:
		data=requestDB('select * from '+item)
		list_data=total_getoff_geton(data)
		pie2.append(sum(list_data))
		for i in range(len(list_data)):
			line2[i]+=list_data[i]
	target={}
	line2_dic={}
	pie2_dic={}
	for i in range(len(line2)):
		line2_dic[i]=line2[i]
	for j in range(len(pie2)):
		pie2_dic[j]=pie2[j]
	target['line2']=[line2_dic]
	target['pie2']=[pie2_dic]
	# print(json.dumps(target))
	return json.dumps(target)


app.run(port=7999,debug=True)

# [[(lati,longi,speed_time),(),(),()],
#  [           ],
#  [           ]
#  ...
#  [           ]
# ]
# dic={0:[{'lati':lati,'longi':longi,'speed_time':speed_time},{...}],
#      1:[{...},...,                                          {...}],
	
#     }