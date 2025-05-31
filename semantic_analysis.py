import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(csv_path):
    return pd.read_csv(csv_path)


def compute_model_averages(df, output_csv='model_corrections_averages.csv'):
    # Compute average semantic similarity per model and correction type
    model_avg = df.groupby(['model', 'correction'])['semantic_similarity'].mean().reset_index()
    model_avg.to_csv(output_csv, index=False)
    return model_avg


def plot_average_corrections(model_avg):
    """Plot a bar chart of average semantic similarity per model and correction type."""
    plt.figure(figsize=(12, 7))
    sns.barplot(x='model', y='semantic_similarity', hue='correction', data=model_avg, palette='viridis')
    plt.title('Average Semantic Similarity per Model and Correction Type')
    plt.ylabel('Average Semantic Similarity')
    plt.xlabel('Model')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def plot_corrections_distribution(df):
    """Plot a boxplot of semantic similarity by model and correction type."""
    plt.figure(figsize=(12, 7))
    sns.boxplot(x='model', y='semantic_similarity', hue='correction', data=df, palette='Set2')
    plt.title('Distribution of Semantic Similarity by Model and Correction Type')
    plt.ylabel('Semantic Similarity')
    plt.xlabel('Model')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df):
    """Plot a correlation heatmap for numerical columns if more than one exists."""
    numeric_cols = df.select_dtypes(include='number')
    if numeric_cols.shape[1] > 1:
        corr = numeric_cols.corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()
    else:
        print("No additional numerical columns for correlation analysis.")


def main():
    input_csv = 'semantic_similarities.csv'
    df = load_data(input_csv)
    print("First few rows of the data:")
    print(df.head())

    print("\nComputing average corrections per model...")
    model_avg = compute_model_averages(df)
    print(model_avg)

    print("\nPlotting average corrections per model...")
    plot_average_corrections(model_avg)

    print("\nPlotting distribution of corrections by model...")
    plot_corrections_distribution(df)

    print("\nPlotting correlation heatmap (if applicable)...")
    plot_correlation_heatmap(df)

    print("\nAnalysis complete. See generated plots and CSV file for results.")


if __name__ == "__main__":
    main()
