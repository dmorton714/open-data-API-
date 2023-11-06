# url = 'place URL here'

# batch_size = 1000  # Number of records to retrieve per batch
# offset = 0  # Initial offset value
# data_list = []
# # ​Create the feature layer object
# feature_layer = FeatureLayer(url)

# while True:
#     # Query the feature layer with pagination
#     query_result = feature_layer.query(where='1=1', out_fields='*', return_geometry=False, result_offset=offset, result_record_count=batch_size)
    
#     # Retrieve the features from the query result
#     features = query_result.features
    
#     # Process the data for the current batch
#     for feature in features:
#         data_list.append(feature.attributes)
    
#     # Break the loop if the response is empty or the desired number of records is reached
#     if len(features) == 0 or len(data_list) >= 1000:
#         break
    
#     # Increment the offset by the batch size
#     offset += batch_size
# # Create a DataFrame from the data list
# df = pd.DataFrame(data_list)

# df.to_csv('../json_files/local_working.csv')
