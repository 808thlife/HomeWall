from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    pass

def create(request):
    if request.method == "POST":
    
        # Create a rule object
        #rule = iptc.Rule()

        table = request.POST["table"] # filter by default
        chain = request.POST["chain"]
        rule = request.POST["rule"]

        print(f"table {table}, chain {chain}, rule {rule}")

        # Commit the changes
        #iptc.easy.commit()
    
        # Return success response
        return HttpResponse("Rule created successfully")

def edit(request):
    # Get parameters from the request
    # Example: table, chain, rule_index, new_rule_spec
    
    # Get the chain object
    # Example: chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    
    # Get the rule to edit
    # Example: rule = chain.rules[rule_index]
    
    # Modify the rule properties based on request parameters
    # Example: rule.src = '192.168.2.0/24'
    # Example: rule.target = iptc.Target(rule, 'DROP')
    
    # Update the rule in the chain
    # Example: chain.rules[rule_index] = rule
    
    # Commit the changes
    # Example: iptc.easy.commit()
    
    # Return success response
    return HttpResponse("Rule edited successfully")

def delete(request):
    # Get parameters from the request
    # Example: table, chain, rule_index
    
    # Get the chain object
    # Example: chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    
    # Delete the rule from the chain
    # Example: del chain.rules[rule_index]
    
    # Commit the changes
    # Example: iptc.easy.commit()
    
    # Return success response
    return HttpResponse("Rule deleted successfully")