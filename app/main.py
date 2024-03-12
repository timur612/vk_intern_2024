import streamlit as st
import pandas as pd

from src.predict import get_predictions

if __name__ == "__main__":
    st.title("ВК - стажировка")
    st.title("Ранжировщик")

    uploaded_file = st.file_uploader("Прикрепите файл данных (csv)", type=["csv"])

    get_data = False
    data = None
    data_name = None
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            data_name = uploaded_file.name
            st.write(data)
            get_data = True
        except ():
            get_data = False

    predictions = None
    csv_predictions = None
    get_preds = False
    if st.button("Получить предсказание"):
        if get_data:
            if "target" in data.columns:
                data = data.drop(["target"], axis=1)
            predictions = get_predictions(data.drop(["search_id"], axis=1))

            try:
                csv_predictions = (
                    pd.DataFrame(
                        {"target": predictions, "saerch_id": data["search_id"].values}
                    )
                    .to_csv(index=False)
                    .encode("utf-8")
                )
                get_preds = True
            except ():
                get_preds = False

    if get_preds:
        st.download_button(
            label="Скачать файл",
            data=csv_predictions,
            file_name=f"{data_name.split('.')[0]}_predictions.csv",
            mime="text/csv",
        )
