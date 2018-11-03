# mongo


ansible playbook with two roles
1.	 install mongodb
2.	 create mongodb admin user:
		name="admin"  
		password="123456"  

Run: "python run-mongo.py" to install mongodb and create user admin.
Run: "python run-mongo.py -u user" to skip installation and only create admin user.

