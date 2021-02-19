#Import JSON module
import json

#varibles
#frobnicate_controller_instance_type
fc='r5.2xlarge'
#frobnicate_multi_controller
fmc=2
#frobnicate_worker_count
fwc=5
#frobnicate_worker_instance_type
fw='m5.xlarge'
#smash_controller_instance_type
sc='m5.xlarge'
#smash_worker_count
swc=30
#smash_worker_instance_type
sworker='i3.2xlarge'

os = "Windows"
term = 'OnDemand'
region = "EU (London)"

instance = input("The type of instance. e.g. t2.xlarge: ")
keyvalue = 'instanceType'


print("Prices of AWS")

#open JSON file and assign variable
with open('snippet.json') as data:
  sampleDict = json.load(data)

for m in range(len(sampleDict)):
	if keyvalue in sampleDict[m]['product']['attributes']:
		if sampleDict[m]['product']['attributes']['operatingSystem'] == os:
			if sampleDict[m]['product']['attributes']['location'] == region:
				if term in sampleDict[m]['terms']:
					ext = (sampleDict[m]['terms']['OnDemand']['22VPGB87R2NZ8A4A.JRTCKXETXF']['priceDimensions']['22VPGB87R2NZ8A4A.JRTCKXETXF.6YS6EN2CT7']['pricePerUnit']['USD'])
				else:
					print("not found")


#maths - hours x days
sums = round((float(ext)) * 24 * 28 * fmc, 2)


print("Cost per month for", "frobnicate_controller_instance_type:", sampleDict[m]['product']['attributes']['instanceType'], '$',sums)
# print(sampleDict[m]['product']['attributes']['instanceType'])
# print(sums)