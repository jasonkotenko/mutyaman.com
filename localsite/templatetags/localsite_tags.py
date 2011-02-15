from django import template

register = template.Library()

@register.filter(name='qty_price')
def qty_price(product, qty):
  return product.get_qty_price(qty);
