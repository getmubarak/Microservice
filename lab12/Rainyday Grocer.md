Rainyday Grocer is a cloud-based online grocer that provides customized delivery of groceries. Their business model is 
targeted towards those “rainy day” moments where a person needs groceries but is unable to go the bricks-and-mortar grocery 
store to shop.

Business Scenario
Rainyday Grocer (RG) supports three different ordering options. A customer can:
* Place an order with one of the approved grocery stores, send the item list, and order confirmation to RG via a web interface 
or a mobile application.
* Send a grocery list to RG via a web interface or a mobile application.
* Select from RG grocery items list and place an order.

There are two delivery options:
* Doorstep delivery with text message confirming delivery.
* Collect groceries order from one of the RG collection points.

RG does not own any inventory, supply channels, distribution channels, or data centers. They leverage other service providers 
for all services, and manage quality through a careful selection process and SLAs. They maintain a lean team of 50 people, 
only 5 of whom are IT-focused, to manage their operations across five states in the Eastern US.

The customer has to accept a set of constraints to place a successful order:
* The customer must have an active account in good standing 
* The customer must have a valid payment method registered.
* An order is limited to 10 or less items with a cumulative weight not more than 25lb.
* RG does not guarantee any specific brands.
* There is a four-hour window from order confirmation to requested delivery.
* An order cannot include medicines or hazardous materials.
* The delivery address must be within 50 miles of a city center.

![alt text](https://raw.githubusercontent.com/getmubarak/Microservice/master/lab12/RainyDay.png "Process Diagram")

The ones circled in red represent Atomic Business Activities 
