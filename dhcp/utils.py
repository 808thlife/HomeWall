
def edit_dnsmasq_conf(new_dhcp_range, new_address, file_path = "some_path"):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("#dhcp-range"):
            lines[i] = f"dhcp-range={new_dhcp_range}\n"
        elif line.startswith("#address"):
            lines[i] = f"address={new_address}\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)
