import hashlib
import os
import platform
import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def get_advanced_metadata(file_path):
    metadata = {}
    try:
        stats = os.stat(file_path)
        metadata['Size (Bytes)'] = stats.st_size
        metadata['Created'] = datetime.datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        metadata['Modified'] = datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            image = Image.open(file_path)
            info = image._getexif()
            if info:
                for tag, value in info.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata[f"EXIF_{tag_name}"] = value
        except:
            metadata['Note'] = "No EXIF data found (Non-image file)"
    except FileNotFoundError:
        return None
    return metadata

def generate_forensic_report(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR: File not found at {file_path}")
        print("Please check the file name or upload it again.")
        return

    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    file_hash = sha256_hash.hexdigest()
    meta = get_advanced_metadata(file_path)

    print("="*60)
    print(f"TECHNO-LEGAL FORENSIC ANALYSIS REPORT")
    print("="*60)
    print(f"FILE IDENTITY: {os.path.basename(file_path)}")
    print(f"SHA-256 HASH:  {file_hash}")
    print("-" * 60)
    print("TECHNICAL METADATA:")
    for k, v in meta.items():
        print(f"{k:20}: {v}")
    print("-" * 60)
    print("\nLEGAL COMPLIANCE STATEMENT (Sec 65B IEA / Sec 63 BSA):")
    print(f"I, [Your Name], hereby certify that the digital record identified by ")
    print(f"SHA-256 hash '{file_hash}' was processed on a system running ")
    print(f"{platform.system()} {platform.release()}.")
    print("="*60)



generate_forensic_report('test.txt')
