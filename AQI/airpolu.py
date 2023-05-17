from tkinter import *
import requests
from bs4 import BeautifulSoup


# link for extract html data

def getdata(url):
	r = requests.get(url)
	return r.text


def airinfo():
	htmldata = getdata("https://weather.com/zh-TW/forecast/air-quality/l/6b221b26e046a442e03dc46fbe91d5874c6461afde61187dd4126bddeea1e2aa")
	soup = BeautifulSoup(htmldata, 'html.parser')
	res_data = soup.find(class_="DonutChart--innerValue--3_iFF AirQuality--extendedDialText--1kqIb").text
	air_data = soup.find_all(class_="DonutChart--innerValue--3_iFF AirQuality--pollutantDialText--2Q5Oh")
	air_data=[data.text for data in air_data]
	

	ar.set(res_data)
	pm.set(air_data[0]) 
	co.set(air_data[1])
	no2.set(air_data[2])
	o3.set(air_data[3])
	pml.set(air_data[4])
	so2.set(air_data[5])

	res = int(res_data)
	if res <= 50:
		remark = "良好" #Good
		impact = "空氣品質為良好，污染程度低或無污染。"#Minimal impact
	elif res <= 100 and res > 51:
		remark = "普通"#Satisfactory
		impact = "空氣品質普通；但對非常少數之極敏感族群產生輕微影響。"#Minor breathing discomfort to sensitive people
	elif res <= 150 and res > 101:
		remark = "對敏感族群不健康"#Unhealthy for Sensitive Groups
		impact = "空氣污染物可能會對敏感族群的健康造成影響，但是對一般大眾的影響不明顯。"
	elif res <= 200 and res >= 151:
		remark = "對所有族群不健康"#Unhealthy
		impact = "對所有人的健康開始產生影響，對於敏感族群可能產生較嚴重的健康影響"
	elif res <= 400 and res >= 201:
		remark = "非常不健康"#Very Poor
		impact = "健康警報：所有人都可能產生較嚴重的健康影響。"
	elif res <= 500 and res >= 401:
		remark = "危害"#Severe
		impact = "健康威脅達到緊急，所有人都可能受到影響。"
	res_remark.set(remark)
	res_imp.set(impact)


# object of tkinter
# and background set to grey
master = Tk()
master.configure(bg='light grey')

# Variable Classes in tkinter
air_data = StringVar()
ar = StringVar()
o3 = StringVar()
no2 = StringVar()
so2 = StringVar()
pm = StringVar()
pml = StringVar()
co = StringVar()
res_remark = StringVar()
res_imp = StringVar()


# Creating label for each information
# name using widget Label
Label(master, text="空氣品質：",#Air Quality
	bg="light grey").grid(row=0, sticky=W)
Label(master, text="O3 (μg/m3) 臭氧：",
	bg="light grey").grid(row=4, sticky=W)
Label(master, text="NO2 (μg/m3) 二氧化氮：",
	bg="light grey").grid(row=3, sticky=W)
Label(master, text="SO2 (μg/m3) 二氧化硫：",
	bg="light grey").grid(row=6, sticky=W)
Label(master, text="PM2.5 (μg/m3) 懸浮微粒<2.5微米：",
	bg="light grey").grid(row=1, sticky=W)
Label(master, text="PM10 (μg/m3) 懸浮微粒<10微米：",
	bg="light grey").grid(row=5, sticky=W)
Label(master, text="CO (μg/m3)一氧化碳：",
	bg="light grey").grid(row=2, sticky=W)

Label(master, text="對健康影響與活動建議：",#Remark
	bg="light grey").grid(row=7, sticky=W)
Label(master, text="人體健康影響：", #Possible Health Impacts 
	bg="light grey").grid(row=8, sticky=W)


# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=ar,
	bg="light grey").grid(
	row=0, column=1, sticky=W)
Label(master, text="", textvariable=pm,#o3
	bg="light grey").grid(
	row=1, column=1, sticky=W)
Label(master, text="", textvariable=co,#no2
	bg="light grey").grid(
	row=2, column=1, sticky=W)
Label(master, text="", textvariable=no2,#so2
	bg="light grey").grid(
	row=3, column=1, sticky=W)
Label(master, text="", textvariable=o3,#pm
	bg="light grey").grid(
	row=4, column=1, sticky=W)
Label(master, text="", textvariable=pml,#pml
	bg="light grey").grid(
	row=5, column=1, sticky=W)
Label(master, text="", textvariable=so2,
	bg="light grey").grid(
	row=6, column=1, sticky=W)
Label(master, text="", textvariable=res_remark,
	bg="light grey").grid(row=7, column=1, sticky=W)
Label(master, text="", textvariable=res_imp,
	bg="light grey").grid(row=8, column=1, sticky=W)


# creating a button using the widget
b = Button(master, text="檢測",#Check
		command=airinfo, bg="Yellow")
b.grid(row=0, column=2, columnspan=2,
	rowspan=2, padx=5, pady=5,)

mainloop()