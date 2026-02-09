sqli_error_messages = [
# MySQL
"You have an error in your SQL syntax",
"Warning: mysql_fetch_array()",
"Warning: mysql_fetch_assoc()",
"Warning: mysql_num_rows()",
"MySQL server version for the right syntax",
"supplied argument is not a valid MySQL result resource",

# PostgreSQL
"PG::SyntaxError",
"pg_query(): Query failed",
"unterminated quoted string",
"invalid input syntax for type",

# MSSQL
"Unclosed quotation mark after the character string",
"Microsoft OLE DB Provider for SQL Server",
"Incorrect syntax near",
"The multi-part identifier could not be bound",

# Oracle
"ORA-00933: SQL command not properly ended",
"ORA-00936: missing expression",
"ORA-01756: quoted string not properly terminated",
"ORA-00921: unexpected end of SQL command",

# SQLite
"SQLite3::SQLException",
"near \": syntax error\"",
"unrecognized token",

# Generic / Framework related
"SQLSTATE[42000]",
"SQLSTATE[HY000]",
"PDOException",
"JDBC SQLException",
"ODBC SQL Server Driver"
]