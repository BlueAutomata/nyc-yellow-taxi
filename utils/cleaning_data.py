import pandas as pd

def remove_outliers(df, columns):
    """
    Remove outliers from specified numerical columns using the IQR method.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): List of column names to remove outliers from.

    Returns:
    pd.DataFrame: A DataFrame with outliers removed.
    """
    df_clean = df.copy()
    for col in columns:
        if pd.api.types.is_numeric_dtype(df_clean[col]):
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]
    return df_clean