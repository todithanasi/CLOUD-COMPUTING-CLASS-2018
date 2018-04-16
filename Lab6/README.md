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
![barChart](screenshots/Task6.1.PNG)


#### Task 6.2
![map](screenshots/Task6.2.a.PNG)

Q62a: Now we are showing all the collected tweets on the map. Can you think of a way of restricting the tweets plotted using some constraints? For instance, the user could invoke http://127.0.0.1:8000/map?from=2018-02-01-05-20&to=2018-02-03-00-00. Implement that functionality or any other functionality that you think it could be interesting for the users.
To restrict the tweets on map on a date range , we saved the date as timestamp strings as there is no concept of date range comparison in Dyanamo DB. we took the parameter values of to_date and from_date from url, converted them to timestamp as well and compared them to filter the required date range tweets.

![](screenshots/TaskTask6.2.b.PNG)
Q62b: Make the necessary changes to have geo_data.json distributed using S3, or the method you used for the above section. Publish your changes to EB and explain what changes have you made to have this new function working.
To distribute the geo_data.json, we saved it to s3 bucket and accessed it from s3 bucket. We also implemented caching by saving a file like '2018-04-14-10-30-2018-04-14-11-39.json' using query string in url and every time check if this file exist already, if yes just use that file otherwise fetch the data from database and create this file and then load data.
This reduces the query load to database. 
![](screenshots/TaskTask6.2.c.PNG)

To allow application to access s3 bucket, we edited IAM role to add permissions to read and write in the s3 bucket. 
We also changed CORS configuration of the bucket to allow cross origin requests.

```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>http://*</AllowedOrigin>
    <AllowedOrigin>https://*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

Q62c: How would you run TwitterListener.py in the cloud instead of locally? Try to implement your solution and explain what problems have you found and what solutions have you implemented.

To deploy TwitterListener.py on cloud we needed to create a strategy to start and stop it somehow without closing the instance. We created a web page in the application twitter.py with a button to start and stop the TwitterListener to gather tweets.
