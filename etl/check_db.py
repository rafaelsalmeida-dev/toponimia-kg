import psycopg

with psycopg.connect("dbname=tk user=tk password=tk host=localhost") as conn:
    print(conn.execute("Select PostGIS_Version()").fetchone())