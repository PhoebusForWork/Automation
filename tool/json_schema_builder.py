from genson import SchemaBuilder

# 餵入response body
json_data = {
  "data": "string"
}

# 產生json Schema
make = SchemaBuilder()
make.add_object(json_data)
make.to_schema()
print(make.to_json(indent=4))
