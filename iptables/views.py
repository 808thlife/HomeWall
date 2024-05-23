from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import IptablesRule

import os 
import sys
# Create your views here.

def index(request):
    pass

def create(request):
    if request.method == "POST":
    
        # Create a rule object
        #rule = iptc.Rule()
        name = request.POST.get("name", "empty name")
        type = request.POST.get("table", "filter")  # Default to "filter" table if not provided
        chain = request.POST.get("chain", "INPUT")   # Default to "INPUT" chain if not provided
        action = request.POST.get("action", "empty")         # Default to empty rule
        source_ip = request.POST.get("source_ip", "empty")
        destination_ip = request.POST.get("destination_ip", "empty")
        port = request.POST.get("port", 8000)
        protocol = request.POST.get("protocol", "empty")

        #your code.

        f = IptablesRule(name = name, type = type, chain = chain, action = action, 
                        source_ip = source_ip, destination_ip = destination_ip,
                        port = port, protocol = protocol)
        f.save()

        
    
        return HttpResponseRedirect(reverse("core:rules_view"))


def edit(request, ID):
    name = request.POST.get("name", "empty name")
    type = request.POST.get("table", "filter")  # Default to "filter" table if not provided
    chain = request.POST.get("chain", "INPUT")   # Default to "INPUT" chain if not provided
    action = request.POST.get("action", "empty")         # Default to empty rule
    source_ip = request.POST.get("source_ip", "empty")
    destination_ip = request.POST.get("destination_ip", "empty")
    port = request.POST.get("port", 8000)
    protocol = request.POST.get("protocol", "empty")

    #editing
    rule = IptablesRule.objects.get(id = ID)

    rule.name = name
    rule.type = type
    rule.chain = chain
    rule.action = action
    rule.source_ip = source_ip
    rule.destination_ip = destination_ip
    rule.port = port
    rule.protocol = protocol
    
    rule.save()

    execute_command_from_line(rule, "delete")
    execute_command_from_line(rule, "create")

    # Return success response
    return HttpResponseRedirect(reverse("core:rules_view"))


def delete(request, ID):
    rule = IptablesRule.objects.get(id = ID)

    execute_command_from_line(rule, "delete")

    rule.delete()
    return HttpResponseRedirect(reverse("core:rules_view"))

def execute_command_from_line(rule, action):
    if action == "create":
        command = f"iptables -A {rule.chain}"  # Append rule to the specified chain
        if name:
            command += f" -N {rule.name}"  # Create a new chain with the provided name (optional)
        if source_ip:
            command += f" -s {rule.source_ip}"
        if destination_ip:
            command += f" -d {rule.destination_ip}"
        if port:
            command += f" --dport {rule.port}"
        if protocol:
            command += f" -p {rule.protocol}"
        if action:
            command += f" -j {rule.action}"

        print(f"iptables rule created (name: {name}, chain: {chain})")

    elif action == "delete":
        command = f"iptables -D {rule.chain}"  # Delete rule from the specified chain
        if name:
            command += f" {rule.name}"  # Specify rule name by name (optional)
        print(f"Command is: {command}")

    if action != "delete" or action != "create":
        sys.exit("Invalid action")
        
    os.system(command)