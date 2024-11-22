### A company needs to architect a hybrid DNS solution. This solution will use an Amazon Route 53 private hosted zone for the domain cloud.example.com for the resources stored within VPCs. ✑ The company has the following DNS resolution requirements: On-premises systems should be able to resolve and connect to cloud.example.com. All VPCs should be able to resolve cloud.example.com. There is already an AWS Direct Connect connection between the on-premises corporate network and AWS Transit Gateway. Which architecture should the company use to meet these requirements with the HIGHEST performance?
- [x] Associate the private hosted zone to all the VPCs. Create a Route 53 inbound resolver in the shared services VPC. Attach all VPCs to the transit gateway and create forwarding rules in the on-premises DNS server for cloud.example.com that point to the inbound resolver. Most Voted
- [ ] Associate the private hosted zone to all the VPCs. Deploy an Amazon EC2 conditional forwarder in the shared services VPC. Attach all VPCs to the transit gateway and create forwarding rules in the on-premises DNS server for cloud.example.com that point to the conditional forwarder.
- [ ] Associate the private hosted zone to the shared services VPC. Create a Route 53 outbound resolver in the shared services VPC. Attach all VPCs to the transit gateway and create forwarding rules in the on-premises DNS server for cloud.example.com that point to the outbound resolver.
- [ ] Associate the private hosted zone to the shared services VPC. Create a Route 53 inbound resolver in the shared services VPC. Attach the shared services VPC to the transit gateway and create forwarding rules in the on-premises DNS server for cloud.example.com that point to the inbound resolver.
  
**[⬆ Back to Top](#table-of-contents)**


### Which of the following statements is NOT true about using Elastic IP Address (EIP) in EC2-Classic and EC2-VPC platforms?

- [x] In the EC2-VPC platform, the Elastic IP Address (EIP) does not remain associated with the instance when you stop it.
- [ ] In the EC2-Classic platform, stopping the instance disassociates the Elastic IP Address (EIP) from it.
- [ ] In the EC2-VPC platform, if you have attached a second network interface to an instance, when you disassociate the Elastic IP Address (EIP) from that instance, a new public IP address is not assigned to the instance automatically; you'll have to associate an EIP with it manually.
- [ ] In the EC2-Classic platform, if you disassociate an Elastic IP Address (EIP) from the instance, the instance is automatically assigned a new public IP address within a few minutes.

**[⬆ Back to Top](#table-of-contents)**

### A user has hosted an application on EC2 instances. The EC2 instances are configured with ELB and Auto Scaling. The application server session time out is 2 hours. The user wants to configure connection draining to ensure that all in-flight requests are supported by ELB even though the instance is being deregistered. What time out period should the user specify for connection draining?

- [x] 1 hour.
- [ ] 30 minutes.
- [ ] 5 minutes.
- [ ] 2 hours.

**[⬆ Back to Top](#table-of-contents)**

### What does the following command do with respect to the Amazon EC2 security groups? ec2-create-group CreateSecurityGroup

- [ ] Groups the user created security groups in to a new group for easy access.
- [x] Creates a new security group for use with your account.
- [ ] Creates a new group inside the security group.
- [ ] Creates a new rule inside the security group.

**[⬆ Back to Top](#table-of-contents)**

### You are in the process of moving your friend's WordPress site onto AWS to try and save him some money, and you have told him that he should probably also move his domain name. He asks why he can't leave his domain name where it is and just have his infrastructure on AWS. What would be an incorrect response to his question?

- [ ] Route 53 offers low query latency for your end users.
- [ ] Route 53 is designed to automatically answer queries from the optimal location depending on network conditions.
- [ ] The globally distributed nature of AWS's DNS servers helps ensure a consistent ability to route your end users to your application.
- [x] Route 53 supports Domain Name System Security Extensions (DNSSEC).

**[⬆ Back to Top](#table-of-contents)**

### Which of the following are characteristics of a reserved instance? (Choose 3 answers)

- [x] It can be migrated across Availability Zones.
- [ ] It is specific to an Amazon Machine Image (AMI).
- [ ] It can be applied to instances launched by Auto Scaling.
- [x] It is specific to an instance Type.
- [x] It can be used to lower Total Cost of Ownership (TCO) of a system.

**[⬆ Back to Top](#table-of-contents)**

### A user has defined an AutoScaling termination policy to first delete the instance with the nearest billing hour. AutoScaling has launched 3 instances in the US-East-1A region and 2 instances in the US-East-1B region. One of the instances in the US-East-1B region is running nearest to the billing hour. Which instance will AutoScaling terminate first while executing the termination action?

- [ ] Random Instance from US-East-1A.
- [ ] Instance with the nearest billing hour in US-East-1B.
- [x] Instance with the nearest billing hour in US-East-1A.
- [ ] Random instance from US-East-1B.

**[⬆ Back to Top](#table-of-contents)**

### You have an environment that consists of a public subnet using Amazon VPC and 3 instances that are running in this subnet. These three instances can successfully communicate with other hosts on the Internet. You launch a fourth instance in the same subnet, using the same AMI and security group configuration you used for the others, but find that this instance cannot be accessed from the internet. What should you do to enable Internet access?

- [ ] Deploy a NAT instance into the public subnet.
- [x] Assign an Elastic IP address to the fourth instance.
- [ ] Configure a publically routable IP Address in the host OS of the fourth instance.
- [ ] Modify the routing table for the public subnet.

**[⬆ Back to Top](#table-of-contents)**

### What does the 'Server Side Encryption' option on Amazon S3 provide?

- [x] It provides an encrypted virtual disk in the Cloud.
- [ ] It doesn't exist for Amazon S3, but only for Amazon EC2.
- [ ] It encrypts the files that you send to Amazon S3, on the server side.
- [ ] It allows to upload fi les using an SSL endpoint, for a secure transfer.

**[⬆ Back to Top](#table-of-contents)**

### What is a placement group?

- [ ] A collection of Auto Scaling groups in the same region.
- [x] A feature that enables EC2 instances to interact with each other via high bandwidth, low latency connections.
- [ ] A collection of authorized CloudFront edge locations for a distribution.
- [ ] A collection of Elastic Load Balancers in the same Region or Availability Zone.

**[⬆ Back to Top](#table-of-contents)**

### You are checking the workload on some of your General Purpose (SSD) and Provisioned IOPS (SSD) volumes and it seems that the I/O latency is higher than you require. You should probably check the [...] to make sure that your application is not trying to drive more IOPS than you have provisioned.

- [ ] amount of IOPS that are available.
- [ ] acknowledgement from the storage subsystem.
- [x] average queue length.
- [ ] time it takes for the I/O operation to complete.

**[⬆ Back to Top](#table-of-contents)**

### Within the IAM service a GROUP is regarded as a:

- [ ] A collection of AWS accounts.
- [ ] It's the group of EC2 machines that gain t he permissions specified in the GROUP.
- [ ] There's no GROUP in IAM, but only USERS and RESOURCES.
- [x] A collection of users.

**[⬆ Back to Top](#table-of-contents)**

### Doug has created a VPC with CIDR 10.201.0.0/16 in his AWS account. in this VPC he has created a public subnet with CIDR block 10.201.31.0/24. While launching a new EC2 from the console, he is not able to assign the private IP address 10.201.31.6 to this instance. Which is the most likely reason for this issue?

- [ ] Private IP address 10.201.31.6 is blocked via ACLs in Amazon infrastructure as a part of platform security.
- [x] Private address IP 10.201.31.6 is currently assigned to another interface.
- [ ] Private IP address 10.201.31.6 is not part of the associated subnet's IP address range.
- [ ] Private IP address 10.201.31.6 is reserved by Amazon for IP networking purposes.

**[⬆ Back to Top](#table-of-contents)**

### A user is planning to make a mobile game which can be played online or offline and will be hosted on EC2. The user wants to ensure that if someone breaks the highest score or they achieve some milestone they can inform all their colleagues through email. Which of the below mentioned AWS services helps achieve this goal?

- [ ] AWS Simple Workflow Service.
- [x] AWS Simple Email Service.
- [ ] Amazon Cognito.
- [ ] AWS Simple Queue Service.

**[⬆ Back to Top](#table-of-contents)**

### Is creating a Read Replica of another Read Replica supported?

- [ ] Only in VPC.
- [ ] Yes.
- [ ] Only in certain regions.
- [x] No.

**[⬆ Back to Top](#table-of-contents)**

### Which of the following is NOT a characteristic of Amazon Elastic Compute Cloud (Amazon EC2)?

- [ ] It can be used to launch as many or as few virtual servers as you need.
- [x] It increases the need to forecast traffic by providing dynamic IP addresses for static cloud computing.
- [ ] It eliminates your need to invest in hardware up front, so you can develop and deploy applications faster.
- [ ] It offers scalable computing capacity in the Amazon Web Services (AWS) cloud.

**[⬆ Back to Top](#table-of-contents)**

### A user has launched one EC2 instance in the US East region and one in the US West region. The user has launched an RDS instance in the US East region. How can the user configure access from both the EC2 instances to RDS?

- [ ] It is not possible to access RDS of the US East region from the US West region.
- [ ] Configure the US West region's security group to allow a request from the US East region's instance and configure the RDS security group's ingress rule for the US East EC2 group.
- [x] Configure the security group of the US East region to allow traffic from the US West region's instance and configure the RDS security group's ingress rule for the US East EC2 group.
- [ ] Configure the security group of both instances in the ingress rule of the RDS security group.

**[⬆ Back to Top](#table-of-contents)**

### What happens to the 1/0 operations while you take a database snapshot?

- [ ] 1/0 operations to the database are suspended for an hour while the backup is in progress.
- [ ] 1/0 operations to the database are sent to a Replica (if available) for a few minutes while the backup is in progress.
- [ ] 1/0 operations will be functioning normally.
- [x] 1/0 operations to the database are suspended for a few minutes while the backup is in progress.

**[⬆ Back to Top](#table-of-contents)**

### When an EC2 EBS-backed (EBS root) instance is stopped, what happens to the data on any ephemeral store volumes?

- [ ] Data is automatically saved in an EBS volume.
- [x] Data is unavailable until the instance is restarted.
- [ ] Data will be deleted and will no longer be accessible.
- [ ] Data is automatically saved as an EBS snapshot.

**[⬆ Back to Top](#table-of-contents)**

### [...] is a durable, block-level storage volume that you can attach to a single, running Amazon EC2 instance.

- [ ] Amazon S3.
- [x] Amazon EBS.
- [ ] None of these.
- [ ] All of these.

**[⬆ Back to Top](#table-of-contents)**

### A favored client needs you to quickly deploy a database that is a relational database service with minimal administration as he wants to spend the least amount of time administering it. Which database would be the best option?

- [ ] Amazon SimpleDB.
- [ ] Your choice of relational AMIs on Amazon EC2 and EB.
- [x] Amazon RDS.
- [ ] Amazon Redshift.

**[⬆ Back to Top](#table-of-contents)**

### You have a number of image files to encode. in an Amazon SQS worker queue, you create an Amazon SQS message for each file specifying the command (jpeg-encode) and the location of the file in Amazon S3. Which of the following statements best describes the functionality of Amazon SQS?

- [x] Amazon SQS is a distributed queuing system that is optimized for horizontal scalability, not for single-threaded sending or receiving speeds.
- [ ] Amazon SQS is for single-threaded sending or receiving speeds.
- [ ] Amazon SQS is a non-distributed queuing system.
- [ ] Amazon SQS is a distributed queuing system that is optimized for vertical scalability and for single-threaded sending or receiving speeds.

**[⬆ Back to Top](#table-of-contents)**

### While creating an Amazon RDS DB, your first task is to set up a DB [...] that controls what IP addresses or EC2 instances have access to your DB Instance.

- [ ] Security Pool.
- [ ] Secure Zone.
- [ ] Security Token Pool.
- [x] Security Group.

**[⬆ Back to Top](#table-of-contents)**

### After launching an instance that you intend to serve as a NAT (Network Address Translation) device in a public subnet you modify your route tables to have the NAT device be the target of internet bound traffic of your private subnet. When you try and make an outbound connection to the internet from an instance in the private subnet, you are not successful. Which of the following steps could resolve the issue?

- [x] Disabling the Source/Destination Check attribute on the NAT instance.
- [ ] Attaching an Elastic IP address to the instance in the private subnet.
- [ ] Attaching a second Elastic Network Interface (EN I) to the NAT instance, and placing it in the private subnet.
- [ ] Attaching a second Elastic Network Interface (ENI) to the instance in the private subnet, and placing it in the public subnet.

**[⬆ Back to Top](#table-of-contents)**

### Which of the following would you use to list your AWS Import/Export jobs?

- [ ] Amazon RDS.
- [ ] AWS Import/Export Web Service Tool.
- [x] Amazon S3 REST API.
- [ ] AWS Elastic Beanstalk.

**[⬆ Back to Top](#table-of-contents)**

### Company B is launching a new game app for mobile devices. Users will log into the game using their existing social media account to streamline data capture. Company B would like to directly save player data and scoring information from the mobile app to a DynamoDS table named Score Data. When a user saves their game the progress data will be stored to the Game state S3 bucket. What is the best approach for storing data to DynamoDB and S3?

- [ ] Use an EC2 Instance that is launched with an EC2 role providing access to the Score Data DynamoDB table and the GameState S3 bucket that communicates with the mobile app via web services.
- [x] Use temporary security credentials that assume a role providing access to the Score Data DynamoDB table and the Game State S3 bucket using web identity federation.
- [ ] Use Login with Amazon allowing users to sign in with an Amazon account providing the mobile app with access to the Score Data DynamoDB table and the Game State S3 bucket.
- [ ] Use an IAM user with access credentials assigned a role providing access to the Score Data DynamoDB table and the Game State S3 bucket for distribution with the mobile app.

**[⬆ Back to Top](#table-of-contents)**

### If your DB instance runs out of storage space or file system resources, its status will change to [...] and your DB Instance will no longer be available.

- [ ] storage-overflow.
- [x] storage-full.
- [ ] storage-exceed.
- [ ] storage-overage.

**[⬆ Back to Top](#table-of-contents)**

### Your application is using an ELB in front of an Auto Scaling group of web/application servers deployed across two AZs and a Multi-AZ RDS Instance for data persistence. The database CPU is often above 80% usage and 90% of 1/0 operations on the database are reads. To improve performance you recently added a single-node Memcached ElastiCache Cluster to cache frequent DB query results. in the next weeks the overall workload is expected to grow by 30%. Do you need to change anything in the architecture to maintain the high availability or the application with the anticipated additional load? Why?

- [x] Yes, you should deploy two Memcached ElastiCache Clusters in different AZs because the RDS instance will not be able to handle the load if the cache node fails.
- [ ] No, if the cache node fails you can always get the same data from the DB without having any availability impact.
- [ ] No, if the cache node fails the automated ElastiCache node recovery feature will prevent any availability impact.
- [ ] Yes, you should deploy the Memcached ElastiCache Cluster with two nodes in the same AZ as the RDS DB master instance to handle the load if one cache node fails.

**[⬆ Back to Top](#table-of-contents)**

### How many Elastic IP by default in Amazon Account?

- [ ] 1 Elastic IP.
- [ ] 3 Elastic IP.
- [ ] 5 Elastic IP.
- [x] 0 Elastic IP.

**[⬆ Back to Top](#table-of-contents)**

### What would be the best way to retrieve the public IP address of your EC2 instance using the CLI?

- [ ] Using tags.
- [ ] Using traceroute.
- [ ] Using ipconfig.
- [x] Using instance metadata.

**[⬆ Back to Top](#table-of-contents)**

### A company is building a two-tier web application to serve dynamic transaction-based content. The data tier is leveraging an Online Transactional Processing (OLTP) database. What services should you leverage to enable an elastic and scalable web tier?

- [x] Elastic Load Balancing, Amazon EC2, and Auto Scaling.
- [ ] Elastic Load Balancing, Amazon RDS with Multi-AZ, and Amazon S3.
- [ ] Amazon RDS with Multi-AZ and Auto Scaling.
- [ ] Amazon EC2, Amazon DynamoDB, and Amazon S3.

**[⬆ Back to Top](#table-of-contents)**

### You are designing a connectivity solution between on-premises infrastructure and Amazon VPC. Your server's on-premises will De communicating with your VPC instances. You will De establishing IPSec tunnels over the internet You will be using VPN gateways and terminating the IPsec tunnels on AWS supported customer gateways. Which of the following objectives would you achieve by implementing an IPSec tunnel as outlined above? (Choose 4 answers)

- [ ] End-to-end protection of data in transit.
- [ ] End-to-end Identity authentication.
- [x] Data encryption across the Internet.
- [x] Protection of data in transit over the Internet.
- [x] Peer identity authentication between VPN gateway and customer gateway.
- [x] Data integrity protection across the Internet.

**[⬆ Back to Top](#table-of-contents)**

### You have been storing massive amounts of data on Amazon Glacier for the past 2 years and now start to wonder if there are any limitations on this. What is the correct answer to your question?

- [ ] The total volume of data is limited but the number of archives you can store are unlimited.
- [ ] The total volume of data is unlimited but the number of archives you can store are limited.
- [x] The total volume of data and number of archives you can store are unlimited.
- [ ] The total volume of data is limited and the number of archives you can store are limited.

**[⬆ Back to Top](#table-of-contents)**

### How are the EBS snapshots saved on Amazon S3?

- [ ] Exponentially.
- [x] Incrementally.
- [ ] EBS snapshots are not stored in the Amazon S3.
- [ ] Decrementally.

**[⬆ Back to Top](#table-of-contents)**

### An online gaming site asked you if you can deploy a database that is a fast, highly scalable NoSQL database service in AWS for a new site that he wants to build. Which database should you recommend?

- [x] Amazon DynamoDB.
- [ ] Amazon RDS.
- [ ] Amazon Redshift.
- [ ] Amazon SimpleDB.

**[⬆ Back to Top](#table-of-contents)**

### You have three Amazon EC2 instances with Elastic IP addresses in the US East (Virginia) region, and you want to distribute requests across all three IPs evenly for users for whom US East (Virginia) is the appropriate region. How many EC2 instances would be sufficient to distribute requests in other regions?

- [ ] 3.
- [ ] 9.
- [ ] 2.
- [x] 1.

**[⬆ Back to Top](#table-of-contents)**

### You are the new IT architect in a company that operates a mobile sleep tracking application. When activated at night, the mobile app is sending collected data points of 1 kilobyte every 5 minutes to your backend. The backend takes care of authenticating the user and writing the data points into an Amazon DynamoDB table. Every morning, you scan the table to extract and aggregate last night's data on a per user basis, and store the results in Amazon S3. Users are notified via Amazon 5M5 mobile push notifications that new data is available, which is parsed and visualized by The mobile app Currently you have around lOOk users who are mostly based out of North America. You have been tasked to optimize the architecture of the backend system to lower cost what would you recommend? (Choose 2 answers)

- [x] Create a new Amazon DynamoDB able each day and drop the one for the previous day after its data is on Amazon S3.
- [ ] Have the mobile app access Amazon DynamoDB directly instead of J50N files stored on Amazon S3.
- [x] Introduce an Amazon SQS queue to buffer writes to the Amazon DynamoDB table and reduce provisioned write throughput.
- [ ] Introduce Amazon Elasticache to cache reads from the Amazon DynamoDB table and reduce provisioned read throughput.
- [ ] Write data directly into an Amazon Redshift cluster replacing both Amazon DynamoDB and Amazon S3.

**[⬆ Back to Top](#table-of-contents)**

### You are implementing a URL whitelisting system for a company that wants to restrict outbound HTTP'S connections to specific domains from their EC2-hosted applications you deploy a single EC2 instance running proxy software and configure It to accept traffic from all subnets and EC2 instances in the VPC. You configure the proxy to only pass through traffic to domains that you define in its whitelist configuration You have a nightly maintenance window or 10 minutes where all instances fetch new software updates. Each update Is about 200MB in size and there are 500 instances in theVPC that routinely fetch updates After a few days you notice that some machines are failing to successfully download some, but not all of their updates within the maintenance window. The download URLs used for these updates are correctly listed in the proxy's whitelist configuration and you are able to access them manually using a web browser on the instances. What might be happening? (Choose 2 answers)

- [x] You are running the proxy on an undersized EC2 instance type so network throughput is not sufficient for all instances to download their updates in time.
- [x] You are running the proxy on a sufficiently-sized EC2 instance in a private subnet and its network throughput is being throttled by a NAT running on an undersized EC2 instance.
- [ ] The route table for the subnets containing the affected EC2 instances is not configured to direct network traffic for the software update locations to the proxy.
- [ ] You have not allocated enough storage to t he EC2 instance running the proxy so the network buffer is filling up, causing some requests to fail.
- [ ] You are running the proxy in a public subnet but have not allocated enough EIPs to support the needed network throughput through the Internet Gateway (IGW).

**[⬆ Back to Top](#table-of-contents)**

### You are playing around with setting up stacks using JSON templates in CloudFormation to try and understand them a little better. You have set up about 5 or 6 but now start to wonder if you are being charged for these stacks. What is AWS's billing policy regarding stack resources?

- [ ] You are not charged for the stack resources if they are not taking any traffic.
- [x] You are charged for the stack resources for the time they were operating (even if you deleted the stack right away).
- [ ] You are charged for the stack resources for the time they were operating (but not if you deleted the stack within 60 minutes).
- [ ] You are charged for the stack resources for the time they were operating (but not if you deleted the stack within 30 minutes).

**[⬆ Back to Top](#table-of-contents)**

### What does Amazon Cloud Formation provide?

- [ ] The ability to setup Autoscaling for Amazon EC2 instances.
- [ ] None of these.
- [ ] A templated resource creation for Amazon Web Services.
- [x] A template to map network resources for Amazon Web Services.

**[⬆ Back to Top](#table-of-contents)**

### You are signed in as root user on your account but there is an Amazon S3 bucket under your account that you cannot access. What is a possible reason for this?

- [x] An IAM user assigned a bucket policy to an Amazon S3 bucket and didn't specify the root user as a principal
- [ ] The S3 bucket is full.
- [ ] The S3 bucket has reached the maximum number of objects allowed.
- [ ] You are in the wrong Availability Zone.

**[⬆ Back to Top](#table-of-contents)**

### When creation of an EBS snapshot is initiated, but not completed, the EBS volume?

- [ ] Can be used while the snapshot is in progress.
- [ ] Cannot be detached or attached to an EC2 instance until the snapshot completes.
- [ ] Can be used in read-only mode while the snapshot is in progress.
- [x] Cannot be used until the snapshot completes.

**[⬆ Back to Top](#table-of-contents)**

### What does Amazon SES stand for?

- [ ] Simple Elastic Server.
- [x] Simple Email Service.
- [ ] Software Email Solution.
- [ ] Software Enabled Server.

**[⬆ Back to Top](#table-of-contents)**

### You receive a bill from AWS but are confused because you see you are incurring different costs for the exact same storage size in different regions on Amazon S3. You ask AWS why this is so. What response would you expect to receive from AWS?

- [ ] We charge less in different time zones.
- [x] We charge less where our costs are less.
- [ ] This will balance out next bill.
- [ ] It must be a mistake.

**[⬆ Back to Top](#table-of-contents)**

### Disabling automated backups [...] disable the point-in-time recovery.

- [ ] if configured to can.
- [ ] will never.
- [x] will.

**[⬆ Back to Top](#table-of-contents)**

### A user has launched a large EBS backed EC2 instance in the US-East-1a region. The user wants to achieve Disaster Recovery (DR) for that instance by creating another small instance in Europe. How can the user achieve DR?

- [ ] Copy the instance from the US East region to the EU region.
- [ ] Use the 'Launch more like this' option to copy the instance from one region to another.
- [ ] Copy the running instance using the 'Instance Copy' command to the EU region.
- [x] Create an AMI of the instance and copy the AMI to the EU region. Then launch the instance from the EU AMI.

**[⬆ Back to Top](#table-of-contents)**

### How many relational database engines does RDS currently support?

- [x] Three: MySQL, Oracle and Microsoft SQL Server.
- [ ] Just two: MySQL and Oracle.
- [ ] Five: MySQL, PostgreSQL, MongoDB, Cassandra and SQLite.
- [ ] Just one: MySQL.

**[⬆ Back to Top](#table-of-contents)**

### Are you able to integrate a multi-factor token service with the AWS Platform?

- [ ] Yes, you can integrate private multi-factor token devices to authenticate users to the AWS platform.
- [ ] No, you cannot integrate multi-factor token devices with the AWS platform.
- [x] Yes, using the AWS multi-factor token devices to authenticate users on the AWS platform.

**[⬆ Back to Top](#table-of-contents)**

### What is the default maximum number of MFA devices in use per AWS account (at the root account level)?

- [x] 1.
- [ ] 5.
- [ ] 15.
- [ ] 10.

**[⬆ Back to Top](#table-of-contents)**

### Select the correct statement: Within Amazon EC2, when using Linux instances, the device name /dev/sda1 is [...].

- [ ] reserved for EBS volumes.
- [ ] recommended for EBS volumes.
- [ ] recommended for instance store volumes.
- [x] reserved for the root device.

**[⬆ Back to Top](#table-of-contents)**

### Does Amazon Route 53 support NS Records?

- [ ] Yes, it supports Name Service records.
- [ ] No.
- [ ] It supports only MX records.
- [x] Yes, it supports Name Server records.

**[⬆ Back to Top](#table-of-contents)**

### Your web application front end consists of multiple EC2 instances behind an Elastic Load Balancer. You configured ELB to perform health checks on these EC2 instances, if an instance fails to pass health checks, which statement will be true?

- [ ] The instance gets terminated automatically by the ELB.
- [ ] The instance gets quarantined by the ELB for root cause analysis.
- [ ] The instance is replaced automatically by the ELB.
- [x] The ELB stops sending traffic to the instance that failed its health check.

**[⬆ Back to Top](#table-of-contents)**

### George has launched three EC2 instances inside the US-East-1a zone with his AWS account. Ray has launched two EC2 instances in the US-East-1a zone with his AWS account. Which of the below mentioned statements will help George and Ray understand the Availability Zone (AZ) concept better?

- [ ] All the instances of George and Ray can communicate over a private IP with a minimal cost.
- [x] The US-East-1a region of George and Ray can be different Availability Zones.
- [ ] All the instances of George and Ray can communicate over a private IP without any cost.
- [ ] The instances of George and Ray will be running in the same data centre.

**[⬆ Back to Top](#table-of-contents)**

### Once again your customers are concerned about the security of their sensitive data and with their latest enquiry ask about what happens to old storage devices on AWS. What would be the best answer to this question?

- [ ] AWS reformats the disks and uses them again.
- [x] AWS uses the techniques detailed in DoD 5220.22-M to destroy data as part of the decommissioning process.
- [ ] AWS uses their own proprietary software to destroy data as part of the decommissioning process.
- [ ] AWS uses a 3rd party security organization to destroy data as part of the decommissioning process.

**[⬆ Back to Top](#table-of-contents)**

### Which of the following are characteristics of Amazon VPC subnets? (Choose 2 answers)

- [ ] Each subnet spans at least 2 Availability Zones to provide a high-availability environment.
- [x] Each subnet maps to a single Availability Zone.
- [ ] CIDR block mask of/25 is the smallest range supported.
- [ ] By default, all subnets can route between each other, whether they are private or public.
- [x] Instances in a private subnet can communicate with the Internet only if they have an Elastic IP.

**[⬆ Back to Top](#table-of-contents)**

### Which AWS instance address has the following characteristics? 'If you stop an instance, its Elastic IP address is unmapped, and you must remap it when you restart the instance.'

- [ ] Both A and B.
- [ ] None of these.
- [ ] VPC Addresses.
- [x] EC2 Addresses.

**[⬆ Back to Top](#table-of-contents)**

### You are designing a data leak prevention solution for your VPC environment. You want your VPC Instances to be able to access software depots and distributions on the Internet for product updates. The depots and distributions are accessible via third party CONs by their URLs. You want to explicitly deny any other outbound connections from your VPC instances to hosts on the internet. Which of the following options would you consider?

- [x] Configure a web proxy server in your VPC and enforce URL-based ru les for outbound access Remove default routes.
- [ ] Implement security groups and configure outbound rules to only permit traffic to software depots.
- [ ] Move all your instances into private VPC subnets remove default routes from all routing tables and add specific routes to the software depots and distributions only.
- [ ] Implement network access control lists to all specific destinations, with an Implicit deny as a rule.

**[⬆ Back to Top](#table-of-contents)**

### What is an isolated database environment running in the cloud (Amazon RDS) called?

- [x] DB Instance.
- [ ] DB Unit.
- [ ] DB Server.
- [ ] DB Volume.

**[⬆ Back to Top](#table-of-contents)**

### A user is sending bulk emails using AWS SES. The emails are not reaching some of the targeted audience because they are not authorized by the ISPs. How can the user ensure that the emails are all delivered?

- [x] Send an email using DKIM with SE.
- [ ] Send an email using SMTP with SE.
- [ ] Open a ticket with AWS support to get it authorized with the IS.
- [ ] Authorize the ISP by sending emails from the development account.

**[⬆ Back to Top](#table-of-contents)**

### What's an ECU?

- [ ] Extended Cluster User.
- [ ] None of these.
- [ ] Elastic Computer Usage.
- [x] Elastic Compute Unit.

**[⬆ Back to Top](#table-of-contents)**

### You would like to create a mirror image of your production environment in another region for disaster recovery purposes. Which of the following AWS resources do not need to be recreated in the second region? (Choose 2 answers)

- [x] Route 53 Record Sets.
- [x] IAM Roles.
- [ ] Elastic IP Addresses (EIP).
- [ ] EC2 Key Pairs.
- [ ] Launch configurations.
- [ ] Security Groups.

**[⬆ Back to Top](#table-of-contents)**

### Which procedure for backing up a relational database on EC2 that is using a set of RAIDed EBS volumes for storage minimizes the time during which the database cannot be written to and results in a consistent backup?

- [x] 1. Detach EBS volumes, 2. Start EBS snapshot of volumes, 3. Re-attach EBS volumes.
- [ ] 1. Stop the EC2 Instance. 2. Snapshot the EBS volumes.
- [ ] 1. Suspend disk 1/0, 2. Create an image of the EC2 Instance, 3. Resume disk 1/0.
- [ ] 1. Suspend disk 1/0, 2. Start EBS snapshot of volumes, 3. Resume disk 1/0.
- [ ] 1. Suspend disk 1/0, 2. Start EBS snapshot of volumes, 3. Wait for snapshots to complete, 4. Resume disk 1/0.

**[⬆ Back to Top](#table-of-contents)**

### My Read Replica appears 'stuck' after a Multi-AZ failover and is unable to obtain or apply updates from the source DB Instance. What do I do?

- [x] You will need to delete the Read Replica and create a new one to rep lace it.
- [ ] You will need to disassociate the DB Engine and re associate it.
- [ ] The instance should be deployed to Single AZ and then moved to Multi-AZ once again.
- [ ] You will need to delete the DB Instance and create a new one to replace it.

**[⬆ Back to Top](#table-of-contents)**

### You are setting up some IAM user policies and have also become aware that some services support resource-based permissions, which let you attach policies to the service's resources instead of to IAM users or groups. Which of the below statements is true in regards to resource-level permissions?

- [ ] All services support resource-level permissions for all actions.
- [ ] Resource-level permissions are supported by Amazon CloudFront.
- [ ] All services support resource-level permissions only for some actions.
- [x] Some services support resource-level permissions only for some actions.

**[⬆ Back to Top](#table-of-contents)**

### You have some very sensitive data stored on AWS S3 and want to try every possible alternative to keeping it secure in regards to access control. What are the mechanisms available for access control on AWS S3?

- [x] (IAM) policies, Access Control Lists (ACLs), bucket policies, and query string authentication.
- [ ] (IAM) policies, Access Control Lists (ACLs) and bucket policies.
- [ ] Access Control Lists (ACLs), bucket policies, and query string authentication.
- [ ] (IAM) policies, Access Control Lists (ACLs), bucket policies, query string authentication and encryption.

**[⬆ Back to Top](#table-of-contents)**

### You are implementing AWS Direct Connect. You intend to use AWS public service end points such as Amazon S3, across the AWS Direct Connect link. You want other Internet traffic to use your existing link to an Internet Service Provider. What is the correct way to configure AWS Direct connect for access to services such as Amazon S3?

- [ ] Configure a public Interface on your AWS Direct Connect link. Configure a static route via your AWS Direct Connect link that points to Amazon S3 Advertise a default route to AWS using BGP.
- [ ] Create a private interface on your AWS Direct Connect link. Configure a static route via your AWS Direct connect link that points to Amazon S3 Configure specific routes to your network in your VPC.
- [x] Create a public interface on your AWS Direct Connect link. Redistribute BGP routes into your existing routing infrastructure; advertise specific routes for your network to AWS.
- [ ] Create a private interface on your AWS Direct connect link. Redistribute BGP routes into your existing routing infrastructure and advertise a default route to AWS.

**[⬆ Back to Top](#table-of-contents)**

### You are setting up your first Amazon Virtual Private Cloud (Amazon VPC) network so you decide you should probably use the AWS Management Console and the VPC Wizard. Which of the following is not an option for network architectures after launching the 'Start VPC Wizard' in Amazon VPC page on the AWS Management Console?

- [ ] VPC with a Single Public Subnet Only.
- [x] VPC with a Public Subnet Only and Hardware VPN Access.
- [ ] VPC with Public and Private Subnets and Hardware VPN Access.
- [ ] VPC with a Private Subnet Only and Hardware VPN Access.

**[⬆ Back to Top](#table-of-contents)**

### True or False: A VPC contains multiple subnets, where each subnet can span multiple Availability Zones.

- [ ] This is true only if requested during the set-up of VPC.
- [x] This is true.
- [ ] This is false.
- [ ] This is true only for US regions.

**[⬆ Back to Top](#table-of-contents)**

### Amazon RDS automated backups and DB Snapshots are currently supported for only the [...] storage engine.

- [x] InnoDB.
- [ ] MyISAM.

**[⬆ Back to Top](#table-of-contents)**

### While signing in REST/ Query requests, for additional security, you should transmit your requests using Secure Sockets Layer (SSL) by using [...].

- [ ] HTTP.
- [ ] Internet Protocol Security (IPsec).
- [ ] TLS (Transport Layer Security).
- [x] HTTPS.

**[⬆ Back to Top](#table-of-contents)**

### Out of the stripping options available for the EBS volumes, which one has the following disadvantage: 'Doubles the amount of 1/0 required from the instance to EBS compared to RAID 0, because you're mirroring all writes to a pair of volumes, limiting how much you can stripe.'?

- [ ] Raid 0.
- [x] RAID 1+0 (RAID 10).
- [ ] Raid 1.
- [ ] Raid.

**[⬆ Back to Top](#table-of-contents)**

### Can I encrypt connections between my application and my DB Instance using SSL?

- [x] Yes.
- [ ] Only in VPC.
- [ ] Only in certain regions.

**[⬆ Back to Top](#table-of-contents)**

### Which of the following items are required to allow an application deployed on an EC2 instance to write data to a DynamoDB table? Assume that no security keys are allowed to be stored on the EC2 instance. (Choose 3 answers)

- [x] Create an IAM Role that allows write access to the DynamoDB table.
- [x] Add an IAM Role to a running EC2 instance.
- [ ] Create an IAM User that al lows write access to the Dynamo DB table.
- [ ] Add an IAM User to a running EC2 instance.
- [x] Launch an EC2 Instance with the IAM Role included in the launch configuration.

**[⬆ Back to Top](#table-of-contents)**

### Identify a true statement about the On-Demand instances purchasing option provided by Amazon EC2.

- [x] Pay for the instances that you use by the hour, with no long-term commitments or up-front payments.
- [ ] Make a low, one-time, up-front payment for an instance, reserve it for a one- or three-year term, and pay a significantly lower hourly rate for these instances.
- [ ] Pay for the instances that you use by the hour, with long-term commitments or up-front payments.
- [ ] Make a high, one-time, all-front payment for an instance, reserve it for a one- or three-year term, and pay a significantly higher hourly rate for these instances.

**[⬆ Back to Top](#table-of-contents)**

### When will you incur costs with an Elastic IP address (EIP)?

- [ ] When an EIP is allocated.
- [ ] When it is allocated and associated with a running instance.
- [ ] When it is allocated and associated with a stopped instance.
- [x] Costs are incurred regardless of whether the ElP is associated with a running instance.

**[⬆ Back to Top](#table-of-contents)**

### IAM provides several policy templates you can use to automatically assign permissions to the groups you create. The [...] policy template gives the Admins group permission to access all account resources, except your AWS account information.

- [ ] Read Only Access.
- [ ] Power User Access.
- [ ] AWS Cloud Formation Read Only Access.
- [x] Administrator Access.

**[⬆ Back to Top](#table-of-contents)**

### What does RRS stand for when talking about S3?

- [ ] Redundancy Removal System.
- [ ] Relational Rights Storage.
- [ ] Regional Rights Standard.
- [x] Reduced Redundancy Storage.

**[⬆ Back to Top](#table-of-contents)**

### Can I change the EC2 security groups after an instance is launched in EC2-Classic?

- [ ] Yes, you can change security groups after you launch an instance in EC2-Classic.
- [x] No, you cannot change security groups after you launch an instance in EC2-Classic.
- [ ] Yes, you can only when you remove rules from a security group.
- [ ] Yes, you can only when you add rules to a security group.

**[⬆ Back to Top](#table-of-contents)**

### Please select the Amazon EC2 resource which cannot be tagged.

- [ ] Images (AMIs, kernels, RAM disks).
- [ ] Amazon EBS volumes.
- [x] Elastic IP addresses.
- [ ] VPCs.

**[⬆ Back to Top](#table-of-contents)**

### Does Route 53 support MX Records?

- [x] Yes.
- [ ] It supports CNAME records, but not MX records.
- [ ] No.
- [ ] Only Primary MX records. Secondary MX records are not supported.

**[⬆ Back to Top](#table-of-contents)**

### Which of the following notification endpoints or clients are supported by Amazon Simple Notification Service? (Choose 2 answers)

- [x] Email.
- [ ] CloudFront distribution.
- [ ] File Transfer Protocol.
- [x] Short Message Service.
- [ ] Simple Network Management Protocol.

**[⬆ Back to Top](#table-of-contents)**

### AWS Identity and Access Management is a web service that enables Amazon Web Services (AWS) customers to manage users and user permissions in AWS. In addition to supporting IAM user policies, some services support resource-based permissions. Which of the following services are supported by resource-based permissions?

- [ ] Amazon SNS, and Amazon SQS and AWS Direct Connect.
- [ ] Amazon S3 and Amazon SQS and Amazon ElastiCache.
- [x] Amazon S3, Amazon SNS, Amazon SQS, Amazon Glacier and Amazon EB
- [ ] Amazon Glacier, Amazon SNS, and Amazon CloudWatch.

**[⬆ Back to Top](#table-of-contents)**

### What does the following policy for Amazon EC2 do? { 'Statement':[{ 'Effect': 'Allow', 'Action':'ec2: Describe*', 'Resource':'*' }] }

- [x] Allow users to use actions that start with 'Describe' over all the EC2 resources.
- [ ] Share an AMI with a partner.
- [ ] Share an AMI within the account.
- [ ] Allow a group to only be able to describe, run, stop, start, and terminate instances.

**[⬆ Back to Top](#table-of-contents)**

### Which IAM role do you use to grant AWS Lambda permission to access a DynamoDB Stream?

- [ ] Dynamic role.
- [ ] Invocation role.
- [x] Execution role.
- [ ] Event Source role.

**[⬆ Back to Top](#table-of-contents)**

### Can resource record sets in a hosted zone have a different domain suffix (for example, <www.blog>. acme.com and <www.acme.ca>)?

- [ ] Yes, it can have for a maximum of three different TLDs.
- [ ] Yes.
- [x] Yes, it can have depending on the TL.
- [ ] No.

**[⬆ Back to Top](#table-of-contents)**

### In Amazon Elastic Compute Cloud, which of the following is used for communication between instances in the same network (EC2-Classic or a VPC)?

- [x] Private IP addresses.
- [ ] Elastic IP addresses.
- [ ] Static IP addresses.
- [ ] Public IP addresses.

**[⬆ Back to Top](#table-of-contents)**

### A user is planning to host a mobile game on EC2 which sends notifications to active users on either high score or the addition of new features. The user should get this notification when he is online on his mobile device. Which of the below mentioned AWS services can help achieve this functionality?

- [x] AWS Simple Notification Service.
- [ ] AWS Simple Email Service.
- [ ] AWS Mobile Communication Service.
- [ ] AWS Simple Queue Service.

**[⬆ Back to Top](#table-of-contents)**

### You need to create an Amazon Machine Image (AMI) for a customer for an application which does not appear to be part of the standard AWS AMI template that you can see in the AWS console. What are the alternative possibilities for creating an AMI on AWS?

- [ ] You can purchase an AMIs from a third party but cannot create your own AMI.
- [x] You can purchase an AMIs from a third party or can create your own AMI.
- [ ] Only AWS can create AMIs and you need to wait till it becomes available.
- [ ] Only AWS can create AMIs and you need to request them to create one for you.

**[⬆ Back to Top](#table-of-contents)**

### Will I be charged if the DB instance is idle?

- [x] Yes.
- [ ] Only is running in GovCloud.
- [ ] Only if running in VPC.

**[⬆ Back to Top](#table-of-contents)**

### Your company has been storing a lot of data in Amazon Glacier and has asked for an inventory of what is in there exactly. So you have decided that you need to download a vault inventory. Which of the following statements is incorrect in relation to Vault Operations in Amazon Glacier?

- [ ] You can use Amazon Simple Notification Service (Amazon SNS) notifications to notify you when the job completes.
- [ ] A vault inventory refers to the list of archives in a vault.
- [x] You can use Amazon Simple Queue Service (Amazon SQS) notifications to notify you when the job completes.
- [ ] Downloading a vault inventory is an asynchronous operation.

**[⬆ Back to Top](#table-of-contents)**

### Your fortune 500 company has under taken a TCO analysis evaluating the use of Amazon S3 versus acquiring more hardware The outcome was that ail employees would be granted access to use Amazon S3 for storage of their personal documents. Which of the following will you need to consider so you can set up a solution that incorporates single sign-on from your corporate AD or LDAP directory and restricts access for each user to a designated user folder in a bucket? (Choose 3 answers)

- [x] Setting up a federation proxy or identity provider.
- [x] Using AWS Security Token Service to generate temporary tokens.
- [ ] Tagging each folder in the bucket.
- [x] Configuring IAM role.
- [ ] Setting up a matching IAM user for every user in your corporate directory that needs access to a folder in the bucket.

**[⬆ Back to Top](#table-of-contents)**

### Your company policies require encryption of sensitive data at rest. You are considering the possible options for protecting data while storing it at rest on an EBS data volume, attached to an EC2 instance. Which of these options would allow you to encrypt your data at rest? (Choose 3 answers)

- [x] Implement third party volume encryption tools.
- [ ] Do nothing as EBS volumes are encrypted by default.
- [x] Encrypt data inside your applications before storing it on EBS.
- [x] Encrypt data using native data encryption drivers at the file system level.
- [ ] Implement SSL/TLS for all services running on the server.

**[⬆ Back to Top](#table-of-contents)**

### A scope has been handed to you to set up a super fast gaming server and you decide that you will use Amazon DynamoDB as your database. For efficient access to data in a table, Amazon DynamoDB creates and maintains indexes for the primary key attributes. A secondary index is a data structure that contains a subset of attributes from a table, along with an alternate key to support Query operations. How many types of secondary indexes does DynamoDB support?

- [x] 2.
- [ ] 16.
- [ ] 4.
- [ ] As many as you need.

**[⬆ Back to Top](#table-of-contents)**

### True or False: in Amazon Route 53, you can create a hosted zone for a top-level domain (TLD).

- [x] False.
- [ ] False, Amazon Route 53 automatically creates it for you.
- [ ] True, only if you send an XML document with a CreateHostedZoneRequest element for TLD.
- [ ] True.

**[⬆ Back to Top](#table-of-contents)**

### You want to use AWS Import/Export to send data from your S3 bucket to several of your branch offices. What should you do if you want to send 10 storage units to AWS?

- [ ] Make sure your disks are encrypted prior to shipping.
- [ ] Make sure you format your disks prior to shipping.
- [ ] Make sure your disks are 1TB or more.
- [x] Make sure you submit a separate job request for each device.

**[⬆ Back to Top](#table-of-contents)**

### You are deploying an application to track GPS coordinates of delivery trucks in the United States. Coordinates are transmitted from each delivery t ruck once every three seconds. You need to design an architecture that will enable real-time processing of these coordinates from multiple consumers. Which service should you use to implement data ingestion?

- [x] Amazon Kinesis.
- [ ] AWS Data Pipeline.
- [ ] Amazon AppStream.
- [ ] Amazon Simple Queue Service.

**[⬆ Back to Top](#table-of-contents)**

### While performing the volume status checks, if the status is insufficient-data, what does it mean?

- [x] The checks may still be in progress on the volume.
- [ ] The check has passed.
- [ ] The check has failed.

**[⬆ Back to Top](#table-of-contents)**

### Can you create IAM security credentials for existing users?

- [x] Yes, existing users can have security credentials associated with their account.
- [ ] No, IAM requires that all users who have credentials set up are not existing users.
- [ ] No, security credentials are created within GROUPS, and then users are associated to GROUPS at a later time.
- [ ] Yes, but only IAM credentials, not ordinary security credentials.

**[⬆ Back to Top](#table-of-contents)**

### Can I move a Reserved Instance from one Region to another?

- [x] No.
- [ ] Only if they are moving into GovCloud.
- [ ] Yes.
- [ ] Only if they are moving to US East from another region.

**[⬆ Back to Top](#table-of-contents)**

### A user has created an ELB with the Availability Zone US-East-1A. The user wants to add more zones to ELB to achieve High Availability. How can the user add more zones to the existing ELB?

- [ ] The user should stop the ELB and add zones and instances as required.
- [ ] The only option is to launch instances in different zones and add to ELB.
- [ ] It is not possible to add more zones to the existing ELB.
- [x] The user can add zones on the fly from the AWS console.

**[⬆ Back to Top](#table-of-contents)**

### Amazon SWF is designed to help users …

- [ ] Design graphical user interface interactions.
- [ ] Manage user identification and authorization.
- [ ] Store Web content.
- [x] Coordinate synchronous and asynchronous tasks which are distributed and fault tolerant.

**[⬆ Back to Top](#table-of-contents)**

### Which technique can be used to integrate AWS IAM (Identity and Access Management) with an on-premise LDAP (Lightweight Directory Access Protocol) directory service?

- [ ] Use an IAM policy that references the LDAP account identifiers and the AWS credentials.
- [x] Use SAML (Security Assertion Markup Language) to enable single sign-on between AWS and LDAP.
- [ ] Use AWS Security Token Service from an identity broker to issue short-lived AWS credentials.
- [ ] Use IAM roles to automatically rotate the IAM credentials when LDAP credentials are updated.
- [ ] Use the LDAP credentials to restrict a group of users from launching specific EC2 instance types.

**[⬆ Back to Top](#table-of-contents)**

### You are building a solution for a customer to extend their on-premises data center to AWS. The customer requires a 50-Mbps dedicated and private connection to their VPC. Which AWS product or feature satisfies this requirement?

- [ ] Amazon VPC peering.
- [ ] Elastic IP Addresses.
- [x] AWS Direct Connect.
- [ ] Amazon VPC virtual private gateway.

**[⬆ Back to Top](#table-of-contents)**

### A customer wants to leverage Amazon Simple Storage Service (S3) and Amazon Glacier as part of their backup and archive infrastructure. The customer plans to use third-party software to support this integration. Which approach will limit the access of the third party software to only the Amazon S3 bucket named 'company-backup'?

- [ ] A custom bucket policy limited to the Amazon S3 API in the Amazon Glacier archive 'company backup'.
- [ ] A custom bucket policy limited to the Amazon S3 API in 'company-backup'.
- [ ] A custom IAM user policy limited to the Amazon S3 API for the Amazon Glacier archive 'company backup'.
- [x] A custom IAM user policy limited to the Amazon S3 API in 'company-backup'.

**[⬆ Back to Top](#table-of-contents)**

### A user needs to run a batch process which runs for 10 minutes. This will only be run once, or at maximum twice, in the next month, so the processes will be temporary only. The process needs 15 X-Large instances. The process downloads the code from S3 on each instance when it is launched, and then generates a temporary log file. Once the instance is terminated, all the data will be lost. Which of the below mentioned pricing models should the user choose in this case?

- [x] Spot instance.
- [ ] Reserved instance.
- [ ] On-demand instance.
- [ ] EBS optimized instance.

**[⬆ Back to Top](#table-of-contents)**

### You have been doing a lot of testing of your VPC Network by deliberately failing EC2 instances to test whether instances are failing over properly. Your customer who will be paying the AWS bill for all this asks you if he being charged for all these instances. You try to explain to him how the billing works on EC2 instances to the best of your knowledge. What would be an appropriate response to give to the customer in regards to this?

- [ ] Billing commences when Amazon EC2 AMI instance is completely up and billing ends as soon as the instance starts to shutdown.
- [ ] Billing only commences only after 1 hour of uptime and billing ends when the instance terminates.
- [x] Billing commences when Amazon EC2 initiates the boot sequence of an AMI instance and billing ends when the instance shuts down.
- [ ] Billing commences when Amazon EC2 initiates the boot sequence of an AMI instance and billing ends as soon as the instance starts to shutdown.

**[⬆ Back to Top](#table-of-contents)**

### Refer to the architecture diagram above of a batch processing solution using Simple Queue Service (SQS) to set up a message queue between EC2 instances which are used as batch processors Cloud Watch monitors the number of Job requests (queued messages) and an Auto Scaling group adds or deletes batch servers automatically based on parameters set in Cloud Watch alarms. You can use this architecture to implement which of the following features in a cost effective and efficient manner?

![Question 563](images/question563.jpg)

- [ ] Reduce the overall lime for executing jobs through parallel processing by allowing a busy EC2 instance that receives a message to pass it to the next instance in a daisy-chain setup.
- [ ] Implement fault tolerance against EC2 instance failure since messages would remain in SQS and worn can continue with recovery of EC2 instances implement fault tolerance against SQS failure by backing up messages to S3.
- [x] Implement message passing between EC2 instances within a batch by exchanging messages through SQS.
- [ ] Coordinate number of EC2 instances with number of job requests automatically thus Improving cost effectiveness.
- [ ] Handle high priority jobs before lower priority jobs by assigning a priority metadata fie ld to SQS messages.

**[⬆ Back to Top](#table-of-contents)**

### You are migrating an internal server on your DC to an EC2 instance with EBS volume. Your server disk usage is around 500GB so you just copied all your data to a 2TB disk to be used with AWS Import/Export. Where will the data be imported once it arrives at Amazon?

- [ ] To a 2TB EBS volume.
- [x] To an S3 bucket with 2 objects of 1TB.
- [ ] To an 500GB EBS volume.
- [ ] To an S3 bucket as a 2TB snapshot.

**[⬆ Back to Top](#table-of-contents)**

### Is there any way to own a direct connection to Amazon Web Services?

- [ ] You can create an encrypted tunnel to VPC, but you don't own the connection.
- [ ] Yes, it's called Amazon Dedicated Connection.
- [ ] No, AWS only allows access from the public Internet.
- [x] Yes, it's called Direct Connect.

**[⬆ Back to Top](#table-of-contents)**

### Which of the following strategies can be used to control access to your Amazon EC2 instances?

- [ ] DB security groups.
- [ ] IAM policies.
- [ ] None of these.
- [x] EC2 security groups.

**[⬆ Back to Top](#table-of-contents)**

### A client of yours has a huge amount of data stored on Amazon S3, but is concerned about someone stealing it while it is in transit. You know that all data is encrypted in transit on AWS, but which of the following is wrong when describing server-side encryption on AWS?

- [ ] Amazon S3 server-side encryption employs strong multi-factor encryption.
- [ ] Amazon S3 server-side encryption uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data.
- [x] In server-side encryption, you manage encryption/decryption of your data, the encryption keys, and related tools.
- [ ] Server-side encryption is about data encryption at rest―that is, Amazon S3 encrypts your data as it writes it to disks.

**[⬆ Back to Top](#table-of-contents)**

### When you run a DB Instance as a Multi-AZ deployment, the [...] serves database writes and reads

- [ ] secondary.
- [ ] backup.
- [ ] stand by.
- [x] primary.

**[⬆ Back to Top](#table-of-contents)**

### In Amazon EC2, how many Elastic IP addresses can you have by default?

- [ ] 10.
- [ ] 2.
- [x] 5.
- [ ] 20.

**[⬆ Back to Top](#table-of-contents)**

### A user has created photo editing software and hosted it on EC2. The software accepts requests from the user about the photo format and resolution and sends a message to S3 to enhance the picture accordingly. Which of the below mentioned AWS services will help make a scalable software with the AWS infrastructure in this scenario?

- [ ] AWS Simple Notification Service.
- [x] AWS Simple Queue Service.
- [ ] AWS Elastic Transcoder.
- [ ] AWS Glacier.

**[⬆ Back to Top](#table-of-contents)**

### Using Amazon CloudWatch's Free Tier, what is the frequency of metric updates which you receive?

- [x] 5 minutes.
- [ ] 500 milliseconds.
- [ ] 30 seconds
- [ ] 1 minute.

**[⬆ Back to Top](#table-of-contents)**

### When you resize the Amazon RDS DB instance, Amazon RDS will perform the upgrade during the next maintenance window. If you want the upgrade to be performed now, rather than waiting for the maintenance window, specify the [...] option.

- [ ] Apply Now.
- [ ] Apply Soon.
- [ ] Apply This.
- [x] Apply Immediately.

**[⬆ Back to Top](#table-of-contents)**

### A user is running a webserver on EC2. The user wants to receive the SMS when the EC2 instance utilization is above the threshold limit. Which AWS services should the user configure in this case?

- [ ] AWS CloudWatch + AWS SQS.
- [x] AWS CloudWatch + AWS SNS.
- [ ] AWS CloudWatch + AWS SES.
- [ ] AWS EC2 + AWS Cloudwatch.

**[⬆ Back to Top](#table-of-contents)**

### You're running an application on-premises due to its dependency on non-x86 hardware and want to use AWS for data backup. Your backup application is only able to write to POSIX-compatible block based storage. You have 140TB of data and would like to mount it as a single folder on your file server Users must be able to access portions of this data while the backups are taking place. What backup solution would be most appropriate for this use case?

- [x] Use Storage Gateway and configure it to use Gateway Cached volumes.
- [ ] Configure your backup software to use S3 as the target for your data backups.
- [ ] Configure your backup software to use Glacier as the target for your data backups.
- [ ] Use Storage Gateway and configure it to use Gateway Stored volumes.

**[⬆ Back to Top](#table-of-contents)**

### What happens to Amazon EBS root device volumes, by default, when an instance terminates?

- [ ] Amazon EBS root device volumes are moved to IA
- [x] Amazon EBS root device volumes are copied into Amazon RD
- [ ] Amazon EBS root device volumes are automatically deleted.
- [ ] Amazon EBS root device volumes remain in the database until you delete them.

**[⬆ Back to Top](#table-of-contents)**

### You require the ability to analyze a customer's clickstream data on a website so they can do behavioral analysis. Your customer needs to know what sequence of pages and ads their customer clicked on. This data will be used in real time to modify the page layouts as customers click through the site to increase stickiness and advertising click-through. Which option meets the requirements for captioning and analyzing this data?

- [ ] Log clicks in weblogs by URL store to Amazon S3, and then analyze with Elastic MapReduce.
- [x] Push web clicks by session to Amazon Kinesis and analyze behavior using Kinesis workers.
- [ ] Write click events directly to Amazon Redshift and then analyze with SQL.
- [ ] Publish web clicks by session to an Amazon SQS queue men periodically drain these events to Amazon RDS and analyze with SQL.

**[⬆ Back to Top](#table-of-contents)**

### What happens when you create a topic on Amazon SNS?

- [ ] The topic is created, and it has the name you specified for it.
- [x] An ARN (Amazon Resource Name) is created.
- [ ] You can create a topic on Amazon SQS, not on Amazon SNS.
- [ ] This question doesn't make sense.

**[⬆ Back to Top](#table-of-contents)**

### A company needs to deploy virtual desktops to its customers in a virtual private cloud, leveraging existing security controls. Which set of AWS services and features will meet the company's requirements?

- [ ] Virtual Private Network connection. AWS Directory Services, and Classic link.
- [ ] Virtual Private Network connection. AWS Di rectory Services, and Amazon Workspaces.
- [x] AWS Directory Service, Amazon Workspaces, and AWS Identity and Access Management.
- [ ] Amazon Elastic Compute Cloud, and AWS Identity and Access Management.

**[⬆ Back to Top](#table-of-contents)**

### You are designing a multi-platform web application for AWS The application will run on EC2 instances and will be accessed from PCs. tablets and smart phones Supported accessing platforms are Windows, macOS, iOS and Android Separate sticky session and SSL certificate setups are required for different platform types which of the following describes the most cost effective and performance efficient architecture setup?

- [ ] Setup a hybrid architecture to handle session state and SSL certificates on-prem and separate EC2 Instance groups running web applications for different platform types running in a VPC.
- [ ] Set up one ELB for all platforms to distribute load among multiple instance under it Each EC2 instance implements ail functionality for a particular platform.
- [ ] Set up two ELBs The first ELB handles SSL certificates for all platforms and the second ELB handles session stickiness for all platforms for each ELB run separate EC2 instance groups to handle the web application for each platform.
- [x] Assign multiple ELBS to an EC2 instance or group of EC2 instances running the common components of the web application, one ELB for each platform type Session stickiness and SSLtermination are done at the ELBs.

**[⬆ Back to Top](#table-of-contents)**

### A company is deploying a two-tier, highly available web application to AWS. Which service provides durable storage for static content while utilizing lower Overall CPU resources for the web tier?

- [ ] Amazon EBS volume.
- [x] Amazon S3.
- [ ] Amazon EC2 instance store.
- [ ] Amazon RD5 instance.

**[⬆ Back to Top](#table-of-contents)**

### Select the incorrect statement.

- [ ] In Amazon EC2, the private IP addresses only returned to Amazon EC2 when the instance is stopped or terminated.
- [ ] In Amazon VPC, an instance retains its private IP addresses when the instance is stopped.
- [x] In Amazon VPC, an instance does NOT retain its private IP addresses when the instance is stopped.
- [ ] In Amazon EC2, the private IP address is associated exclusive ly with the instance for its lifetime.

**[⬆ Back to Top](#table-of-contents)**

### An organization has a statutory requirement to protect the data at rest for data stored in EBS volumes. Which of the below mentioned options can the organization use to achieve data protection?

- [ ] Data replication.
- [ ] Data encryption.
- [ ] Data snapshot.
- [x] All the options listed here.

**[⬆ Back to Top](#table-of-contents)**

### A web design company currently runs several FTP servers that their 250 customers use to upload and download large graphic files They wish to move this system to AWS to make it more scalable, butthey wish to maintain customer privacy and Keep costs to a minimum. What AWS architecture would you recommend?

- [x] Ask their customers to use an S3 client instead of an FTP client. Create a single S3 bucket Create an IAM user for each customer Put the IAM Users in a Group that has an IAM policy that permits access to sub-directories within the bucket via use of the 'username' Policy variable.
- [ ] Create a single S3 bucket with Reduced Redundancy Storage turned on and ask their customers to use an S3 client instead of an FTP client Create a bucket for each customer with a Bucket Policy that permits access only to that one customer.
- [ ] Create an auto-scaling group of FTP servers with a scaling policy to automatically scale-in when minimum network traffic on the auto-scaling group is below a given threshold. Load a central list of ftp users from S3 as part of the user Data startup script on each Instance.
- [ ] Create a single S3 bucket with Requester Pays turned on and ask their customers to use an S3 client instead of an FTP client Create a bucket tor each customer with a Bucket Policy that permits access only to that one customer.

**[⬆ Back to Top](#table-of-contents)**

### Amazon RDS DB snapshots and automated backups are stored in:

- [x] Amazon S3.
- [ ] Amazon ECS Volume.
- [ ] Amazon RDS.
- [ ] Amazon EMR.

**[⬆ Back to Top](#table-of-contents)**

### Can Amazon S3 uploads resume on failure or do they need to restart?

- [ ] Restart from beginning.
- [ ] You can resume them, if you flag the 'resume on fai lure' option before uploading.
- [x] Resume on failure.
- [ ] Depends on the file size.

**[⬆ Back to Top](#table-of-contents)**

### Prior to the introduction of this function, the HA feature provided redundancy and performance, but required that a failed/lost group member be [...] reinstated.

- [ ] automatically.
- [ ] periodically.
- [x] manually.
- [ ] continuously.

**[⬆ Back to Top](#table-of-contents)**

### A company has a workflow that sends video files from their on-premise system to AWS for transcoding. They use EC2 worker instances that pull transcoding jobs from SQS. Why is SQS an appropriate service for this scenario?

- [ ] SQS guarantees the order of the messages.
- [ ] SQS synchronously provides transcoding output.
- [ ] SQS checks the health of the worker instances.
- [x] SQS helps to facilitate horizontal scaling of encoding tasks.

**[⬆ Back to Top](#table-of-contents)**

### Which statement below best describes what thresholds you can set to trigger a CloudWatch Alarm?

- [x] Set a target value and choose whether the alarm will trigger when the value is greater than (>), greater than or equal to (>=), less than (<), or less than or equal to (<=) that value.
- [ ] Thresholds need to be set in IAM not CloudWatch.
- [ ] Only default thresholds can be set you can't choose your own thresholds.
- [ ] Set a target value and choose whether the alarm will trigger when the value hits this threshold.

**[⬆ Back to Top](#table-of-contents)**

### You are designing a web application that stores static assets in an Amazon Simple Storage Service (S3) bucket. You expect this bucket to immediately receive over 150 PUT requests per second. What should you do to ensure optimal performance?

- [x] Use multi-part upload.
- [ ] Add a random prefix to the key names.
- [ ] Amazon S3 will automatically manage performance at this scale.
- [ ] Use a predictable naming scheme, such as sequential numbers or date time sequences, in the key names.

**[⬆ Back to Top](#table-of-contents)**

### What does Amazon EC2 provide?

- [x] Virtual servers in the Cloud.
- [ ] A platform to run code (Java, PHP, Python), paying on an hourly basis.
- [ ] Computer Clusters in the Cloud.
- [ ] Physical servers, remotely managed by the customer.

**[⬆ Back to Top](#table-of-contents)**

### A customer has a single 3-TB volume on-premises that is used to hold a large repository of images and print layout files. This repository is growing at 500 GB a year and must be presented as a single logical volume. The customer is becoming increasingly constrained with their local storage capacity and wants an off-site backup of this data, while maintaining low-latency access to their frequently accessed data. Which AWS Storage Gateway configuration meets the customer requirements?

- [ ] Gateway-Cached volumes with snapshots scheduled to Amazon S3.
- [ ] Gateway-Stored volumes with snapshots scheduled to Amazon S3.
- [ ] Gateway-Virtual Tape Library with snapshots to Amazon S3.
- [x] Gateway-Virtual Tape Library with snapshots to Amazon Glacier.

**[⬆ Back to Top](#table-of-contents)**

### You are architecting an auto-scalable batch processing system using video processing pipelines and Amazon Simple Queue Service (Amazon SQS) for a customer. You are unsure of the limitations of SQS and need to find out. What do you think is a correct statement about the limitations of Amazon SQS?

- [ ] It supports an unlimited number of queues but a limited number of messages per queue for each user but automatically deletes messages that have been in the queue for more than 4 weeks.
- [x] It supports an unlimited number of queues and unlimited number of messages per queue for each user but automatically deletes messages that have been in the queue for more than 4 days.
- [ ] It supports an unlimited number of queues but a limited number of messages per queue for each user but automatically deletes messages that have been in the queue for more than 4 days.
- [ ] It supports an unlimited number of queues and unlimited number of messages per queue for each user but automatically deletes messages that have been in the queue for more than 4 weeks.

**[⬆ Back to Top](#table-of-contents)**

### Which Amazon service can I use to define a virtual network that closely resembles a traditional data center?

- [x] Amazon VPC.
- [ ] Amazon Service Bus.
- [ ] Amazon EMR.
- [ ] Amazon RDS.

**[⬆ Back to Top](#table-of-contents)**

### Select the correct set of options. These are the initial settings for the default security group:

- [x] Allow no inbound traffic, Allow all outbound traffic and Allow instances associated with this security group to talk to each other.
- [ ] Allow all inbound traffic, Allow no outbound traffic and Allow instances associated with this security group to talk to each other.
- [ ] Allow no inbound traffic, Allow all outbound traffic and Does NOT allow instances associated with this security group to talk to each other.
- [ ] Al low all inbound traffic, Allow all outbound traffic and Does NOT allow instances associated with this security group to talk to each other.

**[⬆ Back to Top](#table-of-contents)**

### You need to migrate a large amount of data into the cloud that you have stored on a hard disk and you decide that the best way to accomplish this is with AWS Import/Export and you mail the hard disk to AWS. Which of the following statements is incorrect in regards to AWS Import/Export?

- [ ] It can export from Amazon S3.
- [ ] It can Import to Amazon Glacier.
- [x] It can export from Amazon Glacier.
- [ ] It can Import to Amazon EBS.

**[⬆ Back to Top](#table-of-contents)**

### Can I control if and when MySQL based RDS Instance is upgraded to new supported versions?

- [ ] No.
- [ ] Only in VPC.
- [x] Yes.

**[⬆ Back to Top](#table-of-contents)**

### If I have multiple Read Replicas for my master DB Instance and I promote one of them, what happens to the rest of the Read Replicas?

- [x] The remaining Read Replicas will still replicate from the older master DB Instance.
- [ ] The remaining Read Replicas will be deleted.
- [ ] The remaining Read Replicas will be combined to one read replica.

**[⬆ Back to Top](#table-of-contents)**

### A user is running a batch process which runs for 1 hour every day. Which of the below mentioned options is the right instance type and costing model in this case if the user performs the same task for the whole year?

- [x] EBS backed instance with on-demand instance pricing.
- [ ] EBS backed instance with heavy utilized reserved instance pricing.
- [ ] EBS backed instance with low utilized reserved instance pricing.
- [ ] Instance store backed instance with spot instance pricing.

**[⬆ Back to Top](#table-of-contents)**

### You are in the process of building an online gaming site for a client and one of the requirements is that it must be able to process vast amounts of data easily. Which AWS Service would be very helpful in processing all this data?

- [ ] Amazon S3.
- [ ] AWS Data Pipeline.
- [ ] AWS Direct Connect.
- [x] Amazon EMR.

**[⬆ Back to Top](#table-of-contents)**

### Your team has a tomcat-based Java application you need to deploy into development, test and production environments. After some research, you opt to use Elastic Beanstalk due to its tight integration with your developer tools and RDS due to its ease of management. Your QA team lead points out that you need to roll a sanitized set of production data into your environment on a nightly basis. Similarly, other software teams in your org want access to that same restored data via their EC2 instances in your VPC. The optimal setup for persistence and security that meets the above requirements would be the following:

- [x] Create your RDS instance as part of your Elastic Beanstalk definition and alter its security group to allow access to it from hosts in your application subnets.
- [ ] Create your RDS instance separately and add its IP address to your application's DB connection strings in your code Alter its security group to allow access to it from hosts within your VPC's IPaddress block.
- [ ] Create your RDS instance separately and pass its DNS name to your app's DB connection string as an environment variable. Create a security group for client machines and add it as a valid source for DB traffic to the security group of the RDS instance itself.
- [ ] Create your RDS instance separately and pass its DNS name to your's DB connection string as an environment variable Alter its security group to allow access to It from hosts in your application subnets.

**[⬆ Back to Top](#table-of-contents)**

### What are characteristics of Amazon S3? (Choose 2 answers)

- [ ] Amazon S3 allows you to store objects of virtually unlimited size.
- [ ] Amazon S3 offers Provisioned IOP.
- [x] Amazon S3 allows you to store unlimited amounts of data.
- [ ] Amazon S3 should be used to host a relational database.
- [x] Objects are directly accessible via a URL.

**[⬆ Back to Top](#table-of-contents)**

### You need to set up a complex network infrastructure for your organization that will be reasonably easy to deploy, replicate, control, and track changes on. Which AWS service would be best to use to help you accomplish this?

- [ ] AWS Import/Export.
- [x] AWS CloudFormation.
- [ ] Amazon Route 53.
- [ ] Amazon CloudWatch.

**[⬆ Back to Top](#table-of-contents)**

### How should the application use AWS credentials to access the S3 bucket securely?

- [ ] Use the AWS account access Keys the application retrieves the credentials from the source code of the application.
- [ ] Create an IAM user for the application with permissions that allow list access to the S3 bucket launch the instance as the IAM user and retrieve the IAM user's credentials from the EC2 instance user data.
- [x] Create an IAM role for EC2 that allows list access to objects in the S3 bucket. Launch the instance with the role, and retrieve the role's credentials from the EC2 Instance metadata.
- [ ] Create an IAM user for the application with permissions that allow list access to the S3 bucket. The application retrieves the IAM user credentials from a temporary directory with permissions that allow read access only to the application user.

**[⬆ Back to Top](#table-of-contents)**

### You are setting up a VPC and you need to set up a public subnet within that VPC. Which following requirement must be met for this subnet to be considered a public subnet?

- [ ] Subnet's traffic is not routed to an internet gateway but has its traffic routed to a virtual private gateway.
- [x] Subnet's traffic is routed to an internet gateway.
- [ ] Subnet's traffic is not routed to an internet gateway.
- [ ] None of these answers can be considered a public subnet.

**[⬆ Back to Top](#table-of-contents)**

### Is it possible to access your EBS snapshots?

- [ ] Yes, through the Amazon S3 APIs.
- [x] Yes, through the Amazon EC2 APIs.
- [ ] No, EBS snapshots cannot be accessed; they can only be used to create a new EBS volume.
- [ ] EBS doesn't provide snapshots.

**[⬆ Back to Top](#table-of-contents)**

### How many types of block devices does Amazon EC2 support?

- [ ] 4.
- [ ] 5.
- [x] 2.
- [ ] 1.

**[⬆ Back to Top](#table-of-contents)**

### SQL Server [...] store log ins and passwords in the master database.

- [ ] can be configured to but by default does not.
- [ ] doesn't.
- [x] does.

**[⬆ Back to Top](#table-of-contents)**

### You are using an m1.small EC2 Instance with one 300GB EBS volume to host a relational database. You determined that write throughput to the database needs to be increased. Which of the following approaches can help achieve this? (Choose 2 answers)

- [x] Use an array of EBS volumes.
- [ ] Enable Multi-AZ mode.
- [ ] Place the instance in an Auto Scaling Groups.
- [ ] Add an EBS volume and place into RAID 5.
- [x] Increase the size of the EC2 Instance.
- [ ] Put the database behind an Elastic Load Balancer.

**[⬆ Back to Top](#table-of-contents)**

### A user is hosting a website in the US West-1 region. The website has the highest client base from the Asia-Pacific (Singapore / Japan) region. The application is accessing data from S3 before serving it to client. Which of the below mentioned regions gives a better performance for S3 objects?

- [ ] Japan.
- [ ] Singapore.
- [ ] US East.
- [x] US West-1.

**[⬆ Back to Top](#table-of-contents)**

### You need to set up security for your VPC and you know that Amazon VPC provides two features that you can use to increase security for your VPC: Security groups and network access control lists (ACLs). You start to look into security groups first. Which statement below is incorrect in relation to security groups?

- [ ] Are stateful: Return traffic is automatically allowed, regardless of any rules.
- [ ] Evaluate all rules before deciding whether to allow traffic.
- [x] Support allow rules and deny rules.
- [ ] Operate at the instance level (first layer of defense).

**[⬆ Back to Top](#table-of-contents)**

### Can a single EBS volume be attached to multiple EC2 instances at the same time?

- [ ] Yes.
- [x] No.
- [ ] Only for high-performance EBS volumes.
- [ ] Only when the instances are located in the US regions.

**[⬆ Back to Top](#table-of-contents)**

### You are planning and configuring some EBS volumes for an application. in order to get the most performance out of your EBS volumes, you should attach them to an instance with enough [...] to support your volumes.

- [ ] redundancy.
- [ ] storage.
- [x] bandwidth.
- [ ] memory.

**[⬆ Back to Top](#table-of-contents)**

### An organization has three separate AWS accounts, one each for development, testing, and production. The organization wants the testing team to have access to certain AWS resources in the production account. How can the organization achieve this?

- [ ] It is not possible to access resources of one account with another account.
- [x] Create the IAM roles with cross account access.
- [ ] Create the IAM user in a test account, and allow it access to the production environment with the IAM policy.
- [ ] Create the IAM users with cross account access.

**[⬆ Back to Top](#table-of-contents)**

### A benefits enrollment company is hosting a 3-tier web application running in a VPC on AWS which includes a NAT (Network Address Translation) instance in the public Web tier. There is enough provisioned capacity for the expected workload tor the new fiscal year benefit enrollment period plus some extra overhead Enrollment proceeds nicely for two days and then the web tier becomes unresponsive, upon investigation using CloudWatch and other monitoring tools it is discovered that there is an extremely large and unanticipated amount of inbound traffic coming from a set of 15specific IP addresses over port 80 from a country where the benefits company has no customers. The web tier instances are so overloaded that benefit enrollment administrators cannot even SSH into them. Which activity would be useful in defending against this attack?

- [ ] Create a custom route table associated with the web tier and block the attacking IP addresses from the IGW (Internet Gateway).
- [ ] Change the EIP (Elastic IP Address) of the NAT instance in the web tier subnet and update the Main Route Table with the new EIP.
- [ ] Create 15 Security Group rules to block the attacking IP addresses over port 80.
- [x] Create an inbound NACL (Network Access control list) associated with the web tier subnet with deny rules to block the attacking IP addresses.

**[⬆ Back to Top](#table-of-contents)**

### You launch an Amazon EC2 instance without an assigned AVVS identity and Access Management (IAM) role. Later, you decide that the instance should be running with an IAM role. Which action must you take in order to have a running Amazon EC2 instance with an IAM role assigned to it?

- [ ] Create an image of the instance, and register the image with an IAM role assigned and an Amazon EBS volume mapping.
- [ ] Create a new IAM role with the same permissions as an existing IAM role, and assign it to the running instance.
- [ ] Create an image of the instance, add a new IAM role with the same permissions as the desired IAM role, and deregister the image with the new role assigned.
- [x] Create an image of the instance, and use this image to launch a new instance with the desired Lam role assigned.

**[⬆ Back to Top](#table-of-contents)**

### Does AWS Direct Connect allow you access to all Availabilities Zones within a Region?

- [x] Depends on the type of connection.
- [ ] Yes.
- [ ] No.
- [ ] Only when there's just one Availability Zone in a region. If there are more than one, only one availability zone can be accessed directly.

**[⬆ Back to Top](#table-of-contents)**

### What is the durability of S3 RRS?

- [x] 99.99%.
- [ ] 99.95%.
- [ ] 99.995%.
- [ ] 99.999999999%.

**[⬆ Back to Top](#table-of-contents)**

### Your organization is in the business of architecting complex transactional databases. For a variety of reasons, this has been done on EBS. What is AWS's recommendation for customers who have architected databases using EBS for backups?

- [x] Backups to Amazon S3 be performed through the database management system.
- [ ] Backups to AWS Storage Gateway be performed through the database management system.
- [ ] If you take regular snapshots no further backups are required.
- [ ] Backups to Amazon Glacier be performed through the database management system.

**[⬆ Back to Top](#table-of-contents)**

### You need to create a load balancer in a VPC network that you are building. You can make your load balancer internal (private) or internet-facing (public). When you make your load balancer internal, a DNS name will be created, and it will contain the private IP address of the load balancer. An internal load balancer is not exposed to the internet. When you make your load balancer internet-facing, a DNS name will be created with the public IP address. If you want the Internet-facing load balancer to be connected to the Internet, where must this load balancer reside?

- [x] The load balancer must reside in a subnet that is connected to the internet using the internet gateway.
- [ ] The load balancer must reside in a subnet that is not connected to the internet.
- [ ] The load balancer must not reside in a subnet that is connected to the internet.
- [ ] The load balancer must be completely outside of your IP.

**[⬆ Back to Top](#table-of-contents)**

### In the Amazon CloudWatch, which metric should I be checking to ensure that your DB Instance has enough free storage space?

- [ ] Free Storage.
- [x] Free Storage Space.
- [ ] Free Storage Volume.
- [ ] Free DB Storage Space.

**[⬆ Back to Top](#table-of-contents)**

### A web-startup runs its very successful social news application on Amazon EC2 with an Elastic Load Balancer, an Auto-Scaling group of Java/Tomcat application-servers, and DynamoDB as data store. The main web-application best runs on m2 x large instances since it is highly memory- bound Each new deployment requires semi-automated creation and testing of a new AMI for the application servers which takes quite a while ana is therefore only done once per week. Recently, a new chat feature has been implemented in nodejs and wails to be integrated in the architecture. First tests show that the new component is CPU bound Because the company has some experience with using Chef, they decided to streamline the deployment process and use AWS OpsWorks as an application life cycle tool to simplify management of the application and reduce the deployment cycles. What configuration in AWS OpsWorks is necessary to integrate the new chat module in the most cost-efficient and flexible way?

- [ ] Create one AWS OpsWorks stack, create one AWS OpsWorks layer, create one custom recipe.
- [ ] Create one AWS OpsWorks stack create two AWS OpsWorks layers create one custom recipe.
- [x] Create two AWS OpsWorks stacks create two AWS OpsWorks layers create one custom recipe.
- [ ] Create two AWS OpsWorks stacks create two AWS OpsWorks layers create two custom recipe.

**[⬆ Back to Top](#table-of-contents)**

### A client needs you to import some existing infrastructure from a dedicated hosting provider to AWS to try and save on the cost of running his current website. He also needs an automated process that manages backups, software patching, automatic failure detection, and recovery. You are aware that his existing set up currently uses an Oracle database. Which of the following AWS databases would be best for accomplishing this task?

- [x] Amazon RDS.
- [ ] Amazon Redshift.
- [ ] Amazon SimpleDB.
- [ ] Amazon ElastiCache.

**[⬆ Back to Top](#table-of-contents)**

### A user is currently building a website which will require a large number of instances in six months, when a demonstration of the new site will be given upon launch. Which of the below mentioned options allows the user to procure the resources beforehand so that they need not worry about infrastructure availability during the demonstration?

- [x] Procure all the instances as reserved instances beforehand.
- [ ] Launch all the instances as part of the cluster group to ensure resource availability.
- [ ] Pre-warm all the instances one month prior to ensure resource availability.
- [ ] Ask AWS now to procure the dedicated instances in 6 months.

**[⬆ Back to Top](#table-of-contents)**

### Amazon RDS creates an SSL certificate and installs the certificate on the DB Instance when Amazon RDS provisions the instance. These certificates are signed by a certificate authority. The [...] is stored at <https://rds.amazonaws.com/doc/rds-ssl-ca-cert.pem>.

- [x] private key.
- [ ] foreign key.
- [ ] public key.
- [ ] protected key.

**[⬆ Back to Top](#table-of-contents)**

### What happens to data on an ephemeral volume of an EBS-backed EC2 instance if it is terminated or if it fails?

- [ ] Data is automatically copied to another volume.
- [ ] The volume snapshot is saved in S3.
- [ ] Data persists.
- [x] Data is deleted.

**[⬆ Back to Top](#table-of-contents)**

### You manually launch a NAT AMI in a public subnet. The network is properly configured. Security groups and network access control lists are property configured. Instances in a private subnet can access the NAT. The NAT can access the Internet. However, private instances cannot access the Internet. What additional step is required to allow access from the private instances?

- [ ] Enable Source/Destination Check on the private Instances.
- [x] Enable Source/Destination Check on the NAT instance.
- [ ] Disable Source/Destination Check on the private instances.
- [ ] Disable Source/Destination Check on the NAT instance.

**[⬆ Back to Top](#table-of-contents)**

### You have just discovered that you can upload your objects to Amazon S3 using Multipart Upload API. You start to test it out but are unsure of the benefits that it would provide. Which of the following is not a benefit of using multipart uploads?

- [ ] You can begin an upload before you know the final object size.
- [ ] Quick recovery from any network issues.
- [ ] Pause and resume object uploads.
- [x] It's more secure than normal upload.

**[⬆ Back to Top](#table-of-contents)**

### To help you manage your Amazon EC2 instances, images, and other Amazon EC2 resources, you can assign your own metadata to each resource in the form of [...].

- [ ] special filters.
- [ ] functions.
- [x] tags.
- [ ] wildcards.

**[⬆ Back to Top](#table-of-contents)**

### Do the Amazon EBS volumes persist independently from the running life of an Amazon EC2 instance?

- [ ] No.
- [ ] Only if instructed to when created.
- [x] Yes.

**[⬆ Back to Top](#table-of-contents)**

### If I write the below command, what does it do? ec2-run ami-e3a5408a -n 20 -g appserver

- [x] Start twenty instances as members of appserver group.
- [ ] Creates 20 rules in the security group named appserver.
- [ ] Terminate twenty instances as members of appserver group.
- [ ] Start 20 security groups.

**[⬆ Back to Top](#table-of-contents)**

### A company is deploying a new two-tier web application in AWS. The company has limited staff and requires high availability, and the application requires complex queries and table joins. Which configuration provides the solution for the company's requirements?

- [ ] MySQL Installed on two Amazon EC2 Instances in a single Availability Zone.
- [x] Amazon RDS for MySQL with Multi-AZ.
- [ ] Amazon ElastiCache
- [ ] Amazon DynamoDB.

**[⬆ Back to Top](#table-of-contents)**

### In order to optimize performance for a compute cluster that requires low inter-node latency, which of the following feature should you use?

- [ ] Multiple Availability Zones.
- [ ] AWS Direct Connect.
- [ ] EC2 Dedicated Instances.
- [x] Placement Groups.
- [ ] VPC private subnets.

**[⬆ Back to Top](#table-of-contents)**

### Regarding the attaching of ENI to an instance, what does 'warm attach' refer to?

- [x] Attaching an ENI to an instance when it is stopped.
- [ ] This question doesn't make sense.
- [ ] Attaching an ENI to an instance when it is running.
- [ ] Attaching an ENI to an instance during the launch process.

**[⬆ Back to Top](#table-of-contents)**

### Can I attach more than one policy to a particular entity?

- [x] Yes always.
- [ ] Only if within GovCloud.
- [ ] No.
- [ ] Only if within VPC.

**[⬆ Back to Top](#table-of-contents)**

### By default, when an EBS volume is attached to a Windows instance, it may show up as any drive letter on the instance. You can change the settings of the [...] Service to set the drive letters of the EBS volumes per your specifications.

- [ ] EBS Config Service.
- [ ] AMI Config Service.
- [x] EC2 Config Service.
- [ ] EC2-AMI Config Service.

**[⬆ Back to Top](#table-of-contents)**

### Select the correct set of steps for exposing the snapshot only to specific AWS accounts.

- [ ] Select public for all the accounts and check mark t hose accounts with whom you want to expose the snapshots and cl ick save.
- [ ] Select Private, enter the IDs of t hose AWS accounts, and click Save.
- [x] Select Public, enter the IDs of those AWS accounts, and click Save.
- [ ] Select Public, mark the IDs of those AWS accounts as private, and click Save.

**[⬆ Back to Top](#table-of-contents)**

### How can you apply more than 100 rules to an Amazon EC2-Classic?

- [ ] By adding more security groups.
- [ ] You need to create a default security group specifying your required rules if you need to use more than 100 rules per security group.
- [ ] By default the Amazon EC2 security groups support 500 rules.
- [x] You can't add more than 100 rules to security groups for an Amazon EC2 instance.

**[⬆ Back to Top](#table-of-contents)**

### A user has created an ELB with Auto Scaling. Which of the below mentioned offerings from ELB helps the user to stop sending new requests traffic from the load balancer to the EC2 instance when the instance is being deregistered while continuing in-flight requests?

- [ ] ELB sticky session.
- [ ] ELB deregistration check.
- [ ] ELB auto registration Off.
- [x] ELB connection draining.

**[⬆ Back to Top](#table-of-contents)**

### What can I access by visiting the URL: http://status.aws.amazon.com/?

- [ ] Amazon Cloud Watch.
- [ ] Status of the Amazon RDS DB.
- [x] AWS Service Health Dashboard.
- [ ] AWS Cloud Monitor.

**[⬆ Back to Top](#table-of-contents)**

### In Route 53, what does a Hosted Zone refer to?

- [ ] A hosted zone is a collection of geographical load balancing rules for Route 53.
- [x] A hosted zone is a collection of resource record sets hosted by Route 53.
- [ ] A hosted zone is a selection of specific resource record sets hosted by CloudFront for distribution to Route 53.
- [ ] A hosted zone is the Edge Location that hosts the Route 53 records for a user.

**[⬆ Back to Top](#table-of-contents)**

### A user is launching an EC2 instance in the US East region. Which of the below mentioned options is recommended by AWS with respect to the selection of the Availability Zone?

- [ ] Always select the AZ while launching an instance.
- [ ] Always select the US-East-1-a zone for HA.
- [x] Do not select the AZ; instead let AWS select the AZ.
- [ ] The user can never select the Availability Zone while launching an instance.

**[⬆ Back to Top](#table-of-contents)**

### ec2-revoke RevokeSecurityGroup Ingress

- [ ] Removes one or more security groups from a rule.
- [ ] Removes one or more security groups from an Amazon EC2 instance.
- [x] Removes one or more rules from a security group.
- [ ] Removes a security group from our account.

**[⬆ Back to Top](#table-of-contents)**

### Select the correct statement.

- [ ] You don't need not specify the resource identifier while stopping a resource.
- [ ] You can terminate, stop, or delete a resource based solely on its tags.
- [x] You can't terminate, stop, or delete a resource based solely on its tags.
- [ ] You don't need to specify the resource identifier while terminating a resource.

**[⬆ Back to Top](#table-of-contents)**

### What is the time period with which metric data is sent to CloudWatch when detailed monitoring is enabled on an Amazon EC2 instance?

- [ ] 15 minutes.
- [ ] 5 minutes.
- [x] 1 minute.
- [ ] 45 seconds.

**[⬆ Back to Top](#table-of-contents)**

### A large real -estate brokerage is exploring the option of adding a cost-effective location based alert to their existing mobile application The application backend infrastructure currently runs on AWS Users who opt in to this service will receive alerts on their mobile device regarding real-estate otters in proximity to their location. For the alerts to be relevant delivery time needs to be in the low minute count the existing mobile app has 5 million users across the us. Which one of the following architectural suggestions would you make to the customer?

- [x] The mobile application will submit its location to a web service endpoint utilizing Elastic Load Balancing and EC2 instances: DynamoDB will be used to store and retrieve relevant otters EC2 instances will communicate with mobile earners/device providers to push alerts back to mobile application.
- [ ] Use AWS DirectConnect or VPN to establish connectivity with mobile carriers EC2 instances will receive the mobile applications' location through carrier connection: ROS will be used to store and relevant relevant offers EC2 instances will communicate with mobile carriers to push alerts back to the mobile application.
- [ ] The mobile application will send device location using SQS.
- [ ] EC2 instances will retrieve the re levant others from DynamoDB AWS Mobile Push will be used to send offers to the mobile application to push alerts back to the mobile application.
- [ ] The mobile application will send device location using AWS Mobile Push EC2 instances will retrieve the relevant offers from DynamoDB EC2 instances will communicate with mobile carriers/device providers to push alerts back to the mobile application.

**[⬆ Back to Top](#table-of-contents)**

### You are running PostgreSQL on Amazon RDS and it seems to be all running smoothly deployed in one Availability Zone. A database administrator asks you if DB instances running PostgreSQL support Multi-AZ deployments. What would be a correct response to this question?

- [x] Yes.
- [ ] Yes but only for small db instances.
- [ ] No.
- [ ] Yes but you need to request the service from AWS.

**[⬆ Back to Top](#table-of-contents)**

### What is the data model of DynamoDB?

- [ ] Since DynamoDB is schema-less, there is no data model.
- [ ] 'Items', with Keys and one or more Attribute; and 'Attribute', with Name and Value.
- [x] 'Table', a collection of Items; 'Items', with Keys and one or more Attribute; and 'Attribute', with Name and Value.
- [ ] 'Database', which is a set of 'Tables', which is a set of 'Items', which is a set of 'Attributes'.

**[⬆ Back to Top](#table-of-contents)**

### What is a placement group in Amazon EC2?

- [x] It is a group of EC2 instances within a single Availability Zone.
- [ ] It the edge location of your web content.
- [ ] It is the AWS region where you run the EC2 instance of your web content.
- [ ] It is a group used to span multiple Availability Zones.

**[⬆ Back to Top](#table-of-contents)**

### A company is running an SMB file server in its data center. The file server stores large files that are accessed frequently for the first few days after the files are created. After 7 days the files are rarely accessed. The total data size is increasing and is close to the company's total storage capacity. A solutions architect must increase the company's available storage space without losing low-latency access to the most recently accessed files. The solutions architect must also provide file lifecycle management to avoid future storage issues.Which solution will meet these requirements?

- [ ] Use AWS DataSync to copy data that is older than 7 days from the SMB file server to AWS.
- [ ] Create an Amazon S3 File Gateway to extend the company's storage space. Create an S3 Lifecycle policy to transition the data to S3 Glacier Deep Archive after 7 days.
- [ ] Create an Amazon FSx for Windows File Server file system to extend the company's storage space.
- [x] Install a utility on each user's computer to access Amazon S3. Create an S3 Lifecycle policy to transition the data to S3 Glacier Flexible Retrieval after 7 days.

**[⬆ Back to Top](#table-of-contents)**

### A large company wants to provide its globally located developers separate, limited size, managed PostgreSQL databases for development purposes. The databases will be low volume. The developers need the databases only when they are actively working.Which solution will meet these requirements MOST cost-effectively?

- [ ] Give the developers the ability to launch separate Amazon Aurora instances. Set up a process to shut down Aurora instances at the end of the workday and to start Aurora instances at the beginning of the next workday.
- [ ] Develop an AWS Service Catalog product that enforces size restrictions for launching Amazon Aurora instances. Give the developers access to launch the product when they need a development database.
- [x] Create an Amazon Aurora Serverless cluster. Develop an AWS Service Catalog product to launch databases in the cluster with the default capacity settings. Grant the developers access to the product.
- [ ] Monitor AWS Trusted Advisor checks for idle Amazon RDS databases. Create a process to terminate identified idle RDS databases.

**[⬆ Back to Top](#table-of-contents)**

### A company is building a web application that serves a content management system. The content management system runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The EC2 instances run in an Auto Scaling group across multiple Availability Zones. Users are constantly adding and updating files, blogs, and other website assets in the content management system. A solutions architect must implement a solution in which all the EC2 instances share up-to-date website content with the least possible lag time. Which solution meets these requirements?

- [ ] Update the EC2 user data in the Auto Scaling group lifecycle policy to copy the website assets from the EC2 instance that was launched most recently. Configure the ALB to make changes to the website assets only in the newest EC2 instance.
- [x] Copy the website assets to an Amazon Elastic File System (Amazon EFS) file system. Configure each EC2 instance to mount the EFS file system locally. Configure the website hosting application to reference the website assets that are stored in the EFS file system.
- [ ] Copy the website assets to an Amazon S3 bucket. Ensure that each EC2 instance downloads the website assets from the S3 bucket to the attached Amazon Elastic Block Store (Amazon EBS) volume. Run the S3 sync command once each hour to keep files up to date.
- [ ] Restore an Amazon Elastic Block Store (Amazon EBS) snapshot with the website assets. Attach the EBS snapshot as a secondary EBS volume when a new EC2 instance is launched. Configure the website hosting application to reference the website assets that are stored in the secondary EBS volume.

**[⬆ Back to Top](#table-of-contents)**

### A company's web application consists of multiple Amazon EC2 instances that run behind an Application Load Balancer in a VPC. An Amazon RDS for MySQL DB instance contains the data. The company needs the ability to automatically detect and respond to suspicious or unexpected behavior in its AWS environment. The company already has added AWS WAF to its architecture. What should a solutions architect do next to protect against threats?

- [x] Use Amazon GuardDuty to perform threat detection. Configure Amazon EventBridge (Amazon CloudWatch Events) to filter for GuardDuty findings and to invoke an AWS Lambda function to adjust the AWS WAF rules.
- [ ] Use AWS Firewall Manager to perform threat detection. Configure Amazon EventBridge (Amazon CloudWatch Events) to filter for Firewall Manager findings and to invoke an AWS Lambda function to adjust the AWS WAF web ACL.
- [ ] Use Amazon Inspector to perform threat detection and to update the AWS WAF rules. Create a VPC network ACL to limit access to the web application.
- [ ] Use Amazon Macie to perform threat detection and to update the AWS WAF rules. Create a VPC network ACL to limit access to the web application.

**[⬆ Back to Top](#table-of-contents)**

### A company is planning to run a group of Amazon EC2 instances that connect to an Amazon Aurora database. The company has built an AWS CloudFormation template to deploy the EC2 instances and the Aurora DB cluster. The company wants to allow the instances to authenticate to the database in a secure way. The company does not want to maintain static database credentials. Which solution meets these requirements with the LEAST operational effort?

- [ ] Create a database user with a user name and password. Add parameters for the database user name and password to the CloudFormation template. Pass the parameters to the EC2 instances when the instances are launched.
- [ ] Create a database user with a user name and password. Store the user name and password in AWS Systems Manager Parameter Store. Configure the EC2 instances to retrieve the database credentials from Parameter Store.
- [x] Configure the DB cluster to use IAM database authentication. Create a database user to use with IAM authentication. Associate a role with the EC2 instances to allow applications on the instances to access the database.
- [ ] Configure the DB cluster to use IAM database authentication with an IAM user. Create a database user that has a name that matches the IAM user. Associate the IAM user with the EC2 instances to allow applications on the instances to access the database.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to configure its Amazon CloudFront distribution to use SSL/TLS certificates. The company does not want to use the default domain name for the distribution. Instead, the company wants to use a different domain name for the distribution. Which solution will deploy the certificate without incurring any additional costs?

- [ ] Request an Amazon issued private certificate from AWS Certificate Manager (ACM) in the us-east-1 Region.
- [ ] Request an Amazon issued private certificate from AWS Certificate Manager (ACM) in the us-west-1 Region.
- [x] Request an Amazon issued public certificate from AWS Certificate Manager (ACM) in the us-east-1 Region.
- [ ] Request an Amazon issued public certificate from AWS Certificate Manager (ACM) in the us-west-1 Region.

**[⬆ Back to Top](#table-of-contents)**

### A company creates operations data and stores the data in an Amazon S3 bucket. For the company's annual audit, an external consultant needs to access an annual report that is stored in the S3 bucket. The external consultant needs to access the report for 7 days. The company must implement a solution to allow the external consultant access to only the report. Which solution will meet these requirements with the MOST operational efficiency?

- [ ] Create a new S3 bucket that is configured to host a public static website. Migrate the operations data to the new S3 bucket. Share the S3 website URL with the external consultant.
- [ ] Enable public access to the S3 bucket for 7 days. Remove access to the S3 bucket when the external consultant completes the audit.
- [ ] Create a new IAM user that has access to the report in the S3 bucket. Provide the access keys to the external consultant. Revoke the access keys after 7 days.
- [x] Generate a presigned URL that has the required access to the location of the report on the S3 bucket. Share the presigned URL with the external consultant.

**[⬆ Back to Top](#table-of-contents)**

### A company plans to run a high performance computing (HPC) workload on Amazon EC2 Instances. The workload requires low-latency network performance and high network throughput with tightly coupled node-to-node communication. Which solution will meet these requirements?

- [x] Configure the EC2 instances to be part of a cluster placement group.
- [ ] Launch the EC2 instances with Dedicated Instance tenancy.
- [ ] Launch the EC2 instances as Spot Instances.
- [ ] Configure an On-Demand Capacity Reservation when the EC2 instances are launched.

**[⬆ Back to Top](#table-of-contents)**

### A company has primary and secondary data centers that are 500 miles (804.7 km) apart and interconnected with high-speed fiber-optic cable. The company needs a highly available and secure network connection between its data centers and a VPC on AWS for a mission-critical workload. A solutions architect must choose a connection solution that provides maximum resiliency. Which solution meets these requirements?

- [ ] Two AWS Direct Connect connections from the primary data center terminating at two Direct Connect locations on two separate devices.
- [ ] A single AWS Direct Connect connection from each of the primary and secondary data centers terminating at one Direct Connect location on the same device.
- [x] Two AWS Direct Connect connections from each of the primary and secondary data centers terminating at two Direct Connect locations on two separate devices.
- [ ] A single AWS Direct Connect connection from each of the primary and secondary data centers terminating at one Direct Connect location on two separate devices.

**[⬆ Back to Top](#table-of-contents)**

### A company runs several Amazon RDS for Oracle On-Demand DB instances that have high utilization. The RDS DB instances run in member accounts that are in an organization in AWS Organizations. The company's finance team has access to the organization's management account and member accounts. The finance team wants to find ways to optimize costs by using AWS Trusted Advisor. Which combination of steps will meet these requirements? (Choose two.)

- [x] Use the Trusted Advisor recommendations in the management account.
- [ ] Use the Trusted Advisor recommendations in the member accounts where the RDS DB instances are running.
- [x] Review the Trusted Advisor checks for Amazon RDS Reserved Instance Optimization.
- [ ] Review the Trusted Advisor checks for Amazon RDS Idle DB Instances.
- [ ] Review the Trusted Advisor checks for compute optimization. Crosscheck the results by using AWS Compute Optimizer.

**[⬆ Back to Top](#table-of-contents)**

### A solutions architect is creating an application. The application will run on Amazon EC2 instances in private subnets across multiple Availability Zones in a VPC. The EC2 instances will frequently access large files that contain confidential information. These files are stored in Amazon S3 buckets for processing. The solutions architect must optimize the network architecture to minimize data transfer costs. What should the solutions architect do to meet these requirements?

- [x] Create a gateway endpoint for Amazon S3 in the VPC. In the route tables for the private subnets, add an entry for the gateway endpoint.
- [ ] Create a single NAT gateway in a public subnet. In the route tables for the private subnets, add a default route that points to the NAT gateway.
- [ ] Create an AWS PrivateLink interface endpoint for Amazon S3 in the VPC. In the route tables for the private subnets, add an entry for the interface endpoint.
- [ ] Create one NAT gateway for each Availability Zone in public subnets. In each of the route tables for the private subnets, add a default route that points to the NAT gateway in the same Availability Zone.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to relocate its on-premises MySQL database to AWS. The database accepts regular imports from a client-facing application, which causes a high volume of write operations. The company is concerned that the amount of traffic might be causing performance issues within the application. How should a solutions architect design the architecture on AWS?

- [x] Provision an Amazon RDS for MySQL DB instance with Provisioned IOPS SSD storage. Monitor write operation metrics by using Amazon CloudWatch. Adjust the provisioned IOPS if necessary.
- [ ] Provision an Amazon RDS for MySQL DB instance with General Purpose SSD storage. Place an Amazon ElastiCache cluster in front of the DB instance. Configure the application to query ElastiCache instead.
- [ ] Provision an Amazon DocumentDB (with MongoDB compatibility) instance with a memory optimized instance type. Monitor Amazon CloudWatch for performance-related issues. Change the instance class if necessary.
- [ ] Provision an Amazon Elastic File System (Amazon EFS) file system in General Purpose performance mode. Monitor Amazon CloudWatch for IOPS bottlenecks. Change to Provisioned Throughput performance mode if necessary.

**[⬆ Back to Top](#table-of-contents)**

### A company runs an application in the AWS Cloud that generates sensitive archival data files. The company wants to rearchitect the application's data storage. The company wants to encrypt the data files and to ensure that third parties do not have access to the data before the data is encrypted and sent to AWS. The company has already created an Amazon S3 bucket. Which solution will meet these requirements?

- [ ] Configure the S3 bucket to use client-side encryption with an Amazon S3 managed encryption key. Configure the application to use the S3 bucket to store the archival files.
- [ ] Configure the S3 bucket to use server-side encryption with AWS KMS keys (SSE-KMS). Configure the application to use the S3 bucket to store the archival files.
- [ ] Configure the S3 bucket to use dual-layer server-side encryption with AWS KMS keys (SSE-KMS). Configure the application to use the S3 bucket to store the archival files.
- [x] Configure the application to use client-side encryption with a key stored in AWS Key Management Service (AWS KMS). Configure the application to store the archival files in the S3 bucket.

**[⬆ Back to Top](#table-of-contents)**

### A company uses Amazon RDS with default backup settings for its database tier. The company needs to make a daily backup of the database to meet regulatory requirements. The company must retain the backups for 30 days. Which solution will meet these requirements with the LEAST operational overhead?

- [ ] Write an AWS Lambda function to create an RDS snapshot every day.
- [x] Modify the RDS database to have a retention period of 30 days for automated backups.
- [ ] Use AWS Systems Manager Maintenance Windows to modify the RDS backup retention period.
- [ ] Create a manual snapshot every day by using the AWS CLI. Modify the RDS backup retention period.

**[⬆ Back to Top](#table-of-contents)**

### A company is running a multi-tier web application on AWS. The application runs its database tier on Amazon Aurora MySQL. The application and database tiers are in the us-east-1 Region. A database administrator who regularly monitors the Aurora DB cluster finds that an intermittent increase in read traffic is creating high CPUutilization on the read replica and causing increased read latency of the application. What should a solutions architect do to improve read scalability?

- [ ] Reboot the Aurora DB cluster.
- [ ] Create a cross-Region read replica
- [ ] Increase the instance class of the read replica.
- [x] Configure Aurora Auto Scaling for the read replica.

**[⬆ Back to Top](#table-of-contents)**

### A company that runs its application on AWS uses an Amazon Aurora DB cluster as its database. During peak usage hours when multiple users access and read the data, the monitoring system shoes degradation of database performancefor write queries. The company wants to increase the scalability of the application to meet peak usage demands. Which solution will meet these requirements MOST cost effectively?

- [ ] Create a second Aurora DB cluster. Configure a copy job to replicate the users' data to the new database. Update the application to use the second database to read the data.
- [ ] Create an Amazon DynamoDB Accelerator (DAX) cluster in front of the existing Aurora DB cluster. Update the application to use the DAX cluster for read-only queries. Write data directly to the Aurora DB cluster.
- [x] Create an Aurora read replica in the existing Aurora DB clu ster. Update tyhe applicatio nto uyser the replica endpoint for read only queries and to use the cluster endpoint for write queries.
- [ ] Create an Amazon Redshift cluster. Copy the users' data to the Redshift cluster. Update the application to connect to the Redshift cluster and to perform read-only queries on the Redshift cluster.

**[⬆ Back to Top](#table-of-contents)**

### A company's near-real-time streaming application is running on AWS. As the data is ingested, a job runs on the data and takes 30 minutes to complete. The workload frequently experiences high latency due to large amounts of incoming data. A solutions architect needs to design a scalable and serverless solution to enhance performance. Which combination of steps should the solutions architect take? (Choose two.)

- [x] Use Amazon Kinesis Data Firehose to ingest the data.
- [ ] Use AWS Lambda with AWS Step Functions to process the data.
- [ ] Use AWS Database Migration Service (AWS DMS) to ingest the data.
- [ ] Use Amazon EC2 instances in an Auto Scaling group to process the data.
- [x] Use AWS Fargate with Amazon Elastic Container Service (Amazon ECS) to process the data.

**[⬆ Back to Top](#table-of-contents)**

### A company runs a web application on multiple Amazon EC2 instances in a VPC. The application needs to write sensitive data to an Amazon S3 bucket. The data cannot be sent over the public internet. Which solution will meet these requirements?

- [x] Create a gateway VPC endpoint for Amazon S3. Create a route in the VPC route table to the endpoint.
- [ ] Create an internal Network Load Balancer that has the S3 bucket as the target.
- [ ] Deploy the S3 bucket inside the VPC. Create a route in the VPC route table to the bucket.
- [ ] Create an AWS Direct Connect connection between the VPC and an S3 regional endpoint.

**[⬆ Back to Top](#table-of-contents)**

### A company runs its production workload on Amazon EC2 instances with Amazon Elastic Block Store (Amazon EBS) volumes. A solutions architect needs to analyze the current EBS volume cost and to recommend optimizations. The recommendations need to include estimated monthly saving opportunities. Which solution will meet these requirements?

- [ ] Use Amazon Inspector reporting to generate EBS volume recommendations for optimization.
- [ ] Use AWS Systems Manager reporting to determine EBS volume recommendations for optimization.
- [ ] Use Amazon CloudWatch metrics reporting to determine EBS volume recommendations for optimization.
- [x] Use AWS Compute Optimizer to generate EBS volume recommendations for optimization.

**[⬆ Back to Top](#table-of-contents)**

### A global company runs its workloads on AWS. The company's application uses Amazon S3 buckets across AWS Regions for sensitive data storage and analysis. The company stores millions of objects in multiple S3 buckets daily. The company wants to identify all S3 buckets that are not versioning-enabled. Which solution will meet these requirements?

- [ ] Use AWS Config managed rule to identify S3 bucket that is not version controlled
- [x] Use Amazon S3 Storage Lens to identify all S3 buckets that are not versioning-enabled across Regions.
- [ ] Enable IAM Access Analyzer for S3 to identify all S3 buckets that are not versioning-enabled across Regions.
- [ ] Create an S3 Multi-Region Access Point to identify all S3 buckets that are not versioning-enabled across Regions.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to enhance its ecommerce order-processing application that is deployed on AWS. The application must process each order exactly once without affecting the customer experience during unpredictable traffic surges. Which solution will meet these requirements?

- [x] Create an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Put all the orders in the SQS queue. Configure an AWS Lambda function as the target to process the orders.
- [ ] Create an Amazon Simple Notification Service (Amazon SNS) standard topic. Publish all the orders to the SNS standard topic. Configure the application as a notification target.
- [ ] Create a flow by using Amazon AppFlow. Send the orders to the flow. Configure an AWS Lambda function as the target to process the orders.
- [ ] Configure AWS X-Ray in the application to track the order requests. Configure the application to process the orders by pulling the orders from Amazon CloudWatch.

**[⬆ Back to Top](#table-of-contents)**

### A company has two AWS accounts: Production and Development. There are code changes ready in the Development account to push to the Production account. In the alpha phase, only two senior developers on the development team need access to the Production account. In the beta phase, more developers might need access to perform testing as well. What should a solutions architect recommend?

- [ ] Create two policy documents using the AWS Management Console in each account. Assign the policy to developers who need access.
- [ ] Create an IAM role in the Development account. Give one IAM role access to the Production account. Allow developers to assume the role.
- [x] Create an IAM role in the Production account with the trust policy that specifies the Development account. Allow developers to assume the role.
- [ ] Create an IAM group in the Production account and add it as a principal in the trust policy that specifies the Production account. Add developers to the group.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to restrict access to the content of its web application. The company needs to protect the content by using authorization techniques that are available on AWS. The company also wants to implement a serverless architecture for authorization and authentication that has low login latency. The solution must integrate with the web application and serve web content globally. The application currently has a small user base, but the company expects the application's user base to increase. Which solution will meet these requirements?

- [x] Configure Amazon Cognito for authentication. Implement Lambda@Edge for authorization. Configure Amazon CloudFront to serve the web application globally.
- [ ] Configure AWS Directory Service for Microsoft Active Directory for authentication. Implement AWS Lambda for authorization. Use an Application Load Balancer to serve the web application globally.
- [ ] Configure Amazon Cognito for authentication. Implement AWS Lambda for authorization. Use Amazon S3 Transfer Acceleration to serve the web application globally.
- [ ] Configure AWS Directory Service for Microsoft Active Directory for authentication. Implement Lambda@Edge for authorization. Use AWS Elastic Beanstalk to serve the web application globally.

**[⬆ Back to Top](#table-of-contents)**

### A development team uses multiple AWS accounts for its development, Staging, and production environments Team members have been launching large Amazon EC2 instances that are underutilized. A solutions architect must prevent large instances from being launched in all accounts. How can the solutions architect meet this requirement with the LEAST operational overhead?

- [ ] Update the IAM policies to deny the launch of large EC2 instances. Apply the policies to all users
- [ ] Define a resource in AWS Resource Access Manager that prevents the launch of large EC2 instances.
- [ ] Create an IAM role in each account that denies the launch of large EC2 instances. Grant the developers IAM group access to the role.
- [x] Create an orgainization in AWS Organizations in the managment account with the default policy. Create a Service control prolicy that denies the launch of large  EC2 instances and apply to all aws accounts.

**[⬆ Back to Top](#table-of-contents)**

### A company has migrated a fleet of hundreds of on-premises virtual machines (VMs) to Amazon EC2 instances. The instances run a diverse fleet of Windows Server versions along with several Linux distributions. The company wants a solution that will automate inventory and updates of the operating systems. The company also needs a summary of common vulnerabilities of each instance for regular monthly reviews. What should a solutions architect recommend to meet these requirements?

- [ ] Set up AWS Systems Manager Patch Manager to manage all the EC2 instances. Configure AWS Security Hub to produce monthly reports.
- [x] Set up AWS Systems Manager Patch Manager to manage all the EC2 instances. Deploy Amazon Inspector, and configure monthly reports.
- [ ] Set up AWS Shield Advanced, and configure monthly reports. Deploy AWS Config to automate patch installations on the EC2 instances.
- [ ] Set up Amazon GuardDuty in the account to monitor all EC2 instances. Deploy AWS Config to automate patch installations on the EC2 instances.

**[⬆ Back to Top](#table-of-contents)**

### A company hosts its application in the AWS Cloud. The application runs on Amazon EC2 instances behind an Elastic Load Balancer in an Auto Scaling group and with an Amazon DynamoDB table. The company wants to ensure the application can be made available in another AWS Region with minimal downtime. What should a solutions architect do to meet these requirements with the LEAST amount of downtime?

- [x] Create an Auto Scaling group and a load balancer in the disaster recovery Region. Configure the DynamoDB table as a global table. Configure DNS failover to point to the new disaster recovery Region's load balancer.
- [ ] Create an AWS CloudFormation template to create EC2 instances, load balancers, and DynamoDB tables to be executed when needed. Configure DNS failover to point to the new disaster recovery Region's load balancer.
- [ ] Create an AWS CloudFormation template to create EC2 instances and a load balancer to be executed when needed. Configure the DynamoDB table as a global table. Configure DNS failover to point to the new disaster recovery Region's load balancer.
- [ ] Create an Auto Scaling group and load balancer in the disaster recovery Region. Configure the DynamoDB table as a global table. Create an Amazon CloudWatch alarm to trigger and AWS Lambda function that updates Amazon Route 53 pointing to the disaster recovery load balancer.

**[⬆ Back to Top](#table-of-contents)**

### A company runs an application on Amazon EC2 instances in a private subnet. The application needs to store and retrieve data in Amazon S3 buckets. According to regulatory requirements, the data must not travel across the public internet. What should a solutions architect do to meet these requirements MOST cost-effectively?

- [ ] Deploy a NAT gateway to access the S3 buckets.
- [ ] Deploy AWS Storage Gateway to access the S3 buckets.
- [ ] Deploy an S3 interface endpoint to access the S3 buckets.
- [x] Deploy an S3 gateway endpoint to access the S3 buckets.

**[⬆ Back to Top](#table-of-contents)**

### A company hosts an application on Amazon EC2 instances that run in a single Availability Zone. The application is accessible by using the transport layer of the Open Systems Interconnection (OSI) model. The company needs the application architecture to have high availability. Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

- [ ] Configure new EC2 instances in a different Availability Zone. Use Amazon Route 53 to route traffic to all instances.
- [x] Configure a Network Load Balancer in front of the EC2 instances.
- [ ] Configure a Network Load Balancer for TCP traffic to the instances. Configure an Application Load Balancer for HTTP and HTTPS traffic to the instances.
- [x] Create an Auto Scaling group for the EC2 instances. Configure the Auto Scaling group to use multiple Availability Zones. Configure the Auto Scaling group to run application health checks on the instances.
- [ ] Create an Amazon CloudWatch alarm. Configure the alarm to restart EC2 instances that transition to a stopped state.

**[⬆ Back to Top](#table-of-contents)**

### A company hosts its static website by using Amazon S3. The company wants to add a contact form to its webpage. The contact form will have dynamic server-side components for users to input their name, email address, phone number, and user message. The company anticipates that there will be fewer than 100 site visits each month. Which solution will meet these requirements MOST cost-effectively?

- [ ] Host the dynamic contact form in Amazon Elastic Container Service (Amazon ECS). Set up Amazon Simple Email Service (Amazon SES) to connect to a third-party email provider.
- [x] Create an Amazon API Gateway endpoint that returns the contact form from an AWS Lambda function. Configure another Lambda function on the API Gateway to publish a message to an Amazon Simple Notification Service (Amazon SNS) topic.
- [ ] Host the website by using AWS Amplify Hosting for static content and dynamic content. Use server-side scripting to build the contact form. Configure Amazon Simple Queue Service (Amazon SQS) to deliver the message to the company.
- [ ] Migrate the website from Amazon S3 to Amazon EC2 instances that run Windows Server. Use Internet Information Services (IIS) for Windows Server to host the webpage. Use client-side scripting to build the contact form. Integrate the form with Amazon WorkMail.

**[⬆ Back to Top](#table-of-contents)**

### A company uses AWS Organizations to create dedicated AWS accounts for each business unit to manage each business unit's account independently upon request. The root email recipient missed a notification that was sent to the root user email address of one account. The company wants to ensure that all future notifications are not missed. Future notifications must be limited to account administrators.Which solution will meet these requirements?

- [ ] Configure the company's email server to forward notification email messages that are sent to the AWS account root user email address to all users in the organization.
- [x] Configure all AWS account root user email addresses as distribution lists that go to a few administrators who can respond to alerts. Configure AWS account alternate contacts in the AWS Organizations console or programmatically.
- [ ] Configure all AWS account root user email messages to be sent to one administrator who is responsible for monitoring alerts and forwarding those alerts to the appropriate groups.
- [ ] Configure all existing AWS accounts and all newly created accounts to use the same root user email address. Configure AWS account alternate contacts in the AWS Organizations console or programmatically.

**[⬆ Back to Top](#table-of-contents)**

### A company runs an ecommerce application on AWS. Amazon EC2 instances process purchases and store the purchase details in an Amazon Aurora PostgreSQL DB cluster. Customers are experiencing application timeouts during times of peak usage. A solutions architect needs to rearchitect the application so that the application can scale to meet peak usage demands. Which combination of actions will meet these requirements MOST cost-effectively? (Choose two.)

- [x] Configure an Auto Scaling group of new EC2 instances to retry the purchases until the processing is complete. Update the applications to connect to the DB cluster by using Amazon RDS Proxy.
- [ ] Configure the application to use an Amazon ElastiCache cluster in front of the Aurora PostgreSQL DB cluster.
- [x] Update the application to send the purchase requests to an Amazon Simple Queue Service (Amazon SQS) queue. Configure an Auto Scaling group of new EC2 instances that read from the SQS queue.
- [ ] Configure an AWS Lambda function to retry the ticket purchases until the processing is complete.
- [ ] Configure an Amazon AP! Gateway REST API with a usage plan.

**[⬆ Back to Top](#table-of-contents)**

### A company that uses AWS Organizations runs 150 applications across 30 different AWS accounts. The company used AWS Cost and Usage Report to create a new report in the management account. The report is delivered to an Amazon S3 bucket that is replicated to a bucket in the data collection account. The company's senior leadership wants to view a custom dashboard that provides NAT gateway costs each day starting at the beginning of the current month. Which solution will meet these requirements?

- [ ] Share an Amazon QuickSight dashboard that includes the requested table visual. Configure QuickSight to use AWS DataSync to query the new report.
- [x] Share an Amazon QuickSight dashboard that includes the requested table visual. Configure QuickSight to use Amazon Athena to query the new report.
- [ ] Share an Amazon CloudWatch dashboard that includes the requested table visual. Configure CloudWatch to use AWS DataSync to query the new report.
- [ ] Share an Amazon CloudWatch dashboard that includes the requested table visual. Configure CloudWatch to use Amazon Athena to query the new report.

**[⬆ Back to Top](#table-of-contents)**

### A company is hosting a high-traffic static website on Amazon S3 with an Amazon CloudFront distribution that has a default TTL of 0 seconds. The company wants to implement caching to improve performance for the website. However, the company also wants to ensure that stale content is not served for more than a few minutes after a deployment. Which combination of caching methods should a solutions architect implement to meet these requirements? (Choose two.)

- [x] Set the CloudFront default TTL to 2 minutes.
- [ ] Set a default TTL of 2 minutes on the S3 bucket.
- [ ] Add a Cache-Control private directive to the objects in Amazon S3.
- [ ] Create an AWS Lambda@Edge function to add an Expires header to HTTP responses. Configure the function to run on viewer response.
- [x] Add a Cache-Control max-age directive of 24 hours to the objects in Amazon S3. On deployment, create a CloudFront invalidation to clear any changed files from edge caches.

**[⬆ Back to Top](#table-of-contents)**

### A company uses Amazon EC2 instances and AWS Lambda functions to run its application. The company has VPCs with public subnets and private subnets in its AWS account. The EC2 instances run in a private subnet in one of the VPCs. The Lambda functions need direct network access to the EC2 instances for the application to work. The application will run for at least 1 year. The company expects the number of Lambda functions that the application uses to increase during that time. The company wants to maximize its savings on all application resources and to keep network latency between the services low. Which solution will meet these requirements?

- [ ] Purchase an EC2 Instance Savings Plan Optimize the Lambda functions' duration and memory usage and the number of invocations. Connect the Lambda functions to the private subnet that contains the EC2 instances.
- [ ] Purchase an EC2 Instance Savings Plan Optimize the Lambda functions' duration and memory usage, the number of invocations, and the amount of data that is transferred. Connect the Lambda functions to a public subnet in the same VPC where the EC2 instances run.
- [x] Purchase a Compute Savings Plan. Optimize the Lambda functions' duration and memory usage, the number of invocations, and the amount of data that is transferred. Connect the Lambda functions to the private subnet that contains the EC2 instances.
- [ ] Purchase a Compute Savings Plan. Optimize the Lambda functions' duration and memory usage, the number of invocations, and the amount of data that is transferred. Keep the Lambda functions in the Lambda service VPC.

**[⬆ Back to Top](#table-of-contents)**

### A company hosts a data lake on AWS. The data lake consists of data in Amazon S3 and Amazon RDS for PostgreSQL. The company needs a reporting solution that provides data visualization and includes all the data sources within the data lake. Only the company's management team should have full access to all the visualizations. The rest of the company should have only limited access. Which solution will meet these requirements?

- [x] Create an analysis in Amazon QuickSight. Connect all the data sources and create new datasets. Publish dashboards to visualize the data. Share the dashboards with the appropriate IAM roles.
- [ ] Create an analysis in Amazon QuickSight. Connect all the data sources and create new datasets. Publish dashboards to visualize the data. Share the dashboards with the appropriate users and groups.
- [ ] Create an AWS Glue table and crawler for the data in Amazon S3. Create an AWS Glue extract, transform, and load (ETL) job to produce reports. Publish the reports to Amazon S3. Use S3 bucket policies to limit access to the reports.
- [ ] Create an AWS Glue table and crawler for the data in Amazon S3. Use Amazon Athena Federated Query to access data within Amazon RDS for PostgreSQL. Generate reports by using Amazon Athena. Publish the reports to Amazon S3. Use S3 bucket policies to limit access to the reports.

**[⬆ Back to Top](#table-of-contents)**

### A company runs an ecommerce application on Amazon EC2 instances behind an Application Load Balancer. The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. The Auto Scaling group scales based on CPU utilization metrics. The ecommerce application stores the transaction data in a MySQL 8.0 database that is hosted on a large EC2 instance. The database's performance degrades quickly as application load increases. The application handles more read requests than write transactions. The company wants a solution that will automatically scale the database to meet the demand of unpredictable read workloads while maintaining high availability. Which solution will meet these requirements?

- [ ] Use Amazon Redshift with a single node for leader and compute functionality.
- [ ] Use Amazon RDS with a Single-AZ deployment Configure Amazon RDS to add reader instances in a different Availability Zone.
- [x] Use Amazon Aurora with a Multi-AZ deployment. Configure Aurora Auto Scaling with Aurora Replicas.
- [ ] Use Amazon ElastiCache for Memcached with EC2 Spot Instances.

**[⬆ Back to Top](#table-of-contents)**

### A company has an application that ingests incoming messages. Dozens of other applications and microservices then quickly consume these messages. The number of messages varies drastically and sometimes increases suddenly to 100,000 each second. The company wants to decouple the solution and increase scalability. Which solution meets these requirements?

- [ ] Persist the messages to Amazon Kinesis Data Analytics. Configure the consumer applications to read and process the messages.
- [ ] Deploy the ingestion application on Amazon EC2 instances in an Auto Scaling group to scale the number of EC2 instances based on CPU metrics.
- [ ] Write the messages to Amazon Kinesis Data Streams with a single shard. Use an AWS Lambda function to preprocess messages and store them in Amazon DynamoDB. Configure the consumer applications to read from DynamoDB to process the messages.
- [x] Publish the messages to an Amazon Simple Notification Service (Amazon SNS) topic with multiple Amazon Simple Queue Service (Amazon SOS) subscriptions. Configure the consumer applications to process the messages from the queues.

**[⬆ Back to Top](#table-of-contents)**

### An application development team is designing a microservice that will convert large images to smaller, compressed images. When a user uploads an image through the web interface, the microservice should store the image in an Amazon S3 bucket, process and compress the image with an AWS Lambda function, and store the image in its compressed form in a different S3 bucket. A solutions architect needs to design a solution that uses durable, stateless components to process the images automatically. Which combination of actions will meet these requirements? (Choose two.)

- [x] Create an Amazon Simple Queue Service (Amazon SQS) queue. Configure the S3 bucket to send a notification to the SQS queue when an image is uploaded to the S3 bucket.
- [x] Configure the Lambda function to use the Amazon Simple Queue Service (Amazon SQS) queue as the invocation source. When the SQS message is successfully processed, delete the message in the queue.
- [ ] Configure the Lambda function to monitor the S3 bucket for new uploads. When an uploaded image is detected, write the file name to a text file in memory and use the text file to keep track of the images that were processed.
- [ ] Launch an Amazon EC2 instance to monitor an Amazon Simple Queue Service (Amazon SQS) queue. When items are added to the queue, log the file name in a text file on the EC2 instance and invoke the Lambda function.
- [ ] Configure an Amazon EventBridge (Amazon CloudWatch Events) event to monitor the S3 bucket. When an image is uploaded, send an alert to an Amazon ample Notification Service (Amazon SNS) topic with the application owner's email address for further processing.

**[⬆ Back to Top](#table-of-contents)**

### A company has a three-tier web application that is deployed on AWS. The web servers are deployed in a public subnet in a VPC. The application servers and database servers are deployed in private subnets in the same VPC. The company has deployed a third-party virtual firewall appliance from AWS Marketplace in an inspection VPC. The appliance is configured with an IP interface that can accept IP packets. A solutions architect needs to integrate the web application with the appliance to inspect all traffic to the application before the traffic reaches the web server. Which solution will meet these requirements with the LEAST operational overhead?

- [ ] Create a Network Load Balancer in the public subnet of the application's VPC to route the traffic to the appliance for packet inspection.
- [ ] Create an Application Load Balancer in the public subnet of the application's VPC to route the traffic to the appliance for packet inspection.
- [ ] Deploy a transit gateway in the inspection VPConfigure route tables to route the incoming packets through the transit gateway.
- [x] Deploy a Gateway Load Balancer in the inspection VPC. Create a Gateway Load Balancer endpoint to receive the incoming packets and forward the packets to the appliance.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to improve its ability to clone large amounts of production data into a test environment in the same AWS Region. The data is stored in Amazon EC2 instances on Amazon Elastic Block Store (Amazon EBS) volumes. Modifications to the cloned data must not affect the production environment. The software that accesses this data requires consistently high I/O performance. A solutions architect needs to minimize the time that is required to clone the production data into the test environment. Which solution will meet these requirements?

- [ ] Take EBS snapshots of the production EBS volumes. Restore the snapshots onto EC2 instance store volumes in the test environment.
- [ ] Configure the production EBS volumes to use the EBS Multi-Attach feature. Take EBS snapshots of the production EBS volumes. Attach the production EBS volumes to the EC2 instances in the test environment.
- [ ] Take EBS snapshots of the production EBS volumes. Create and initialize new EBS volumes. Attach the new EBS volumes to EC2 instances in the test environment before restoring the volumes from the production EBS snapshots.
- [x] Take EBS snapshots of the production EBS volumes. Turn on the EBS fast snapshot restore feature on the EBS snapshots. Restore the snapshots into new EBS volumes. Attach the new EBS volumes to EC2 instances in the test environment.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company wants to launch a one-deal-a-day website on AWS. Each day will feature exactly one product on sale for a period of 24 hours. The company wants to be able to handle millions of requests each hour with millisecond latency during peak hours. Which solution will meet these requirements with the LEAST operational overhead?

- [ ] Use Amazon S3 to host the full website in different S3 buckets. Add Amazon CloudFront distributions. Set the S3 buckets as origins for the distributions. Store the order data in Amazon S3.
- [ ] Deploy the full website on Amazon EC2 instances that run in Auto Scaling groups across multiple Availability Zones. Add an Application Load Balancer (ALB) to distribute the website traffic. Add another ALB for the backend APIs. Store the data in Amazon RDS for MySQL.
- [ ] Migrate the full application to run in containers. Host the containers on Amazon Elastic Kubernetes Service (Amazon EKS). Use the Kubernetes Cluster Autoscaler to increase and decrease the number of pods to process bursts in traffic. Store the data in Amazon RDS for MySQL.
- [x] Use an Amazon S3 bucket to host the website's static content. Deploy an Amazon CloudFront distribution. Set the S3 bucket as the origin. Use Amazon API Gateway and AWS Lambda functions for the backend APIs. Store the data in Amazon DynamoDB.

**[⬆ Back to Top](#table-of-contents)**

### A solutions architect is using Amazon S3 to design the storage architecture of a new digital media application. The media files must be resilient to the loss of an Availability Zone. Some files are accessed frequently while other files are rarely accessed in an unpredictable pattern. The solutions architect must minimize the costs of storing and retrieving the media files. Which storage option meets these requirements?

- [ ] S3 Standard.
- [x] S3 Intelligent-Tiering.
- [ ] S3 Standard-Infrequent Access (S3 Standard-IA).
- [ ] S3 One Zone-Infrequent Access (S3 One Zone-IA).

**[⬆ Back to Top](#table-of-contents)**

### A company is storing backup files by using Amazon S3 Standard storage. The files are accessed frequently for 1 month. However, the files are not accessed after 1 month. The company must keep the files indefinitely. Which storage solution will meet these requirements MOST cost-effectively?

- [ ] Configure S3 Intelligent-Tiering to automatically migrate objects.
- [x] Create an S3 Lifecycle configuration to transition objects from S3 Standard to S3 Glacier Deep Archive after 1 month.
- [ ] Create an S3 Lifecycle configuration to transition objects from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) after 1 month.
- [ ] Create an S3 Lifecycle configuration to transition objects from S3 Standard to S3 One Zone-Infrequent Access (S3 One Zone-IA) after 1 month.

**[⬆ Back to Top](#table-of-contents)**

### A company observes an increase in Amazon EC2 costs in its most recent bill. The billing team notices unwanted vertical scaling of instance types for a couple of EC2 instances. A solutions architect needs to create a graph comparing the last 2 months of EC2 costs and perform an in-depth analysis to identify the root cause of the vertical scaling. How should the solutions architect generate the information with the LEAST operational overhead?

- [ ] Use AWS Budgets to create a budget report and compare EC2 costs based on instance types.
- [x] Use Cost Explorer's granular filtering feature to perform an in-depth analysis of EC2 costs based on instance types.
- [ ] Use graphs from the AWS Billing and Cost Management dashboard to compare EC2 costs based on instance types for the last 2 months.
- [ ] Use AWS Cost and Usage Reports to create a report and send it to an Amazon S3 bucket. Use Amazon QuickSight with Amazon S3 as a source to generate an interactive graph based on instance types.

**[⬆ Back to Top](#table-of-contents)**

### A company is designing an application. The application uses an AWS Lambda function to receive information through Amazon API Gateway and to store the information in an Amazon Aurora PostgreSQL database. During the proof-of-concept stage, the company has to increase the Lambda quotas significantly to handle the high volumes of data that the company needs to load into the database. A solutions architect must recommend a new design to improve scalability and minimize the configuration effort. Which solution will meet these requirements?

- [ ] Refactor the Lambda function code to Apache Tomcat code that runs on Amazon EC2 instances. Connect the database by using native Java Database Connectivity (JDBC) drivers.
- [ ] Change the platform from Aurora to Amazon DynamoDProvision a DynamoDB Accelerator (DAX) cluster. Use the DAX client SDK to point the existing DynamoDB API calls at the DAX cluster.
- [ ] Set up two Lambda functions. Configure one function to receive the information. Configure the other function to load the information into the database. Integrate the Lambda functions by using Amazon Simple Notification
- [x] Set up two Lambda functions. Configure one function to receive the information. Configure the other function to load the information into the database. Integrate the Lambda functions by using an Amazon Simple Queue Service (Amazon SQS) queue.

**[⬆ Back to Top](#table-of-contents)**

### A company needs to review its AWS Cloud deployment to ensure that its Amazon S3 buckets do not have unauthorized configuration changes. What should a solutions architect do to accomplish this goal?

- [x] Turn on AWS Config with the appropriate rules.
- [ ] Turn on AWS Trusted Advisor with the appropriate checks.
- [ ] Turn on Amazon Inspector with the appropriate assessment template.
- [ ] Turn on Amazon S3 server access logging. Configure Amazon EventBridge (Amazon Cloud Watch Events).

**[⬆ Back to Top](#table-of-contents)**

### A company is launching a new application and will display application metrics on an Amazon CloudWatch dashboard. The company's product manager needs to access this dashboard periodically. The product manager does not have an AWS account. A solutions architect must provide access to the product manager by following the principle of least privilege. Which solution will meet these requirements?

- [x] Share the dashboard from the CloudWatch console. Enter the product manager's email address, and complete the sharing steps. Provide a shareable link for the dashboard to the product manager.
- [ ] Create an IAM user specifically for the product manager. Attach the CloudWatchReadOnlyAccess AWS managed policy to the user. Share the new login credentials with the product manager. Share the browser URL of the correct dashboard with the product manager.
- [ ] Create an IAM user for the company's employees. Attach the ViewOnlyAccess AWS managed policy to the IAM user. Share the new login credentials with the product manager. Ask the product manager to navigate to the CloudWatch console and locate the dashboard by name in the Dashboards section.
- [ ] Deploy a bastion server in a public subnet. When the product manager requires access to the dashboard, start the server and share the RDP credentials. On the bastion server, ensure that the browser is configured to open the dashboard URL with cached AWS credentials that have appropriate permissions to view the dashboard.

**[⬆ Back to Top](#table-of-contents)**

### A company is migrating applications to AWS. The applications are deployed in different accounts. The company manages the accounts centrally by using AWS Organizations. The company's security team needs a single sign-on (SSO) solution across all the company's accounts. The company must continue managing the users and groups in its on-premises self-managed Microsoft Active Directory. Which solution will meet these requirements?

- [ ] Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a one-way forest trust or a one-way domain trust to connect the company's self-managed Microsoft Active Directory with AWS SSO by using AWS Directory Service for Microsoft Active Directory.
- [x] Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a two-way forest trust to connect the company's self-managed Microsoft Active Directory with AWS SSO by using AWS Directory Service for Microsoft Active Directory.
- [ ] Use AWS Directory Service. Create a two-way trust relationship with the company's self-managed Microsoft Active Directory.
- [ ] Deploy an identity provider (IdP) on premises. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console.

**[⬆ Back to Top](#table-of-contents)**

### A company provides a Voice over Internet Protocol (VoIP) service that uses UDP connections. The service consists of Amazon EC2 instances that run in an Auto Scaling group. The company has deployments across multiple AWS Regions. The company needs to route users to the Region with the lowest latency. The company also needs automated failover between Regions. Which solution will meet these requirements?

- [x] Deploy a Network Load Balancer (NLB) and an associated target group. Associate the target group with the Auto Scaling group. Use the NLB as an AWS Global Accelerator endpoint in each Region.
- [ ] Deploy an Application Load Balancer (ALB) and an associated target group. Associate the target group with the Auto Scaling group. Use the ALB as an AWS Global Accelerator endpoint in each Region.
- [ ] Deploy a Network Load Balancer (NLB) and an associated target group. Associate the target group with the Auto Scaling group. Create an Amazon Route 53 latency record that points to aliases for each NLB. Create an Amazon CloudFront distribution that uses the latency record as an origin.
- [ ] Deploy an Application Load Balancer (ALB) and an associated target group. Associate the target group with the Auto Scaling group. Create an Amazon Route 53 weighted record that points to aliases for each ALB. Deploy an Amazon CloudFront distribution that uses the weighted record as an origin.

**[⬆ Back to Top](#table-of-contents)**

### A development team runs monthly resource-intensive tests on its general purpose Amazon RDS for MySQL DB instance with Performance Insights enabled. The testing lasts for 48 hours once a month and is the only process that uses the database. The team wants to reduce the cost of running the tests without reducing the compute and memory attributes of the DB instance. Which solution meets these requirements MOST cost-effectively?

- [ ] Stop the DB instance when tests are completed. Restart the DB instance when required.
- [ ] Use an Auto Scaling policy with the DB instance to automatically scale when tests are completed.
- [x] Create a snapshot when tests are completed. Terminate the DB instance and restore the snapshot when required.
- [ ] Modify the DB instance to a low-capacity instance when tests are completed. Modify the DB instance again when required.

**[⬆ Back to Top](#table-of-contents)**

### A company that hosts its web application on AWS wants to ensure all Amazon EC2 instances, Amazon RDS DB instances, and Amazon Redshift clusters are configured with tags. The company wants to minimize the effort of configuring and operating this check. What should a solutions architect do to accomplish this?

- [x] Use AWS Config rules to define and detect resources that are not properly tagged.
- [ ] Use Cost Explorer to display resources that are not properly tagged. Tag those resources manually.
- [ ] Write API calls to check all resources for proper tag allocation. Periodically run the code on an EC2 instance.
- [ ] Write API calls to check all resources for proper tag allocation. Schedule an AWS Lambda function through Amazon CloudWatch to periodically run the code.

**[⬆ Back to Top](#table-of-contents)**

### A company runs an online marketplace web application on AWS. The application serves hundreds of thousands of users during peak hours. The company needs a scalable, near-real-time solution to share the details of millions of financial transactions with several other internal applications. Transactions also need to be processed to remove sensitive data before being stored in a document database for low-latency retrieval. What should a solutions architect recommend to meet these requirements?

- [ ] Store the transactions data into Amazon DynamoDB. Set up a rule in DynamoDB to remove sensitive data from every transaction upon write. Use DynamoDB Streams to share the transactions data with other applications.
- [ ] Stream the transactions data into Amazon Kinesis Data Firehose to store data in Amazon DynamoDB and Amazon S3. Use AWS Lambda integration with Kinesis Data Firehose to remove sensitive data. Other applications can consume the data stored in Amazon S3.
- [x] Stream the transactions data into Amazon Kinesis Data Streams. Use AWS Lambda integration to remove sensitive data from every transaction and then store the transactions data in AmazonDynamoDB. Other applications can consume the transactions data off the Kinesis data stream.
- [ ] Store the batched transactions data in Amazon S3 as files. Use AWS Lambda to process every file and remove sensitive data before updating the files in Amazon S3. The Lambda function then stores the data in Amazon DynamoDB. Other applications can consume transaction files stored in Amazon S3.

**[⬆ Back to Top](#table-of-contents)**

### A company is preparing to launch a public-facing web application in the AWS Cloud. The architecture consists of Amazon EC2 instances within a VPC behind an Elastic Load Balancer (ELB). A third-party service is used for the DNS. The company's solutions architect must recommend a solution to detect and protect against large-scale DDoS attacks. Which solution meets these requirements?

- [ ] Enable Amazon GuardDuty on the account.
- [ ] Enable Amazon Inspector on the EC2 instances.
- [ ] Enable AWS Shield and assign Amazon Route 53 to it.
- [x] Enable AWS Shield Advanced and assign the ELB to it.

**[⬆ Back to Top](#table-of-contents)**

### A company is building an application in the AWS Cloud. The application will store data in Amazon S3 buckets in two AWS Regions. The company must use an AWS Key Management Service (AWS KMS) customer managed key to encrypt all data that is stored in the S3 buckets. The data in both S3 buckets must be encrypted and decrypted with the same KMS key. The data and the key must be stored in each of the two Regions. Which solution will meet these requirements with the LEAST operational overhead?

- [ ] Create an S3 bucket in each Region. Configure the S3 buckets to use server-side encryption with Amazon S3 managed encryption keys (SSE-S3). Configure replication between the S3 buckets.
- [x] Create a customer managed multi-Region KMS key. Create an S3 bucket in each Region. Configure replication between the S3 buckets. Configure the application to use the KMS key with client-side encryption.
- [ ] Create a customer managed KMS key and an S3 bucket in each Region. Configure the S3 buckets to use server-side encryption with Amazon S3 managed encryption keys (SSE-S3). Configure replication between the S3 buckets.
- [ ] Create a customer managed KMS key and an S3 bucket in each Region. Configure the S3 buckets to use server-side encryption with AWS KMS keys (SSE-KMS). Configure replication between the S3 buckets.

**[⬆ Back to Top](#table-of-contents)**

### A company recently launched a variety of new workloads on Amazon EC2 instances in its AWS account. The company needs to create a strategy to access and administer the instances remotely and securely. The company needs to implement a repeatable process that works with native AWS services and follows the AWS Well-Architected Framework. Which solution will meet these requirements with the LEAST operational overhead?

- [ ] Use the EC2 serial console to directly access the terminal interface of each instance for administration.
- [x] Attach the appropriate IAM role to each existing instance and new instance. Use AWS Systems Manager Session Manager to establish a remote SSH session.
- [ ] Create an administrative SSH key pair. Load the public key into each EC2 instance. Deploy a bastion host in a public subnet to provide a tunnel for administration of each instance.
- [ ] Establish an AWS Site-to-Site VPN connection. Instruct administrators to use their local on-premises machines to connect directly to the instances by using SSH keys across the VPN tunnel.

**[⬆ Back to Top](#table-of-contents)**

### A development team needs to host a website that will be accessed by other teams. The website contents consist of HTML, CSS, client-side JavaScript, and images. Which method is the MOST cost-effective for hosting the website?

- [ ] Containerize the website and host it in AWS Fargate.
- [x] Create an Amazon S3 bucket and host the website there.
- [ ] Deploy a web server on an Amazon EC2 instance to host the website.
- [ ] Configure an Application Load Balancer with an AWS Lambda target that uses the Express.js framework.

**[⬆ Back to Top](#table-of-contents)**

### A company has a production workload that runs on 1,000 Amazon EC2 Linux instances. The workload is powered by third-party software. The company needs to patch the third-party software on all EC2 instances as quickly as possible to remediate a critical security vulnerability. What should a solutions architect do to meet these requirements?

- [ ] Create an AWS Lambda function to apply the patch to all EC2 instances.
- [ ] Configure AWS Systems Manager Patch Manager to apply the patch to all EC2 instances.
- [ ] Schedule an AWS Systems Manager maintenance window to apply the patch to all EC2 instances.
- [x] Use AWS Systems Manager Run Command to run a custom command that applies the patch to all EC2 instances.

**[⬆ Back to Top](#table-of-contents)**

### A company uses Amazon RDS for PostgreSQL databases for its data tier. The company must implement password rotation for the databases. Which solution meets this requirement with the LEAST operational overhead?

- [x] Store the password in AWS Secrets Manager. Enable automatic rotation on the secret.
- [ ] Store the password in AWS Systems Manager Parameter Store. Enable automatic rotation on the parameter.
- [ ] Store the password in AWS Systems Manager Parameter Store. Write an AWS Lambda function that rotates the password.
- [ ] Store the password in AWS Key Management Service (AWS KMS). Enable automatic rotation on the customer master key (CMK).

**[⬆ Back to Top](#table-of-contents)**

### A company runs its application on Oracle Database Enterprise Edition. The company needs to migrate the application and the database to AWS. The company can use the Bring Your Own License (BYOL) model while migrating to AWS. The application uses third-party database features that require privileged access. A solutions architect must design a solution for the database migration. Which solution will meet these requirements MOST cost-effectively?

- [ ] Migrate the database to Amazon RDS for Oracle by using native tools. Replace the third-party features with AWS Lambda.
- [x] Migrate the database to Amazon RDS Custom for Oracle by using native tools. Customize the new database settings to support the third-party features.
- [ ] Migrate the database to Amazon DynamoDB by using AWS Database Migration Service (AWS DMS). Customize the new database settings to support the third-party features.
- [ ] Migrate the database to Amazon RDS for PostgreSQL by using AWS Database Migration Service (AWS DMS). Rewrite the application code to remove the dependency on third-party features.

**[⬆ Back to Top](#table-of-contents)**

### A company has deployed a multi-account strategy on AWS by using AWS Control Tower. The company has provided individual AWS accounts to each of its developers. The company wants to implement controls to limit AWS resource costs that the developers incur. Which solution will meet these requirements with the LEAST operational overhead?

- [ ] Instruct each developer to tag all their resources with a tag that has a key of CostCenter and a value of the developer's name. Use the required-tags AWS Config managed rule to check for the tag. Create an AWS Lambda function to terminate resources that do not have the tag. Configure AWS Cost Explorer to send a daily report to each developer to monitor their spending.
- [x] Use AWS Budgets to establish budgets for each developer account. Set up budget alerts for actual and forecast values to notify developers when they exceed or expect to exceed their assigned budget. Use AWS Budgets actions to apply a DenyAll policy to the developer's IAM role to prevent additional resources from being launched when the assigned budget is reached.
- [ ] Use AWS Cost Explorer to monitor and report on costs for each developer account. Configure Cost Explorer to send a daily report to each developer to monitor their spending. Use AWS Cost Anomaly Detection to detect anomalous spending and provide alerts.
- [ ] Use AWS Service Catalog to allow developers to launch resources within a limited cost range. Create AWS Lambda functions in each AWS account to stop running resources at the end of each work day. Configure the Lambda functions to resume the resources at the start of each work day.

**[⬆ Back to Top](#table-of-contents)**

### A solutions architect is designing an application that will allow business users to upload objects to Amazon S3. The solution needs to maximize object durability. Objects also must be readily available at any time and for any length of time. Users will access objects frequently within the first 30 days after the objects are uploaded, but users are much less likely to access objects that are older than 30 days. Which solution meets these requirements MOST cost-effectively?

- [ ] Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Glacier after 30 days.
- [x] Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.
- [ ] Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 One Zone-Infrequent Access (S3 One Zone-IA) after 30 days.
- [ ] Store all the objects in S3 Intelligent-Tiering with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.

**[⬆ Back to Top](#table-of-contents)**

### A solutions architect is designing a three-tier web application. The architecture consists of an internet-facing Application Load Balancer (ALB) and a web tier that is hosted on Amazon EC2 instances in private subnets. The application tier with the business logic runs on EC2 instances in private subnets. The database tier consists of Microsoft SQL Server that runs on EC2 instances in private subnets. Security is a high priority for the company. Which combination of security group congurations should the solutions architect use? (Choose three.)

- [x] Configure the security group for the web tier to allow inbound HTTPS traffic from the security group for the ALB.
- [ ] Configure the security group for the web tier to allow outbound HTTPS traffic to 0.0.0.0/0.
- [x] Configure the security group for the database tier to allow inbound Microsoft SQL Server traffic from the security group for the application tier.
- [ ] Configure the security group for the database tier to allow outbound HTTPS traffic and Microsoft SQL Server trac to the security group for the web tier.
- [x] Configure the security group for the application tier to allow inbound HTTPS traffic from the security group for the web tier.
- [ ] Configure the security group for the application tier to allow outbound HTTPS traffic and Microsoft SQL Server traffic to the security group for the web tier.

**[⬆ Back to Top](#table-of-contents)**

### A company has released a new version of its production application. The company's workload uses Amazon EC2, AWS Lambda, AWS Fargate, and Amazon SageMaker. The company wants to cost optimize the workload now that usage is at a steady state. The company wants to cover the most services with the fewest savings plans. Which combination of savings plans will meet these requirements? (Choose two.)

- [ ] Purchase an EC2 Instance Savings Plan for Amazon EC2 and SageMaker.
- [ ] Purchase a Compute Savings Plan for Amazon EC2, Lambda, and SageMaker.
- [x] Purchase a SageMaker Savings Plan.
- [x] Purchase a Compute Savings Plan for Lambda, Fargate, and Amazon EC2.
- [ ] Purchase an EC2 Instance Savings Plan for Amazon EC2 and Fargate.

**[⬆ Back to Top](#table-of-contents)**

### A company uses a Microsoft SQL Server database. The company's applications are connected to the database. The company wants to migrate to an Amazon Aurora PostgreSQL database with minimal changes to the application code. Which combination of steps will meet these requirements? (Choose two.)

- [ ] Use the AWS Schema Conversion Tool (AWS SCT) to rewrite the SQL queries in the applications.
- [x] Enable Babelfish on Aurora PostgreSQL to run the SQL queries from the applications.
- [x] Migrate the database schema and data by using the AWS Schema Conversion Tool (AWS SCT) and AWS Database Migration Service (AWS DMS).
- [ ] Use Amazon RDS Proxy to connect the applications to Aurora PostgreSQL.
- [ ] Use AWS Database Migration Service (AWS DMS) to rewrite the SQL queries in the applications.

**[⬆ Back to Top](#table-of-contents)**

### A company plans to rehost an application to Amazon EC2 instances that use Amazon Elastic Block Store (Amazon EBS) as the attached storage. A solutions architect must design a solution to ensure that all newly created Amazon EBS volumes are encrypted by default. The solution must also prevent the creation of unencrypted EBS volumes. Which solution will meet these requirements?

- [ ] Configure the EC2 account attributes to always encrypt new EBS volumes.
- [x] Use AWS Config. Configure the encrypted-volumes identifier. Apply the default AWS Key Management Service (AWS KMS) key.
- [ ] Configure AWS Systems Manager to create encrypted copies of the EBS volumes. Reconfigure the EC2 instances to use the encrypted volumes.
- [ ] Create a customer managed key in AWS Key Management Service (AWS KMS). Configure AWS Migration Hub to use the key when the company migrates workloads.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company wants to collect user clickstream data from the company's website for real-time analysis. The website experiences fluctuating traffic patterns throughout the day. The company needs a scalable solution that can adapt to varying levels of traffic. Which solution will meet these requirements?

- [x] Use a data stream in Amazon Kinesis Data Streams in on-demand mode to capture the clickstream data. Use AWS Lambda to process the data in real time.
- [ ] Use Amazon Kinesis Data Firehose to capture the clickstream data. Use AWS Glue to process the data in real time.
- [ ] Use Amazon Kinesis Video Streams to capture the clickstream data. Use AWS Glue to process the data in real time.
- [ ] Use Amazon Managed Service for Apache Flink (previously known as Amazon Kinesis Data Analytics) to capture the clickstream data. Use AWS Lambda to process the data in real time

**[⬆ Back to Top](#table-of-contents)**

### A global company runs its workloads on AWS. The company's application uses Amazon S3 buckets across AWS Regions for sensitive data storage and analysis. The company stores millions of objects in multiple S3 buckets daily. The company wants to identify all S3 buckets that are not versioning-enable- [ ]  Which solution will meet these requirements?

- [ ] Set up an AWS CloudTrail event that has a rule to identify all S3 buckets that are not versioning-enabled across Regions.
- [x] Use Amazon S3 Storage Lens to identify all S3 buckets that are not versioning-enabled across Regions.
- [ ] Enable IAM Access Analyzer for S3 to identify all S3 buckets that are not versioning-enabled across Regions.
- [ ] Create an S3 Multi-Region Access Point to identify all S3 buckets that are not versioning-enabled across Regions.

**[⬆ Back to Top](#table-of-contents)**

### A company's infrastructure consists of hundreds of Amazon EC2 instances that use Amazon Elastic Block Store (Amazon EBS) storage. A solutions architect must ensure that every EC2 instance can be recovered after a disaster. What should the solutions architect do to meet this requirement with the LEAST amount of effort?

- [ ] Take a snapshot of the EBS storage that is attached to each EC2 instance. Create an AWS CloudFormation template to launch new EC2
instances from the EBS storage.
- [ ] Take a snapshot of the EBS storage that is attached to each EC2 instance. Use AWS Elastic Beanstalk to set the environment based on the
EC2 template and attach the EBS storage.
- [x] Use AWS Backup to set up a backup plan for the entire group of EC2 instances. Use the AWS Backup API or the AWS CLI to speed up the
restore process for multiple EC2 instances.
- [ ] Create an AWS Lambda function to take a snapshot of the EBS storage that is attached to each EC2 instance and copy the Amazon
Machine Images (AMIs). Create another Lambda function to perform the restores with the copied AMIs and attach the EBS storage.

**[⬆ Back to Top](#table-of-contents)**

### A company recently migrated to the AWS Clou- [ ]  The company wants a serverless solution for large-scale parallel on-demand processing of asemistructured dataset. The data consists of logs, media files, sales transactions, and IoT sensor data that is stored in Amazon S3. The company wants the solution to process thousands of items in the dataset in parallel. Which solution will meet these requirements with the MOST operational efficiency?

- [ ]  Use the AWS Step Functions Map state in Inline mode to process the data in parallel.
- [x]  Use the AWS Step Functions Map state in Distributed mode to process the data in parallel.
- [ ]  Use AWS Glue to process the data in parallel.
- [ ]  Use several AWS Lambda functions to process the data in parallel.
  
**[⬆ Back to Top](#table-of-contents)**

### A company will migrate 10 PB of data to Amazon S3 in 6 weeks. The current data center has a 500 Mbps uplink to the internet. Other on-premises applications share the uplink. The company can use 80% of the internet bandwidth for this one-time migration task. Which solution will meet these requirements?

- [ ] Configure AWS DataSync to migrate the data to Amazon S3 and to automatically verify the dat- [ ]  
- [ ] Use rsync to transfer the data directly to Amazon S3.
- [ ] Use the AWS CLI and multiple copy processes to send the data directly to Amazon S3.
- [x] Order multiple AWS Snowball devices. Copy the data to the devices. Send the devices to AWS to copy the data to Amazon S3.

**[⬆ Back to Top](#table-of-contents)**

### A company has several on-premises Internet Small Computer Systems Interface (ISCSI) network storage servers. The company wants to reducethe number of these servers by moving to the AWS Clou- [ ]  A solutions architect must provide low-latency access to frequently used data and reduce the dependency on on-premises servers with a minimal number of infrastructure changes. Which solution will meet these requirements?
- [ ]  Deploy an Amazon S3 File Gateway.
- [ ]  Deploy Amazon Elastic Block Store (Amazon EBS) storage with backups to Amazon S3.
- [ ]  Deploy an AWS Storage Gateway volume gateway that is configured with stored volumes.
- [x]  Deploy an AWS Storage Gateway volume gateway that is configured with cached volumes.

**[⬆ Back to Top](#table-of-contents)**

### A solutions architect is designing an application that will allow business users to upload objects to Amazon S3. The solution needs to maximize object durability. Objects also must be readily available at any time and for any length of time. Users will access objects  requently within the first 30 days after the objects are uploaded, but users are much less likely to access objects that are older than 30 days. Which solution meets these requirements MOST cost-effectively?

- [ ]  Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Glacier after 30 days.
- [x]  Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA)
after 30 days.
- [ ]  Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 One Zone-Infrequent Access (S3 One Zone-IA)
after 30 days.
- [ ]  Store all the objects in S3 Intelligent-Tiering with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3
Standard-IA) after 30 days.

**[⬆ Back to Top](#table-of-contents)**

###  A company has migrated a two-tier application from its on-premises data center to the AWS Clou- [ ]  The data tier is a Multi-AZ deployment of Amazon RDS for Oracle with 12 TB of General Purpose SSD Amazon Elastic Block Store (Amazon EBS) storage. The application is  designed to process and store documents in the database as binary large objects (blobs) with an average document size of 6 M- [ ]  The database size has grown over time, reducing the performance and increasing the cost of storage. The company must improve the database performance and needs a solution that is highly available and resilient. Which solution will meet these requirements MOST cost-effectively?

- [ ]  Reduce the RDS DB instance size. Increase the storage capacity to 24 Ti- [ ]  Change the storage type to Magneti- [ ] 
- [ ] Increase the RDS DB instance size. Increase the storage capacity to 24 TiChange the storage type to Provisioned IOPS.
- [x]  Create an Amazon S3 bucket. Update the application to store documents in the S3 bucket. Store the object metadata in the existing
database.
- [ ]  Create an Amazon DynamoDB table. Update the application to use DynamoD- [ ]  Use AWS Database Migration Service (AWS DMS) to migrate
data from the Oracle database to DynamoDb

**[⬆ Back to Top](#table-of-contents)**

### Cost Explorer is showing charges higher than expected for Amazon Elastic Block Store (Amazon EBS) volumes connected to application servers in a production account. A significant portion of the charges from Amazon EBS are from volumes that were created as Provisioned IOPS SSD (io2) volume types. Controlling costs is the highest priority for this application.  Which steps should the user take to analyze and reduce the EBS costs without incurring any application downtime? (Select TWO.)

- [ ] Use the Amazon EC2 ModifyInstanceAttribute action to enable EBS optimization on the application server instances. 

- [x] Use the Amazon CloudWatch GetMetricData action to evaluate the read/write operations and read/write bytes of each volume.

- [ ] Use the Amazon EC2 ModifyVolume action to reduce the size of the underutilized io2 volumes.

- [x] Use the Amazon EC2 ModifyVolume action to change the volume type of the underutilized io2 volumes to General Purpose SSD (gp3).
- [ ] Use an Amazon S3 PutBucketPolicy action to migrate existing volume snapshots to Amazon S3 Glacier Flexible Retrieval.

**[⬆ Back to Top](#table-of-contents)**

### A company is creating a three-tier web application consisting of a web server, an application server, and a database server. The application will track GPS coordinates of packages as they are being delivere- [ ]  The application will update the database every 0.5 seconds. The tracking will need to be read as fast as possible for users to check the status of their packages. Only a few packages might be tracked on some days, whereas millions of packages might be tracked on other days. Tracking will need to be searchable by tracking ID, customer ID, and order I- [ ]  Orders older than 1 month no longer need to be tracke- [ ]  What should a solutions architect recommend to accomplish this with minimal total cost of ownership?

- [ ] Use Amazon DynamoD- [ ]  Activate Auto Scaling for the DynamoDB table. Schedule an automatic deletion script for items older than 1 month.
- [x] Use Amazon DynamoDB with global secondary indexes. Activate Auto Scaling for the DynamoDB table and the global secondary indexes. Turn on TTL for the DynamoDB table.
- [ ] Use an Amazon RDS On-Demand Instance with Provisioned IOPS (PIOPS). Configure Amazon CloudWatch alarms to send notifications when PIOPS are exceede- [ ]  Increase and decrease PIOPS as neede- [ ] 
- [ ] Use an Amazon RDS Reserved Instance with Provisioned IOPS (PIOPS). Configure Amazon CloudWatch alarms to send notifications when PIOPS are exceede- [ ]  Increase and decrease PIOPS as neede- [ ] 

**[⬆ Back to Top](#table-of-contents)**

### A company is designing a website that will be hosted on Amazon S3. How should users be prevented from linking directly to the assets in the S3 bucket?

- [ ] Create a static website, then update the bucket policy to require users to access the resources with the static website URL.
- [x] Create an Amazon CloudFront distribution with an origin access control (OAC) and update the bucket policy to grant permission to the OAC only.
- [ ] Create a static website, then configure an Amazon Route 53 record set with an alias pointing to the static website. Provide this URL to users.
- [ ] Create an Amazon CloudFront distribution with an AWS WAF web ACL that permits access to the origin server through the distribution only.

**[⬆ Back to Top](#table-of-contents)**

### A company has a well-architected application that streams audio data by using UDP in the AWS Clou- [ ]  The company hosts the application in the eu-central-1 Region. The company plans to offer services to North American users. A solutions architect must improve application network performance for the North American users. Which of the following is the MOST cost-effective solution?

- [x] Create an AWS Global Accelerator standard accelerator with an endpoint group in eu-central-1.
- [ ] Use AWS CloudFormation to deploy additional application infrastructure in the us-east-1 Region and the us-west-1 Region.
- [ ] Use AWS CloudFormation to deploy additional application infrastructure in the us-east-1 Region and the us-west-1 Region.
- [ ] Configure the application to use an Amazon Route 53 latency-based routing policy.

**[⬆ Back to Top](#table-of-contents)**


### A company's cloud operations team wants to standardize resource remediation. The company wants to provide a standard set of governance evaluations and remediations to all member accounts in its organization in AWS Organizations. Which self-managed AWS service can the company use to meet these requirements with the LEAST amount of operational effort?
- [ ] AWS Security Hub compliance standards
- [x] AWS Config conformance packs
- [ ] AWS CloudTrail
- [ ] AWS Trusted Advisor

**[⬆ Back to Top](#table-of-contents)**

### A company is designing a website that will be hosted on Amazon S3.How should users be prevented from linking directly to the assets in the S3 bucket?

- [ ] Create a static website, then update the bucket policy to require users to access the resources with the static website URL.
- [x] Create an Amazon CloudFront distribution with an origin access control (OAC) and update the bucket policy to grant permission to the OAC only.
- [ ] Create a static website, then configure an Amazon Route 53 record set with an alias pointing to the static website. Provide this URL to users.
- [ ] Create an Amazon CloudFront distribution with an AWS WAF web ACL that permits access to the origin server through the distribution only.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to build an immutable infrastructure for its software applications. The company wants to test the software applications before sending traffic to them. The company seeks an efficient solution that limits the effects of application bugs.Which combination of steps should a solutions architect recommend? (Select TWO.)
- [ ] Use AWS CloudFormation to update the production infrastructure and roll back the stack if the update fails.
- [x] Apply Amazon Route 53 weighted routing to test the staging environment and gradually increase the traffic as the tests pass.
- [ ] Apply Amazon Route 53 failover routing to test the staging environment and fail over to the production environment if the tests pass.
- [x] Use AWS CloudFormation with a parameter set to the staging value in a separate environment other than the production environment.
- [ ] Use AWS CloudFormation to deploy the staging environment with a snapshot deletion policy and reuse the resources in the production environment if the tests pass.

**[⬆ Back to Top](#table-of-contents)**

### Cost Explorer is showing charges higher than expected for Amazon Elastic Block Store (Amazon EBS) volumes connected to application servers in a production account. A significant portion of the charges from Amazon EBS are from volumes that were created as Provisioned IOPS SSD (io2) volume types. Controlling costs is the highest priority for this application. Which steps should the user take to analyze and reduce the EBS costs without incurring any application downtime? (Select TWO.)
- [x] Use the Amazon EC2 ModifyInstanceAttribute action to enable EBS optimization on the application server instances.
- [ ] Use the Amazon CloudWatch GetMetricData action to evaluate the read/write operations and read/write bytes of each volume.
- [ ] Use the Amazon EC2 ModifyVolume action to reduce the size of the underutilized io2 volumes.
- [x] Use the Amazon EC2 ModifyVolume action to change the volume type of the underutilized io2 volumes to General Purpose SSD (gp3).
- [ ] Use an Amazon S3 PutBucketPolicy action to migrate existing volume snapshots to Amazon S3 Glacier Flexible Retrieval.

**[⬆ Back to Top](#table-of-contents)**

### A company designs a mobile app for its customers to upload photos to a website. The app needs a secure login with multi-factor authentication (MFA). The company wants to limit the initial build time and the maintenance of the solution. Which solution should a solutions architect recommend to meet these requirements?
- [x] Use Amazon Cognito Identity with SMS-based MF- [ ]  
- [ ] Edit IAM policies to require MFA for all users.
- [ ] Federate IAM against the corporate Active Directory that requires MF- [ ]  
- [ ] Use Amazon API Gateway and require server-side encryption (SSE) for photos.

**[⬆ Back to Top](#table-of-contents)**

### An application running in a private subnet accesses an Amazon DynamoDB table. The data cannot leave the AWS network to meet security requirements. How should this requirement be met?
- [ ] Configure a network ACL on DynamoDB to limit traffic to the private subnet.
- [ ] Enable DynamoDB encryption at rest using an AWS Key Management Service (AWS KMS) key.
- [ ] Add a NAT gateway and configure the route table on the private subnet.
- [x] Create a VPC endpoint for DynamoDB and configure the endpoint policy. 

**[⬆ Back to Top](#table-of-contents)**

### A company is planning to use Amazon S3 to store images uploaded by its users. The images must be encrypted at rest in Amazon S3. The company does not want to spend time managing and rotating the keys, but it does want to control who can access those keys. What should a solutions architect use to accomplish this?
- [ ] Server-Side Encryption with encryption keys stored in an S3 bucket
- [ ] Server-Side Encryption with Customer-Provided Keys (SSE-C)
- [ ] Server-Side Encryption with encryption keys stored in AWS Systems Manager Parameter Store
- [x] Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)

**[⬆ Back to Top](#table-of-contents)**

### A company's legacy application is currently relying on a single-instance Amazon RDS MySQL database without encryption. Due to new compliance requirements, all existing and new data in this database must be encrypte- [ ]  How should this be accomplished?
- [ ] Create an Amazon S3 bucket with server-side encryption turned on. Move all the data to Amazon S3. Delete the RDS instance.
- [ ] Configure RDS Multi-AZ mode with encryption at rest turned on. Perform a failover to the standby instance to delete the original instance.
- [x] Take a snapshot of the RDS instance. Create an encrypted copy of the snapshot. Restore the RDS instance from the encrypted snapshot.
- [ ] Create an RDS read replica with encryption at rest turned on. Promote the read replica to primary and switch the application over to the new primary. Delete the old RDS instance.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company is preparing to deploy a web application on AWS to ensure continuous service for customers. The architecture includes a web application that the company hosts on Amazon EC2 instances, a relational database in Amazon RDS, and static assets that the company stores in Amazon S3. The company wants to design a robust and resilient architecture for the application. Which solution will meet these requirements?

- [ ] Deploy Amazon EC2 instances in a single Availability Zone. Deploy an RDS DB instance in the same Availability Zone. Use Amazon S3 with versioning enabled to store static assets.
- [x] Deploy Amazon EC2 instances in an Auto Scaling group across multiple Availability Zones. Deploy a Multi-AZ RDS DB instance. Use Amazon CloudFront to distribute static assets.
- [ ] Deploy Amazon EC2 instances in a single Availability Zone. Deploy an RDS DB instance in a second Availability Zone for cross-AZ redundancy. Serve static assets directly from the EC2 instances.
- [ ] Use AWS Lambda functions to serve the web application. Use Amazon Aurora Serverless v2 for the database. Store static assets in Amazon Elastic File System (Amazon EFS) One Zone-Infrequent Access (One Zone-IA).

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company runs several internal applications in multiple AWS accounts. The company uses AWS Organizations to manage its AWS accounts. A security appliance in the company’s networking account must inspect interactions between applications across AWS accounts. Which solution will meet these requirements?

- [ ] Deploy a Network Load Balancer (NLB) in the networking account to send traffic to the security appliance. Configure the application accounts to send traffic to the NLB by using an interface VPC endpoint in the application accounts.
- [ ] Deploy an Application Load Balancer (ALB) in the application accounts to send traffic directly to the security appliance.
- [x] Deploy a Gateway Load Balancer (GWLB) in the networking account to send traffic to the security appliance. Configure the application accounts to send traffic to the GWLB by using an interface GWLB endpoint in the application accounts.
- [ ] Deploy an interface VPC endpoint in the application accounts to send traffic directly to the security appliance.

**[⬆ Back to Top](#table-of-contents)**

### A company runs its production workload on an Amazon Aurora MySQL DB cluster that includes six Aurora Replicas. The company wants near-real-lime reporting queries from one of its departments to be automatically distributed across three of the Aurora Replicas. Those three replicas have a different compute and memory specification from the rest of the DB cluster.Which solution meets these requirements?
- [x]   Create and use a custom endpoint for the workload
- [ ]  Create a three-node cluster clone and use the reader endpoint.
- [ ]  Use any of the instance endpoints for the selected three nodes.
- [ ]  Use the reader endpoint to automatically distribute the read-only workloa- 

### A company has a well-architected application that streams audio data by using UDP in the AWS Clou- [ ]  The company hosts the application in the eu-central-1 Region. The company plans to offer services to North American users. A solutions architect must improve application network performance for the North American users. Which of the following is the MOST cost-effective solution?

- [x] Create an AWS Global Accelerator standard accelerator with an endpoint group in eu-central-1.
- [ ] Use AWS CloudFormation to deploy additional application infrastructure in the us-east-1 Region and the us-west-1 Region.
- [ ] Use AWS CloudFormation to deploy additional application infrastructure in the us-east-1 Region and the us-west-1 Region.
- [ ] Configure the application to use an Amazon Route 53 latency-based routing policy.

**[⬆ Back to Top](#table-of-contents)**

### A company has multiple applications that use Amazon RDS for MySQL as is database. The company recently discovered that a new custom reporting application has increased the number of Queries on the database. This is slowing down performance.How should a solutions architect resolve this issue with the LEAST amount of application changes?
- [ ]   Add a secondary DB instance using Multi-AZ.
- [x]  Set up a road replica and Multi-AZ on Amazon RDS.
- [ ]  Set up a standby replica and Multi-AZ on Amazon RDS.
- [ ]  Use caching on Amazon RDS to improve the overall performance.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to automate the security assessment of its Amazon EC2 instances. The company needs to validate and demonstrate that security and compliance standards are being followed throughout the development process.What should a solutions architect do to meet these requirements?
- [ ]   Use Amazon Macie to automatically discover, classify and protect the EC2 instances.
- [ ]  Use Amazon GuardDuty to publish Amazon Simple Notification Service (Amazon SNS) notifications.
- [x]  Use Amazon Inspector with Amazon CloudWatch to publish Amazon Simple Notification Service (Amazon SNS) notifications
- [ ]  Use Amazon EventBridge (Amazon CloudWatch Events) to detect and react to changes in the status of AWS Trusted Advisor checks.

**[⬆ Back to Top](#table-of-contents)**

### A company stores 200 GB of data each month in Amazon S3. The company needs to perform analytics on this data at the end of each month to determine the number of items sold in each sales region for the previous month.Which analytics strategy is MOST cost-effective for the company to use?
- [ ]   Create an Amazon Elasticsearch Service (Amazon ES) cluster. Query the data in Amazon ES. Visualize the data by using Kiban- [ ]  
- [x]  Create a table in the AWS Glue Data Catalog. Query the data in Amazon S3 by using Amazon Athen- [ ]   Visualize the data in Amazon QuickSight.
- [ ]  Create an Amazon EMR cluster. Query the data by using Amazon EMR, and store the results in Amazon S3. Visualize the data in Amazon QuickSight.
- [ ]  Create an Amazon Redshift cluster. Query the data in Amazon Redshift, and upload the results to Amazon S3. Visualize the data in Amazon QuickSight.

### A company's cloud operations team wants to standardize resource remediation. The company wants to provide a standard set of governance evaluations and remediations to all member accounts in its organization in AWS Organizations. Which self-managed AWS service can the company use to meet these requirements with the LEAST amount of operational effort?
- [ ] AWS Security Hub compliance standards
- [x] AWS Config conformance packs
- [ ] AWS CloudTrail
- [ ] AWS Trusted Advisor

**[⬆ Back to Top](#table-of-contents)**

### A company is designing a website that will be hosted on Amazon S3.How should users be prevented from linking directly to the assets in the S3 bucket?

- [ ] Create a static website, then update the bucket policy to require users to access the resources with the static website URL.
- [x] Create an Amazon CloudFront distribution with an origin access control (OAC) and update the bucket policy to grant permission to the OAC only.
- [ ] Create a static website, then configure an Amazon Route 53 record set with an alias pointing to the static website. Provide this URL to users.
- [ ] Create an Amazon CloudFront distribution with an AWS WAF web ACL that permits access to the origin server through the distribution only.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to build an immutable infrastructure for its software applications. The company wants to test the software applications before sending traffic to them. The company seeks an efficient solution that limits the effects of application bugs.Which combination of steps should a solutions architect recommend? (Select TWO.)
- [ ] Use AWS CloudFormation to update the production infrastructure and roll back the stack if the update fails.
- [x] Apply Amazon Route 53 weighted routing to test the staging environment and gradually increase the traffic as the tests pass.
- [ ] Apply Amazon Route 53 failover routing to test the staging environment and fail over to the production environment if the tests pass.
- [x] Use AWS CloudFormation with a parameter set to the staging value in a separate environment other than the production environment.
- [ ] Use AWS CloudFormation to deploy the staging environment with a snapshot deletion policy and reuse the resources in the production environment if the tests pass.

**[⬆ Back to Top](#table-of-contents)**

### Cost Explorer is showing charges higher than expected for Amazon Elastic Block Store (Amazon EBS) volumes connected to application servers in a production account. A significant portion of the charges from Amazon EBS are from volumes that were created as Provisioned IOPS SSD (io2) volume types. Controlling costs is the highest priority for this application. Which steps should the user take to analyze and reduce the EBS costs without incurring any application downtime? (Select TWO.)
- [x] Use the Amazon EC2 ModifyInstanceAttribute action to enable EBS optimization on the application server instances.
- [ ] Use the Amazon CloudWatch GetMetricData action to evaluate the read/write operations and read/write bytes of each volume.
- [ ] Use the Amazon EC2 ModifyVolume action to reduce the size of the underutilized io2 volumes.
- [x] Use the Amazon EC2 ModifyVolume action to change the volume type of the underutilized io2 volumes to General Purpose SSD (gp3).
- [ ] Use an Amazon S3 PutBucketPolicy action to migrate existing volume snapshots to Amazon S3 Glacier Flexible Retrieval.

**[⬆ Back to Top](#table-of-contents)**


### A company wants to move its on-premises network, attached storage (NAS) to AWS. The company wants to make the data available to any Linux instances within its VPC and ensure changes are automatically synchronized across all instances accessing the data store. The majority of the data is accessed very rarely, and some files are accessed by multiple users at the same time.Which solution meets these requirements and is MOST cost-effective?
- [ ]   Create an Amazon Elastic Block Store (Amazon EBS) snapshot containing the dat- [ ]   Share it with users within the VP- [ ] 
- [ ]  Create an Amazon S3 bucket that has a lifecycle policy set to transition the data to S3 Standard-Infrequent Access (S3 Standard-IA) after the appropriate number of days.
- [ ]  Create an Amazon Elastic File System (Amazon EFS) file system within the VP- [ ]  Set the throughput mode to Provisioned and to the required amount of IOPS to support concurrent usage.
- [x]  Create an Amazon Elastic File System (Amazon EFS) file system within the VP- [ ]  Set the lifecycle policy to transition the data to EFS Infrequent Access (EFS IA) after the appropriate number of days.


**[⬆ Back to Top](#table-of-contents)**

### A company plans to host a survey website on AWS. The company anticipates an unpredictable amount of traffi- [ ]  This traffic results in asynchronous updates to the database. The company wants to ensure that writes to the database hosted on AWS do not get droppe- [ ] How should the company write its application to handle these database requests?
- [ ]   Configure the application to publish to an Amazon Simple Notification Service (Amazon SNS) topi- [ ]  Subscribe the database to the SNS topi- [ ] 
- [ ]  Configure the application to subscribe to an Amazon Simple Notification Service (Amazon SNS) topi- [ ]  Publish the database updates to the SNS topi- [ ] 
- [ ]  Use Amazon Simple Queue Service (Amazon SQS) FIFO queues to queue the database connection until the database has resources to write the dat- [ ]  
- [x]  Use Amazon Simple Queue Service (Amazon SQS) FIFO queues for capturing the writes and draining the queue as each write is made to the database.


**[⬆ Back to Top](#table-of-contents)**

### A company that recently started using AWS establishes a Site-to-Site VPN between its on-premises datacenter and AWS. The company's security mandate states that traffic originating from on premises should stay within the companyג€™s private IP space when communicating with an Amazon Elastic Container Service(Amazon ECS) cluster that is hosting a sample web application.Which solution meets this requirement?
- [ ]   Configure a gateway endpoint for Amazon ECS. Modify the route table to include an entry pointing to the ECS cluster.
- [ ]  Create a Network Load Balancer and AWS PrivateLink endpoint for Amazon ECS in the same VPC that is hosting the ECS cluster.
- [x]  Create a Network Load Balancer in one VPC and an AWS PrivateLink endpoint for Amazon ECS in another VP- [ ]  Connect the two VPCs by using VPC peering.
- [ ]  Configure an Amazon Route 53 record with Amazon ECS as the target. Apply a server certificate to Route 53 from AWS Certificate Manager (ACM) for SSL offloading.


**[⬆ Back to Top](#table-of-contents)**

### A solutions architect must analyze and update a companyג€™s existing IAM policies prior to deploying a new workloa- [ ]  The solutions architect created the following policy:What is the net effect of this policy?
- [ ]   Users will be allowed all actions except s3:PutObject if multi-factor authentication (MFA) is enable- [ ] 
- [ ]  Users will be allowed all actions except s3:PutObject if multi-factor authentication (MFA) is not enable- [ ] 
- [ ]  Users will be denied all actions except s3:PutObject if multi-factor authentication (MFA) is enable- [ ] 
- [x]  Users will be denied all actions except s3:PutObject if multi-factor authentication (MFA) is not enabled


**[⬆ Back to Top](#table-of-contents)**

### A company is running a multi-tier web application on premises. The web application is containerized and runs on a number of Linux hosts connected to aPostgreSQL database that contains user records. The operational overhead of maintaining the infrastructure and capacity planning is limiting the companyג€™s growth. A solutions architect must improve the applicationג€™s infrastructure.Which combination of actions should the solutions architect take to accomplish this? (Choose two.)
- [x]   Migrate the PostgreSQL database to Amazon Auror- [ ]  
- [ ]  Migrate the web application to be hosted on Amazon EC2 instances.
- [ ]  Set up an Amazon CloudFront distribution for the web application content.
- [ ]  Set up Amazon ElastiCache between the web application and the PostgreSQL database.
- [x] Migrate the web application to be hosted on AWS Fargate with Amazon Elastic Container Service (Amazon ECS)

**[⬆ Back to Top](#table-of-contents)**

### An application allows users at a companyג€™s headquarters to access product dat- [ ]   The product data is stored in an Amazon RDS MySQL DB instance. The operations team has isolated an application performance slowdown and wants to separate read traffic from write traffic  A solutions architect needs to optimize the applicationג€™s performance quickly.What should the solutions architect recommend?
- [ ]   Change the existing database to a Multi-AZ deployment. Serve the read requests from the primary Availability Zone.
- [ ]  Change the existing database to a Multi-AZ deployment. Serve the read requests from the secondary Availability Zone.
- [ ]  Create read replicas for the database. Configure the read replicas with half of the compute and storage resources as the source database.
- [x]  Create read replicas for the database. Configure the read replicas with the same compute and storage resources as the source database.

**[⬆ Back to Top](#table-of-contents)**

### A company is using Amazon DynamoDB with provisioned throughput for the database tier of its ecommerce website. During flash sales, customers experience periods of time when the database cannot handle the high number of transactions taking place. This causes the company to lose transactions. During normal periods, the database performs appropriately.Which solution solves the performance problem the company faces?
- [x]   Switch DynamoDB to on-demand mode during flash sales.
- [ ]  Implement DynamoDB Accelerator for fast in memory performance.
- [ ]  Use Amazon Kinesis to queue transactions for processing to DynamoD- [ ] 
- [ ]  Use Amazon Simple Queue Service (Amazon SQS) to queue transactions to DynamoD- [ ] 


**[⬆ Back to Top](#table-of-contents)**

### A company is reviewing a recent migration of a three-tier application to a VP- [ ]  The security team discovers that the principle of least privilege is not being applied to Amazon EC2 security group ingress and egress rules between the application tiers.What should a solutions architect do to correct this issue?
- [x]  Create security group rules using the instance ID as the source or destination.
- [ ]  Create security group rules using the security group ID as the source or destination.
- [ ]  Create security group rules using the VPC CIDR blocks as the source or destination.
- [ ]  Create security group rules using the subnet CIDR blocks as the source or destination

**[⬆ Back to Top](#table-of-contents)**

### A company requires that all versions of objects in its Amazon S3 bucket be retaine- [ ]  Current object versions will be frequently accessed during the first 30 days, after which they will be rarely accessed and must be retrievable within 5 minutes. Previous object versions need to be kept forever, will be rarely accessed, and can be retrieved within 1 week. All storage solutions must be highly available and highly durable.What should a solutions architect recommend to meet these requirements in the MOST cost-effective manner?
- [x]   Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 Glacier after 30 days and moves previous object versions to S3 Glacier after 1 day.
- [ ]  Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 Glacier after 30 days and moves previous object versions to S3 Glacier Deep Archive after 1 day.
- [ ]  Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 Standard-infrequent Access (S3 Standard-IA) after 30 days and moves previous object versions toS3 Glacier Deep Archive after 1 day.
- [ ]  Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 One Zone-Infrequent Access (S3 One Zone-IA) after 30 days and moves previous object versions to S3 Glacier Deep Archive after 1 day.

**[⬆ Back to Top](#table-of-contents)**

### A development team is collaborating with another company to create an integrated product. The other company needs to access an Amazon Simple QueueService (Amazon SQS) queue that is contained in the development team's account. The other company wants to poll the queue without giving up its own account permissions to do so.How should a solutions architect provide access to the SQS queue?
- [ ]   Create an instance profile that provides the other company access to the SQS queue.
- [ ]  Create an IAM policy that provides the other company access to the SQS queue.
- [x]  Create an SQS access policy that provides the other company access to the SQS queue.
- [ ]  Create an Amazon Simple Notification Service (Amazon SNS) access policy that provides the other company access to the SQS queue.


**[⬆ Back to Top](#table-of-contents)**

### A company is developing a video conversion application hosted on AWS. The application will be available in two tiers: a free tier and a paid tier. Users in the paid tier will have their videos converted first and then the tree tier users will have their videos converted. Which solution meets these requirements and is MOST cost-effective?
- [ ]   One FIFO queue for the paid tier and one standard queue for the free tier.
- [ ]  A single FIFO Amazon Simple Queue Service (Amazon SQS) queue for all file types.
- [ ]  A single standard Amazon Simple Queue Service (Amazon SQS) queue for all file types.
- [x]  Two standard Amazon Simple Queue Service (Amazon SQS) queues with one for the paid tier and one for the free tier.


**[⬆ Back to Top](#table-of-contents)**

### An administrator of a large company wants to monitor for and prevent any cryptocurrency-related attacks on the companyג€™s AWS accounts.Which AWS service can the administrator use to protect the company against attacks?
- [ ]   Amazon Cognito
- [x]  Amazon GuardDuty
- [ ]  Amazon Inspector
- [ ]  Amazon Macie

**[⬆ Back to Top](#table-of-contents)**

### A company has applications hosted on Amazon EC2 instances with IPv6 addresses. The applications must initiate communications with other external applications using the internet. However, the companyג€™'s security policy states that any external service cannot initiate a connection to the EC2 instances. What should a solutions architect recommend to resolve this issue?
- [ ]   Create a NAT gateway and make it the destination of the subnetג€™s route table.
- [ ]  Create an internet gateway and make it the destination of the subnetג€™s route table.
- [ ]  Create a virtual private gateway and make it the destination of the subnetג€™s route table.
- [x]  Create an egress-only internet gateway and make it the destination of the subnetג€™s route table.

**[⬆ Back to Top](#table-of-contents)**

### A company provides an online service for posting video content and transcoding it for use by any mobile platform. The application architecture uses AmazonElastic File System (Amazon EFS) Standard to collect and store the videos so that multiple Amazon EC2 Linux instances can access the video content for processing. As the popularity of the service has grown over time, the storage costs have become too expensive.Which storage solution is MOST cost-effective?
- [ ]   Use AWS Storage Gateway for files to store and process the video content.
- [ ]  Use AWS Storage Gateway for volumes to store and process the video content.
- [ ]  Use Amazon EFS for storing the video content. Once processing is complete, transfer the files to Amazon Elastic Block Store (Amazon EBS).
- [x]  Use Amazon S3 for storing the video content. Move the files temporarily over to an Amazon ElasticBlock Store (Amazon EBS) volume attached to the server for processing.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to host its web application on AWS using multiple Amazon EC2 instances across different AWS Regions. Since the application content will be specific to each geographic region, the client requests need to be routed to the server that hosts the content for that clients Region.What should a solutions architect do to accomplish this?
- [ ]   Configure Amazon Route 53 with a latency routing policy.
- [ ]  Configure Amazon Route 53 with a weighted routing policy.
- [x]  Configure Amazon Route 53 with a geolocation routing policy.
- [ ]  Configure Amazon Route 53 with a multivalue answer routing policy

**[⬆ Back to Top](#table-of-contents)**

### A solutions architect is planning the deployment of a new static website. The solution must minimize costs and provide at least 99% availability. Which solution meets these requirements?
- [x]   Deploy the application to an Amazon S3 bucket in one AWS Region that has versioning disable- [ ] 
- [ ]  Deploy the application to Amazon EC2 instances that run in two AWS Regions and two Availability Zones.
- [ ]  Deploy the application to an Amazon S3 bucket that has versioning and cross-Region replication enable- [ ] 
- [ ]  Deploy the application to an Amazon EC2 instance that runs in one AWS Region and one Availability Zone.

**[⬆ Back to Top](#table-of-contents)**

### A recently created startup built a three-tier web application. The front end has static content. The application layer is based on microservices. User data is stored as JSON documents that need to be accessed with low latency. The company expects regular traffic to be low during the first year, with peaks in traffic when it publicizes new features every month. The startup team needs to minimize operational overhead costs.What should a solutions architect recommend to accomplish this?
- [ ]   Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use AWS Elastic Beanstalk for the application layer. Use Amazon DynamoDB to store user dat- [ ]  
- [ ]  Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use Amazon Elastic KubernetesService (Amazon EKS) for the application layer. Use Amazon DynamoDB to store user dat- [ ]  
- [x]  Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use Amazon API Gateway and AWS Lambda functions for the application layer. Use Amazon DynamoDB to store user dat- [ ]  
- [ ]  Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use Amazon API Gateway and AWS Lambda functions for the application layer. Use Amazon RDS with read replicas to store user dat- [ ]  

**[⬆ Back to Top](#table-of-contents)**

### A company is building a payment application that must be highly available even during regional service disruptions. A solutions architect must design a data storage solution that can be easily replicated and used in other AWS Regions. The application also requires low-latency atomicity, consistency, isolation, and durability (ACID) transactions that need to be immediately available to generate reports The development team also needs to use SQL.Which data storage solution meets these requirements?
- [x]   Amazon Aurora Global Database
- [ ]  Amazon DynamoDB global tables
- [ ]  Amazon S3 with cross-Region replication and Amazon Athena
- [ ]  MySQL on Amazon EC2 instances with Amazon Elastic Block Store (Amazon EBS) snapshot replication

**[⬆ Back to Top](#table-of-contents)**

### A company stores call recordings on a monthly basis. Statistically, the recorded data may be referenced randomly within a year but accessed rarely after 1 year.Files that are newer than 1 year old must be queried and retrieved as quickly as possible. A delay in retrieving older files is acceptable. A solutions architect needs to store the recorded data at a minimal cost.Which solution is MOST cost-effective?
- [ ]   Store individual files in Amazon S3 Glacier and store search metadata in object tags created in S3 Glacier Query S3 Glacier tags and retrieve the files from S3 Glacier.
- [x]  Store individual files in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after1 year. Query and retrieve the files from Amazon S3 or S3 Glacier.
- [ ]  Archive individual files and store search metadata for each archive in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after 1 year. Query and retrieve the files by searching for metadata from Amazon S3.
- [ ]  Archive individual files in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after 1 year. Store search metadata in Amazon DynamoD- [ ]  Query the files from DynamoDB and retrieve them from Amazon S3 or S3 Glacier.

**[⬆ Back to Top](#table-of-contents)**

### A company is developing a new machine learning model solution in AWS. The models are developed as independent microservices that fetch about 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent.The company provides models to hundreds of users. The usage patterns for the models are irregular Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time.Which solution meets these requirements?
- [ ]   The requests from the API are sent to an Application Load Balancer (ALB). Models are deployed as AWS Lambda functions invoked by the AL- [ ] 
- [ ]  The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as AWS Lambda functions triggered by SQS events AWS Auto Scaling is enabled on Lambda to increase the number of vCPUs based on the SQS queue size.
- [ ]  The requests from the API are sent to the modelג€™s Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS App Mesh scales the instances of the ECS cluster based on the SQS queue size.
- [x]  The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS Auto Scaling is enabled on Amazon ECS for both the cluster and copies of the service based on the queue size


**[⬆ Back to Top](#table-of-contents)**

### A company has no existing file share services. A new project requires access to file storage that is mountable as a drive for on-premises desktops. The file server must authenticate users to an Active Directory domain before they are able to access the storage.Which service will allow Active Directory users to mount storage as a drive on their desktops?
- [ ]   Amazon S3 Glacier
- [ ]  AWS DataSync
- [ ]  AWS Snowball Edge
- [x]  AWS Storage Gateway

**[⬆ Back to Top](#table-of-contents)**

### A company is preparing to launch a public-facing web application in the AWS Clou- [ ]  The architecture consists of Amazon EC2 instances within a VPC behind anElastic Load Balancer (ELB). A third party service is used for the DNS. The companyג€™s solutions architect must recommend a solution to detect and protect against largescale DDoS attacks.Which solution meets these requirements?
- [ ]   Enable Amazon GuardDuty on the account.
- [ ]  Enable Amazon Inspector on the EC2 instances.
- [ ]  Enable AWS Shield and assign Amazon Route 53 to it.
- [x]  Enable AWS Shield Advanced and assign the ELB to it.


**[⬆ Back to Top](#table-of-contents)**

### A company has a custom application with embedded credentials that retrieves information from an Amazon RDS MySQL DB instance. Management says the application must be made more secure with the least amount of programming effort.What should a solutions architect do to meet these requirements?
- [ ]   Use AWS Key Management Service (AWS KMS) customer master keys (CMKs) to create keys. Configure the application to load the database credentials from AWS KMS. Enable automatic key rotation.
- [ ]  Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Secrets Manager. Configure the application to load the database credentials from Secrets Manager. Create an AWS Lambda function that rotates the credentials in Secret Manager.
- [x]  Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Secrets Manager. Configure the application to load the database credentials from Secrets Manager. Set up a credentials rotation schedule for the application user in the RDS for MySQL database using Secrets Manager.
- [ ]  Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Systems Manager Parameter Store. Configure the application to load the database credentials from Parameter Store. Set up a credentials rotation schedule for the application user in the RDS for MySQL database using Parameter Store.

**[⬆ Back to Top](#table-of-contents)**

A company is running a multi-tier web application on AWS. The application runs its database tier on Amazon Aurora MySQL. The application and database tiers are in the us-east-1 Region. A database administrator who regularly monitors the Aurora DB cluster finds that an intermittent increase in read traffic is creating high CPUutilization on the read replica and causing increased read latency of the application.What should a solutions architect do to improve read scalability?
- [ ]   Reboot the Aurora DB cluster.
- [ ]  Create a cross-Region read replica
- [ ]  Increase the instance class of the read replic- [ ]  
- [x]  Configure Aurora Auto Scaling for the read replic- [ ]  

**[⬆ Back to Top](#table-of-contents)**

### A companyג€™s order fulfillment service uses a MySQL database. The database needs to support a large number of concurrent queries and transactions. Developers are spending time patching and tuning the database This is causing delays in releasing new product features.The company wants to use cloud-based services to help address this new challenge. The solution must allow the developers to migrate the database with little or no code changes and must optimize performance.Which service should a solutions architect use to meet these requirements?
- [x]   Amazon Aurora
- [ ]  Amazon DynamoDB
- [ ]  Amazon ElastiCache
- [ ]  MySQL on Amazon EC2

**[⬆ Back to Top](#table-of-contents)**

### A company is planning to transfer multiple terabytes of data to AWS. The data is collected offline from ships. The company want to run complex transformation before transferring the dat- [ ]  Which AWS service should a solutions architect recommend for this migration?
- [ ]   AWS Snowball
- [ ]  AWS Snowmobile
- [ ]  AWS Snowball Edge Storage Optimize
- [x]  AWS Snowball Edge Compute Optimize


**[⬆ Back to Top](#table-of-contents)**

### A company is running an online transaction processing (OLTP) workload on AWS. This workload uses an unencrypted Amazon RDS DB instance in a Multi-AZ deployment. Daily database snapshots are taken from this instance.What should a solutions architect do to ensure the database and snapshots are always encrypted moving forward?
- [x]   Encrypt a copy of the latest DB snapshot. Replace existing DB instance by restoring the encrypted snapshot.
- [ ]  Create a new encrypted Amazon Elastic Block Store (Amazon EBS) volume and copy the snapshots to it. Enable encryption on the DB instance.
- [ ]  Copy the snapshots and enable encryption using AWS Key Management Service (AWS KMS). Restore encrypted snapshot to an existing DB instance.
- [ ]  Copy the snapshots to an Amazon S3 bucket that is encrypted using server-side encryption with AWS Key Management Service (AWS KMS) managed keys (SSE-KMS).

**[⬆ Back to Top](#table-of-contents)**

### A company is selling up an application to use an Amazon RDS MySQL DB instance. The database must be architected for high availability across AvailabilityZones and AWS Regions with minimal downtime.How should a solutions architect meet this requirement?
- [ ]   Set up an RDS MySQL Multi-AZ DB instance. Configure an appropriate backup window.
- [x]  Set up an RDS MySQL Multi-AZ DB instance. Configure a read replica in a different Region.
- [ ]  Set up an RDS MySQL Single-AZ DB instance. Configure a read replica in a different Region.
- [ ]  Set up an RDS MySQL Single-AZ DB instance. Copy automated snapshots to at least one other Region.


**[⬆ Back to Top](#table-of-contents)**

### A company hosts its web application on AWS using seven Amazon EC2 instances. The company requires that the IP addresses of all healthy EC2 instances be returned in response to DNS queries.Which policy should be used to meet this requirement?
- [ ]   Simple routing policy
- [ ]  Latency routing policy
- [x]  Multi-value routing policy
- [ ]  Geolocation routing policy


**[⬆ Back to Top](#table-of-contents)**

### A company has 700 TB of backup data stored in network attached storage (NAS) in its data center This backup data need to be accessible for infrequent regulatory requests and must be retained 7 years. The company has decided to migrate this backup data from its data center to AWS. The migration must be complete within 1 month. The company has 500 Mbps of dedicated bandwidth on its public internet connection available for data transfer.What should a solutions architect do to migrate and store the data at the LOWEST cost?
- [x]   Order AWS Snowball devices to transfer the dat- [ ]   Use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive.
- [ ]  Deploy a VPN connection between the data center and Amazon VP- [ ]  Use the AWS CLI to copy the data from on premises to Amazon S3 Glacier.
- [ ]  Provision a 500 Mbps AWS Direct Connect connection and transfer the data to Amazon S3. Use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive.
- [ ]  Use AWS DataSync to transfer the data and deploy a DataSync agent on premises. Use the DataSync task to copy files from the on-premises NAS storage to Amazon S3 Glacier.


**[⬆ Back to Top](#table-of-contents)**

### A company is preparing to deploy a data lake on AWS. A solutions architect must define the encryption strategy tor data at rest m Amazon S3/ The companyג€™s security policy states:✑ Keys must be rotated every 90 days.✑ Strict separation of duties between key users and key administrators must be implemente- [ ] ✑ Auditing key usage must be possible.What should the solutions architect recommend?
- [x]   Server-side encryption with AWS KMS managed keys (SSE-KMS) with customer managed customer master keys (CMKs)
- [ ]  Server-side encryption with AWS KMS managed keys (SSE-KMS) with AWS managed customer master keys (CMKs)
- [ ]  Server-side encryption with Amazon S3 managed keys (SSE-S3) with customer managed customer master keys (CMKs)
- [ ]  Server-side encryption with Amazon S3 managed keys (SSE-S3) with AWS managed customer master keys (CMKs)


**[⬆ Back to Top](#table-of-contents)**

### A company has an application that generates a large number of files, each approximately 5 MB in size. The files are stored in Amazon S3. Company policy requires the files to be stored for 4 years before they can be delete- [ ]  Immediate accessibility is always required as the files contain critical business data that is not easy to reproduce. The files are frequently accessed in the first 30 days of the object creation but are rarely accessed after the first 30 days.Which storage solution is MOST cost-effective?
- [ ]   Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Glacier 30 days from object creation. Delete the files 4 years after object creation.
- [ ]  Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 One Zone-Infrequent Access (S3 One Zone-IA) 30 days from object creation. Delete the files 4 years after object creation.
- [x]  Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Delete the files 4 years after object creation.
- [ ]  Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Move the files to S3 Glacier 4 years after object creation.

**[⬆ Back to Top](#table-of-contents)**

### A company previously migrated its data warehouse solution to AWS. The company also has an AWS Direct Connect connection. Corporate office users query the data warehouse using a visualization tool. The average size of a query returned by the data warehouse is 50 MB and each webpage sent by the visualization tool is approximately 500 K- [ ]  Result sets returned by the data warehouse are not cache- [ ] Which solution provides the LOWEST data transfer egress cost for the company?
- [ ]   Host the visualization tool on premises and query the data warehouse directly over the internet.
- [ ]  Host the visualization tool in the same AWS Region as the data warehouse. Access it over the internet.
- [ ]  Host the visualization tool on premises and query the data warehouse directly over a Direct Connect connection at a location in the same AWS Region.
- [x]  Host the visualization tool in the same AWS Region as the data warehouse and access it over a DirectConnect connection at a location in the same Region.

**[⬆ Back to Top](#table-of-contents)**

### A mobile gaming company runs application servers on Amazon EC2 instances. The servers receive updates from players every 15 minutes. The mobile game creates a JSON object of the progress made in the game since the last update, and sends the JSON object to an Application Load Balancer. As the mobile game is played, game updates are being lost. The company wants to create a durable way to get the updates in older.What should a solutions architect recommend to decouple the system?

- [ ]   Use Amazon Kinesis Data Streams to capture the data and store the JSON object in Amazon S3.
- [ ]  Use Amazon Kinesis Data Firehose to capture the data and store the JSON object in Amazon S3.
- [x]  Use Amazon Simple Queue Service (Amazon SQS) FIFO queues to capture the data and EC2 instances to process the messages in the queue.
- [ ]  Use Amazon Simple Notification Service (Amazon SNS) to capture the data and EC2 instances to process the messages sent to the Application Load Balancer.

**[⬆ Back to Top](#table-of-contents)**

### A company has an application that runs on Amazon EC2 instances within a private subnet in a VPC  The instances access data in an Amazon S3 bucket in the same AWS Region. The VPC contains a NAT gateway in a public subnet to access the S3 bucket. The company wants to reduce costs by replacing the NAT gateway without compromising security or redundancy. Which solution meets these requirements?

- [ ]  Replace the NAT gateway with a NAT instance.
- [ ]  Replace the NAT gateway with an internet gateway.
- [x]  Replace the NAT gateway with a gateway VPC endpoint.
- [ ]  Replace the NAT gateway with an AWS Direct Connect connection.

**[⬆ Back to Top](#table-of-contents)**

### A company hosts a website on premises and wants to migrate it to the AWS Clou- [ ]  The website exposes a single hostname to the internet but it routes its functions to different on-premises server groups based on the path of the URL. The server groups are scaled independently depending on the needs of the functions they support. The company has an AWS Direct Connect connection configured to its on-premises network.What should a solutions architect do to provide path-based routing to send the traffic to the correct group of servers?
- [ ]   Route all traffic to an internet gateway. Configure pattern matching rules at the internet gateway to route traffic to the group of servers supporting that path.
- [ ]  Route all traffic to a Network Load Balancer (NLB) with target groups for each group of servers. Use pattern matching rules at the NLB to route traffic to the correct target group.
- [x]  Route all traffic to an Application Load Balancer (ALB). Configure path-based routing at the ALB to route traffic to the correct target group for the servers supporting that path.
- [ ]  Use Amazon Route 53 as the DNS server. Configure Route 53 path-based alias records to route traffic to the correct Elastic Load Balancer for the group of servers supporting that path.

**[⬆ Back to Top](#table-of-contents)**

### An application uses an Amazon RDS MySQL DB instance. The RDS database is becoming low on disk space. A solutions architect wants to increase the disk space without downtime. Which solution meets these requirements with the LEAST amount of effort?
- [x]   Enable storage auto scaling in RDS.
- [ ]  Increase the RDS database instance size.
- [ ]  Change the RDS database instance storage type to Provisioned IOPS.
- [ ]  Back up the RDS database, increase the storage capacity, restore the database and stop the previous instance.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce website is deploying its web application as Amazon Elastic Container Service (Amazon ECS) container instances behind an Application LoadBalancer (ALB). During periods of high activity, the website slows down and availability is reduce- [ ]  A solutions architect uses Amazon CloudWatch alarms to receive notifications whenever there is an availability issue so they can scale out resources. Company management wants a solution that automatically responds to such events.Which solution meets these requirements?
- [ ]   Set up AWS Auto Scaling to scale out the ECS service when there are timeouts on the AL- [ ]  Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.
- [ ]  Set up AWS Auto Scaling to scale out the ECS service when the ALB CPU utilization is too high. Setup AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.
- [x]  Set up AWS Auto Scaling to scale out the ECS service when the services CPU utilization is too high. Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.
- [ ]  Set up AWS Auto Scaling to scale out the ECS service when the ALB target group CPU utilization is too high. Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.

**[⬆ Back to Top](#table-of-contents)**

### A company has a website deployed on AWS. The database backend is hosted on Amazon RDS for MySQL with a primary instance and five read replicas to support scaling needs. The read replicas should lag no more than 1 second behind the primary instance to support the user experience.As traffic on the website continues to increase, the replicas are falling further behind during periods of peak load, resulting in complaints from users when searches yield inconsistent results. A solutions architect needs to reduce the replication lag as much as possible, with minimal changes to the application code or operational requirements.Which solution meets these requirements?
- [x]   Migrate the database to Amazon Aurora MySQL. Replace the MySQL read replicas with Aurora Replicas and enable Aurora Auto Scaling
- [ ]  Deploy an Amazon ElastiCache for Redis cluster in front of the database. Modify the website to check the cache before querying the database read endpoints.
- [ ]  Migrate the database from Amazon RDS to MySQL running on Amazon EC2 compute instances. Choose very large compute optimized instances for all replica nodes.
- [ ]  Migrate the database to Amazon DynamoD- [ ]  Initially provision a large number of read capacity units (RCUs) to support the required throughput with on- demand capacity scaling enabled

**[⬆ Back to Top](#table-of-contents)**

## A company has an API-based inventory reporting application running on Amazon EC2 instances. The application stores information in an Amazon DynamoDB table. The companyג distribution centers have an on-premises shipping application that calls an API to update the inventory before printing shipping labels. The company has been experiencing application interruptions several times each day, resulting in lost transactions.What should a solutions architect recommend to improve application resiliency?
- [ ]  Modify the shipping application to write to a local database.
- [ ]  Modify the application APIs to run serverless using AWS Lambda
- [ ]  Configure Amazon API Gateway to call the EC2 inventory application APIs.
- [x]  Modify the application to send inventory updates using Amazon Simple Queue Service (Amazon SQS).

**[⬆ Back to Top](#table-of-contents)**

### A company has a three-tier environment on AWS that ingests sensor data from its usersג€™ devices. The traffic flows through a Network Load Balancer (NLB) then toAmazon EC2 instances for the web tier, and finally toEC2 instances for the application tier that makes database calls.What should a solutions architect do to improve the security of data in transit to the web tier?
- [x]   Configure a TLS listener and add the server certificate on the NLB
- [ ]  Configure AWS Shield Advanced and enable AWS WAF on the NLB
- [ ]  Change the load balancer to an Application Load Balancer and attach AWS WAF to it.
- [ ]  Encrypt the Amazon Elastic Block Store (Amazon EBS) volume on the EC2 instances using AWS Key Management Service (AWS KMS).

**[⬆ Back to Top](#table-of-contents)**

### A company runs an online marketplace web application on AWS. The application serves hundreds of thousands of users during peak hours. The company needs a scalable, near-real-time solution to share the details of millions of financial transactions with several other internal applications. Transactions also need to be processed to remove sensitive data before being stored in a document database for low-latency retrieval.What should a solutions architect recommend to meet these requirements?
- [ ]   Store the transactions data into Amazon DynamoD- [ ]  Set up a rule in DynamoDB to remove sensitive data from every transaction upon write. Use DynamoDB Streams to share the transactions data with other applications.
- [ ]  Stream the transactions data into Amazon Kinesis Data Firehose to store data in Amazon DynamoDB and Amazon S3. Use AWS Lambda integration with Kinesis Data Firehose to remove sensitive dat- [ ]   Other applications can consume the data stored in Amazon S3.
- [x]  Stream the transactions data into Amazon Kinesis Data Streams. Use AWS Lambda integration to remove sensitive data from every transaction and then store the transactions data in AmazonDynamoD- [ ]  Other applications can consume the transactions data off the Kinesis data stream.
- [ ]  Store the batched transactions data in Amazon S3 as files. Use AWS Lambda to process every file and remove sensitive data before updating the files in Amazon S3. The Lambda function then stores the data in Amazon DynamoD- [ ]  Other applications can consume transaction files stored in Amazon S3.

**[⬆ Back to Top](#table-of-contents)**

### A company has a dynamic web application hosted on two Amazon EC2 instances. The company has its own SSL certificate, which is on each instance to performSSL termination.There has been an increase in traffic recently, and the operations team determined that SSL encryption and decryption is causing the compute capacity of the web servers to reach their maximum limit.What should a solutions architect do to increase the applicationג€™s performance?
- [ ]   Create a new SSL certificate using AWS Certificate Manager (ACM). Install the ACM certificate on each instance.
- [ ]  Create an Amazon S3 bucket. Migrate the SSL certificate to the S3 bucket. Configure the EC2 instances to reference the bucket for SSL termination.
- [ ]  Create another EC2 instance as a proxy server. Migrate the SSL certificate to the new instance and configure it to direct connections to the existing EC2 instances.
- [x]  Import the SSL certificate into AWS Certificate Manager (ACM). Create an Application Load Balancer with an HTTPS listener that uses the SSL certificate from ACM.


**[⬆ Back to Top](#table-of-contents)**

### A web application must persist order data to Amazon S3 to support neat-real time processing. A solutions architect needs create an architecture that is both scalable and fault tolerant.Which solutions meet these requirements? (Choose two.)
- [ ]   Write the order event to an Amazon DynamoDB table. Use DynamoDB Streams to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [x]  Write the order event to an Amazon Simple Queue Service (Amazon SQS) queue. Use the queue to trigger an AWSLambda function that parsers the payload and writes the data to Amazon S3.
- [ ]  Write the order event to an Amazon Simple Notification Service (Amazon SNS) topic
- [ ] Use the SNS topic to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [x]  Write the order event to an Amazon Simple Queue Service (Amazon SQS) queue. Use an Amazon EventBridge (Amazon CloudWatch Events) rule to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [ ] Write the order event to an Amazon Simple Notification Service (Amazon SNS) topi
- [ ]  Use an Amazon EventBridge (Amazon CloudWatch Events) rule to trigger an AWS Lambda function that parses the payload andwrites the data to Amazon S3.

### A company has an application hosted on Amazon EC2 instances in two VPCs across different AWS Regions. To communicate with each other, the instances use the internet for connectivity. The security team wants to ensure that no communication between the instances happens over the internet.What should a solutions architect do to accomplish this?
- [ ]   Create a NAT gateway and update the route table of the EC2 instancesג€™ subnet.
- [ ]  Create a VPC endpoint and update the route table of the EC2 instancesג€™ subnet.
- [ ]  Create a VPN connection and update the route table of the EC2 instancesג€™ subnet.
- [x]  Create a VPC peering connection and update the route table of the EC2 instancesג€™ subnet.

**[⬆ Back to Top](#table-of-contents)**

### A company is developing a new machine learning model solution in AWS. The models are developed as independent microservices that fetch about 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent. The company provides models to hundreds of users. The usage patterns for the models are irregular Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time. Which solution meets these requirements?
- [ ] The requests from the API are sent to an Application Load Balancer (ALB). Models are deployed as AWS Lambda functions invoked by the ALB.
- [ ] The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as AWS Lambda functions triggered by SQS events AWS Auto Scaling is enabled on Lambda to increase the number of vCPUs based on the SQS queue size.
- [ ] The requests from the API are sent to the model's Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS App Mesh scales the instances of the ECS cluster based on the SQS queue size.
- [x] The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS Auto Scaling is enabled on Amazon ECS for both the cluster and copies of the service based on the queue size.


**[⬆ Back to Top](#table-of-contents)**

### A company runs a web application on Amazon EC2 instances in an Auto Scaling group that has a target group. The company designed the application to work with session affinity (sticky sessions) for a better user experience. The application must be available publicly over the internet as an endpoint. A WAF must be applied to the endpoint for additional security. Session affinity (sticky sessions) must be configured on the endpoint. Which combination of steps will meet these requirements? (Choose two.)

- [ ] Create a public Network Load Balancer. Specify the application target group.
- [ ] Create a Gateway Load Balancer. Specify the application target group.
- [x] Create a public Application Load Balancer. Specify the application target group.
- [ ] Create a second target group. Add Elastic IP addresses to the EC2 instances.
- [x] Create a web ACL in AWS WAF. Associate the web ACL with the endpoint


**[⬆ Back to Top](#table-of-contents)**

### A company runs a web application on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer that has sticky sessions enabled. The web server currently hosts the user session state. The company wants to ensure high availability and avoid user session state loss in the event of a web server outage. Which solution will meet these requirements? 

- [ ]  Use an Amazon ElastiCache for Memcached instance to store the session dat- [  ] Update the application to use ElastiCache for Memcached to store the session state. 
- [x]  Use Amazon ElastiCache for Redis to store the session state. Update the application to use ElastiCache for Redis to store the session state. 
- [ ]  Use an AWS Storage Gateway cached volume to store session data. Update the application to use AWS Storage Gateway cached volume to store the session state. 
- [ ]  Use Amazon RDS to store the session state. Update the application to use Amazon RDS to store the session state. 

**[⬆ Back to Top](#table-of-contents)**


### A company is designing a web application with an internet-facing Application Load Balancer (ALB). The company needs the ALB to receive HTTPS web traffic from the public internet. The ALB must send only HTTPS traffic to the web application servers hosted on the Amazon EC2 instances on port 443. The ALB must perform a health check of the web application servers over HTTPS on port 8443. Which combination of configurations of the security group that is associated with the ALB will meet these requirements? (Choose three.)

- [x] Allow HTTPS inbound traffic from 0.0.0.0/0 for port 443.
- [ ] Allow all outbound traffic to 0.0.0.0/0 for port 443.
- [x] Allow HTTPS outbound traffic to the web application instances for port 443.
- [ ] Allow HTTPS inbound traffic from the web application instances for port 443.
- [x] Allow HTTPS outbound traffic to the web application instances for the health check on port 8443.
- [ ] Allow HTTPS inbound traffic from the web application instances for the health check on port 8443.

**[⬆ Back to Top](#table-of-contents)**


### A company hosts an application on AWS. The application gives users the ability to upload photos and store the photos in an Amazon S3 bucket. The company wants to use Amazon CloudFront and a custom domain name to upload the photo files to the S3 bucket in the eu-west-1 Region. Which solution will meet these requirements? (Choose two.)

- [x] Use AWS Certificate Manager (ACM) to create a public certificate in the us-east-1 Region. Use the certificate in CloudFront. Most Voted
- [ ] Use AWS Certificate Manager (ACM) to create a public certificate in eu-west-1. Use the certificate in CloudFront.
- [ ] Configure Amazon S3 to allow uploads from CloudFront. Configure S3 Transfer Acceleration.
- [x] Configure Amazon S3 to allow uploads from CloudFront origin access control (OAC). Most Voted
- [ ] Configure Amazon S3 to allow uploads from CloudFront. Configure an Amazon S3 website endpoint.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company wants to collect user clickstream data from the company's website for real-time analysis. The website experiences fluctuating traffic patterns throughout the day. The company needs a scalable solution that can adapt to varying levels of traffic. Which solution will meet these requirements?

- [x] Use a data stream in Amazon Kinesis Data Streams in on-demand mode to capture the clickstream data. Use AWS Lambda to process the data in real time.
- [ ] Use Amazon Kinesis Data Firehose to capture the clickstream data. Use AWS Glue to process the data in real time.
- [ ] Use Amazon Kinesis Video Streams to capture the clickstream data. Use AWS Glue to process the data in real time.
- [ ] Use Amazon Managed Service for Apache Flink (previously known as Amazon Kinesis Data Analytics) to capture the clickstream data. Use AWS Lambda to process the data in real time.

**[⬆ Back to Top](#table-of-contents)**


### A global company runs its workloads on AWS. The company's application uses Amazon S3 buckets across AWS Regions for sensitive data storage and analysis. The company stores millions of objects in multiple S3 buckets daily. The company wants to identify all S3 buckets that are not versioning-enable- [ ]  Which solution will meet these requirements?

- [ ] Set up an AWS CloudTrail event that has a rule to identify all S3 buckets that are not versioning-enabled across Regions.
- [x] Use Amazon S3 Storage Lens to identify all S3 buckets that are not versioning-enabled across Regions.
- [ ] Enable IAM Access Analyzer for S3 to identify all S3 buckets that are not versioning-enabled across Regions.
- [ ] Create an S3 Multi-Region Access Point to identify all S3 buckets that are not versioning-enabled across Regions.

**[⬆ Back to Top](#table-of-contents)**

### A company's infrastructure consists of hundreds of Amazon EC2 instances that use Amazon Elastic Block Store (Amazon EBS) storage. A solutions architect must ensure that every EC2 instance can be recovered after a disaster. What should the solutions architect do to meet this requirement with the LEAST amount of effort?

- [ ] Take a snapshot of the EBS storage that is attached to each EC2 instance. Create an AWS CloudFormation template to launch new EC2
instances from the EBS storage.
- [ ] Take a snapshot of the EBS storage that is attached to each EC2 instance. Use AWS Elastic Beanstalk to set the environment based on the
EC2 template and attach the EBS storage.
- [x] Use AWS Backup to set up a backup plan for the entire group of EC2 instances. Use the AWS Backup API or the AWS CLI to speed up the
restore process for multiple EC2 instances.
- [ ] Create an AWS Lambda function to take a snapshot of the EBS storage that is attached to each EC2 instance and copy the Amazon
Machine Images (AMIs). Create another Lambda function to perform the restores with the copied AMIs and attach the EBS storage.

**[⬆ Back to Top](#table-of-contents)**

### A company recently migrated to the AWS Clou- [ ]  The company wants a serverless solution for large-scale parallel on-demand processing of asemistructured dataset. The data consists of logs, media files, sales transactions, and IoT sensor data that is stored in Amazon S3. The company wants the solution to process thousands of items in the dataset in parallel. Which solution will meet these requirements with the MOST operational efficiency?

- [ ]  Use the AWS Step Functions Map state in Inline mode to process the data in parallel.
- [x]  Use the AWS Step Functions Map state in Distributed mode to process the data in parallel.
- [ ]  Use AWS Glue to process the data in parallel.
- [ ]  Use several AWS Lambda functions to process the data in parallel.
  
**[⬆ Back to Top](#table-of-contents)**

### A company will migrate 10 PB of data to Amazon S3 in 6 weeks. The current data center has a 500 Mbps uplink to the internet. Other on-premises applications share the uplink. The company can use 80% of the internet bandwidth for this one-time migration task. Which solution will meet these requirements?

- [ ] Configure AWS DataSync to migrate the data to Amazon S3 and to automatically verify the dat- [ ]  
- [ ] Use rsync to transfer the data directly to Amazon S3.
- [ ] Use the AWS CLI and multiple copy processes to send the data directly to Amazon S3.
- [x] Order multiple AWS Snowball devices. Copy the data to the devices. Send the devices to AWS to copy the data to Amazon S3.

**[⬆ Back to Top](#table-of-contents)**

### A company has several on-premises Internet Small Computer Systems Interface (ISCSI) network storage servers. The company wants to reducethe number of these servers by moving to the AWS Clou- [ ]  A solutions architect must provide low-latency access to frequently used data and reduce the dependency on on-premises servers with a minimal number of infrastructure changes. Which solution will meet these requirements?
- [ ]  Deploy an Amazon S3 File Gateway.
- [ ]  Deploy Amazon Elastic Block Store (Amazon EBS) storage with backups to Amazon S3.
- [ ]  Deploy an AWS Storage Gateway volume gateway that is configured with stored volumes.
- [x]  Deploy an AWS Storage Gateway volume gateway that is configured with cached volumes.

**[⬆ Back to Top](#table-of-contents)**

### A solutions architect is designing an application that will allow business users to upload objects to Amazon S3. The solution needs to maximize object durability. Objects also must be readily available at any time and for any length of time. Users will access objects  requently within the first 30 days after the objects are uploaded, but users are much less likely to access objects that are older than 30 days. Which solution meets these requirements MOST cost-effectively?

- [ ]  Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Glacier after 30 days.
- [x]  Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA)
after 30 days.
- [ ]  Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 One Zone-Infrequent Access (S3 One Zone-IA)
after 30 days.
- [ ]  Store all the objects in S3 Intelligent-Tiering with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3
Standard-IA) after 30 days.

**[⬆ Back to Top](#table-of-contents)**

###  A company has migrated a two-tier application from its on-premises data center to the AWS Clou- [ ]  The data tier is a Multi-AZ deployment of Amazon RDS for Oracle with 12 TB of General Purpose SSD Amazon Elastic Block Store (Amazon EBS) storage. The application is  designed to process and store documents in the database as binary large objects (blobs) with an average document size of 6 M- [ ]  The database size has grown over time, reducing the performance and increasing the cost of storage. The company must improve the database performance and needs a solution that is highly available and resilient. Which solution will meet these requirements MOST cost-effectively?

- [ ]  Reduce the RDS DB instance size. Increase the storage capacity to 24 Ti- [ ]  Change the storage type to Magneti- [ ] 
- [ ] Increase the RDS DB instance size. Increase the storage capacity to 24 TiChange the storage type to Provisioned IOPS.
- [x]  Create an Amazon S3 bucket. Update the application to store documents in the S3 bucket. Store the object metadata in the existing
database.
- [ ]  Create an Amazon DynamoDB table. Update the application to use DynamoD- [ ]  Use AWS Database Migration Service (AWS DMS) to migrate
data from the Oracle database to DynamoDb

**[⬆ Back to Top](#table-of-contents)**

### Cost Explorer is showing charges higher than expected for Amazon Elastic Block Store (Amazon EBS) volumes connected to application servers in a production account. A significant portion of the charges from Amazon EBS are from volumes that were created as Provisioned IOPS SSD (io2) volume types. Controlling costs is the highest priority for this application.  Which steps should the user take to analyze and reduce the EBS costs without incurring any application downtime? (Select TWO.)

- [ ] Use the Amazon EC2 ModifyInstanceAttribute action to enable EBS optimization on the application server instances. 

- [x] Use the Amazon CloudWatch GetMetricData action to evaluate the read/write operations and read/write bytes of each volume.

- [ ] Use the Amazon EC2 ModifyVolume action to reduce the size of the underutilized io2 volumes.

- [x] Use the Amazon EC2 ModifyVolume action to change the volume type of the underutilized io2 volumes to General Purpose SSD (gp3).
- [ ] Use an Amazon S3 PutBucketPolicy action to migrate existing volume snapshots to Amazon S3 Glacier Flexible Retrieval.

**[⬆ Back to Top](#table-of-contents)**

### A company is creating a three-tier web application consisting of a web server, an application server, and a database server. The application will track GPS coordinates of packages as they are being delivere- [ ]  The application will update the database every 0.5 seconds. The tracking will need to be read as fast as possible for users to check the status of their packages. Only a few packages might be tracked on some days, whereas millions of packages might be tracked on other days. Tracking will need to be searchable by tracking ID, customer ID, and order I- [ ]  Orders older than 1 month no longer need to be tracke- [ ]  What should a solutions architect recommend to accomplish this with minimal total cost of ownership?

- [ ] Use Amazon DynamoD- [ ]  Activate Auto Scaling for the DynamoDB table. Schedule an automatic deletion script for items older than 1 month.
- [x] Use Amazon DynamoDB with global secondary indexes. Activate Auto Scaling for the DynamoDB table and the global secondary indexes. Turn on TTL for the DynamoDB table.
- [ ] Use an Amazon RDS On-Demand Instance with Provisioned IOPS (PIOPS). Configure Amazon CloudWatch alarms to send notifications when PIOPS are exceede- [ ]  Increase and decrease PIOPS as neede- [ ] 
- [ ] Use an Amazon RDS Reserved Instance with Provisioned IOPS (PIOPS). Configure Amazon CloudWatch alarms to send notifications when PIOPS are exceede- [ ]  Increase and decrease PIOPS as neede- [ ] 

**[⬆ Back to Top](#table-of-contents)**

### A company is designing a website that will be hosted on Amazon S3. How should users be prevented from linking directly to the assets in the S3 bucket?

- [ ] Create a static website, then update the bucket policy to require users to access the resources with the static website URL.
- [x] Create an Amazon CloudFront distribution with an origin access control (OAC) and update the bucket policy to grant permission to the OAC only.
- [ ] Create a static website, then configure an Amazon Route 53 record set with an alias pointing to the static website. Provide this URL to users.
- [ ] Create an Amazon CloudFront distribution with an AWS WAF web ACL that permits access to the origin server through the distribution only.

**[⬆ Back to Top](#table-of-contents)**

### A company has a well-architected application that streams audio data by using UDP in the AWS Clou- [ ]  The company hosts the application in the eu-central-1 Region. The company plans to offer services to North American users. A solutions architect must improve application network performance for the North American users. Which of the following is the MOST cost-effective solution?

- [x] Create an AWS Global Accelerator standard accelerator with an endpoint group in eu-central-1.
- [ ] Use AWS CloudFormation to deploy additional application infrastructure in the us-east-1 Region and the us-west-1 Region.
- [ ] Use AWS CloudFormation to deploy additional application infrastructure in the us-east-1 Region and the us-west-1 Region.
- [ ] Configure the application to use an Amazon Route 53 latency-based routing policy.

**[⬆ Back to Top](#table-of-contents)**


### A company's cloud operations team wants to standardize resource remediation. The company wants to provide a standard set of governance evaluations and remediations to all member accounts in its organization in AWS Organizations. Which self-managed AWS service can the company use to meet these requirements with the LEAST amount of operational effort?
- [ ] AWS Security Hub compliance standards
- [x] AWS Config conformance packs
- [ ] AWS CloudTrail
- [ ] AWS Trusted Advisor

**[⬆ Back to Top](#table-of-contents)**

### A company is designing a website that will be hosted on Amazon S3.How should users be prevented from linking directly to the assets in the S3 bucket?

- [ ] Create a static website, then update the bucket policy to require users to access the resources with the static website URL.
- [x] Create an Amazon CloudFront distribution with an origin access control (OAC) and update the bucket policy to grant permission to the OAC only.
- [ ] Create a static website, then configure an Amazon Route 53 record set with an alias pointing to the static website. Provide this URL to users.
- [ ] Create an Amazon CloudFront distribution with an AWS WAF web ACL that permits access to the origin server through the distribution only.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to build an immutable infrastructure for its software applications. The company wants to test the software applications before sending traffic to them. The company seeks an efficient solution that limits the effects of application bugs.Which combination of steps should a solutions architect recommend? (Select TWO.)
- [ ] Use AWS CloudFormation to update the production infrastructure and roll back the stack if the update fails.
- [x] Apply Amazon Route 53 weighted routing to test the staging environment and gradually increase the traffic as the tests pass.
- [ ] Apply Amazon Route 53 failover routing to test the staging environment and fail over to the production environment if the tests pass.
- [x] Use AWS CloudFormation with a parameter set to the staging value in a separate environment other than the production environment.
- [ ] Use AWS CloudFormation to deploy the staging environment with a snapshot deletion policy and reuse the resources in the production environment if the tests pass.

**[⬆ Back to Top](#table-of-contents)**

### Cost Explorer is showing charges higher than expected for Amazon Elastic Block Store (Amazon EBS) volumes connected to application servers in a production account. A significant portion of the charges from Amazon EBS are from volumes that were created as Provisioned IOPS SSD (io2) volume types. Controlling costs is the highest priority for this application. Which steps should the user take to analyze and reduce the EBS costs without incurring any application downtime? (Select TWO.)
- [x] Use the Amazon EC2 ModifyInstanceAttribute action to enable EBS optimization on the application server instances.
- [ ] Use the Amazon CloudWatch GetMetricData action to evaluate the read/write operations and read/write bytes of each volume.
- [ ] Use the Amazon EC2 ModifyVolume action to reduce the size of the underutilized io2 volumes.
- [x] Use the Amazon EC2 ModifyVolume action to change the volume type of the underutilized io2 volumes to General Purpose SSD (gp3).
- [ ] Use an Amazon S3 PutBucketPolicy action to migrate existing volume snapshots to Amazon S3 Glacier Flexible Retrieval.

**[⬆ Back to Top](#table-of-contents)**

### A company designs a mobile app for its customers to upload photos to a website. The app needs a secure login with multi-factor authentication (MFA). The company wants to limit the initial build time and the maintenance of the solution. Which solution should a solutions architect recommend to meet these requirements?
- [x] Use Amazon Cognito Identity with SMS-based MF- [ ]  
- [ ] Edit IAM policies to require MFA for all users.
- [ ] Federate IAM against the corporate Active Directory that requires MF- [ ]  
- [ ] Use Amazon API Gateway and require server-side encryption (SSE) for photos.

**[⬆ Back to Top](#table-of-contents)**

### An application running in a private subnet accesses an Amazon DynamoDB table. The data cannot leave the AWS network to meet security requirements. How should this requirement be met?
- [ ] Configure a network ACL on DynamoDB to limit traffic to the private subnet.
- [ ] Enable DynamoDB encryption at rest using an AWS Key Management Service (AWS KMS) key.
- [ ] Add a NAT gateway and configure the route table on the private subnet.
- [x] Create a VPC endpoint for DynamoDB and configure the endpoint policy. 

**[⬆ Back to Top](#table-of-contents)**

### A company is planning to use Amazon S3 to store images uploaded by its users. The images must be encrypted at rest in Amazon S3. The company does not want to spend time managing and rotating the keys, but it does want to control who can access those keys. What should a solutions architect use to accomplish this?
- [ ] Server-Side Encryption with encryption keys stored in an S3 bucket
- [ ] Server-Side Encryption with Customer-Provided Keys (SSE-C)
- [ ] Server-Side Encryption with encryption keys stored in AWS Systems Manager Parameter Store
- [x] Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)

**[⬆ Back to Top](#table-of-contents)**

### A company's legacy application is currently relying on a single-instance Amazon RDS MySQL database without encryption. Due to new compliance requirements, all existing and new data in this database must be encrypte- [ ]  How should this be accomplished?
- [ ] Create an Amazon S3 bucket with server-side encryption turned on. Move all the data to Amazon S3. Delete the RDS instance.
- [ ] Configure RDS Multi-AZ mode with encryption at rest turned on. Perform a failover to the standby instance to delete the original instance.
- [x] Take a snapshot of the RDS instance. Create an encrypted copy of the snapshot. Restore the RDS instance from the encrypted snapshot.
- [ ] Create an RDS read replica with encryption at rest turned on. Promote the read replica to primary and switch the application over to the new primary. Delete the old RDS instance.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company is preparing to deploy a web application on AWS to ensure continuous service for customers. The architecture includes a web application that the company hosts on Amazon EC2 instances, a relational database in Amazon RDS, and static assets that the company stores in Amazon S3. The company wants to design a robust and resilient architecture for the application. Which solution will meet these requirements?

- [ ] Deploy Amazon EC2 instances in a single Availability Zone. Deploy an RDS DB instance in the same Availability Zone. Use Amazon S3 with versioning enabled to store static assets.
- [x] Deploy Amazon EC2 instances in an Auto Scaling group across multiple Availability Zones. Deploy a Multi-AZ RDS DB instance. Use Amazon CloudFront to distribute static assets.
- [ ] Deploy Amazon EC2 instances in a single Availability Zone. Deploy an RDS DB instance in a second Availability Zone for cross-AZ redundancy. Serve static assets directly from the EC2 instances.
- [ ] Use AWS Lambda functions to serve the web application. Use Amazon Aurora Serverless v2 for the database. Store static assets in Amazon Elastic File System (Amazon EFS) One Zone-Infrequent Access (One Zone-IA).

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company runs several internal applications in multiple AWS accounts. The company uses AWS Organizations to manage its AWS accounts. A security appliance in the company’s networking account must inspect interactions between applications across AWS accounts. Which solution will meet these requirements?

- [ ] Deploy a Network Load Balancer (NLB) in the networking account to send traffic to the security appliance. Configure the application accounts to send traffic to the NLB by using an interface VPC endpoint in the application accounts.
- [ ] Deploy an Application Load Balancer (ALB) in the application accounts to send traffic directly to the security appliance.
- [x] Deploy a Gateway Load Balancer (GWLB) in the networking account to send traffic to the security appliance. Configure the application accounts to send traffic to the GWLB by using an interface GWLB endpoint in the application accounts.
- [ ] Deploy an interface VPC endpoint in the application accounts to send traffic directly to the security appliance.

**[⬆ Back to Top](#table-of-contents)**

### A company runs its production workload on an Amazon Aurora MySQL DB cluster that includes six Aurora Replicas. The company wants near-real-lime reporting queries from one of its departments to be automatically distributed across three of the Aurora Replicas. Those three replicas have a different compute and memory specification from the rest of the DB cluster.Which solution meets these requirements?
- [x]   Create and use a custom endpoint for the workload
- [ ]  Create a three-node cluster clone and use the reader endpoint.
- [ ]  Use any of the instance endpoints for the selected three nodes.
- [ ]  Use the reader endpoint to automatically distribute the read-only workloa- 

### A company has a well-architected application that streams audio data by using UDP in the AWS Clou- [ ]  The company hosts the application in the eu-central-1 Region. The company plans to offer services to North American users. A solutions architect must improve application network performance for the North American users. Which of the following is the MOST cost-effective solution?

- [x] Create an AWS Global Accelerator standard accelerator with an endpoint group in eu-central-1.
- [ ] Use AWS CloudFormation to deploy additional application infrastructure in the us-east-1 Region and the us-west-1 Region.
- [ ] Use AWS CloudFormation to deploy additional application infrastructure in the us-east-1 Region and the us-west-1 Region.
- [ ] Configure the application to use an Amazon Route 53 latency-based routing policy.

**[⬆ Back to Top](#table-of-contents)**

### A company has multiple applications that use Amazon RDS for MySQL as is database. The company recently discovered that a new custom reporting application has increased the number of Queries on the database. This is slowing down performance.How should a solutions architect resolve this issue with the LEAST amount of application changes?
- [ ]   Add a secondary DB instance using Multi-AZ.
- [x]  Set up a road replica and Multi-AZ on Amazon RDS.
- [ ]  Set up a standby replica and Multi-AZ on Amazon RDS.
- [ ]  Use caching on Amazon RDS to improve the overall performance.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to automate the security assessment of its Amazon EC2 instances. The company needs to validate and demonstrate that security and compliance standards are being followed throughout the development process.What should a solutions architect do to meet these requirements?
- [ ]   Use Amazon Macie to automatically discover, classify and protect the EC2 instances.
- [ ]  Use Amazon GuardDuty to publish Amazon Simple Notification Service (Amazon SNS) notifications.
- [x]  Use Amazon Inspector with Amazon CloudWatch to publish Amazon Simple Notification Service (Amazon SNS) notifications
- [ ]  Use Amazon EventBridge (Amazon CloudWatch Events) to detect and react to changes in the status of AWS Trusted Advisor checks.

**[⬆ Back to Top](#table-of-contents)**

### A company stores 200 GB of data each month in Amazon S3. The company needs to perform analytics on this data at the end of each month to determine the number of items sold in each sales region for the previous month.Which analytics strategy is MOST cost-effective for the company to use?
- [ ]   Create an Amazon Elasticsearch Service (Amazon ES) cluster. Query the data in Amazon ES. Visualize the data by using Kiban- [ ]  
- [x]  Create a table in the AWS Glue Data Catalog. Query the data in Amazon S3 by using Amazon Athen- [ ]   Visualize the data in Amazon QuickSight.
- [ ]  Create an Amazon EMR cluster. Query the data by using Amazon EMR, and store the results in Amazon S3. Visualize the data in Amazon QuickSight.
- [ ]  Create an Amazon Redshift cluster. Query the data in Amazon Redshift, and upload the results to Amazon S3. Visualize the data in Amazon QuickSight.

### A company's cloud operations team wants to standardize resource remediation. The company wants to provide a standard set of governance evaluations and remediations to all member accounts in its organization in AWS Organizations. Which self-managed AWS service can the company use to meet these requirements with the LEAST amount of operational effort?
- [ ] AWS Security Hub compliance standards
- [x] AWS Config conformance packs
- [ ] AWS CloudTrail
- [ ] AWS Trusted Advisor

**[⬆ Back to Top](#table-of-contents)**

### A company is designing a website that will be hosted on Amazon S3.How should users be prevented from linking directly to the assets in the S3 bucket?

- [ ] Create a static website, then update the bucket policy to require users to access the resources with the static website URL.
- [x] Create an Amazon CloudFront distribution with an origin access control (OAC) and update the bucket policy to grant permission to the OAC only.
- [ ] Create a static website, then configure an Amazon Route 53 record set with an alias pointing to the static website. Provide this URL to users.
- [ ] Create an Amazon CloudFront distribution with an AWS WAF web ACL that permits access to the origin server through the distribution only.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to build an immutable infrastructure for its software applications. The company wants to test the software applications before sending traffic to them. The company seeks an efficient solution that limits the effects of application bugs.Which combination of steps should a solutions architect recommend? (Select TWO.)
- [ ] Use AWS CloudFormation to update the production infrastructure and roll back the stack if the update fails.
- [x] Apply Amazon Route 53 weighted routing to test the staging environment and gradually increase the traffic as the tests pass.
- [ ] Apply Amazon Route 53 failover routing to test the staging environment and fail over to the production environment if the tests pass.
- [x] Use AWS CloudFormation with a parameter set to the staging value in a separate environment other than the production environment.
- [ ] Use AWS CloudFormation to deploy the staging environment with a snapshot deletion policy and reuse the resources in the production environment if the tests pass.

**[⬆ Back to Top](#table-of-contents)**

### Cost Explorer is showing charges higher than expected for Amazon Elastic Block Store (Amazon EBS) volumes connected to application servers in a production account. A significant portion of the charges from Amazon EBS are from volumes that were created as Provisioned IOPS SSD (io2) volume types. Controlling costs is the highest priority for this application. Which steps should the user take to analyze and reduce the EBS costs without incurring any application downtime? (Select TWO.)
- [x] Use the Amazon EC2 ModifyInstanceAttribute action to enable EBS optimization on the application server instances.
- [ ] Use the Amazon CloudWatch GetMetricData action to evaluate the read/write operations and read/write bytes of each volume.
- [ ] Use the Amazon EC2 ModifyVolume action to reduce the size of the underutilized io2 volumes.
- [x] Use the Amazon EC2 ModifyVolume action to change the volume type of the underutilized io2 volumes to General Purpose SSD (gp3).
- [ ] Use an Amazon S3 PutBucketPolicy action to migrate existing volume snapshots to Amazon S3 Glacier Flexible Retrieval.

**[⬆ Back to Top](#table-of-contents)**


### A company wants to move its on-premises network, attached storage (NAS) to AWS. The company wants to make the data available to any Linux instances within its VPC and ensure changes are automatically synchronized across all instances accessing the data store. The majority of the data is accessed very rarely, and some files are accessed by multiple users at the same time.Which solution meets these requirements and is MOST cost-effective?
- [ ]   Create an Amazon Elastic Block Store (Amazon EBS) snapshot containing the dat- [ ]   Share it with users within the VP- [ ] 
- [ ]  Create an Amazon S3 bucket that has a lifecycle policy set to transition the data to S3 Standard-Infrequent Access (S3 Standard-IA) after the appropriate number of days.
- [ ]  Create an Amazon Elastic File System (Amazon EFS) file system within the VP- [ ]  Set the throughput mode to Provisioned and to the required amount of IOPS to support concurrent usage.
- [x]  Create an Amazon Elastic File System (Amazon EFS) file system within the VP- [ ]  Set the lifecycle policy to transition the data to EFS Infrequent Access (EFS IA) after the appropriate number of days.


**[⬆ Back to Top](#table-of-contents)**

### A company plans to host a survey website on AWS. The company anticipates an unpredictable amount of traffi- [ ]  This traffic results in asynchronous updates to the database. The company wants to ensure that writes to the database hosted on AWS do not get droppe- [ ] How should the company write its application to handle these database requests?
- [ ]   Configure the application to publish to an Amazon Simple Notification Service (Amazon SNS) topi- [ ]  Subscribe the database to the SNS topi- [ ] 
- [ ]  Configure the application to subscribe to an Amazon Simple Notification Service (Amazon SNS) topi- [ ]  Publish the database updates to the SNS topi- [ ] 
- [ ]  Use Amazon Simple Queue Service (Amazon SQS) FIFO queues to queue the database connection until the database has resources to write the dat- [ ]  
- [x]  Use Amazon Simple Queue Service (Amazon SQS) FIFO queues for capturing the writes and draining the queue as each write is made to the database.


**[⬆ Back to Top](#table-of-contents)**

### A company that recently started using AWS establishes a Site-to-Site VPN between its on-premises datacenter and AWS. The company's security mandate states that traffic originating from on premises should stay within the companyג€™s private IP space when communicating with an Amazon Elastic Container Service(Amazon ECS) cluster that is hosting a sample web application.Which solution meets this requirement?
- [ ]   Configure a gateway endpoint for Amazon ECS. Modify the route table to include an entry pointing to the ECS cluster.
- [ ]  Create a Network Load Balancer and AWS PrivateLink endpoint for Amazon ECS in the same VPC that is hosting the ECS cluster.
- [x]  Create a Network Load Balancer in one VPC and an AWS PrivateLink endpoint for Amazon ECS in another VP- [ ]  Connect the two VPCs by using VPC peering.
- [ ]  Configure an Amazon Route 53 record with Amazon ECS as the target. Apply a server certificate to Route 53 from AWS Certificate Manager (ACM) for SSL offloading.


**[⬆ Back to Top](#table-of-contents)**

### A solutions architect must analyze and update a companyג€™s existing IAM policies prior to deploying a new workloa- [ ]  The solutions architect created the following policy:What is the net effect of this policy?
- [ ]   Users will be allowed all actions except s3:PutObject if multi-factor authentication (MFA) is enable- [ ] 
- [ ]  Users will be allowed all actions except s3:PutObject if multi-factor authentication (MFA) is not enable- [ ] 
- [ ]  Users will be denied all actions except s3:PutObject if multi-factor authentication (MFA) is enable- [ ] 
- [x]  Users will be denied all actions except s3:PutObject if multi-factor authentication (MFA) is not enabled


**[⬆ Back to Top](#table-of-contents)**

### A company is running a multi-tier web application on premises. The web application is containerized and runs on a number of Linux hosts connected to aPostgreSQL database that contains user records. The operational overhead of maintaining the infrastructure and capacity planning is limiting the companyג€™s growth. A solutions architect must improve the applicationג€™s infrastructure.Which combination of actions should the solutions architect take to accomplish this? (Choose two.)
- [x]   Migrate the PostgreSQL database to Amazon Auror- [ ]  
- [ ]  Migrate the web application to be hosted on Amazon EC2 instances.
- [ ]  Set up an Amazon CloudFront distribution for the web application content.
- [ ]  Set up Amazon ElastiCache between the web application and the PostgreSQL database.
- [x] Migrate the web application to be hosted on AWS Fargate with Amazon Elastic Container Service (Amazon ECS)

**[⬆ Back to Top](#table-of-contents)**

### An application allows users at a companyג€™s headquarters to access product dat- [ ]   The product data is stored in an Amazon RDS MySQL DB instance. The operations team has isolated an application performance slowdown and wants to separate read traffic from write traffic  A solutions architect needs to optimize the applicationג€™s performance quickly.What should the solutions architect recommend?
- [ ]   Change the existing database to a Multi-AZ deployment. Serve the read requests from the primary Availability Zone.
- [ ]  Change the existing database to a Multi-AZ deployment. Serve the read requests from the secondary Availability Zone.
- [ ]  Create read replicas for the database. Configure the read replicas with half of the compute and storage resources as the source database.
- [x]  Create read replicas for the database. Configure the read replicas with the same compute and storage resources as the source database.

**[⬆ Back to Top](#table-of-contents)**

### A company is using Amazon DynamoDB with provisioned throughput for the database tier of its ecommerce website. During flash sales, customers experience periods of time when the database cannot handle the high number of transactions taking place. This causes the company to lose transactions. During normal periods, the database performs appropriately.Which solution solves the performance problem the company faces?
- [x]   Switch DynamoDB to on-demand mode during flash sales.
- [ ]  Implement DynamoDB Accelerator for fast in memory performance.
- [ ]  Use Amazon Kinesis to queue transactions for processing to DynamoD- [ ] 
- [ ]  Use Amazon Simple Queue Service (Amazon SQS) to queue transactions to DynamoD- [ ] 


**[⬆ Back to Top](#table-of-contents)**

### A company is reviewing a recent migration of a three-tier application to a VP- [ ]  The security team discovers that the principle of least privilege is not being applied to Amazon EC2 security group ingress and egress rules between the application tiers.What should a solutions architect do to correct this issue?
- [x]  Create security group rules using the instance ID as the source or destination.
- [ ]  Create security group rules using the security group ID as the source or destination.
- [ ]  Create security group rules using the VPC CIDR blocks as the source or destination.
- [ ]  Create security group rules using the subnet CIDR blocks as the source or destination

**[⬆ Back to Top](#table-of-contents)**

### A company requires that all versions of objects in its Amazon S3 bucket be retaine- [ ]  Current object versions will be frequently accessed during the first 30 days, after which they will be rarely accessed and must be retrievable within 5 minutes. Previous object versions need to be kept forever, will be rarely accessed, and can be retrieved within 1 week. All storage solutions must be highly available and highly durable.What should a solutions architect recommend to meet these requirements in the MOST cost-effective manner?
- [x]   Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 Glacier after 30 days and moves previous object versions to S3 Glacier after 1 day.
- [ ]  Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 Glacier after 30 days and moves previous object versions to S3 Glacier Deep Archive after 1 day.
- [ ]  Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 Standard-infrequent Access (S3 Standard-IA) after 30 days and moves previous object versions toS3 Glacier Deep Archive after 1 day.
- [ ]  Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 One Zone-Infrequent Access (S3 One Zone-IA) after 30 days and moves previous object versions to S3 Glacier Deep Archive after 1 day.

**[⬆ Back to Top](#table-of-contents)**

### A development team is collaborating with another company to create an integrated product. The other company needs to access an Amazon Simple QueueService (Amazon SQS) queue that is contained in the development team's account. The other company wants to poll the queue without giving up its own account permissions to do so.How should a solutions architect provide access to the SQS queue?
- [ ]   Create an instance profile that provides the other company access to the SQS queue.
- [ ]  Create an IAM policy that provides the other company access to the SQS queue.
- [x]  Create an SQS access policy that provides the other company access to the SQS queue.
- [ ]  Create an Amazon Simple Notification Service (Amazon SNS) access policy that provides the other company access to the SQS queue.


**[⬆ Back to Top](#table-of-contents)**

### A company is developing a video conversion application hosted on AWS. The application will be available in two tiers: a free tier and a paid tier. Users in the paid tier will have their videos converted first and then the tree tier users will have their videos converted. Which solution meets these requirements and is MOST cost-effective?
- [ ]   One FIFO queue for the paid tier and one standard queue for the free tier.
- [ ]  A single FIFO Amazon Simple Queue Service (Amazon SQS) queue for all file types.
- [ ]  A single standard Amazon Simple Queue Service (Amazon SQS) queue for all file types.
- [x]  Two standard Amazon Simple Queue Service (Amazon SQS) queues with one for the paid tier and one for the free tier.


**[⬆ Back to Top](#table-of-contents)**

### An administrator of a large company wants to monitor for and prevent any cryptocurrency-related attacks on the companyג€™s AWS accounts.Which AWS service can the administrator use to protect the company against attacks?
- [ ]   Amazon Cognito
- [x]  Amazon GuardDuty
- [ ]  Amazon Inspector
- [ ]  Amazon Macie

**[⬆ Back to Top](#table-of-contents)**

### A company has applications hosted on Amazon EC2 instances with IPv6 addresses. The applications must initiate communications with other external applications using the internet. However, the companyג€™'s security policy states that any external service cannot initiate a connection to the EC2 instances. What should a solutions architect recommend to resolve this issue?
- [ ]   Create a NAT gateway and make it the destination of the subnetג€™s route table.
- [ ]  Create an internet gateway and make it the destination of the subnetג€™s route table.
- [ ]  Create a virtual private gateway and make it the destination of the subnetג€™s route table.
- [x]  Create an egress-only internet gateway and make it the destination of the subnetג€™s route table.

**[⬆ Back to Top](#table-of-contents)**

### A company provides an online service for posting video content and transcoding it for use by any mobile platform. The application architecture uses AmazonElastic File System (Amazon EFS) Standard to collect and store the videos so that multiple Amazon EC2 Linux instances can access the video content for processing. As the popularity of the service has grown over time, the storage costs have become too expensive.Which storage solution is MOST cost-effective?
- [ ]   Use AWS Storage Gateway for files to store and process the video content.
- [ ]  Use AWS Storage Gateway for volumes to store and process the video content.
- [ ]  Use Amazon EFS for storing the video content. Once processing is complete, transfer the files to Amazon Elastic Block Store (Amazon EBS).
- [x]  Use Amazon S3 for storing the video content. Move the files temporarily over to an Amazon ElasticBlock Store (Amazon EBS) volume attached to the server for processing.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to host its web application on AWS using multiple Amazon EC2 instances across different AWS Regions. Since the application content will be specific to each geographic region, the client requests need to be routed to the server that hosts the content for that clients Region.What should a solutions architect do to accomplish this?
- [ ]   Configure Amazon Route 53 with a latency routing policy.
- [ ]  Configure Amazon Route 53 with a weighted routing policy.
- [x]  Configure Amazon Route 53 with a geolocation routing policy.
- [ ]  Configure Amazon Route 53 with a multivalue answer routing policy

**[⬆ Back to Top](#table-of-contents)**

### A solutions architect is planning the deployment of a new static website. The solution must minimize costs and provide at least 99% availability. Which solution meets these requirements?
- [x]   Deploy the application to an Amazon S3 bucket in one AWS Region that has versioning disable- [ ] 
- [ ]  Deploy the application to Amazon EC2 instances that run in two AWS Regions and two Availability Zones.
- [ ]  Deploy the application to an Amazon S3 bucket that has versioning and cross-Region replication enable- [ ] 
- [ ]  Deploy the application to an Amazon EC2 instance that runs in one AWS Region and one Availability Zone.

**[⬆ Back to Top](#table-of-contents)**

### A recently created startup built a three-tier web application. The front end has static content. The application layer is based on microservices. User data is stored as JSON documents that need to be accessed with low latency. The company expects regular traffic to be low during the first year, with peaks in traffic when it publicizes new features every month. The startup team needs to minimize operational overhead costs.What should a solutions architect recommend to accomplish this?
- [ ]   Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use AWS Elastic Beanstalk for the application layer. Use Amazon DynamoDB to store user dat- [ ]  
- [ ]  Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use Amazon Elastic KubernetesService (Amazon EKS) for the application layer. Use Amazon DynamoDB to store user dat- [ ]  
- [x]  Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use Amazon API Gateway and AWS Lambda functions for the application layer. Use Amazon DynamoDB to store user dat- [ ]  
- [ ]  Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use Amazon API Gateway and AWS Lambda functions for the application layer. Use Amazon RDS with read replicas to store user dat- [ ]  

**[⬆ Back to Top](#table-of-contents)**

### A company is building a payment application that must be highly available even during regional service disruptions. A solutions architect must design a data storage solution that can be easily replicated and used in other AWS Regions. The application also requires low-latency atomicity, consistency, isolation, and durability (ACID) transactions that need to be immediately available to generate reports The development team also needs to use SQL.Which data storage solution meets these requirements?
- [x]   Amazon Aurora Global Database
- [ ]  Amazon DynamoDB global tables
- [ ]  Amazon S3 with cross-Region replication and Amazon Athena
- [ ]  MySQL on Amazon EC2 instances with Amazon Elastic Block Store (Amazon EBS) snapshot replication

**[⬆ Back to Top](#table-of-contents)**

### A company stores call recordings on a monthly basis. Statistically, the recorded data may be referenced randomly within a year but accessed rarely after 1 year.Files that are newer than 1 year old must be queried and retrieved as quickly as possible. A delay in retrieving older files is acceptable. A solutions architect needs to store the recorded data at a minimal cost.Which solution is MOST cost-effective?
- [ ]   Store individual files in Amazon S3 Glacier and store search metadata in object tags created in S3 Glacier Query S3 Glacier tags and retrieve the files from S3 Glacier.
- [x]  Store individual files in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after1 year. Query and retrieve the files from Amazon S3 or S3 Glacier.
- [ ]  Archive individual files and store search metadata for each archive in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after 1 year. Query and retrieve the files by searching for metadata from Amazon S3.
- [ ]  Archive individual files in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after 1 year. Store search metadata in Amazon DynamoD- [ ]  Query the files from DynamoDB and retrieve them from Amazon S3 or S3 Glacier.

**[⬆ Back to Top](#table-of-contents)**

### A company is developing a new machine learning model solution in AWS. The models are developed as independent microservices that fetch about 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent.The company provides models to hundreds of users. The usage patterns for the models are irregular Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time.Which solution meets these requirements?
- [ ]   The requests from the API are sent to an Application Load Balancer (ALB). Models are deployed as AWS Lambda functions invoked by the AL- [ ] 
- [ ]  The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as AWS Lambda functions triggered by SQS events AWS Auto Scaling is enabled on Lambda to increase the number of vCPUs based on the SQS queue size.
- [ ]  The requests from the API are sent to the modelג€™s Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS App Mesh scales the instances of the ECS cluster based on the SQS queue size.
- [x]  The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS Auto Scaling is enabled on Amazon ECS for both the cluster and copies of the service based on the queue size


**[⬆ Back to Top](#table-of-contents)**

### A company has no existing file share services. A new project requires access to file storage that is mountable as a drive for on-premises desktops. The file server must authenticate users to an Active Directory domain before they are able to access the storage.Which service will allow Active Directory users to mount storage as a drive on their desktops?
- [ ]   Amazon S3 Glacier
- [ ]  AWS DataSync
- [ ]  AWS Snowball Edge
- [x]  AWS Storage Gateway

**[⬆ Back to Top](#table-of-contents)**

### A company is preparing to launch a public-facing web application in the AWS Clou- [ ]  The architecture consists of Amazon EC2 instances within a VPC behind anElastic Load Balancer (ELB). A third party service is used for the DNS. The companyג€™s solutions architect must recommend a solution to detect and protect against largescale DDoS attacks.Which solution meets these requirements?
- [ ]   Enable Amazon GuardDuty on the account.
- [ ]  Enable Amazon Inspector on the EC2 instances.
- [ ]  Enable AWS Shield and assign Amazon Route 53 to it.
- [x]  Enable AWS Shield Advanced and assign the ELB to it.


**[⬆ Back to Top](#table-of-contents)**

### A company has a custom application with embedded credentials that retrieves information from an Amazon RDS MySQL DB instance. Management says the application must be made more secure with the least amount of programming effort.What should a solutions architect do to meet these requirements?
- [ ]   Use AWS Key Management Service (AWS KMS) customer master keys (CMKs) to create keys. Configure the application to load the database credentials from AWS KMS. Enable automatic key rotation.
- [ ]  Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Secrets Manager. Configure the application to load the database credentials from Secrets Manager. Create an AWS Lambda function that rotates the credentials in Secret Manager.
- [x]  Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Secrets Manager. Configure the application to load the database credentials from Secrets Manager. Set up a credentials rotation schedule for the application user in the RDS for MySQL database using Secrets Manager.
- [ ]  Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Systems Manager Parameter Store. Configure the application to load the database credentials from Parameter Store. Set up a credentials rotation schedule for the application user in the RDS for MySQL database using Parameter Store.

**[⬆ Back to Top](#table-of-contents)**

A company is running a multi-tier web application on AWS. The application runs its database tier on Amazon Aurora MySQL. The application and database tiers are in the us-east-1 Region. A database administrator who regularly monitors the Aurora DB cluster finds that an intermittent increase in read traffic is creating high CPUutilization on the read replica and causing increased read latency of the application.What should a solutions architect do to improve read scalability?
- [ ]   Reboot the Aurora DB cluster.
- [ ]  Create a cross-Region read replica
- [ ]  Increase the instance class of the read replic- [ ]  
- [x]  Configure Aurora Auto Scaling for the read replic- [ ]  

**[⬆ Back to Top](#table-of-contents)**

### A companyג€™s order fulfillment service uses a MySQL database. The database needs to support a large number of concurrent queries and transactions. Developers are spending time patching and tuning the database This is causing delays in releasing new product features.The company wants to use cloud-based services to help address this new challenge. The solution must allow the developers to migrate the database with little or no code changes and must optimize performance.Which service should a solutions architect use to meet these requirements?
- [x]   Amazon Aurora
- [ ]  Amazon DynamoDB
- [ ]  Amazon ElastiCache
- [ ]  MySQL on Amazon EC2

**[⬆ Back to Top](#table-of-contents)**

### A company is planning to transfer multiple terabytes of data to AWS. The data is collected offline from ships. The company want to run complex transformation before transferring the dat- [ ]  Which AWS service should a solutions architect recommend for this migration?
- [ ]   AWS Snowball
- [ ]  AWS Snowmobile
- [ ]  AWS Snowball Edge Storage Optimize
- [x]  AWS Snowball Edge Compute Optimize


**[⬆ Back to Top](#table-of-contents)**

### A company is running an online transaction processing (OLTP) workload on AWS. This workload uses an unencrypted Amazon RDS DB instance in a Multi-AZ deployment. Daily database snapshots are taken from this instance.What should a solutions architect do to ensure the database and snapshots are always encrypted moving forward?
- [x]   Encrypt a copy of the latest DB snapshot. Replace existing DB instance by restoring the encrypted snapshot.
- [ ]  Create a new encrypted Amazon Elastic Block Store (Amazon EBS) volume and copy the snapshots to it. Enable encryption on the DB instance.
- [ ]  Copy the snapshots and enable encryption using AWS Key Management Service (AWS KMS). Restore encrypted snapshot to an existing DB instance.
- [ ]  Copy the snapshots to an Amazon S3 bucket that is encrypted using server-side encryption with AWS Key Management Service (AWS KMS) managed keys (SSE-KMS).

**[⬆ Back to Top](#table-of-contents)**

### A company is selling up an application to use an Amazon RDS MySQL DB instance. The database must be architected for high availability across AvailabilityZones and AWS Regions with minimal downtime.How should a solutions architect meet this requirement?
- [ ]   Set up an RDS MySQL Multi-AZ DB instance. Configure an appropriate backup window.
- [x]  Set up an RDS MySQL Multi-AZ DB instance. Configure a read replica in a different Region.
- [ ]  Set up an RDS MySQL Single-AZ DB instance. Configure a read replica in a different Region.
- [ ]  Set up an RDS MySQL Single-AZ DB instance. Copy automated snapshots to at least one other Region.


**[⬆ Back to Top](#table-of-contents)**

### A company hosts its web application on AWS using seven Amazon EC2 instances. The company requires that the IP addresses of all healthy EC2 instances be returned in response to DNS queries.Which policy should be used to meet this requirement?
- [ ]   Simple routing policy
- [ ]  Latency routing policy
- [x]  Multi-value routing policy
- [ ]  Geolocation routing policy


**[⬆ Back to Top](#table-of-contents)**

### A company has 700 TB of backup data stored in network attached storage (NAS) in its data center This backup data need to be accessible for infrequent regulatory requests and must be retained 7 years. The company has decided to migrate this backup data from its data center to AWS. The migration must be complete within 1 month. The company has 500 Mbps of dedicated bandwidth on its public internet connection available for data transfer.What should a solutions architect do to migrate and store the data at the LOWEST cost?
- [x]   Order AWS Snowball devices to transfer the dat- [ ]   Use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive.
- [ ]  Deploy a VPN connection between the data center and Amazon VP- [ ]  Use the AWS CLI to copy the data from on premises to Amazon S3 Glacier.
- [ ]  Provision a 500 Mbps AWS Direct Connect connection and transfer the data to Amazon S3. Use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive.
- [ ]  Use AWS DataSync to transfer the data and deploy a DataSync agent on premises. Use the DataSync task to copy files from the on-premises NAS storage to Amazon S3 Glacier.


**[⬆ Back to Top](#table-of-contents)**

### A company is preparing to deploy a data lake on AWS. A solutions architect must define the encryption strategy tor data at rest m Amazon S3/ The companyג€™s security policy states:✑ Keys must be rotated every 90 days.✑ Strict separation of duties between key users and key administrators must be implemente- [ ] ✑ Auditing key usage must be possible.What should the solutions architect recommend?
- [x]   Server-side encryption with AWS KMS managed keys (SSE-KMS) with customer managed customer master keys (CMKs)
- [ ]  Server-side encryption with AWS KMS managed keys (SSE-KMS) with AWS managed customer master keys (CMKs)
- [ ]  Server-side encryption with Amazon S3 managed keys (SSE-S3) with customer managed customer master keys (CMKs)
- [ ]  Server-side encryption with Amazon S3 managed keys (SSE-S3) with AWS managed customer master keys (CMKs)


**[⬆ Back to Top](#table-of-contents)**

### A company has an application that generates a large number of files, each approximately 5 MB in size. The files are stored in Amazon S3. Company policy requires the files to be stored for 4 years before they can be delete- [ ]  Immediate accessibility is always required as the files contain critical business data that is not easy to reproduce. The files are frequently accessed in the first 30 days of the object creation but are rarely accessed after the first 30 days.Which storage solution is MOST cost-effective?
- [ ]   Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Glacier 30 days from object creation. Delete the files 4 years after object creation.
- [ ]  Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 One Zone-Infrequent Access (S3 One Zone-IA) 30 days from object creation. Delete the files 4 years after object creation.
- [x]  Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Delete the files 4 years after object creation.
- [ ]  Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Move the files to S3 Glacier 4 years after object creation.

**[⬆ Back to Top](#table-of-contents)**

### A company previously migrated its data warehouse solution to AWS. The company also has an AWS Direct Connect connection. Corporate office users query the data warehouse using a visualization tool. The average size of a query returned by the data warehouse is 50 MB and each webpage sent by the visualization tool is approximately 500 K- [ ]  Result sets returned by the data warehouse are not cache- [ ] Which solution provides the LOWEST data transfer egress cost for the company?
- [ ]   Host the visualization tool on premises and query the data warehouse directly over the internet.
- [ ]  Host the visualization tool in the same AWS Region as the data warehouse. Access it over the internet.
- [ ]  Host the visualization tool on premises and query the data warehouse directly over a Direct Connect connection at a location in the same AWS Region.
- [x]  Host the visualization tool in the same AWS Region as the data warehouse and access it over a DirectConnect connection at a location in the same Region.

**[⬆ Back to Top](#table-of-contents)**

### A mobile gaming company runs application servers on Amazon EC2 instances. The servers receive updates from players every 15 minutes. The mobile game creates a JSON object of the progress made in the game since the last update, and sends the JSON object to an Application Load Balancer. As the mobile game is played, game updates are being lost. The company wants to create a durable way to get the updates in older.What should a solutions architect recommend to decouple the system?

- [ ]   Use Amazon Kinesis Data Streams to capture the data and store the JSON object in Amazon S3.
- [ ]  Use Amazon Kinesis Data Firehose to capture the data and store the JSON object in Amazon S3.
- [x]  Use Amazon Simple Queue Service (Amazon SQS) FIFO queues to capture the data and EC2 instances to process the messages in the queue.
- [ ]  Use Amazon Simple Notification Service (Amazon SNS) to capture the data and EC2 instances to process the messages sent to the Application Load Balancer.

**[⬆ Back to Top](#table-of-contents)**

### A company has an application that runs on Amazon EC2 instances within a private subnet in a VPC  The instances access data in an Amazon S3 bucket in the same AWS Region. The VPC contains a NAT gateway in a public subnet to access the S3 bucket. The company wants to reduce costs by replacing the NAT gateway without compromising security or redundancy. Which solution meets these requirements?

- [ ]  Replace the NAT gateway with a NAT instance.
- [ ]  Replace the NAT gateway with an internet gateway.
- [x]  Replace the NAT gateway with a gateway VPC endpoint.
- [ ]  Replace the NAT gateway with an AWS Direct Connect connection.

**[⬆ Back to Top](#table-of-contents)**

### A company hosts a website on premises and wants to migrate it to the AWS Clou- [ ]  The website exposes a single hostname to the internet but it routes its functions to different on-premises server groups based on the path of the URL. The server groups are scaled independently depending on the needs of the functions they support. The company has an AWS Direct Connect connection configured to its on-premises network.What should a solutions architect do to provide path-based routing to send the traffic to the correct group of servers?
- [ ]   Route all traffic to an internet gateway. Configure pattern matching rules at the internet gateway to route traffic to the group of servers supporting that path.
- [ ]  Route all traffic to a Network Load Balancer (NLB) with target groups for each group of servers. Use pattern matching rules at the NLB to route traffic to the correct target group.
- [x]  Route all traffic to an Application Load Balancer (ALB). Configure path-based routing at the ALB to route traffic to the correct target group for the servers supporting that path.
- [ ]  Use Amazon Route 53 as the DNS server. Configure Route 53 path-based alias records to route traffic to the correct Elastic Load Balancer for the group of servers supporting that path.

**[⬆ Back to Top](#table-of-contents)**

### An application uses an Amazon RDS MySQL DB instance. The RDS database is becoming low on disk space. A solutions architect wants to increase the disk space without downtime. Which solution meets these requirements with the LEAST amount of effort?
- [x]   Enable storage auto scaling in RDS.
- [ ]  Increase the RDS database instance size.
- [ ]  Change the RDS database instance storage type to Provisioned IOPS.
- [ ]  Back up the RDS database, increase the storage capacity, restore the database and stop the previous instance.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce website is deploying its web application as Amazon Elastic Container Service (Amazon ECS) container instances behind an Application LoadBalancer (ALB). During periods of high activity, the website slows down and availability is reduce- [ ]  A solutions architect uses Amazon CloudWatch alarms to receive notifications whenever there is an availability issue so they can scale out resources. Company management wants a solution that automatically responds to such events.Which solution meets these requirements?
- [ ]   Set up AWS Auto Scaling to scale out the ECS service when there are timeouts on the AL- [ ]  Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.
- [ ]  Set up AWS Auto Scaling to scale out the ECS service when the ALB CPU utilization is too high. Setup AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.
- [x]  Set up AWS Auto Scaling to scale out the ECS service when the services CPU utilization is too high. Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.
- [ ]  Set up AWS Auto Scaling to scale out the ECS service when the ALB target group CPU utilization is too high. Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.

**[⬆ Back to Top](#table-of-contents)**

### A company has a website deployed on AWS. The database backend is hosted on Amazon RDS for MySQL with a primary instance and five read replicas to support scaling needs. The read replicas should lag no more than 1 second behind the primary instance to support the user experience.As traffic on the website continues to increase, the replicas are falling further behind during periods of peak load, resulting in complaints from users when searches yield inconsistent results. A solutions architect needs to reduce the replication lag as much as possible, with minimal changes to the application code or operational requirements.Which solution meets these requirements?
- [x]   Migrate the database to Amazon Aurora MySQL. Replace the MySQL read replicas with Aurora Replicas and enable Aurora Auto Scaling
- [ ]  Deploy an Amazon ElastiCache for Redis cluster in front of the database. Modify the website to check the cache before querying the database read endpoints.
- [ ]  Migrate the database from Amazon RDS to MySQL running on Amazon EC2 compute instances. Choose very large compute optimized instances for all replica nodes.
- [ ]  Migrate the database to Amazon DynamoD- [ ]  Initially provision a large number of read capacity units (RCUs) to support the required throughput with on- demand capacity scaling enabled

**[⬆ Back to Top](#table-of-contents)**

## A company has an API-based inventory reporting application running on Amazon EC2 instances. The application stores information in an Amazon DynamoDB table. The companyג distribution centers have an on-premises shipping application that calls an API to update the inventory before printing shipping labels. The company has been experiencing application interruptions several times each day, resulting in lost transactions.What should a solutions architect recommend to improve application resiliency?
- [ ]  Modify the shipping application to write to a local database.
- [ ]  Modify the application APIs to run serverless using AWS Lambda
- [ ]  Configure Amazon API Gateway to call the EC2 inventory application APIs.
- [x]  Modify the application to send inventory updates using Amazon Simple Queue Service (Amazon SQS).

**[⬆ Back to Top](#table-of-contents)**

### A company has a three-tier environment on AWS that ingests sensor data from its usersג€™ devices. The traffic flows through a Network Load Balancer (NLB) then toAmazon EC2 instances for the web tier, and finally toEC2 instances for the application tier that makes database calls.What should a solutions architect do to improve the security of data in transit to the web tier?
- [x]   Configure a TLS listener and add the server certificate on the NLB
- [ ]  Configure AWS Shield Advanced and enable AWS WAF on the NLB
- [ ]  Change the load balancer to an Application Load Balancer and attach AWS WAF to it.
- [ ]  Encrypt the Amazon Elastic Block Store (Amazon EBS) volume on the EC2 instances using AWS Key Management Service (AWS KMS).

**[⬆ Back to Top](#table-of-contents)**

### A company runs an online marketplace web application on AWS. The application serves hundreds of thousands of users during peak hours. The company needs a scalable, near-real-time solution to share the details of millions of financial transactions with several other internal applications. Transactions also need to be processed to remove sensitive data before being stored in a document database for low-latency retrieval.What should a solutions architect recommend to meet these requirements?
- [ ]   Store the transactions data into Amazon DynamoD- [ ]  Set up a rule in DynamoDB to remove sensitive data from every transaction upon write. Use DynamoDB Streams to share the transactions data with other applications.
- [ ]  Stream the transactions data into Amazon Kinesis Data Firehose to store data in Amazon DynamoDB and Amazon S3. Use AWS Lambda integration with Kinesis Data Firehose to remove sensitive dat- [ ]   Other applications can consume the data stored in Amazon S3.
- [x]  Stream the transactions data into Amazon Kinesis Data Streams. Use AWS Lambda integration to remove sensitive data from every transaction and then store the transactions data in AmazonDynamoD- [ ]  Other applications can consume the transactions data off the Kinesis data stream.
- [ ]  Store the batched transactions data in Amazon S3 as files. Use AWS Lambda to process every file and remove sensitive data before updating the files in Amazon S3. The Lambda function then stores the data in Amazon DynamoD- [ ]  Other applications can consume transaction files stored in Amazon S3.

**[⬆ Back to Top](#table-of-contents)**

### A company has a dynamic web application hosted on two Amazon EC2 instances. The company has its own SSL certificate, which is on each instance to performSSL termination.There has been an increase in traffic recently, and the operations team determined that SSL encryption and decryption is causing the compute capacity of the web servers to reach their maximum limit.What should a solutions architect do to increase the applicationג€™s performance?
- [ ]   Create a new SSL certificate using AWS Certificate Manager (ACM). Install the ACM certificate on each instance.
- [ ]  Create an Amazon S3 bucket. Migrate the SSL certificate to the S3 bucket. Configure the EC2 instances to reference the bucket for SSL termination.
- [ ]  Create another EC2 instance as a proxy server. Migrate the SSL certificate to the new instance and configure it to direct connections to the existing EC2 instances.
- [x]  Import the SSL certificate into AWS Certificate Manager (ACM). Create an Application Load Balancer with an HTTPS listener that uses the SSL certificate from ACM.


**[⬆ Back to Top](#table-of-contents)**

### A web application must persist order data to Amazon S3 to support neat-real time processing. A solutions architect needs create an architecture that is both scalable and fault tolerant.Which solutions meet these requirements? (Choose two.)
- [ ]   Write the order event to an Amazon DynamoDB table. Use DynamoDB Streams to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [x]  Write the order event to an Amazon Simple Queue Service (Amazon SQS) queue. Use the queue to trigger an AWSLambda function that parsers the payload and writes the data to Amazon S3.
- [ ]  Write the order event to an Amazon Simple Notification Service (Amazon SNS) topic
- [ ] Use the SNS topic to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [x]  Write the order event to an Amazon Simple Queue Service (Amazon SQS) queue. Use an Amazon EventBridge (Amazon CloudWatch Events) rule to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [ ] Write the order event to an Amazon Simple Notification Service (Amazon SNS) topi
- [ ]  Use an Amazon EventBridge (Amazon CloudWatch Events) rule to trigger an AWS Lambda function that parses the payload andwrites the data to Amazon S3.

### A company has an application hosted on Amazon EC2 instances in two VPCs across different AWS Regions. To communicate with each other, the instances use the internet for connectivity. The security team wants to ensure that no communication between the instances happens over the internet.What should a solutions architect do to accomplish this?
- [ ]   Create a NAT gateway and update the route table of the EC2 instancesג€™ subnet.
- [ ]  Create a VPC endpoint and update the route table of the EC2 instancesג€™ subnet.
- [ ]  Create a VPN connection and update the route table of the EC2 instancesג€™ subnet.
- [x]  Create a VPC peering connection and update the route table of the EC2 instancesג€™ subnet.

**[⬆ Back to Top](#table-of-contents)**

### A company is developing a new machine learning model solution in AWS. The models are developed as independent microservices that fetch about 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent. The company provides models to hundreds of users. The usage patterns for the models are irregular Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time. Which solution meets these requirements?
- [ ] The requests from the API are sent to an Application Load Balancer (ALB). Models are deployed as AWS Lambda functions invoked by the ALB.
- [ ] The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as AWS Lambda functions triggered by SQS events AWS Auto Scaling is enabled on Lambda to increase the number of vCPUs based on the SQS queue size.
- [ ] The requests from the API are sent to the model's Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS App Mesh scales the instances of the ECS cluster based on the SQS queue size.
- [x] The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS Auto Scaling is enabled on Amazon ECS for both the cluster and copies of the service based on the queue size.


**[⬆ Back to Top](#table-of-contents)**

### A company runs a web application on Amazon EC2 instances in an Auto Scaling group that has a target group. The company designed the application to work with session affinity (sticky sessions) for a better user experience. The application must be available publicly over the internet as an endpoint. A WAF must be applied to the endpoint for additional security. Session affinity (sticky sessions) must be configured on the endpoint. Which combination of steps will meet these requirements? (Choose two.)

- [ ] Create a public Network Load Balancer. Specify the application target group.
- [ ] Create a Gateway Load Balancer. Specify the application target group.
- [x] Create a public Application Load Balancer. Specify the application target group.
- [ ] Create a second target group. Add Elastic IP addresses to the EC2 instances.
- [x] Create a web ACL in AWS WAF. Associate the web ACL with the endpoint


**[⬆ Back to Top](#table-of-contents)**

### A company runs a web application on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer that has sticky sessions enabled. The web server currently hosts the user session state. The company wants to ensure high availability and avoid user session state loss in the event of a web server outage. Which solution will meet these requirements? 

- [ ]  Use an Amazon ElastiCache for Memcached instance to store the session dat- [  ] Update the application to use ElastiCache for Memcached to store the session state. 
- [x]  Use Amazon ElastiCache for Redis to store the session state. Update the application to use ElastiCache for Redis to store the session state. 
- [ ]  Use an AWS Storage Gateway cached volume to store session data. Update the application to use AWS Storage Gateway cached volume to store the session state. 
- [ ]  Use Amazon RDS to store the session state. Update the application to use Amazon RDS to store the session state. 

**[⬆ Back to Top](#table-of-contents)**


### A company is designing a web application with an internet-facing Application Load Balancer (ALB). The company needs the ALB to receive HTTPS web traffic from the public internet. The ALB must send only HTTPS traffic to the web application servers hosted on the Amazon EC2 instances on port 443. The ALB must perform a health check of the web application servers over HTTPS on port 8443. Which combination of configurations of the security group that is associated with the ALB will meet these requirements? (Choose three.)

- [x] Allow HTTPS inbound traffic from 0.0.0.0/0 for port 443.
- [ ] Allow all outbound traffic to 0.0.0.0/0 for port 443.
- [x] Allow HTTPS outbound traffic to the web application instances for port 443.
- [ ] Allow HTTPS inbound traffic from the web application instances for port 443.
- [x] Allow HTTPS outbound traffic to the web application instances for the health check on port 8443.
- [ ] Allow HTTPS inbound traffic from the web application instances for the health check on port 8443.

**[⬆ Back to Top](#table-of-contents)**


### A company hosts an application on AWS. The application gives users the ability to upload photos and store the photos in an Amazon S3 bucket. The company wants to use Amazon CloudFront and a custom domain name to upload the photo files to the S3 bucket in the eu-west-1 Region. Which solution will meet these requirements? (Choose two.)

- [x] Use AWS Certificate Manager (ACM) to create a public certificate in the us-east-1 Region. Use the certificate in CloudFront. Most Voted
- [ ] Use AWS Certificate Manager (ACM) to create a public certificate in eu-west-1. Use the certificate in CloudFront.
- [ ] Configure Amazon S3 to allow uploads from CloudFront. Configure S3 Transfer Acceleration.
- [x] Configure Amazon S3 to allow uploads from CloudFront origin access control (OAC). Most Voted
- [ ] Configure Amazon S3 to allow uploads from CloudFront. Configure an Amazon S3 website endpoint.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company wants to collect user clickstream data from the company's website for real-time analysis. The website experiences fluctuating traffic patterns throughout the day. The company needs a scalable solution that can adapt to varying levels of traffic. Which solution will meet these requirements?

- [x] Use a data stream in Amazon Kinesis Data Streams in on-demand mode to capture the clickstream data. Use AWS Lambda to process the data in real time.
- [ ] Use Amazon Kinesis Data Firehose to capture the clickstream data. Use AWS Glue to process the data in real time.
- [ ] Use Amazon Kinesis Video Streams to capture the clickstream data. Use AWS Glue to process the data in real time.
- [ ] Use Amazon Managed Service for Apache Flink (previously known as Amazon Kinesis Data Analytics) to capture the clickstream data. Use AWS Lambda to process the data in real time.

**[⬆ Back to Top](#table-of-contents)**

### A company designs a mobile app for its customers to upload photos to a website. The app needs a secure login with multi-factor authentication (MFA). The company wants to limit the initial build time and the maintenance of the solution. Which solution should a solutions architect recommend to meet these requirements?
- [x] Use Amazon Cognito Identity with SMS-based MF- [ ]  
- [ ] Edit IAM policies to require MFA for all users.
- [ ] Federate IAM against the corporate Active Directory that requires MF- [ ]  
- [ ] Use Amazon API Gateway and require server-side encryption (SSE) for photos.

**[⬆ Back to Top](#table-of-contents)**

### An application running in a private subnet accesses an Amazon DynamoDB table. The data cannot leave the AWS network to meet security requirements. How should this requirement be met?
- [ ] Configure a network ACL on DynamoDB to limit traffic to the private subnet.
- [ ] Enable DynamoDB encryption at rest using an AWS Key Management Service (AWS KMS) key.
- [ ] Add a NAT gateway and configure the route table on the private subnet.
- [x] Create a VPC endpoint for DynamoDB and configure the endpoint policy. 

**[⬆ Back to Top](#table-of-contents)**

### A company is planning to use Amazon S3 to store images uploaded by its users. The images must be encrypted at rest in Amazon S3. The company does not want to spend time managing and rotating the keys, but it does want to control who can access those keys. What should a solutions architect use to accomplish this?
- [ ] Server-Side Encryption with encryption keys stored in an S3 bucket
- [ ] Server-Side Encryption with Customer-Provided Keys (SSE-C)
- [ ] Server-Side Encryption with encryption keys stored in AWS Systems Manager Parameter Store
- [x] Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)

**[⬆ Back to Top](#table-of-contents)**

### A company's legacy application is currently relying on a single-instance Amazon RDS MySQL database without encryption. Due to new compliance requirements, all existing and new data in this database must be encrypte- [ ]  How should this be accomplished?
- [ ] Create an Amazon S3 bucket with server-side encryption turned on. Move all the data to Amazon S3. Delete the RDS instance.
- [ ] Configure RDS Multi-AZ mode with encryption at rest turned on. Perform a failover to the standby instance to delete the original instance.
- [x] Take a snapshot of the RDS instance. Create an encrypted copy of the snapshot. Restore the RDS instance from the encrypted snapshot.
- [ ] Create an RDS read replica with encryption at rest turned on. Promote the read replica to primary and switch the application over to the new primary. Delete the old RDS instance.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company is preparing to deploy a web application on AWS to ensure continuous service for customers. The architecture includes a web application that the company hosts on Amazon EC2 instances, a relational database in Amazon RDS, and static assets that the company stores in Amazon S3. The company wants to design a robust and resilient architecture for the application. Which solution will meet these requirements?

- [ ] Deploy Amazon EC2 instances in a single Availability Zone. Deploy an RDS DB instance in the same Availability Zone. Use Amazon S3 with versioning enabled to store static assets.
- [x] Deploy Amazon EC2 instances in an Auto Scaling group across multiple Availability Zones. Deploy a Multi-AZ RDS DB instance. Use Amazon CloudFront to distribute static assets.
- [ ] Deploy Amazon EC2 instances in a single Availability Zone. Deploy an RDS DB instance in a second Availability Zone for cross-AZ redundancy. Serve static assets directly from the EC2 instances.
- [ ] Use AWS Lambda functions to serve the web application. Use Amazon Aurora Serverless v2 for the database. Store static assets in Amazon Elastic File System (Amazon EFS) One Zone-Infrequent Access (One Zone-IA).

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce company runs several internal applications in multiple AWS accounts. The company uses AWS Organizations to manage its AWS accounts. A security appliance in the company’s networking account must inspect interactions between applications across AWS accounts. Which solution will meet these requirements?

- [ ] Deploy a Network Load Balancer (NLB) in the networking account to send traffic to the security appliance. Configure the application accounts to send traffic to the NLB by using an interface VPC endpoint in the application accounts.
- [ ] Deploy an Application Load Balancer (ALB) in the application accounts to send traffic directly to the security appliance.
- [x] Deploy a Gateway Load Balancer (GWLB) in the networking account to send traffic to the security appliance. Configure the application accounts to send traffic to the GWLB by using an interface GWLB endpoint in the application accounts.
- [ ] Deploy an interface VPC endpoint in the application accounts to send traffic directly to the security appliance.

**[⬆ Back to Top](#table-of-contents)**

### A company runs its production workload on an Amazon Aurora MySQL DB cluster that includes six Aurora Replicas. The company wants near-real-lime reporting queries from one of its departments to be automatically distributed across three of the Aurora Replicas. Those three replicas have a different compute and memory specification from the rest of the DB cluster.Which solution meets these requirements?
- [x]   Create and use a custom endpoint for the workload
- [ ]  Create a three-node cluster clone and use the reader endpoint.
- [ ]  Use any of the instance endpoints for the selected three nodes.
- [ ]  Use the reader endpoint to automatically distribute the read-only workloa- 


**[⬆ Back to Top](#table-of-contents)**

### A company has multiple applications that use Amazon RDS for MySQL as is database. The company recently discovered that a new custom reporting application has increased the number of Queries on the database. This is slowing down performance.How should a solutions architect resolve this issue with the LEAST amount of application changes?
- [ ]   Add a secondary DB instance using Multi-AZ.
- [x]  Set up a road replica and Multi-AZ on Amazon RDS.
- [ ]  Set up a standby replica and Multi-AZ on Amazon RDS.
- [ ]  Use caching on Amazon RDS to improve the overall performance.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to automate the security assessment of its Amazon EC2 instances. The company needs to validate and demonstrate that security and compliance standards are being followed throughout the development process.What should a solutions architect do to meet these requirements?
- [ ]   Use Amazon Macie to automatically discover, classify and protect the EC2 instances.
- [ ]  Use Amazon GuardDuty to publish Amazon Simple Notification Service (Amazon SNS) notifications.
- [x]  Use Amazon Inspector with Amazon CloudWatch to publish Amazon Simple Notification Service (Amazon SNS) notifications
- [ ]  Use Amazon EventBridge (Amazon CloudWatch Events) to detect and react to changes in the status of AWS Trusted Advisor checks.

**[⬆ Back to Top](#table-of-contents)**

### A company stores 200 GB of data each month in Amazon S3. The company needs to perform analytics on this data at the end of each month to determine the number of items sold in each sales region for the previous month.Which analytics strategy is MOST cost-effective for the company to use?
- [ ]   Create an Amazon Elasticsearch Service (Amazon ES) cluster. Query the data in Amazon ES. Visualize the data by using Kiban- [ ]  
- [x]  Create a table in the AWS Glue Data Catalog. Query the data in Amazon S3 by using Amazon Athen- [ ]   Visualize the data in Amazon QuickSight.
- [ ]  Create an Amazon EMR cluster. Query the data by using Amazon EMR, and store the results in Amazon S3. Visualize the data in Amazon QuickSight.
- [ ]  Create an Amazon Redshift cluster. Query the data in Amazon Redshift, and upload the results to Amazon S3. Visualize the data in Amazon QuickSight.


**[⬆ Back to Top](#table-of-contents)**

### A company wants to move its on-premises network, attached storage (NAS) to AWS. The company wants to make the data available to any Linux instances within its VPC and ensure changes are automatically synchronized across all instances accessing the data store. The majority of the data is accessed very rarely, and some files are accessed by multiple users at the same time.Which solution meets these requirements and is MOST cost-effective?
- [ ]   Create an Amazon Elastic Block Store (Amazon EBS) snapshot containing the dat- [ ]   Share it with users within the VP- [ ] 
- [ ]  Create an Amazon S3 bucket that has a lifecycle policy set to transition the data to S3 Standard-Infrequent Access (S3 Standard-IA) after the appropriate number of days.
- [ ]  Create an Amazon Elastic File System (Amazon EFS) file system within the VP- [ ]  Set the throughput mode to Provisioned and to the required amount of IOPS to support concurrent usage.
- [x]  Create an Amazon Elastic File System (Amazon EFS) file system within the VP- [ ]  Set the lifecycle policy to transition the data to EFS Infrequent Access (EFS IA) after the appropriate number of days.


**[⬆ Back to Top](#table-of-contents)**

### A company plans to host a survey website on AWS. The company anticipates an unpredictable amount of traffi- [ ]  This traffic results in asynchronous updates to the database. The company wants to ensure that writes to the database hosted on AWS do not get droppe- [ ] How should the company write its application to handle these database requests?
- [ ]   Configure the application to publish to an Amazon Simple Notification Service (Amazon SNS) topi- [ ]  Subscribe the database to the SNS topi- [ ] 
- [ ]  Configure the application to subscribe to an Amazon Simple Notification Service (Amazon SNS) topi- [ ]  Publish the database updates to the SNS topi- [ ] 
- [ ]  Use Amazon Simple Queue Service (Amazon SQS) FIFO queues to queue the database connection until the database has resources to write the dat- [ ]  
- [x]  Use Amazon Simple Queue Service (Amazon SQS) FIFO queues for capturing the writes and draining the queue as each write is made to the database.


**[⬆ Back to Top](#table-of-contents)**

### A company that recently started using AWS establishes a Site-to-Site VPN between its on-premises datacenter and AWS. The company's security mandate states that traffic originating from on premises should stay within the companyג€™s private IP space when communicating with an Amazon Elastic Container Service(Amazon ECS) cluster that is hosting a sample web application.Which solution meets this requirement?
- [ ]   Configure a gateway endpoint for Amazon ECS. Modify the route table to include an entry pointing to the ECS cluster.
- [ ]  Create a Network Load Balancer and AWS PrivateLink endpoint for Amazon ECS in the same VPC that is hosting the ECS cluster.
- [x]  Create a Network Load Balancer in one VPC and an AWS PrivateLink endpoint for Amazon ECS in another VP- [ ]  Connect the two VPCs by using VPC peering.
- [ ]  Configure an Amazon Route 53 record with Amazon ECS as the target. Apply a server certificate to Route 53 from AWS Certificate Manager (ACM) for SSL offloading.


**[⬆ Back to Top](#table-of-contents)**

### A solutions architect must analyze and update a companyג€™s existing IAM policies prior to deploying a new workloa- [ ]  The solutions architect created the following policy:What is the net effect of this policy?
- [ ]   Users will be allowed all actions except s3:PutObject if multi-factor authentication (MFA) is enable- [ ] 
- [ ]  Users will be allowed all actions except s3:PutObject if multi-factor authentication (MFA) is not enable- [ ] 
- [ ]  Users will be denied all actions except s3:PutObject if multi-factor authentication (MFA) is enable- [ ] 
- [x]  Users will be denied all actions except s3:PutObject if multi-factor authentication (MFA) is not enabled


**[⬆ Back to Top](#table-of-contents)**

### A company is running a multi-tier web application on premises. The web application is containerized and runs on a number of Linux hosts connected to aPostgreSQL database that contains user records. The operational overhead of maintaining the infrastructure and capacity planning is limiting the companyג€™s growth. A solutions architect must improve the applicationג€™s infrastructure.Which combination of actions should the solutions architect take to accomplish this? (Choose two.)
- [x]   Migrate the PostgreSQL database to Amazon Auror- [ ]  
- [ ]  Migrate the web application to be hosted on Amazon EC2 instances.
- [ ]  Set up an Amazon CloudFront distribution for the web application content.
- [ ]  Set up Amazon ElastiCache between the web application and the PostgreSQL database.
- [x] Migrate the web application to be hosted on AWS Fargate with Amazon Elastic Container Service (Amazon ECS)

**[⬆ Back to Top](#table-of-contents)**

### An application allows users at a companyג€™s headquarters to access product dat- [ ]   The product data is stored in an Amazon RDS MySQL DB instance. The operations team has isolated an application performance slowdown and wants to separate read traffic from write traffic  A solutions architect needs to optimize the applicationג€™s performance quickly.What should the solutions architect recommend?
- [ ]   Change the existing database to a Multi-AZ deployment. Serve the read requests from the primary Availability Zone.
- [ ]  Change the existing database to a Multi-AZ deployment. Serve the read requests from the secondary Availability Zone.
- [ ]  Create read replicas for the database. Configure the read replicas with half of the compute and storage resources as the source database.
- [x]  Create read replicas for the database. Configure the read replicas with the same compute and storage resources as the source database.

**[⬆ Back to Top](#table-of-contents)**

### A company is using Amazon DynamoDB with provisioned throughput for the database tier of its ecommerce website. During flash sales, customers experience periods of time when the database cannot handle the high number of transactions taking place. This causes the company to lose transactions. During normal periods, the database performs appropriately.Which solution solves the performance problem the company faces?
- [x]   Switch DynamoDB to on-demand mode during flash sales.
- [ ]  Implement DynamoDB Accelerator for fast in memory performance.
- [ ]  Use Amazon Kinesis to queue transactions for processing to DynamoD- [ ] 
- [ ]  Use Amazon Simple Queue Service (Amazon SQS) to queue transactions to DynamoD- [ ] 


**[⬆ Back to Top](#table-of-contents)**

### A company is reviewing a recent migration of a three-tier application to a VP- [ ]  The security team discovers that the principle of least privilege is not being applied to Amazon EC2 security group ingress and egress rules between the application tiers.What should a solutions architect do to correct this issue?
- [x]  Create security group rules using the instance ID as the source or destination.
- [ ]  Create security group rules using the security group ID as the source or destination.
- [ ]  Create security group rules using the VPC CIDR blocks as the source or destination.
- [ ]  Create security group rules using the subnet CIDR blocks as the source or destination

**[⬆ Back to Top](#table-of-contents)**

### A company requires that all versions of objects in its Amazon S3 bucket be retaine- [ ]  Current object versions will be frequently accessed during the first 30 days, after which they will be rarely accessed and must be retrievable within 5 minutes. Previous object versions need to be kept forever, will be rarely accessed, and can be retrieved within 1 week. All storage solutions must be highly available and highly durable.What should a solutions architect recommend to meet these requirements in the MOST cost-effective manner?
- [x]   Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 Glacier after 30 days and moves previous object versions to S3 Glacier after 1 day.
- [ ]  Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 Glacier after 30 days and moves previous object versions to S3 Glacier Deep Archive after 1 day.
- [ ]  Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 Standard-infrequent Access (S3 Standard-IA) after 30 days and moves previous object versions toS3 Glacier Deep Archive after 1 day.
- [ ]  Create an S3 lifecycle policy for the bucket that moves current object versions from S3 Standard storage to S3 One Zone-Infrequent Access (S3 One Zone-IA) after 30 days and moves previous object versions to S3 Glacier Deep Archive after 1 day.

**[⬆ Back to Top](#table-of-contents)**

### A development team is collaborating with another company to create an integrated product. The other company needs to access an Amazon Simple QueueService (Amazon SQS) queue that is contained in the development team's account. The other company wants to poll the queue without giving up its own account permissions to do so.How should a solutions architect provide access to the SQS queue?
- [ ]   Create an instance profile that provides the other company access to the SQS queue.
- [ ]  Create an IAM policy that provides the other company access to the SQS queue.
- [x]  Create an SQS access policy that provides the other company access to the SQS queue.
- [ ]  Create an Amazon Simple Notification Service (Amazon SNS) access policy that provides the other company access to the SQS queue.


**[⬆ Back to Top](#table-of-contents)**

### A company is developing a video conversion application hosted on AWS. The application will be available in two tiers: a free tier and a paid tier. Users in the paid tier will have their videos converted first and then the tree tier users will have their videos converted. Which solution meets these requirements and is MOST cost-effective?
- [ ]   One FIFO queue for the paid tier and one standard queue for the free tier.
- [ ]  A single FIFO Amazon Simple Queue Service (Amazon SQS) queue for all file types.
- [ ]  A single standard Amazon Simple Queue Service (Amazon SQS) queue for all file types.
- [x]  Two standard Amazon Simple Queue Service (Amazon SQS) queues with one for the paid tier and one for the free tier.


**[⬆ Back to Top](#table-of-contents)**

### An administrator of a large company wants to monitor for and prevent any cryptocurrency-related attacks on the companyג€™s AWS accounts.Which AWS service can the administrator use to protect the company against attacks?
- [ ]   Amazon Cognito
- [x]  Amazon GuardDuty
- [ ]  Amazon Inspector
- [ ]  Amazon Macie

**[⬆ Back to Top](#table-of-contents)**

### A company has applications hosted on Amazon EC2 instances with IPv6 addresses. The applications must initiate communications with other external applications using the internet. However, the companyג€™'s security policy states that any external service cannot initiate a connection to the EC2 instances. What should a solutions architect recommend to resolve this issue?
- [ ]   Create a NAT gateway and make it the destination of the subnetג€™s route table.
- [ ]  Create an internet gateway and make it the destination of the subnetג€™s route table.
- [ ]  Create a virtual private gateway and make it the destination of the subnetג€™s route table.
- [x]  Create an egress-only internet gateway and make it the destination of the subnetג€™s route table.

**[⬆ Back to Top](#table-of-contents)**

### A company provides an online service for posting video content and transcoding it for use by any mobile platform. The application architecture uses AmazonElastic File System (Amazon EFS) Standard to collect and store the videos so that multiple Amazon EC2 Linux instances can access the video content for processing. As the popularity of the service has grown over time, the storage costs have become too expensive.Which storage solution is MOST cost-effective?
- [ ]   Use AWS Storage Gateway for files to store and process the video content.
- [ ]  Use AWS Storage Gateway for volumes to store and process the video content.
- [ ]  Use Amazon EFS for storing the video content. Once processing is complete, transfer the files to Amazon Elastic Block Store (Amazon EBS).
- [x]  Use Amazon S3 for storing the video content. Move the files temporarily over to an Amazon ElasticBlock Store (Amazon EBS) volume attached to the server for processing.

**[⬆ Back to Top](#table-of-contents)**

### A company wants to host its web application on AWS using multiple Amazon EC2 instances across different AWS Regions. Since the application content will be specific to each geographic region, the client requests need to be routed to the server that hosts the content for that clients Region.What should a solutions architect do to accomplish this?
- [ ]   Configure Amazon Route 53 with a latency routing policy.
- [ ]  Configure Amazon Route 53 with a weighted routing policy.
- [x]  Configure Amazon Route 53 with a geolocation routing policy.
- [ ]  Configure Amazon Route 53 with a multivalue answer routing policy

**[⬆ Back to Top](#table-of-contents)**

### A solutions architect is planning the deployment of a new static website. The solution must minimize costs and provide at least 99% availability. Which solution meets these requirements?
- [x]   Deploy the application to an Amazon S3 bucket in one AWS Region that has versioning disable- [ ] 
- [ ]  Deploy the application to Amazon EC2 instances that run in two AWS Regions and two Availability Zones.
- [ ]  Deploy the application to an Amazon S3 bucket that has versioning and cross-Region replication enable- [ ] 
- [ ]  Deploy the application to an Amazon EC2 instance that runs in one AWS Region and one Availability Zone.

**[⬆ Back to Top](#table-of-contents)**

### A recently created startup built a three-tier web application. The front end has static content. The application layer is based on microservices. User data is stored as JSON documents that need to be accessed with low latency. The company expects regular traffic to be low during the first year, with peaks in traffic when it publicizes new features every month. The startup team needs to minimize operational overhead costs.What should a solutions architect recommend to accomplish this?
- [ ]   Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use AWS Elastic Beanstalk for the application layer. Use Amazon DynamoDB to store user dat- [ ]  
- [ ]  Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use Amazon Elastic KubernetesService (Amazon EKS) for the application layer. Use Amazon DynamoDB to store user dat- [ ]  
- [x]  Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use Amazon API Gateway and AWS Lambda functions for the application layer. Use Amazon DynamoDB to store user dat- [ ]  
- [ ]  Use Amazon S3 static website hosting to store and serve the front en- [ ]  Use Amazon API Gateway and AWS Lambda functions for the application layer. Use Amazon RDS with read replicas to store user dat- [ ]  

**[⬆ Back to Top](#table-of-contents)**

### A company is building a payment application that must be highly available even during regional service disruptions. A solutions architect must design a data storage solution that can be easily replicated and used in other AWS Regions. The application also requires low-latency atomicity, consistency, isolation, and durability (ACID) transactions that need to be immediately available to generate reports The development team also needs to use SQL.Which data storage solution meets these requirements?
- [x]   Amazon Aurora Global Database
- [ ]  Amazon DynamoDB global tables
- [ ]  Amazon S3 with cross-Region replication and Amazon Athena
- [ ]  MySQL on Amazon EC2 instances with Amazon Elastic Block Store (Amazon EBS) snapshot replication

**[⬆ Back to Top](#table-of-contents)**

### A company stores call recordings on a monthly basis. Statistically, the recorded data may be referenced randomly within a year but accessed rarely after 1 year.Files that are newer than 1 year old must be queried and retrieved as quickly as possible. A delay in retrieving older files is acceptable. A solutions architect needs to store the recorded data at a minimal cost.Which solution is MOST cost-effective?
- [ ]   Store individual files in Amazon S3 Glacier and store search metadata in object tags created in S3 Glacier Query S3 Glacier tags and retrieve the files from S3 Glacier.
- [x]  Store individual files in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after1 year. Query and retrieve the files from Amazon S3 or S3 Glacier.
- [ ]  Archive individual files and store search metadata for each archive in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after 1 year. Query and retrieve the files by searching for metadata from Amazon S3.
- [ ]  Archive individual files in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after 1 year. Store search metadata in Amazon DynamoD- [ ]  Query the files from DynamoDB and retrieve them from Amazon S3 or S3 Glacier.



**[⬆ Back to Top](#table-of-contents)**

### A company is developing a new machine learning model solution in AWS. The models are developed as independent microservices that fetch about 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent.The company provides models to hundreds of users. The usage patterns for the models are irregular Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time.Which solution meets these requirements?
- [ ]   The requests from the API are sent to an Application Load Balancer (ALB). Models are deployed as AWS Lambda functions invoked by the AL- [ ] 
- [ ]  The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as AWS Lambda functions triggered by SQS events AWS Auto Scaling is enabled on Lambda to increase the number of vCPUs based on the SQS queue size.
- [ ]  The requests from the API are sent to the modelג€™s Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS App Mesh scales the instances of the ECS cluster based on the SQS queue size.
- [x]  The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS Auto Scaling is enabled on Amazon ECS for both the cluster and copies of the service based on the queue size



**[⬆ Back to Top](#table-of-contents)**

### A company has no existing file share services. A new project requires access to file storage that is mountable as a drive for on-premises desktops. The file server must authenticate users to an Active Directory domain before they are able to access the storage.Which service will allow Active Directory users to mount storage as a drive on their desktops?
- [ ]   Amazon S3 Glacier
- [ ]  AWS DataSync
- [ ]  AWS Snowball Edge
- [x]  AWS Storage Gateway



**[⬆ Back to Top](#table-of-contents)**

### A company is preparing to launch a public-facing web application in the AWS Clou- [ ]  The architecture consists of Amazon EC2 instances within a VPC behind anElastic Load Balancer (ELB). A third party service is used for the DNS. The companyג€™s solutions architect must recommend a solution to detect and protect against largescale DDoS attacks.Which solution meets these requirements?
- [ ]   Enable Amazon GuardDuty on the account.
- [ ]  Enable Amazon Inspector on the EC2 instances.
- [ ]  Enable AWS Shield and assign Amazon Route 53 to it.
- [x]  Enable AWS Shield Advanced and assign the ELB to it.


**[⬆ Back to Top](#table-of-contents)**

### A company has a custom application with embedded credentials that retrieves information from an Amazon RDS MySQL DB instance. Management says the application must be made more secure with the least amount of programming effort.What should a solutions architect do to meet these requirements?
- [ ]   Use AWS Key Management Service (AWS KMS) customer master keys (CMKs) to create keys. Configure the application to load the database credentials from AWS KMS. Enable automatic key rotation.
- [ ]  Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Secrets Manager. Configure the application to load the database credentials from Secrets Manager. Create an AWS Lambda function that rotates the credentials in Secret Manager.
- [x]  Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Secrets Manager. Configure the application to load the database credentials from Secrets Manager. Set up a credentials rotation schedule for the application user in the RDS for MySQL database using Secrets Manager.
- [ ]  Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Systems Manager Parameter Store. Configure the application to load the database credentials from Parameter Store. Set up a credentials rotation schedule for the application user in the RDS for MySQL database using Parameter Store.

**[⬆ Back to Top](#table-of-contents)**

A company is running a multi-tier web application on AWS. The application runs its database tier on Amazon Aurora MySQL. The application and database tiers are in the us-east-1 Region. A database administrator who regularly monitors the Aurora DB cluster finds that an intermittent increase in read traffic is creating high CPUutilization on the read replica and causing increased read latency of the application.What should a solutions architect do to improve read scalability?
- [ ]   Reboot the Aurora DB cluster.
- [ ]  Create a cross-Region read replica
- [ ]  Increase the instance class of the read replic- [ ]  
- [x]  Configure Aurora Auto Scaling for the read replic- [ ]  

**[⬆ Back to Top](#table-of-contents)**

### A companyג€™s order fulfillment service uses a MySQL database. The database needs to support a large number of concurrent queries and transactions. Developers are spending time patching and tuning the database This is causing delays in releasing new product features.The company wants to use cloud-based services to help address this new challenge. The solution must allow the developers to migrate the database with little or no code changes and must optimize performance.Which service should a solutions architect use to meet these requirements?
- [x]   Amazon Aurora
- [ ]  Amazon DynamoDB
- [ ]  Amazon ElastiCache
- [ ]  MySQL on Amazon EC2



**[⬆ Back to Top](#table-of-contents)**

### A company is planning to transfer multiple terabytes of data to AWS. The data is collected offline from ships. The company want to run complex transformation before transferring the dat- [ ]  Which AWS service should a solutions architect recommend for this migration?
- [ ]   AWS Snowball
- [ ]  AWS Snowmobile
- [ ]  AWS Snowball Edge Storage Optimize
- [x]  AWS Snowball Edge Compute Optimize


**[⬆ Back to Top](#table-of-contents)**

### A company is running an online transaction processing (OLTP) workload on AWS. This workload uses an unencrypted Amazon RDS DB instance in a Multi-AZ deployment. Daily database snapshots are taken from this instance.What should a solutions architect do to ensure the database and snapshots are always encrypted moving forward?
- [x]   Encrypt a copy of the latest DB snapshot. Replace existing DB instance by restoring the encrypted snapshot.
- [ ]  Create a new encrypted Amazon Elastic Block Store (Amazon EBS) volume and copy the snapshots to it. Enable encryption on the DB instance.
- [ ]  Copy the snapshots and enable encryption using AWS Key Management Service (AWS KMS). Restore encrypted snapshot to an existing DB instance.
- [ ]  Copy the snapshots to an Amazon S3 bucket that is encrypted using server-side encryption with AWS Key Management Service (AWS KMS) managed keys (SSE-KMS).

**[⬆ Back to Top](#table-of-contents)**

### A company is selling up an application to use an Amazon RDS MySQL DB instance. The database must be architected for high availability across AvailabilityZones and AWS Regions with minimal downtime.How should a solutions architect meet this requirement?
- [ ]   Set up an RDS MySQL Multi-AZ DB instance. Configure an appropriate backup window.
- [x]  Set up an RDS MySQL Multi-AZ DB instance. Configure a read replica in a different Region.
- [ ]  Set up an RDS MySQL Single-AZ DB instance. Configure a read replica in a different Region.
- [ ]  Set up an RDS MySQL Single-AZ DB instance. Copy automated snapshots to at least one other Region.


**[⬆ Back to Top](#table-of-contents)**

### A company hosts its web application on AWS using seven Amazon EC2 instances. The company requires that the IP addresses of all healthy EC2 instances be returned in response to DNS queries.Which policy should be used to meet this requirement?
- [ ]   Simple routing policy
- [ ]  Latency routing policy
- [x]  Multi-value routing policy
- [ ]  Geolocation routing policy


**[⬆ Back to Top](#table-of-contents)**

### A company has 700 TB of backup data stored in network attached storage (NAS) in its data center This backup data need to be accessible for infrequent regulatory requests and must be retained 7 years. The company has decided to migrate this backup data from its data center to AWS. The migration must be complete within 1 month. The company has 500 Mbps of dedicated bandwidth on its public internet connection available for data transfer.What should a solutions architect do to migrate and store the data at the LOWEST cost?
- [x]   Order AWS Snowball devices to transfer the dat- [ ]   Use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive.
- [ ]  Deploy a VPN connection between the data center and Amazon VP- [ ]  Use the AWS CLI to copy the data from on premises to Amazon S3 Glacier.
- [ ]  Provision a 500 Mbps AWS Direct Connect connection and transfer the data to Amazon S3. Use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive.
- [ ]  Use AWS DataSync to transfer the data and deploy a DataSync agent on premises. Use the DataSync task to copy files from the on-premises NAS storage to Amazon S3 Glacier.


**[⬆ Back to Top](#table-of-contents)**

### A company is preparing to deploy a data lake on AWS. A solutions architect must define the encryption strategy tor data at rest m Amazon S3/ The companyג€™s security policy states:✑ Keys must be rotated every 90 days.✑ Strict separation of duties between key users and key administrators must be implemente- [ ] ✑ Auditing key usage must be possible.What should the solutions architect recommend?
- [x]   Server-side encryption with AWS KMS managed keys (SSE-KMS) with customer managed customer master keys (CMKs)
- [ ]  Server-side encryption with AWS KMS managed keys (SSE-KMS) with AWS managed customer master keys (CMKs)
- [ ]  Server-side encryption with Amazon S3 managed keys (SSE-S3) with customer managed customer master keys (CMKs)
- [ ]  Server-side encryption with Amazon S3 managed keys (SSE-S3) with AWS managed customer master keys (CMKs)


**[⬆ Back to Top](#table-of-contents)**

### A company has an application that generates a large number of files, each approximately 5 MB in size. The files are stored in Amazon S3. Company policy requires the files to be stored for 4 years before they can be delete- [ ]  Immediate accessibility is always required as the files contain critical business data that is not easy to reproduce. The files are frequently accessed in the first 30 days of the object creation but are rarely accessed after the first 30 days.Which storage solution is MOST cost-effective?
- [ ]   Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Glacier 30 days from object creation. Delete the files 4 years after object creation.
- [ ]  Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 One Zone-Infrequent Access (S3 One Zone-IA) 30 days from object creation. Delete the files 4 years after object creation.
- [x]  Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Delete the files 4 years after object creation.
- [ ]  Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Move the files to S3 Glacier 4 years after object creation.

**[⬆ Back to Top](#table-of-contents)**

### A company previously migrated its data warehouse solution to AWS. The company also has an AWS Direct Connect connection. Corporate office users query the data warehouse using a visualization tool. The average size of a query returned by the data warehouse is 50 MB and each webpage sent by the visualization tool is approximately 500 K- [ ]  Result sets returned by the data warehouse are not cache- [ ] Which solution provides the LOWEST data transfer egress cost for the company?
- [ ]   Host the visualization tool on premises and query the data warehouse directly over the internet.
- [ ]  Host the visualization tool in the same AWS Region as the data warehouse. Access it over the internet.
- [ ]  Host the visualization tool on premises and query the data warehouse directly over a Direct Connect connection at a location in the same AWS Region.
- [x]  Host the visualization tool in the same AWS Region as the data warehouse and access it over a DirectConnect connection at a location in the same Region.

**[⬆ Back to Top](#table-of-contents)**

### A mobile gaming company runs application servers on Amazon EC2 instances. The servers receive updates from players every 15 minutes. The mobile game creates a JSON object of the progress made in the game since the last update, and sends the JSON object to an Application Load Balancer. As the mobile game is played, game updates are being lost. The company wants to create a durable way to get the updates in older.What should a solutions architect recommend to decouple the system?

- [ ]   Use Amazon Kinesis Data Streams to capture the data and store the JSON object in Amazon S3.
- [ ]  Use Amazon Kinesis Data Firehose to capture the data and store the JSON object in Amazon S3.
- [x]  Use Amazon Simple Queue Service (Amazon SQS) FIFO queues to capture the data and EC2 instances to process the messages in the queue.
- [ ]  Use Amazon Simple Notification Service (Amazon SNS) to capture the data and EC2 instances to process the messages sent to the Application Load Balancer.

**[⬆ Back to Top](#table-of-contents)**

### A company has an application that runs on Amazon EC2 instances within a private subnet in a VPC  The instances access data in an Amazon S3 bucket in the same AWS Region. The VPC contains a NAT gateway in a public subnet to access the S3 bucket. The company wants to reduce costs by replacing the NAT gateway without compromising security or redundancy. Which solution meets these requirements?

- [ ]  Replace the NAT gateway with a NAT instance.
- [ ]  Replace the NAT gateway with an internet gateway.
- [x]  Replace the NAT gateway with a gateway VPC endpoint.
- [ ]  Replace the NAT gateway with an AWS Direct Connect connection.

**[⬆ Back to Top](#table-of-contents)**

### A company hosts a website on premises and wants to migrate it to the AWS Clou- [ ]  The website exposes a single hostname to the internet but it routes its functions to different on-premises server groups based on the path of the URL. The server groups are scaled independently depending on the needs of the functions they support. The company has an AWS Direct Connect connection configured to its on-premises network.What should a solutions architect do to provide path-based routing to send the traffic to the correct group of servers?
- [ ]   Route all traffic to an internet gateway. Configure pattern matching rules at the internet gateway to route traffic to the group of servers supporting that path.
- [ ]  Route all traffic to a Network Load Balancer (NLB) with target groups for each group of servers. Use pattern matching rules at the NLB to route traffic to the correct target group.
- [x]  Route all traffic to an Application Load Balancer (ALB). Configure path-based routing at the ALB to route traffic to the correct target group for the servers supporting that path.
- [ ]  Use Amazon Route 53 as the DNS server. Configure Route 53 path-based alias records to route traffic to the correct Elastic Load Balancer for the group of servers supporting that path.

**[⬆ Back to Top](#table-of-contents)**

### An application uses an Amazon RDS MySQL DB instance. The RDS database is becoming low on disk space. A solutions architect wants to increase the disk space without downtime. Which solution meets these requirements with the LEAST amount of effort?
- [x]   Enable storage auto scaling in RDS.
- [ ]  Increase the RDS database instance size.
- [ ]  Change the RDS database instance storage type to Provisioned IOPS.
- [ ]  Back up the RDS database, increase the storage capacity, restore the database and stop the previous instance.

**[⬆ Back to Top](#table-of-contents)**

### An ecommerce website is deploying its web application as Amazon Elastic Container Service (Amazon ECS) container instances behind an Application LoadBalancer (ALB). During periods of high activity, the website slows down and availability is reduce- [ ]  A solutions architect uses Amazon CloudWatch alarms to receive notifications whenever there is an availability issue so they can scale out resources. Company management wants a solution that automatically responds to such events.Which solution meets these requirements?
- [ ]   Set up AWS Auto Scaling to scale out the ECS service when there are timeouts on the AL- [ ]  Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.
- [ ]  Set up AWS Auto Scaling to scale out the ECS service when the ALB CPU utilization is too high. Setup AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.
- [x]  Set up AWS Auto Scaling to scale out the ECS service when the services CPU utilization is too high. Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.
- [ ]  Set up AWS Auto Scaling to scale out the ECS service when the ALB target group CPU utilization is too high. Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.

**[⬆ Back to Top](#table-of-contents)**

### A company has a website deployed on AWS. The database backend is hosted on Amazon RDS for MySQL with a primary instance and five read replicas to support scaling needs. The read replicas should lag no more than 1 second behind the primary instance to support the user experience.As traffic on the website continues to increase, the replicas are falling further behind during periods of peak load, resulting in complaints from users when searches yield inconsistent results. A solutions architect needs to reduce the replication lag as much as possible, with minimal changes to the application code or operational requirements.Which solution meets these requirements?
- [x]   Migrate the database to Amazon Aurora MySQL. Replace the MySQL read replicas with Aurora Replicas and enable Aurora Auto Scaling
- [ ]  Deploy an Amazon ElastiCache for Redis cluster in front of the database. Modify the website to check the cache before querying the database read endpoints.
- [ ]  Migrate the database from Amazon RDS to MySQL running on Amazon EC2 compute instances. Choose very large compute optimized instances for all replica nodes.
- [ ]  Migrate the database to Amazon DynamoD- [ ]  Initially provision a large number of read capacity units (RCUs) to support the required throughput with on- demand capacity scaling enabled

**[⬆ Back to Top](#table-of-contents)**

## A company has an API-based inventory reporting application running on Amazon EC2 instances. The application stores information in an Amazon DynamoDB table. The companyג distribution centers have an on-premises shipping application that calls an API to update the inventory before printing shipping labels. The company has been experiencing application interruptions several times each day, resulting in lost transactions.What should a solutions architect recommend to improve application resiliency?
- [ ]  Modify the shipping application to write to a local database.
- [ ]  Modify the application APIs to run serverless using AWS Lambda
- [ ]  Configure Amazon API Gateway to call the EC2 inventory application APIs.
- [x]  Modify the application to send inventory updates using Amazon Simple Queue Service (Amazon SQS).

**[⬆ Back to Top](#table-of-contents)**

### A company has a three-tier environment on AWS that ingests sensor data from its usersג€™ devices. The traffic flows through a Network Load Balancer (NLB) then toAmazon EC2 instances for the web tier, and finally toEC2 instances for the application tier that makes database calls.What should a solutions architect do to improve the security of data in transit to the web tier?
- [x]   Configure a TLS listener and add the server certificate on the NLB
- [ ]  Configure AWS Shield Advanced and enable AWS WAF on the NLB
- [ ]  Change the load balancer to an Application Load Balancer and attach AWS WAF to it.
- [ ]  Encrypt the Amazon Elastic Block Store (Amazon EBS) volume on the EC2 instances using AWS Key Management Service (AWS KMS).

**[⬆ Back to Top](#table-of-contents)**

### A company runs an online marketplace web application on AWS. The application serves hundreds of thousands of users during peak hours. The company needs a scalable, near-real-time solution to share the details of millions of financial transactions with several other internal applications. Transactions also need to be processed to remove sensitive data before being stored in a document database for low-latency retrieval.What should a solutions architect recommend to meet these requirements?
- [ ]   Store the transactions data into Amazon DynamoD- [ ]  Set up a rule in DynamoDB to remove sensitive data from every transaction upon write. Use DynamoDB Streams to share the transactions data with other applications.
- [ ]  Stream the transactions data into Amazon Kinesis Data Firehose to store data in Amazon DynamoDB and Amazon S3. Use AWS Lambda integration with Kinesis Data Firehose to remove sensitive dat- [ ]   Other applications can consume the data stored in Amazon S3.
- [x]  Stream the transactions data into Amazon Kinesis Data Streams. Use AWS Lambda integration to remove sensitive data from every transaction and then store the transactions data in AmazonDynamoD- [ ]  Other applications can consume the transactions data off the Kinesis data stream.
- [ ]  Store the batched transactions data in Amazon S3 as files. Use AWS Lambda to process every file and remove sensitive data before updating the files in Amazon S3. The Lambda function then stores the data in Amazon DynamoD- [ ]  Other applications can consume transaction files stored in Amazon S3.

**[⬆ Back to Top](#table-of-contents)**

### A company has a dynamic web application hosted on two Amazon EC2 instances. The company has its own SSL certificate, which is on each instance to performSSL termination.There has been an increase in traffic recently, and the operations team determined that SSL encryption and decryption is causing the compute capacity of the web servers to reach their maximum limit.What should a solutions architect do to increase the applicationג€™s performance?
- [ ]   Create a new SSL certificate using AWS Certificate Manager (ACM). Install the ACM certificate on each instance.
- [ ]  Create an Amazon S3 bucket. Migrate the SSL certificate to the S3 bucket. Configure the EC2 instances to reference the bucket for SSL termination.
- [ ]  Create another EC2 instance as a proxy server. Migrate the SSL certificate to the new instance and configure it to direct connections to the existing EC2 instances.
- [x]  Import the SSL certificate into AWS Certificate Manager (ACM). Create an Application Load Balancer with an HTTPS listener that uses the SSL certificate from ACM.


**[⬆ Back to Top](#table-of-contents)**

### A web application must persist order data to Amazon S3 to support near-real time processing. A solutions architect needs to create an architecture that is both scalable and fault tolerant. Which solutions meet these requirements? (Choose two.)
- [ ] Write the order event to an Amazon DynamoDB table. Use DynamoDB Streams to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [x] Write the order event to an Amazon Simple Queue Service (Amazon SQS) queue. Use the queue to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [ ] Write the order event to an Amazon Simple Notification Service (Amazon SNS) topic. Use the SNS topic to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [x] Write the order event to an Amazon Simple Queue Service (Amazon SQS) queue. Use an Amazon EventBridge (Amazon CloudWatch Events) rule to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.
- [ ] Write the order event to an Amazon Simple Notification Service (Amazon SNS) topic. Use an Amazon EventBridge (Amazon CloudWatch Events) rule to trigger an AWS Lambda function that parses the payload and writes the data to Amazon S3.

### A company has an application hosted on Amazon EC2 instances in two VPCs across different AWS Regions. To communicate with each other, the instances use the internet for connectivity. The security team wants to ensure that no communication between the instances happens over the internet.What should a solutions architect do to accomplish this?
- [ ]   Create a NAT gateway and update the route table of the EC2 instancesג€™ subnet.
- [ ]  Create a VPC endpoint and update the route table of the EC2 instancesג€™ subnet.
- [ ]  Create a VPN connection and update the route table of the EC2 instancesג€™ subnet.
- [x]  Create a VPC peering connection and update the route table of the EC2 instancesג€™ subnet.

**[⬆ Back to Top](#table-of-contents)**

### A company is developing a new machine learning model solution in AWS. The models are developed as independent microservices that fetch about 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent. The company provides models to hundreds of users. The usage patterns for the models are irregular Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time. Which solution meets these requirements?
- [ ] The requests from the API are sent to an Application Load Balancer (ALB). Models are deployed as AWS Lambda functions invoked by the ALB.
- [ ] The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as AWS Lambda functions triggered by SQS events AWS Auto Scaling is enabled on Lambda to increase the number of vCPUs based on the SQS queue size.
- [ ] The requests from the API are sent to the model's Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS App Mesh scales the instances of the ECS cluster based on the SQS queue size.
- [x] The requests from the API are sent to the models Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue AWS Auto Scaling is enabled on Amazon ECS for both the cluster and copies of the service based on the queue size.


**[⬆ Back to Top](#table-of-contents)**

### A company runs a web application on Amazon EC2 instances in an Auto Scaling group that has a target group. The company designed the application to work with session affinity (sticky sessions) for a better user experience. The application must be available publicly over the internet as an endpoint. A WAF must be applied to the endpoint for additional security. Session affinity (sticky sessions) must be configured on the endpoint. Which combination of steps will meet these requirements? (Choose two.)

- [ ] Create a public Network Load Balancer. Specify the application target group.
- [ ] Create a Gateway Load Balancer. Specify the application target group.
- [x] Create a public Application Load Balancer. Specify the application target group.
- [ ] Create a second target group. Add Elastic IP addresses to the EC2 instances.
- [x] Create a web ACL in AWS WAF. Associate the web ACL with the endpoint


**[⬆ Back to Top](#table-of-contents)**

### A company runs a web application on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer that has sticky sessions enabled. The web server currently hosts the user session state. The company wants to ensure high availability and avoid user session state loss in the event of a web server outage. Which solution will meet these requirements? 

- [ ]  Use an Amazon ElastiCache for Memcached instance to store the session dat- [  ] Update the application to use ElastiCache for Memcached to store the session state. 
- [x]  Use Amazon ElastiCache for Redis to store the session state. Update the application to use ElastiCache for Redis to store the session state. 
- [ ]  Use an AWS Storage Gateway cached volume to store session data. Update the application to use AWS Storage Gateway cached volume to store the session state. 
- [ ]  Use Amazon RDS to store the session state. Update the application to use Amazon RDS to store the session state. 

**[⬆ Back to Top](#table-of-contents)**


### A company is designing a web application with an internet-facing Application Load Balancer (ALB). The company needs the ALB to receive HTTPS web traffic from the public internet. The ALB must send only HTTPS traffic to the web application servers hosted on the Amazon EC2 instances on port 443. The ALB must perform a health check of the web application servers over HTTPS on port 8443. Which combination of configurations of the security group that is associated with the ALB will meet these requirements? (Choose three.)

- [x] Allow HTTPS inbound traffic from 0.0.0.0/0 for port 443.
- [ ] Allow all outbound traffic to 0.0.0.0/0 for port 443.
- [x] Allow HTTPS outbound traffic to the web application instances for port 443.
- [ ] Allow HTTPS inbound traffic from the web application instances for port 443.
- [x] Allow HTTPS outbound traffic to the web application instances for the health check on port 8443.
- [ ] Allow HTTPS inbound traffic from the web application instances for the health check on port 8443.

**[⬆ Back to Top](#table-of-contents)**


### A company hosts an application on AWS. The application gives users the ability to upload photos and store the photos in an Amazon S3 bucket. The company wants to use Amazon CloudFront and a custom domain name to upload the photo files to the S3 bucket in the eu-west-1 Region. Which solution will meet these requirements? (Choose two.)

- [x] Use AWS Certificate Manager (ACM) to create a public certificate in the us-east-1 Region. Use the certificate in CloudFront.
- [ ] Use AWS Certificate Manager (ACM) to create a public certificate in eu-west-1. Use the certificate in CloudFront.
- [ ] Configure Amazon S3 to allow uploads from CloudFront. Configure S3 Transfer Acceleration.
- [x] Configure Amazon S3 to allow uploads from CloudFront origin access control (OAC).
- [ ] Configure Amazon S3 to allow uploads from CloudFront. Configure an Amazon S3 website endpoint.

**[⬆ Back to Top](#table-of-contents)**
