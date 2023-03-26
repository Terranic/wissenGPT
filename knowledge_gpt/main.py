import streamlit as st
from openai.error import OpenAIError

from knowledge_gpt.components.sidebar import sidebar
from knowledge_gpt.utils import (
    embed_docs,
    get_answer,
    get_sources,
    parse_docx,
    parse_pdf,
    parse_txt,
    search_docs,
    text_to_docs,
    wrap_text_in_html,
)


def clear_submit():
    st.session_state["submit"] = False

key = st.secrets["OPENAI_API_KEY"]
st.session_state["OPENAI_API_KEY"] = key
print("OPENAI Key: ", key[:7], "...")

st.set_page_config(page_title="WissenGPT", page_icon="📖", layout="wide")
st.header("📖WissenGPT")

sidebar()

uploaded_file = st.file_uploader(
    "Lade ein pdf, docx oder txt file hoch",
    type=["pdf", "docx", "txt"],
    help="Keine Unterstützung von gescannten Dokumenten!",
    on_change=clear_submit,
)

index = None
doc = None
if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        doc = parse_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        doc = parse_docx(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        doc = parse_txt(uploaded_file)
    else:
        raise ValueError("Dateityp unbekannt!")
    text = text_to_docs(doc)
    try:
        with st.spinner("Lese dokument...⏳"):
            index = embed_docs(text)
        st.session_state["api_key_configured"] = True
    except OpenAIError as e:
        st.error(e._message)

query = st.text_area("Stell eine Frage zum Dokument", on_change=clear_submit)

show_all_chunks = False
show_full_doc = False

#with st.expander("Extra-Optionen"):
#    show_all_chunks = st.checkbox("Show all chunks retrieved from vector search")
#    show_full_doc = st.checkbox("Show parsed contents of the document")

if show_full_doc and doc:
    with st.expander("Dokument"):
        # Hack to get around st.markdown rendering LaTeX
        st.markdown(f"<p>{wrap_text_in_html(doc)}</p>", unsafe_allow_html=True)

button = st.button("Los...")
if button or st.session_state.get("submit"):
    if not st.session_state.get("api_key_configured"):
        st.error("Please configure your OpenAI API key!")
    elif not index:
        st.error("Please upload a document!")
    elif not query:
        st.error("Please enter a question!")
    else:
        st.session_state["submit"] = True
        # Output Columns
        answer_col, sources_col = st.columns(2)
        sources = search_docs(index, query)

        try:
            answer = get_answer(sources, query)
            if not show_all_chunks:
                # Get the sources for the answer
                sources = get_sources(answer, sources)

            with answer_col:
                st.markdown("#### Antwort")
                st.markdown(answer["output_text"].split("SOURCES: ")[0])

            with sources_col:
                st.markdown("#### Quellen")
                for source in sources:
                    st.markdown(source.page_content)
                    st.markdown(source.metadata["source"])
                    st.markdown("---")

        except OpenAIError as e:
            st.error(e._message)
