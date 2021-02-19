import json

print("Prices of AWS")

os = 'SUSE'
os2 = 'RHEL'

with open('eu-west-2.json') as data:
  sampleDict = json.load(data)

#search through nested json for instancetype and return if instance type is present
def search_aws (instance):
	for m in range(len(sampleDict)):
		if instance in sampleDict[m]['product']['attributes']:
			if sampleDict[m]['product']['attributes']['operatingSystem'] == os:
				return sampleDict[m]['product']['attributes']['operatingSystem']
			else:
				print("The OS is", sampleDict[m]['product']['attributes']['operatingSystem'])


#print the instance type for a check.
print("Instance Type:")
print(search_aws("instanceType"))

