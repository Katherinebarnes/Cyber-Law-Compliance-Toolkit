import hashlib
import datetime
import os

def generate_evidence_report(file_path):
    # 1. Calculate SHA-256 Hash (The 'Digital Fingerprint')
    sha256_hash = hashlib.sha256()
    with open(file_path,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    
    file_hash = sha256_hash.hexdigest()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 2. Print the "Official" Report
    print("-" * 30)
    print("DIGITAL EVIDENCE REPORT")
    print("-" * 30)
    print(f"File Name: {os.path.basename(file_path)}")
    print(f"SHA-256 Hash: {file_hash}")
    print(f"Generated On: {timestamp}")
    print("-" * 30)
    print("\nDRAFT SECTION 65B STATEMENT:")
    print(f"I hereby certify that the digital file '{os.path.basename(file_path)}' ")
    print(f"with hash {file_hash} was produced by a computer system under my control...")

# To run: generate_evidence_report('your_file_here.jpg')
