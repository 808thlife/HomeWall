from django.db import models

# Create your models here.
class IptablesRule(models.Model):
    name = models.CharField(max_length=255 , blank = True)    # Name of the IPTables rule
    type = models.CharField(max_length = 140,blank = True) #filter,nat,mangle,raw
    action = models.CharField(max_length=255,blank = True)    # Type of the IPTables rule (e.g., DROP, MASQUERADE, etc.)
    chain = models.CharField(max_length=50,blank = True) # input,forward,output
    source_ip = models.CharField(max_length=255,blank = True) # Source IP address for the rule
    destination_ip = models.CharField(max_length=255,blank = True) # Destination IP address for the rule
    port = models.IntegerField(blank = True)                 # Port number for the rule
    protocol = models.CharField(max_length=255,blank = True) # Protocol for the rule (e.g., TCP, UDP, etc.)