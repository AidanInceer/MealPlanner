def get_sql_file(sqlfilepath):
    """Get an sql query for the specified filepath.

    Args:
        sqlfilepath (str): sqlfile path.

    Returns:
        sql (str): sql query
    """
    with open(sqlfilepath) as file:
        sql = file.read()
    return sql
