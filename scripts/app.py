"""
Credit Card Cancellation Analysis: Identifying Customer Churn Reasons from Data

This script automatically generates a timestamped folder containing histograms for all dataset features segmented by cancellation status, and compiles them into a single PDF report for comprehensive analysis.
"""

import os
import datetime
import pandas as pd
import plotly.express as px
import PyPDF2

DATA_FILE_PATH = '../dataset/data-bank.csv'
HISTOGRAM_BASE_DIR = '../results/HISTOGRAM'


def load_and_clean_data(file_path):
    """Load and clean the customer data for analysis."""
    df = pd.read_csv(file_path, encoding="latin1")
    df = df.drop(["CLIENTNUM", "Sexo"], axis=1)
    df = df.dropna()
    return df


def show_data_overview(df):
    """Display information and statistics about the dataset."""
    print("DataFrame Info")
    print(df.info())
    print("-" * 100)
    pd.set_option('display.max_columns', None)
    print("Full Cleaned DataFrame")
    print(df)
    print("-" * 100)
    print("Descriptive Statistics")
    print(df.describe().round(1))
    print("-" * 100)
    print("Remaining Columns")
    print(list(df.columns.values))
    print("-" * 100)


def analyze_cancellation_distribution(df):
    """Analyze the distribution of customer churn (cancellation)."""
    print("Customer Churn Distribution")
    churn_count = df["Categoria"].value_counts()
    print(churn_count)
    churn_percentage = df["Categoria"].value_counts(normalize=True).round(2)
    print(churn_percentage)
    print("-" * 100)


def create_histogram_folder():
    """Create a folder to save histogram plots."""
    current_timestamp = datetime.datetime.today().strftime("%Y-%m-%d_%H%M%S")
    folder_path = os.path.join(HISTOGRAM_BASE_DIR, current_timestamp)
    os.makedirs(folder_path, exist_ok=True)
    print(f'Folder {folder_path} created or already exists')
    print("-" * 100)
    return folder_path


def generate_histograms(df, folder_path):
    """Generate and save histograms for each column in the dataset."""
    for column in df:
        fig = px.histogram(df, x=column, color="Categoria", color_discrete_sequence=px.colors.qualitative.D3)
        fig.write_image(os.path.join(folder_path, f"{column}.pdf"))
    print(f"Histograms generated. Check the folder: {folder_path}")


def merge_histograms_to_pdf(folder_path):
    """Merge all histogram PDFs into a single file."""
    histogram_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    merger = PyPDF2.PdfMerger()
    for pdf_file in histogram_files:
        merger.append(os.path.join(folder_path, pdf_file))
    merged_pdf_path = f"{folder_path}-Histograms.pdf"
    merger.write(merged_pdf_path)
    print(f"Combined PDF created successfully: {merged_pdf_path}")
    print("-" * 100)


def main():
    data = load_and_clean_data(DATA_FILE_PATH)
    show_data_overview(data)
    analyze_cancellation_distribution(data)
    histogram_folder = create_histogram_folder()
    generate_histograms(data, histogram_folder)
    merge_histograms_to_pdf(histogram_folder)


if __name__ == "__main__":
    main()