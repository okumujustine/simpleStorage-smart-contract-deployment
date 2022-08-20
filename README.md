Deploys a smart contract that stores a list of people with their names and favorite number on the ethereum blockchain.

#### How to run it locally
##### 1. Prerquisites
- (Ganache installed)[https://trufflesuite.com/ganache/]

##### 2. Clone the project
`$ git clone git@github.com:okumujustine/simpleStorage-smart-contract-deployment.git`

##### 3. Navigate to the project directory
`$ cd simpleStorage-smart-contract-deployment`

##### 4. Create python virtual environment and activate it
`$ python3 venv env && source venv/bin/activate`

##### 5. Install requirements
`$ pip install requirements.txt`

##### 6. Set network/blockchain node configurations in the (config.py)
 - provider_url: is the blochain node provider url e.g http://127.0.0.1:7545 for ganache
 - chain_id: chain id of the provider
 - my_address: deployment account address
 - private_key: deployment account private key

##### 7. Execute deployment
 `$ python deploy.py`