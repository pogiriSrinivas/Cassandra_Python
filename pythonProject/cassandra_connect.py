from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['127.0.0.1:9042'])  # Replace '127.0.0.1' with your Cassandra host IP
session = cluster.connect()

# # Use the keyspace you're interested in
# session.set_keyspace('test_keyspace')
#
# # Execute a CQL query to get a list of tables in the keyspace
# rows = session.execute("SELECT table_name FROM system_schema.tables WHERE keyspace_name = 'your_keyspace_name';")
#
# # Iterate over the rows and print the table names
# for row in rows:
#     print(row.table_name)
#
# # Close the connection
# cluster.shutdown()
