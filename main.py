import nationstates
import time

api = nationstates.Nationstates(input("Main nation?"))  #User agent as per NS API rules please#

rinput = input("Region to be sampled? ")
region = api.region(rinput)
try:
    nations = region.numnations
except:
    print("Region does not exist: Quitting")
    time.sleep(5)
    quit()

print(rinput + " " + "Residency" + " " +nations)
count = int(nations) - 40

residencyinput = input("how many days since last welcome post?")

dispatch_nation_list = []
telegram_nation_list = []
while count < int(nations):
    censusranks_shard = nationstates.Shard("censusranks", scale=80, start=count)
    data = region.get_shards(censusranks_shard)
    nationlist = data["censusranks"]
    nationlist = nationlist["nations"]
    nationlist = nationlist["nation"]
    for i in nationlist:
        if float(i["score"]) < float(residencyinput):
            dispatch_formatted = "[nation]"+i["name"]+"[/nation]"
            dispatch_nation_list += [dispatch_formatted]
            telegram_formatted = i["name"]
            telegram_nation_list += [telegram_formatted]
    count = count + 20


print("Do you want to generate a list for dispatch or telegram?")
response = None
while response not in {"dispatch", "telegram"}:
  response = input("Please enter dispatch or telegram: ")

if response in {"dispatch"}:
  print(', '.join(dispatch_nation_list))
if response in {"telegram"}:
  print(', '.join(telegram_nation_list))
