def deplacer_colonnes(dfs, col_names, pos):
    if not isinstance(dfs, list):
        dfs = [dfs]
        single_input = True
    else:
        single_input = False
    
    if isinstance(col_names, str):
        col_names = [col_names]
    
    if isinstance(pos, int):
        pos = [pos]
    
    if len(col_names) != len(pos):
        raise ValueError("La liste des colonnes et la liste des positions doivent avoir la même longueur.")
    
    dfs_modifies = []
    
    for df in dfs:
        df_copy = df.copy()
        temp_cols = {col:df_copy.pop(col) for col in col_names}
        for col, ps in zip(col_names, pos):
            df_copy.insert(ps, col, temp_cols[col])
        dfs_modifies.append(df_copy)
    return dfs_modifies[0] if single_input else dfs_modifies

def convert_to_category(df, col_names):
    for col in col_names:
        df[col] = df[col].astype('category')
    return df