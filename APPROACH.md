## Approach

I used Python for programming. Flask is used as a framework to help create the webpages on the front end. MongoDB Community Server is used as a database to store visitor entries.

After reaching the Check In page, the visitor has to enter their name, email, phone number, and the host's name, email, phone number and address.

The data entered in the forms is passed through appropriate validation and after appending the check in time to the data, it is inserted into the database at the back end. A `Visitor` object is being created on the way which stores all the information of the visitor. The visitor is given the unique timestamp as a visitor ID, which is also the index of the visitor in the database. A list of currently visiting visitors is modified which keeps track of visitors who haven't checked out yet.

An email is sent to the host as soon as their visitor checks in, containing the details of the visitor.

When the visitor tries to check out, they've to provide a visitor ID that was given to them while checking in. The visitor ID is then tallied with the visitors in the currently visiting list. If the ID is present, the visitor is shown a success screen saying they checked out. Else, they're requested to try again. The check out time is updated in the database by the help of the `Visitor` object that was created when checking in, and the timestamp (visitor ID) used to recognize the visitor.

Once, he checks out, the visitor gets an email summarizing his visit, which contains the check in and check out time too.

The Admin Panel lets the Admin enter his AdminID (AID) to view the full list of recent visitors in chronological order.
