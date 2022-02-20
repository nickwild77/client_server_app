import os
import yaml

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(CURRENT_DIR, '', 'file.yaml')
data = {
    'items': ['iphone_13_pro', 'ipad_mini', 'magic_mouse', 'macbook_pro'],
    'items_quantity': 4,
    'items_price': {
        'iphone_13_pro': '600€-1000€',
        'ipad_mini': '400€-700€',
        'magic_mouse': '50€-70€',
        'macbook_pro': '1000€-3000€'
    }
}

with open(filename, 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)

with open(filename) as f_n:
    print(f_n.read())
