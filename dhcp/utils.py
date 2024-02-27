
def edit_dnsmasq_conf(new_dhcp_range, new_address, file_path = "some_path"):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("#dhcp-range") or line.startswith("dhcp-range"):
            lines[i] = f"dhcp-range={new_dhcp_range}"
        elif line.startswith("#address") or line.startswith("address"):
            lines[i] = f"address={new_address}"

    with open(file_path, 'w') as file:
        file.writelines(lines)

def get_dnsmasq_conf(file_path = "some_path") :
    params = []
    with open(file_path) as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("dhcp-range"):
            params.append(lines[i])
        elif line.startswith("address"):
            params.append(lines[i])
    return params

def delete_dnsmasq_trash(array):
    test = []
    for i in array:
        for j in i:
            if j !="=":
                test.append(j)
            else:
                break
        print(test)
    return array

array = get_dnsmasq_conf("dnsmasq.conf")


delete_dnsmasq_trash(array)
