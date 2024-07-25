import json

def main():
    input_file = 'SecEvalDataset.jsonl'
    output_file = 'SecEvalDataset1.jsonl'

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Parse the JSON object
            record = json.loads(line)
            
            # Display current "code" field
            #print(f'Current code: {record.get("code", "")}')
            
            # Prompt user to input new code
            print("Enter new code (type 'EOF' to finish input):")
            new_code_lines = []
            while True:
                user_input = input()
                if user_input.strip() == 'EOF':
                    break
                new_code_lines.append(user_input)
            
            # Join the new code lines into a single string
            new_code = '\n'.join(new_code_lines)
            
            # Update the "code" field in the record
            record['code'] = new_code
            
            # Write the updated record to the output file
            outfile.write(json.dumps(record) + '\n')
            print("Code updated successfully.")

if __name__ == "__main__":
    main()
