

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
  Parses a configuration file and returns a dictionary of key-value pairs.

  Args:
      filename: The path to the configuration file.

  Returns:
      A dictionary with the extracted values.
  """
  values = {}
  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()  # Remove leading and trailing whitespaces
      if not line or line.startswith('#'):  # Skip comments and empty lines
        continue

      key, value = line.split('=', 1)  # Split line by '=' and get key and value
      values[key.strip()] = value.strip()  # Remove whitespaces from key and value

      # Extract last two values for dhcp-range (if applicable)
      if key == "dhcp-range":
        start_str, end_str = value.split(", ")[-2:]
        values["start"] = int(start_str.split(".")[-1])
        values["end"] = int(end_str.split(".")[-1])
      

  return values



# Get the values from the file
