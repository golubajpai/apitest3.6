import json,time,os,hashlib,hmac,requests,logging,re,pandas
from zlib import compress
from  unittest import TestCase


class ExceptionHandeling:
	def exception(self):
			
			try:
				os.stat("config.json").st_size > 0
			except:
				raise OSError('file does not exist')
			try:
				
				with open('config.json') as json_file:
					data = json.load(json_file)
			except: 
					raise OSError('file is empty')
						
			try:
				owner=data['owner']
			except:
				raise ValueError('owner does not exist')
			try:
				apikey=data['api_key']
				return data
			except:
				raise ValueError('apikey does not exist')

			
		
		


class ApiTest:

	def __init__(self,apiservice,success_status_code,Request_Type,params=None):
		a=ExceptionHandeling()
		data=a.exception()
		#import pdb;pdb.set_trace()
		self.data=data
		self.url=str(data['url'])+apiservice
		self.Request_Type=Request_Type
		self.owner=data['owner']
		print(self.owner)
		self.apikey=data['api_key']
		self.params=params
		self.success_status_code=success_status_code
		


	def createmessage(self):
		msg={}
		link=self.url.strip('.')[-2]
		if link=='downlink':
			msg['username']=self.data['username']
		msg['_ownew']=self.owner
		msg['_timestamp']=int(time.time())

		data=json.dumps(msg)
		_msg=compress(data,9).encode('base64').strip()
		sig=hmac.new(str(self.apikey),_msg,hashlib.sha256).hexdigest()
		parmas={'msg':_msg,'sig':sig}
		return parmas
	def api(self):
		response=requests.request(self.Request_Type,self.url,data=self.params)
		return response
	
	def callapi(self):
		response=requests.request(self.Request_Type,self.url,params=self.createmessage() ,data=self.params)
		a=(response.elapsed.total_seconds())
		logging.info(a)
		return response






		


