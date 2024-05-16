from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    product_name = fields.Str(required=True, strict=True)
    display_name = fields.Str(required=True, strict=True)
    selling_price = fields.Int(required=True, strict=True, validate=validate.Range(min=0))
    mrp = fields.Int(required=True, strict=True, validate=validate.Range(min=0))
    quantity = fields.Int(required=True, strict=True, validate=validate.Range(min=0))
    product_weight = fields.Int(required=True, strict=True, validate=validate.Range(min=0))
    measuring_unit = fields.Str(required=True, strict=True)
    expiry_date = fields.Date(required=True, strict=True)


class UpdateProductSchema(Schema):
    quantity = fields.Int(required=True, strict=True, validate=validate.Range(min=0))

