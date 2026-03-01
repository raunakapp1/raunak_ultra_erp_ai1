import streamlit as st
import sys
import os

# 🔥 ROOT PATH FIX
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from dashboard import admin_dashboard

def main():
    admin_dashboard()

if __name__ == "__main__":
    main()
