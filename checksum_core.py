import hashlib
import requests
import os
from typing import Optional, Dict

class ChecksumVerifier:
    @staticmethod
    def calculate_sha256(file_path: str) -> str:
        """Calculate SHA256 hash of a file"""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                # Read file in chunks to handle large files
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except Exception as e:
            raise Exception(f"Error reading file: {str(e)}")
    
    @staticmethod
    def download_checksum_file(url: str) -> Dict[str, str]:
        """Download checksum file and parse it into a dictionary"""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            checksums = {}
            for line in response.text.splitlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split()
                    if len(parts) >= 2:
                        # Handle both formats: "hash filename" and "hash *filename"
                        hash_value = parts[0]
                        filename = parts[-1].lstrip('*')
                        checksums[filename] = hash_value
            return checksums
        except Exception as e:
            raise Exception(f"Error downloading checksum file: {str(e)}")
    
    @staticmethod
    def load_checksum_file(file_path: str) -> Dict[str, str]:
        """Load and parse local checksum file"""
        try:
            checksums = {}
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        parts = line.split()
                        if len(parts) >= 2:
                            hash_value = parts[0]
                            filename = parts[-1].lstrip('*')
                            checksums[filename] = hash_value
            return checksums
        except Exception as e:
            raise Exception(f"Error reading checksum file: {str(e)}")
    
    @staticmethod
    def verify_checksum(file_hash: str, expected_hash: str) -> bool:
        """Compare two hashes (case insensitive)"""
        return file_hash.lower() == expected_hash.lower()