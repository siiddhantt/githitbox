#!/usr/bin/env python3


import subprocess
import sys


def install_requirements():
    print("Installing requirements...")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
    )


def run_server():
    print("Starting GitHitBox...")
    print("Server will be available at: http://localhost:8000")
    print("API Documentation: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop the server")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "main:app",
            "--host",
            "0.0.0.0",
            "--port",
            "8000",
            "--reload",
        ]
    )


if __name__ == "__main__":
    try:
        import fastapi
        import uvicorn
    except ImportError:
        install_requirements()
    run_server()
