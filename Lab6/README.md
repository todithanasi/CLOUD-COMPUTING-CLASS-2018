# Lab6 - ReadMe

#### GroupId
1102

#### Members & email
- Syeda Noor Zehra Naqvi         <syeda.noor.zehra.naqvi@est.fib.upc.edu>
- Todi Thanasi                   <todi.thanasi@gmail.com>
                         
#### Github url
https://github.com/todithanasi/CLOUD-COMPUTING-CLASS-2018/tree/master/Lab6

#### Task 6.1
Q61a: Having domain_freq.json written as static content is not the best way to distribute it because different clients can invoke different parameters simultaneously? Can you use S3 to solve the problem? Write the changes in the code and explain your solution?
Answer: We did not save the data into a JSON file because the content is dynamic and is changing on every call. We implemented the solution differently, instead of saving the file we are sending to the chat.html page a JSON object and parsing it there.
Q61b: Once you have your solution implemented publish the changes to EB and try the new functionality in the cloud. Did you need to change anything, apart from the code, to make the web app work?
Answer: No. Nothing was needed to be changed in order to make the application work in EBS beside re-deploying after running the freeze command to update the requirements.txt file. 
#### Task 6.2

Q62a: Now we are showing all the collected tweets on the map. Can you think of a way of restricting the tweets plotted using some constraints? For instance, the user could invoke http://127.0.0.1:8000/map?from=2018-02-01-05-20&to=2018-02-03-00-00. Implement that functionality or any other functionality that you think it could be interesting for the users.

Q62b: Make the necessary changes to have geo_data.json distributed using S3, or the method you used for the above section. Publish your changes to EB and explain what changes have you made to have this new function working.

Q62c: How would you run TwitterListener.py in the cloud instead of locally? Try to implement your solution and explain what problems have you found and what solutions have you implemented.
