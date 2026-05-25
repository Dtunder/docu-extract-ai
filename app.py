import streamlit as st
import tempfile
import os
from src.pdf_reader import extract_text
from src.extractor import extract_document
from src.exporter import to_json, to_csv

st.set_page_config(page_title="DocuExtract-AI", page_icon="📄")

st.title("DocuExtract-AI MVP")
st.write("Structured data extraction from invoice and contract PDFs for German KMUs.")

uploaded_file = st.file_uploader("Upload PDF Document", type="pdf")
doc_type = st.selectbox("Document Type", ["auto", "invoice", "contract"])

if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        pages = extract_text(tmp_path)
        os.remove(tmp_path)

    if not pages:
        st.error("Failed to extract text from PDF or PDF is empty.")
    else:
        st.success(f"Successfully read {len(pages)} page(s).")

        with st.spinner("Extracting structured data using AI..."):
            extracted_data = extract_document(pages, doc_type)

        if extracted_data:
            st.subheader("Extracted Data")

            # Display flat data as table
            flat_data = {k: v for k, v in extracted_data.items() if not isinstance(v, list) or (isinstance(v, list) and not all(isinstance(i, dict) for i in v))}
            if flat_data:
                st.table(flat_data)

            # Display nested data (like line items)
            for k, v in extracted_data.items():
                if isinstance(v, list) and all(isinstance(i, dict) for i in v):
                    st.write(f"**{k.replace('_', ' ').title()}**")
                    st.table(v)

            st.subheader("Downloads")
            json_str = to_json(extracted_data)
            csv_str = to_csv(extracted_data)

            col1, col2 = st.columns(2)
            with col1:
                st.download_button("Download JSON", data=json_str, file_name="extracted_data.json", mime="application/json")
            with col2:
                st.download_button("Download CSV", data=csv_str, file_name="extracted_data.csv", mime="text/csv")
        else:
            st.warning("No data extracted.")
