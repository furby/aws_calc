import json

print("Prices of AWS")


with open('snippet.json') as data:
  sampleDict = json.load(data)

#search through nested json for instancetype and return if instance type is present
def search_aws (instance):
	for m in range(len(sampleDict)):
		if instance in sampleDict[m]['product']['attributes']:
			return sampleDict[m]['product']['attributes']['instanceType']
		else:
			print("Keyvalue not present")


aws_instance = input("The type of instance. e.g. m3.large: ")
# vmtype = 't2.xlarge'

#print the instance type for a check.
print("Instance Type:")
print(search_aws("instanceType"))

# print(sampleDict[m]['product']['attributes']['instanceType'])

#for the instnace type return the  0 product - terms - OnDemand - PriceperUnit

