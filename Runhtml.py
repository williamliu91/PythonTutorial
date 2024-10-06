import streamlit as st
from bs4 import BeautifulSoup

def sanitize_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    return str(soup)

st.set_page_config(page_title="HTML Code Executor", layout="wide")
st.title("HTML Code Executor")

# Default HTML code
default_html = """
<!-- Enter your HTML code here -->
<h1>Hello, World!</h1>
<p>This is a sample HTML code.</p>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
"""

# Create a text area for HTML input
html_code = st.text_area("Enter HTML Code", value=default_html, height=300)

# Create a button to run the HTML code
if st.button("Run HTML"):
    # Sanitize the HTML to remove potentially harmful elements
    sanitized_html = sanitize_html(html_code)
    
    # Display the sanitized HTML
    st.subheader("Output:")
    st.components.v1.html(sanitized_html, height=400)

st.markdown("---")
st.write("Note: This app executes HTML code in a restricted environment. Some operations may be limited for security reasons.")