import pandas as pd
import streamlit as st
from PIL import Image

# Veri setini yükle
df = pd.read_csv("/Users/mustafagul/Desktop/GitHub/wiwino_project/wiwino/vivinostreamlit/data/test2.csv")

# Sayfa başlığı ve açıklama
st.set_page_config(page_title="Wine Recommendation", page_icon="🍷", layout="wide")
st.title("🍷 Wine Recommendation")
st.markdown("""
<style>
    .main {
        background-color: #fafafa;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .wine-card {
        background-color: #fff3e6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .wine-card h3 {
        color: #ff4b4b;
        margin-bottom: 15px;
    }
    .wine-card p {
        margin-bottom: 5px;
    }
    .wine-card a {
        color: #ff4b4b;
        text-decoration: none;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        padding: 20px;
        font-size: 16px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Hoş geldiniz mesajı
st.markdown("""
Welcome to the **Wine Recommendation**! 
Use the slider below to select your preferred price range, then click the button to get a random wine recommendation.
""")

# Fiyat aralığı filtresi
price_range = st.slider("Select Price Range", 0, 10000, (0, 300))

# Gelişmiş Seçenekler
with st.expander("Advanced Filters"):
    rating_threshold = st.slider("Minimum Rating", 4.0, 5.0, 4.5)
    group_name = st.multiselect("Select Wine Group", df['Group Name'].unique())

# Rastgele şarap önerisi butonu
if st.button("Get Random Wine Recommendation"):
    filtered_df = df[(df['Price'] >= price_range[0]) & (df['Price'] <= price_range[1])]
    
    # Ekstra filtreler
    if rating_threshold:
        filtered_df = filtered_df[filtered_df['Rating Average'] >= rating_threshold]
    if group_name:
        filtered_df = filtered_df[filtered_df['Group Name'].isin(group_name)]
    
    if not filtered_df.empty:
        wine = filtered_df.sample(1).iloc[0]
        st.subheader("Your Wine Recommendation:")
        st.markdown(f"""
        <div class="wine-card">
            <h3>{wine['Wine']}</h3>
            <p><strong>Rating:</strong> {wine['Rating Average']} ⭐️</p>
            <p><strong>Rating Count:</strong> {wine['Rating Count']}</p>
            <p><strong>Price:</strong> ${wine['Price']}</p>
            <p><strong>Group Name:</strong> {wine['Group Name']}</p>
            <p><strong>Flavour:</strong> {wine['Flavour']}</p>
            <p><strong>Link:</strong> <a href="{wine['URL']}" target="_blank">Buy Now</a></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("No wines found with the selected criteria.")

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    Made with ❤️ by [Musti]
</div>
""", unsafe_allow_html=True)
