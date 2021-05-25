from alg import ford_fulkerson
import json


finish = False
while not finish:
    is_valid_file = False
    while not is_valid_file:
        print("Insert file path:")
        file_path = input()
        try:
            with open(file_path) as f:
                network  = json.load(f)
            is_valid_file = True
        except:
            print("Invalid file path or file format. Try again.")
            print()
    try:
        max_flow = ford_fulkerson(network)
        print(f'The maximum flow of your network is {max_flow}')
    except:
        print("Invalid input file. Check out README.md to learn more")

    print("Do you want to continue? (yes/no)")
    ans = input()
    if ans == 'no' or ans == 'NO':
        break