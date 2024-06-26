import streamlit as st
from html import escape

# Title of the app
st.title('Mini SEO Meta Tag Generator')

st.write("Fill in the details below and click 'Generate Meta Tags' to create your SEO meta tags.")

# Input fields with examples
website_name = st.text_input('Website Name', 'Example Website')
website_description = st.text_area('Website Description', 'This is an example of a website description.')
website_link = st.text_input('Website Link', 'https://www.example.com')
twitter_username = st.text_input('Twitter Username', 'example')
image_link = st.text_input('Image Link', 'https://www.example.com/image.jpg')

if st.button('Generate Meta Tags'):
    if not all([website_name, website_description, website_link, twitter_username, image_link]):
        st.error('Please fill in all the fields.')
    else:
        # Escape user input for HTML safety
        website_name_escaped = escape(website_name)
        website_description_escaped = escape(website_description)
        website_link_escaped = escape(website_link)
        twitter_username_escaped = escape(twitter_username)
        image_link_escaped = escape(image_link)

        # Generate meta tags
        meta_tags = f"""
        <meta name="title" content="{website_name_escaped}">
        <meta name="description" content="{website_description_escaped}">
        
        <!-- Open Graph / Facebook -->
        <meta property="og:type" content="website">
        <meta property="og:url" content="{website_link_escaped}">
        <meta property="og:title" content="{website_name_escaped}">
        <meta property="og:description" content="{website_description_escaped}">
        <meta property="og:image" content="{image_link_escaped}">
        
        <!-- Twitter -->
        <meta property="twitter:card" content="summary_large_image">
        <meta property="twitter:url" content="{website_link_escaped}">
        <meta property="twitter:title" content="{website_name_escaped}">
        <meta property="twitter:description" content="{website_description_escaped}">
        <meta property="twitter:image" content="{image_link_escaped}">
        <meta property="twitter:site" content="@{twitter_username_escaped}">
        """

        # Display meta tags
        st.code(meta_tags, language='html')
        st.success('Meta tags generated successfully!')

        # Provide option to download meta tags as HTML file
        html_content = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {meta_tags}
            <title>{website_name_escaped}</title>
        </head>
        <body>
            <h1>{website_name_escaped}</h1>
            <p>{website_description_escaped}</p>
            <img src="{image_link_escaped}" alt="Sample Image" style="max-width: 100%;">
        </body>
        </html>"""

        st.download_button(
            label="Download Meta Tags as HTML",
            data=html_content,
            file_name="meta_tags.html",
            mime="text/html"
        )

