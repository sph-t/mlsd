import sys
import numpy as np
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
import streamlit as st

K_DEFAULT = 10
torch.classes.__path__ = [] # отсюда https://discuss.streamlit.io/t/message-error-about-torch/90886/7 
# если проблемы при запуске из докера, это именно эта строчка

embedder = SentenceTransformer("all-MiniLM-L6-v2")
item_embeddings = np.load("items_embeddings.npy")
items = pd.read_csv("items_with_search_text.csv")


def find_top_k(query: str, k: int):
    query_embedding = embedder.encode(query, convert_to_tensor=True)

    similarity_scores = embedder.similarity(query_embedding, item_embeddings)[0]
    scores, indices = torch.topk(similarity_scores, k=K_DEFAULT)

    item_names = [items["Product Name"][idx.item()] for idx in indices]
    
    return item_names


def streamlit_ui():
    st.title("Поиск по товарам")
    query = st.text_input("Введите запрос: ")
    # k = st.slider("Количество товаров", 1, 20, K_DEFAULT)
    
    if query:
        results = find_top_k(query, K_DEFAULT)
        st.markdown(f"### Топ {K_DEFAULT} подходящих товаров:")

        for result in results:
            st.markdown(f"- {result}")


if __name__ == "__main__":
    streamlit_ui()
