# Backend for KLiK app
This project is created to experiment with an AWS serverless backend.  

The python functions in this repository contain the code for the AWS Lambda functions which are used as the backend for the KLiK application.
At the moment there are 3 web frontends and 1 JavaFX frontend that use this backend:
- Flutter frontend
  - code: https://github.com/edwinbulter/klik_flutter
  - web-app: https://main.dv7o5mle7kpe3.amplifyapp.com/
- React frontend
  - code: https://github.com/edwinbulter/klik_react
  - web-app: https://main.d3sz66opung9mh.amplifyapp.com/ 
- Angular frontend
  - code: https://github.com/edwinbulter/klik_angular
  - web-app: https://main.d10dznen6oo1he.amplifyapp.com/
- JavaFX frontend
  - code: https://github.com/edwinbulter/klik_javafx
  - The JavaFX frontend can't use the authentication dialogs of Amplify and therefore implements its own dialogs for login, account creation and password reset.

## AWS Components:
![AWS Components](images/aws-components.png)

## Sequence Diagram:
![Sequence Diagram](images/sequence-diagram.png)
