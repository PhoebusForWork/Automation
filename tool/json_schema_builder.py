from genson import SchemaBuilder


if __name__ == "__main__":
    # 產生json Schema
    asd = SchemaBuilder()
    asd.add_object({"data": [{"id": 1, "name": "北京"}]})
    asd.to_schema()
    print(asd.to_json(indent=4))
