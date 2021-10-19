# Office365Enumeration  
This script checks if an email address is valid in **Office365**.  
This script does not perform any login attempt.  
It is extremely handy to use for social engineering assesments to check for valid Office365 email address'.  

The script makes use of the **Microsoft AutoDiscovery API**.  
``` /autodiscover/autodiscover.json/v1.0/{EMAIL}?Protocol=Autodiscoverv1 ``` API endpoint returns different status codes for if an email exists in Office365 or not. 200 status code means the email exists, a 302 means it doesn't exist.  

