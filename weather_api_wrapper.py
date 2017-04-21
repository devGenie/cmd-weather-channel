from urllib import request
import json
class weatherDistro(object):
	def __init__(self,api_token):
		self.api_token=api_token

	def show_current(self,area):
		response=request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+area+"&appid="+self.api_token)
		return json.load(response)

	def weekly_forecast(self,area):
		response=request.urlopen("http://api.openweathermap.org/data/2.5/forecast?q="+area+"&appid="+self.api_token)
		return json.load(response)
