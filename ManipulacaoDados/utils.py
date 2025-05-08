def hora_verao(df, mes):
    if df["month"] == mes:
        return df["hour"] - 1
    else:
        return df["hour"]