Terminology Rules

1. Proper Nouns:
   - Must always be capitalized exactly as specified in the glossary.
   - Example: "Cobo Portal", "MPC Wallets" (not "MPC wallets").
2. Common Terms:
   - Only capitalize the first word when appearing at the beginning of a sentence.
3. Acronyms:
   - Should always be fully capitalized (e.g., "RESTful API", "TSS").

---

Terms in the glossary fall into two categories:
1. Proper nouns: Must be capitalized in all contexts (e.g., "Cobo Portal", "Safe{Wallet}")
2. Common terms: Only capitalize the first word when appearing at the beginning of a sentence (e.g., "user roles and permissions")

|Terms | Definition | Notes|
|--- | --- | ---|
|User roles and permissions | A set of rules defining what actions a user can perform within a system. | If space is a limitation, can use "Roles and permissions", but not only "roles". Do not use "roles" alone.|
|<ul><li>Custodial Wallets<ul><li>Asset Wallets</li><li>Web3 Wallets</li></ul></li><li>MPC Wallets<ul><li>Organization-Controlled Wallets</li><li>User-Controlled Wallets</li></ul></li><li>Smart Contract Wallets<ul><li>Safe{Wallet}</li></ul></li><li>Exchange Wallets<ul><li>Main Account</li><li>Sub Account</li></ul></li></ul> | Wallet type and wallet subtype. | For UI text. Do not use lowercase "wallets".  |
| Custodial Wallets (Asset)<br />Custodial Wallets (Web3)<br />MPC Wallets (Organization-Controlled)<br />MPC Wallets (User-Controlled)<br />Smart Contract Wallets (Safe{Wallet})<br />Exchange Wallets (Main)<br />Exchange Wallets (Sub) | Wallet type and wallet subtype. | For UI text, Product Manuals and Developer Hub. Do not use lowercase "wallets". |
| custodial_asset_wallets /CUSTODIAL_ASSET_WALLETS<br />custodial_web3_wallets / CUSTODIAL_WEB3_WALLETS<br />mpc_organization_controlled_wallets / MPC_ORGANIZATION_CONTROLLED_WALLETS<br />mpc_user_controlled_wallets / MPC_USER_CONTROLLED_WALLETS<br />smart_contract_safe_wallets / SMART_CONTRACT_SAFE_WALLETS<br />exchange_wallets / EXCHANGE_WALLETS | Wallet type and wallet subtype. | For use in code such as webhook/callback.|
| Holder groups | Groups responsible for holding a key share within an MPC system. | Used in Product Manuals and UI text. |
| Key share holder groups |Groups responsible for holding a key share within an MPC system. | Used in Developer Hub. |
| Key share holder| User who holds a key share within an MPC system. | |
| Signing Group<br />Recovery Group<br />Main Group | Groups responsible for different functions within MPC Wallets: signing transactions, recovering keys, and creating other groups. | Used in MPC Wallets. |
| Approval Quorum | The minimum number of approvals required to authorize a transaction. | In the context of Risk Controls such as Governance Policies. |
| Threshold | The minimum number of approvals required to authorize a transaction. | In other contexts such as Signing Key Group |
| Threshold signature scheme (TSS) | A cryptographic method requiring a subset of key shares to sign a transaction. |  |
| RESTful API | An architectural style for designing networked applications. | Do not use "REST API". |
| Service agreement | A formal agreement defining the service terms between a provider and a client. | Do not use "Contract". |
| dApp | A decentralized application running on a blockchain network. | Do not use "DApp". |
| Cobo Portal Apps | Applications available within the Cobo Portal ecosystem. | Do not use "Marketplace". |
| Viewer<br />Spender<br />Approver<br />Staker<br />Operator<br />Admin<br />Owner | The preset user roles in Cobo Portal. | |
| Risk Controls | Measures implemented to manage and mitigate risks. | Risk Controls include transaction policies, governance policies, and user roles and permissions, 
| <ul><li>Transaction policies<ul><li>On-Chain transaction policies</li><li>Off-Chain transaction policies</li></ul> | Policies designed to regulate and control transaction processes within the system, ensuring compliance and security. | |
| Governance policies | Policies that guide the decision-making processes and management of an organization. | |
| A wallet created on Cobo Portal | A digital wallet established through the Cobo Portal platform. | Do not use "Cobo wallet" or "Cobo wallets". |
| Wallet-as-a-Service (WaaS) | A service model providing wallet functionalities as a service. |  |
| Outgoing transfer volume | The total volume of outgoing transfers. | Do not use "outgoing transaction volume". For use in the context of billing and payments. |
