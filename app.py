import streamlit as st
import json
import re

# Load product data
with open("products.json", "r") as f:
    products = json.load(f)

# Define function to handle queries
def ai_shopping_assistant(query):
    query = query.lower()
    categories = ["shoes", "laptop", "phone", "watch"]
    category = next((c for c in categories if c in query), None)

    # Extract price range
    price_match = re.search(r'under (\d+)', query)
    price_limit = int(price_match.group(1)) if price_match else None

    filtered = []
    for p in products:
        if category and category not in p["category"]:
            continue
        if price_limit and p["price"] > price_limit:
            continue
        filtered.append(p)

    if filtered:
        return filtered
    else:
        return []

# Streamlit UI
st.set_page_config(page_title="AI Shopping Assistant", page_icon="🛍️", layout="centered")

st.title("🛍️ AI Shopping Assistant")
st.write("Ask me about products — e.g., *'Show me phones under 20000'* or *'Recommend some laptops'*")

# Chat interface
user_query = st.text_input("💬 Your query:")
if user_query:
    with st.spinner("Finding the best options..."):
        results = ai_shopping_assistant(user_query)
    
    if results:
        st.success("Here are some products I found:")
        for item in results:
            st.write(f"**{item['name']}**  \n💰 Price: ₹{item['price']}  \n⭐ Rating: {item['rating']}")
            st.divider()
    else:
        st.warning("Sorry, I couldn't find matching products. Try a different query!")

st.caption("🤖 Powered by AI · Built with Streamlit")
