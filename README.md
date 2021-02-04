# Stefan's Aries Experiments 


* https://github.com/hyperledger/aries-framework-go


## Init Demos

* Install docker, docker-compose, etc.
* Gen some crypto material: `bash generate_test_keys.sh`



## Demo 1

* Simple agent connection, using Peer DID, *no sidetree or ledger*
    - Establishes DIDExchange connection and issues a credential to Agent 2
* some containers via `docker-compose.yml`:
    - `openapi.university-agent.demo`: Uni Agent API Interface on http://localhost:8089/openapi
    - `agent.university-agent.demo`: Uni Agent API on https://localhost:8082
        + `webhook.university-agent.demo`: Webhooks for Callbacks to Controller on https://localhost:8083
    - `agent.student-agent.demo`: Student Agent API on https://localhost:8092
        + `webhook.student-agent.demo`: Webhooks for Callbacks to Controller on https://localhost:8093
* some configuration in `demo1/.env`


### Run it

```bash
cd demo1
docker-compose -f docker-compose.yml up --force-recreate -d
python3 demoA.py
```


## Demo 2

* similar as demo 1, but with sidetree
* → *currently not working*




## Update Agent API specs

* clone/pull https://github.com/hyperledger/aries-framework-go
* run `make generate-openapi-demo-specs`
* copy into demo1: `cp ../aries-framework-go/test/bdd/fixtures/demo/openapi/specs/openapi-localhost:8082.yml demo1/specs/openapi-university.yml`
* copy into demo2: `cp ../aries-framework-go/test/bdd/fixtures/demo/openapi/specs/openapi-localhost:8082.yml demo2/specs/openapi-university.yml`
* etc.
