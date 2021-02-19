import json

#frobnicate_controller_instance_type
fctrl='r5.2xlarge'
#frobnicate_multi_controller (true = 2)
fmctrl=2
#frobnicate_worker_count
fworkerct=5
#frobnicate_worker_instance_type
fworker='m5.xlarge'
#smash_controller_instance_type
sctrl='m5.xlarge'
#smash_worker_count
sworkerct=30
#smash_worker_instance_type
sworker='i3.2xlarge'

os = "Windows"
term = 'OnDemand'
region = "EU (London)"

#possible input
instance = input("The type of instance. e.g. t2.xlarge: ")
keyvalue = 'instanceType'


print("AWS Price calculator\n")


with open('snippet.json') as data:
  sampleDict = json.load(data)

# check if keyvalue exists and mathces what you are looking for
for m in range(len(sampleDict)):
	if keyvalue in sampleDict[m]['product']['attributes']:
		if sampleDict[m]['product']['attributes']['operatingSystem'] == os:
			if sampleDict[m]['product']['attributes']['location'] == region:
				if term in sampleDict[m]['terms']:
					unitprice = (sampleDict[m]['terms']['OnDemand']['22VPGB87R2NZ8A4A.JRTCKXETXF']['priceDimensions']['22VPGB87R2NZ8A4A.JRTCKXETXF.6YS6EN2CT7']['pricePerUnit']['USD'])
				else:
					print("keyvalue not found or does not meet requirements")


#Calculation - hours x days x count)
calc = round((float(unitprice)) * 24 * 28 * fmctrl, 2)


print("Cost per month for", "frobnicate_controller_instance_type:", sampleDict[m]['product']['attributes']['instanceType'], '$',calc)
