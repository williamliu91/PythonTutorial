import streamlit as st
import sys
import io
import traceback
from contextlib import redirect_stdout, redirect_stderr

def execute_python_code(code):
    # Capture stdout and stderr
    output = io.StringIO()
    error = io.StringIO()
    
    try:
        with redirect_stdout(output), redirect_stderr(error):
            exec(code)
        return output.getvalue(), error.getvalue(), None
    except Exception:
        return output.getvalue(), error.getvalue(), traceback.format_exc()

st.set_page_config(page_title="Python Code Executor", layout="wide")

st.title("Python Code Executor")

# Default code
default_code = """
# Enter your Python code here
print("Hello, World!")

# Example: Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
result = greet("Streamlit")
print(result)
"""

# Create a text area for code input
code = st.text_area("Enter Python Code", value=default_code, height=300)

# Create a button to run the code
if st.button("Run Code"):
    stdout, stderr, exception = execute_python_code(code)
    
    # Display the output
    if stdout:
        st.subheader("Output:")
        st.code(stdout)
    
    # Display any errors
    if stderr or exception:
        st.subheader("Errors:")
        st.error(stderr + (exception or ""))

st.markdown("---")
st.write("Note: This app executes Python code in a restricted environment. Some operations may be limited for security reasons.")