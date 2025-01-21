from setuptools import setup, find_packages

setup(
    name="dvpn-network",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "websockets>=10.0",
        "cryptography>=3.4.7",
        "python-dotenv>=0.19.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Decentralized VPN Network Visualization System",
    python_requires=">=3.7",
)