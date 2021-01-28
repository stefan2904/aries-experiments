# Stefan's Aries Experiments 


* https://github.com/hyperledger/aries-framework-go


## Init Demos

* Install docker, docker-compose, etc.
* Gen some crypto material: `bash generate_test_keys.sh`



## Demo 1:

* Simple agent connection, using Peer DID, *no sidetree or ledger*
    - Establishes DIDExchange connection and issues a credential to Agent 2
* some containers via `docker-compose.yml`:
    - `openapi.university-agent.demo`: Uni Agent API Interface on http://localhost:8089/openapi
    - `agent.university-agent.demo`: Uni Agent API on https://localhost:8082
        + `webhook.university-agent.demo`: Webhooks for Callbacks to Controller on https://localhost:8083
    - `agent.student-agent.demo`: Student Agent API on https://localhost:8092
        + `webhook.student-agent.demo`: Webhooks for Callbacks to Controller on https://localhost:8093
* some configuration in `demo1/.env`


```bash
cd demo1

docker-compose -f docker-compose.yml up --force-recreate -d

python3 demoA.py
```



