from colorama import Fore, Style, init
init()

def txtorfasta(filename):
    sequence = ""
    with open(filename, 'r') as file:
        firstline = file.readline().strip()
        if firstline.startswith(">"):
            for line in file:
                line = line.strip()
                if not line.startswith(">"):
                    sequence += line.upper()
        else:
            sequence = firstline.upper()
            for line in file:
                sequence += line.strip().upper()
    return sequence



def analyzer():
    reference = input("Input reference file name: ")
    sample = input("Input sample file name: ")
    refcontent = txtorfasta(reference)
    samcontent = txtorfasta(sample)
    output = "results.txt"
    with open(output, 'w') as outputfile:
        header = f"{'Position':<10} {'Reference':<10} {'Sample':<10} {'Type':<10}"
        separator = "-" * 40
        print(header)
        print(separator)
        outputfile.write(header + "\n")
        outputfile.write(separator + "\n")
        i = 0
        j = 0
        deletions = 0
        mutations = 0
        while i < len(refcontent) and j < len(samcontent):
            if refcontent[i] == samcontent[j]:
                i += 1
                j += 1
            elif i+1 < len(refcontent) and refcontent[i+1] == samcontent[j]:
                line = f"{i+1:<10} {refcontent[i]:<10} {'-':<10} {'Deletion':<10}"
                print(line)
                outputfile.write(line + "\n")
                deletions += 1
                i +=1 
            else:
                line = f"{i+1:<10} {refcontent[i]:<10} {samcontent[j]:<10} {'Mutation':<10}"
                print(line)
                outputfile.write(line + "\n")
                i += 1
                j += 1
                mutations += 1
        
        print("\nSummary:")
        outputfile.write("\nSummary:\n")

        if deletions > 0:
            print(f"Your sequence contains {deletions} {Fore.BLUE}deletion(s).{Style.RESET_ALL}")
            outputfile.write(f"Your sequence contains {deletions} deletion(s).\n")
        else:
            print("Your sequence does not contain any deletions.")
            outputfile.write("Your sequence does not contain any deletions.\n")

        if mutations > 0:
            print(f"Your sequence contains {mutations} {Fore.RED}mutation(s).{Style.RESET_ALL}")
            outputfile.write(f"Your sequence contains {mutations} mutation(s).\n")
        else:
            print("Your sequence does not contain any mutations.")
            outputfile.write("Your sequence does not contain any mutations.\n")
       
analyzer()