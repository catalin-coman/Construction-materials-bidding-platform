# Construction-materials-bidding-platform

This project is a bidding platform for construction materials.
Initialy we will start with concrete.

The project contains the folowing apps:
  
  1 Accounts app:
      - takes care of account-related functionalities
      - contains a model which stores User related data
      - has a my account page where clients can see their orders
      - login/logout/register functionality
      - i userd a CustomUserModel for the registration of users so we can add more fields to the model later
      - when a client registers into the platform he must chose whether he is a buyer or a seller. A buyer can post orders on the platform and a seller can bid on those requests
  
  2 Concrete app:
      - takes care of the concrete page
      - contains a model which stores the types of concrete
      - it shows information about different types of concrete and concrete pouring
      
  3 Orders app:
      - takes care of the orders/bids
      - contains a model which stores the orders
      - a buyer type user can post an order and a seller type user can bid on the orders he wants
