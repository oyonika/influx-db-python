# query_api = client.query_api()
# query = ' from(bucket:"my-bucket")\
# |> range(start: -10m)\
# |> filter(fn:(r) => r._measurement == "my_measurement")\
# |> filter(fn: (r) => r.location == "Prague")\
# |> filter(fn:(r) => r._field == "temperature" )'
# result = query_api.query(org=org, query=query)
# results = []
# for table in result:
#     for record in table.records:
#         results.append((record.get_field(), record.get_value()))

# print(results)
# [(temperature, 25.3)]