

def edit_dnsmasq_conf(new_dhcp_range, new_address, file_path = "some_path"):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("#dhcp-range") or line.startswith("dhcp-range"):
            lines[i] = f"dhcp-range={new_dhcp_range}\n"
        elif line.startswith("#address") or line.startswith("address"):
            lines[i] = f"address={new_address}\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)



def parse_config(filename):
  """
  Parses a configuration file and returns a dictionary of DHCP range information.

  Args:
      filename: The path to the configuration file.

  Returns:
      A dictionary containing:
          - start_ip: The starting IP address of the DHCP range (string)
          - end_ip: The ending IP address of the DHCP range (string)
          - mask: The subnet mask (string)
          - restart_time: The restart time (string)  # Assuming 24h format
          - address: The IP address of the interface (string)  # If present
  """
  dhcp_range = {}
  address = None  # Initialize address variable to capture it if found

  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()  # Remove leading and trailing whitespaces
      if not line or line.startswith('#'):  # Skip comments and empty lines
        continue

      # Extract key and value based on presence of '='
      if '=' in line:
        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()
      else:
        continue  # Skip lines without '=' (not relevant for parsing)

      # Store key-value pair and handle address separately
      if key == "address":
        address = value
      elif key == "dhcp-range":
        try:
          # Separate dhcp-range values by comma
          values = value.split(",")

          # Extract entire start, end, mask, restart time
          start_ip, end_ip, mask, restart_time = values
          dhcp_range["start_ip"] = start_ip.strip()
          dhcp_range["end_ip"] = end_ip.strip()
          dhcp_range["mask"] = mask.strip()
          dhcp_range["restart_time"] = restart_time.strip()  # Assuming 24h format
        except ValueError:
          # Handle errors gracefully, e.g., log or print an error message
          print(f"Error parsing dhcp-range values in line: {line}")

  # Add address to the dictionary if found
  if address:
    dhcp_range["address"] = address

  return dhcp_range






# Get the values from the file
