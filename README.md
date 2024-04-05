<h1>Indexer Blockchain Project</h1>
<h3> Current working progress is in Steps directory</h3>
<h4> Key files: Extract.pynb, Translate.pynb, load_to_block_table.pynb, load_to_transaction_header_pynb</h4>
<h4> WIP: Transaction Detail Insert statements are in the process of being revised due to recent updates in Schema Design. Latest version can be found in steps < load_to_msg_tables < load_transaction_detail_msg_claim_delegate_rewards.ipynb </h4>
<h4>List of transaction types, and test block numbers for each transaction can be found in Transaction_Type_Test_Blocks.xlsx</h4>
<h4>File for ERD diagram can be found in Indexer_ERD_Diagram</h4>

<h2>Project Summary</h2>
<h4>To create a system that can extract JSON files, translate the encrypted transactions, and upload that information into a database that will act as a distributed ledger. 
</h4>
<h2>Steps for Project</h2>
<h3>1.Extract data</h3>
<h4>a. Pull data from API</h4>
<h4>b. Assign file names as {block#}.json and send to temp directory ("Blocks")
<h3>2.Translate Data</h3>
<h4>a. Isolate TXS data from the rest of the json file and assign it to variable "code"</h4>
<h4>b.Hash TXS data from json file using sha 256</h4>
<h4>c.Decrypt TXS data using Bay64 API </h4>
<h4>d. Move Decrypted data and hash to a new json file, named {block#}.json and send to new directory(Decrypted_files)</h4>
<h3>3.Build Schema</h3>
<h4>a.Create an ERD Diagram</h4>
<h4>b.Write a script that will generate every table need for database</h4>
<h3>4. Writing Loading Scripts</h3>
<h4>a. Loading script for Block Table</h4>
<h4>b. Loading script for Transaction header table</h4>
<h4>c. Individual loading script for every message type</h4>
<h2> How to use </h2>
<h4> Download zip file or use command prompt below</h4>
<h4> git clone https://github.com/Lexi79Ha/indexer_project.git</h4>
<h4> Go to Extract.py,input a test block number for claims delegations (can be found in transaction excel file), run script, json file will be sent to temp directory</h4>
<h4> Go to translate.py, input test block number,run script, hash will be generated and json file will be decoded, and the data will be sent to the decrypted file directory</h4>
<h4> Go to schema.py, run script, database will be generated</h4>
<h4> Go to load_to_block_table.py , input test block number, run script, data will be loaded to block table</h4>
<h4> Go to load_to_transaction_header.py, input test block number, run script, data will be loaded to transaction header table</h4>
<h4> Go to load_msg directory, find load_to_msg_claims_delegations, input block number, run script, data will be loaded to transaction_detail_msg_claims_delegations_table</h4>
<h3>Transaction Types</h3>
<img src="img/transactions.png" alt="alt text" />
<h3>Message Types</h3>
<img src="img/msg.png" alt="alt text" />
<h2>Schema</h2>
<img src="img/erd.png" alt="alt text" />
<h3>Total Tables: 23 </h3>
<h3>Table Types</h3>
<h4>1.Block Table</h4>
<h5>Consists of every transaction loaded into the system.</h5>
<h4>2.Transaction Header Table </h3>
<h5>The header table will contain overview information for each transaction.</h5>
<h4>3.Transaction Detail Tables</h4>
<h5>Each transaction detail table will contain one message type and provide more in-depth data about what occurred in its related messages.</h5>
<h2>Resources and External Tools links</h2>
<p>a.	https://fio.bloks.io/</p>
<p> b. https://github.com/White-Whale-Defi-Platform/migaloo-chain.git</p>
<p>c.https://dbdiagram.io/</p>
<p>d. https://inbloc.org/migaloo/transactions</p>
<h2>Author</h2>
<h4> Alexis Harris</h4>
<h4> lmh.mo.6@gmail.com</h4>
