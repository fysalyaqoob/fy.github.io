import streamlit as st
import streamlit.components.v1 as components

# Page Configurations
st.set_page_config(
    page_title="Fysal Yaqoob - WordPress Developer",
    page_icon=":computer:",
    layout="centered",
)

# SEO Meta Tags
components.html(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Professional WordPress Developer with over 15 years of experience specializing in custom themes, plugins, and advanced WordPress solutions for businesses.">
    <meta name="keywords" content="WordPress Developer, Custom Themes, Plugin Development, Web Developer, Freelance WordPress Developer, Elementor, WooCommerce, Advanced WordPress Solutions">
    <meta name="author" content="Fysal Yaqoob">
    """,
    height=0,
)

# Header
st.title("Fysal Yaqoob")
st.markdown(
    """
    **WordPress Developer | Custom Themes & Advanced Solutions**  
    Specialist in Custom WordPress Development for Businesses
    """
)

# Contact Information
st.markdown(
    """
    **Contact:**  
    📧 [hello@fysalyaqoob.com](mailto:hello@fysalyaqoob.com)  
    📱 +1 607-270-0798  
    🌐 [Portfolio](https://fysalyaqoob.com)  
    💼 [LinkedIn](https://www.linkedin.com/in/fysalyaqoob) | [Fiverr](https://www.fiverr.com/fysalyaqoob)  
    """
)

# Summary Section
st.subheader("About Me")
st.markdown(
    """
    I am a seasoned WordPress developer with over 15 years of experience, specializing in creating scalable, responsive, and user-friendly websites.  
    Proficient in **HTML, CSS, JavaScript (ES6+), PHP, MySQL**, and tools like **Elementor, Avada, Divi**, and **Gutenberg**.
    """
)

# Skills
st.subheader("Key Skills")
st.markdown(
    """
    - Custom WordPress Themes & Plugins Development  
    - WooCommerce & Advanced Custom Fields (ACF)  
    - REST API Integrations & Dynamic Content  
    - Frontend Development with Bootstrap & Gulp.js  
    """
)

# Experience Section
st.subheader("Experience")
st.markdown(
    """
    - **Searchbloom**: WordPress Developer (2015 - Present)  
      Providing custom solutions to marketing agencies.  

    - **Fiverr & Upwork**: Freelance WordPress Developer (2010 - Present)  
      500+ 5-star reviews from global clients.  

    - **NetWise UK**: WordPress Developer (2015 - 2024)  
      Built tailored websites for councils in the UK.  
    """
)

# Footer
st.markdown("---")
st.markdown(
    "Built with ❤️ using [Streamlit](https://streamlit.io) | © 2024 Fysal Yaqoob"
)
