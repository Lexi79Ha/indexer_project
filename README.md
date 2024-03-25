<h1>Indexer Blockchain Project</h1>
<h3> Current working progress is in steps directory</h3>
<h4>List of transaction types, and test block numbers for each transaction can be found in Transaction_Type_Test_Blocks.xlsx</h4>
<h4>Link to working progress ERD diagram</h4>
<h5>https://lucid.app/lucidchart/e8bc1a58-1e72-4db6-b1df-f35f6bdbc233/edit?viewport_loc=-1892%2C-1095%2C5712%2C2532%2C0_0&invitationId=inv_55835d51-10c4-4f24-81b9-1b498f9b88b5</h5>
<h2>Project Summary</h2>
<h4>To create a system that can extract JSON files, translate the encrypted transactions, and upload that information into a database that will act as a distributed ledger. 
</h4>
<h3>A.	What Is a Blockchain?</h3>
<p>•	 A blockchain is a distributed database or ledger shared among a network of computers (nodes).</p>
<p>•	While it’s most famous for its role in cryptocurrency systems, it’s not limited to just that.</p>
<p>•	Blockchains can be used to make data in any industry immutable, meaning it cannot be altered.</p>
<p>•	Unlike traditional databases, where trust often relies on third parties, blockchains operate without a central authority.</p>
<p>•	Decentralized blockchains are particularly interesting because no single person or group controls them—instead, all users collectively retain control.</p>
<h3>B.	How Does a Blockchain Work?</h3>
<p>•	Imagine a spreadsheet or database where information is entered and stored.</p>
<p>•	In a blockchain, data is structured differently and accessed via a series of blocks linked together using cryptography.</p>
<p>•	Here’s how it works:</p>
<p>•	Transaction Information: The blockchain collects transaction data and enters it into a block.</p>
<p>•	Creation: A block is created after a predetermined amount of time.</p>         
<p>•	Chained Blocks: This hash becomes part of the next block, creating a chain of blocks.</p>
<p>•	Immutable: Once data is recorded, it’s irreversible. For example, in Bitcoin, transactions are permanently viewable by anyone.</p>
<h3>Schema</h3>
![Screenshot 2024-03-25 113301](https://github.com/Lexi79Ha/indexer_project/assets/139013867/1cd81362-464e-483c-a126-a06db760290b)
<h3>Total Tables: 41</h3>
<h3>Table Types</h3>
<h4>1.Block Table</h4>
<h5>a.Consists of every transaction loaded into the system.</h5>
<h4>2.Transaction Header Tables </h3>
<h5>a.Each header table will contain one transaction type and will show overview information for those transactions.</h5>
<h4>3.Transaction Detail Tables</h4>
<h5>a.Each transaction detail table will contain one message type and provide more in-depth data about what occurred in its related messages.</h5>
<h3>C.	Blockchain-related links</h3>
<p>a.	https://fio.bloks.io/</p>
<p> b. https://github.com/White-Whale-Defi-Platform/migaloo-chain.git</p>
