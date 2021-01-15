import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# https://github.com/hyperledger/aries-framework-go/blob/main/docs/rest/openapi_demo.md#steps-for-didexchange


def step(s, agentId=1):
	print()
	if agentId == 1:
		print('\033[91m\033[1m### {} \033[0m'.format(s))
	else:
		print('\033[95m\033[1m### {} \033[0m'.format(s))
	print()


AGENT1 = 'https://localhost:8082' # university
AGENT2 = 'https://localhost:8092' # student


step("Agent 1: Test connections", 1)

r = requests.get(AGENT1 + '/connections', verify=False)
if r.status_code == 200:
	print('connection to agent 1 works!')

r = requests.get(AGENT2 + '/connections', verify=False)
if r.status_code == 200:
	print('connection to agent 2 works!')


step("Agent 1: Create invite", 1)

invite = requests.post(AGENT1 + '/connections/create-invitation', verify=False).json()
print(invite)
invite = invite['invitation']
inviteIDagent1 = invite['@id']


#input('Press any key to continue ...')
step("Agent 2: receive invite", 2)

connection = requests.post(AGENT2 + '/connections/receive-invitation', json=invite, verify=False).json()
print(connection)
connectionIDagent2 = connection['connection_id']
print(connectionIDagent2)


#input('Press any key to continue ...')
#step("Agent 1: List connections")

#details = requests.get(AGENT1 + '/connections', verify=False)
#print('connections agent 1: ' + details.text)

#details = requests.get(AGENT2 + '/connections', verify=False)
#print('connections agent 2: ' + details.text)


step("Agent 2: List connections", 2)

details = requests.get(AGENT2 + '/connections/' + connectionIDagent2, verify=False)
print('details last invite agent 2: ' + details.text)


step("Agent 2: Accept invite", 2)

details = requests.post(AGENT2 + '/connections/' + connectionIDagent2 + '/accept-invitation', verify=False)
print('details accept invite at agent 2: ' + details.text)


step("Agent 2: List accepted connection", 2)

details = requests.get(AGENT2 + '/connections/' + connectionIDagent2, verify=False)
print('connection agent 2: ' + str(details.json()['result']))


step("Agent 1: List own invite again", 1)

connections = requests.get(AGENT1 + '/connections', verify=False).json()
for connection in connections['results']:
	if connection['InvitationID'] == inviteIDagent1:
		print('connection agent 1: ' + str(connection))
		connectionIDagent1 = connection['ConnectionID']



step("Get connection states")

details = requests.get(AGENT1 + '/connections/' + connectionIDagent1, verify=False)
print('connection agent 1: state = ' + str(details.json()['result']['State']))

details = requests.get(AGENT2 + '/connections/' + connectionIDagent2, verify=False)
print('connection agent 2: state = ' + str(details.json()['result']['State']))


#input('Press any key to continue ...')


step("Agent 1: Accept request", 1)

details = requests.post(AGENT1 + '/connections/' + connectionIDagent1 + '/accept-request', verify=False)
print('details accept invite at agent 1: ' + details.text)



step("Get connection states again")

details = requests.get(AGENT1 + '/connections/' + connectionIDagent1, verify=False)
print('connection agent 1: state = ' + str(details.json()['result']['State']))

details = requests.get(AGENT2 + '/connections/' + connectionIDagent2, verify=False)
print('connection agent 2: state = ' + str(details.json()['result']['State']))



# step("Agent 1: send some message to Agent 2")

# msg = 'hallo student, agent zwei!'
# r = requests.post(AGENT1 + '/connections/' + connectionIDagent1 + '/send-message', json={'content': msg}, verify=False)
# print(r.text)



# TODO: issue credential ?



step("Some more experiments", 1)

r = requests.get(AGENT1 + '/issuecredential/actions', verify=False)
print('issuecredential actions: {}'.format(r.text))

r = requests.get(AGENT1 + '/mediator/connections', verify=False)
print('mediator connections: {}'.format(r.text))

r = requests.get(AGENT1 + '/message/services', verify=False)
print('message services: {}'.format(r.text))

r = requests.get(AGENT1 + '/outofband/actions', verify=False)
print('outofband actions: {}'.format(r.text))

r = requests.get(AGENT1 + '/presentproof/actions', verify=False)
print('presentproofs: {}'.format(r.text))

r = requests.get(AGENT1 + '/vdr/did/records', verify=False)
print('dids: {}'.format(r.text))

r = requests.get(AGENT1 + '/verifiable/credentials', verify=False)
print('credentials: {}'.format(r.text))

r = requests.get(AGENT1 + '/verifiable/presentations', verify=False)
print('presentations: {}'.format(r.text))

