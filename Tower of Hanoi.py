def tower_of_hanoi(n, source, destination, auxiliary):
   
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1
    steps = tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    steps += 1
    steps += tower_of_hanoi(n-1, auxiliary, destination, source)
    return steps


n = int(input("Enter the number of disks: "))


steps = tower_of_hanoi(n, 'A', 'C', 'B')
print(f"Total steps: {steps}")
