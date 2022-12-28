from marshmallow import Schema, fields

class EventSchema(Schema):
    id = fields.String(dump_only=True)
    event_name = fields.String(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)

# class EventsUpdateSchema(Schema):
#     event_name = fields.String(required=True)
#     start_date = fields.DateTime(required=True)
#     end_date = fields.DateTime(required=True)
# class PlainItemSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str(required=True)
#     price = fields.Float(required=True)


# class PlainStoreSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str()


# class ItemSchema(PlainItemSchema):
#     store_id = fields.Int(required=True, load_only=True)
#     store = fields.Nested(PlainStoreSchema(), dump_only=True)


# class ItemUpdateSchema(Schema):
#     name = fields.Str()
#     price = fields.Float()


# class StoreSchema(PlainStoreSchema):
#     items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
