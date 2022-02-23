import xmlrpc.client

url = 'https://edu-alberti.odoo.com'
db = 'edu-alberti'
username = 'mborvar361@g.educaand.es'
password = '!Lunatommy19'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Ejercicio1
print(models.execute_kw(db, uid, password,
                        'sale.order', 'search_count',
                        [[['amount_total', '>', '1000']]]))

# Ejercicio2
print(models.execute_kw(db, uid, password,
                        'sale.order', 'search_read',
                        [[['amount_total', '>', '1000']]]
                        , {'fields': ['amount_total'], 'offset': 2, 'limit': 2}))

ventas = models.execute_kw(db, uid, password,
                           'sale.order', 'search_read',
                           [[['amount_total', '>', '1000']]]
                           , {'fields': ['amount_total'], 'offset': 2, 'limit': 2})

print(ventas[0]['amount_total'] + ventas[1]['amount_total'])

# Ejercicio3
print(models.execute_kw(db, uid, password,
                        'product.product', 'search_read',
                        [[['qty_available', '<', 15.0], ['qty_available', '>=', 1.0]]]
                        , {'fields': ['name']}))

# Ejercicio4
print(models.execute_kw(db, uid, password,
                        'res.partner', 'search_read',
                        [[['country_id', '=', 'US']]]
                        , {'fields': ['email']}))

# Ejercicio5
print(models.execute_kw(db, uid, password,
                        'res.partner', 'search_read',
                        [[['message_unread', '=', True]]]
                        , {'fields': ['phone']}))

# Ejercicio6
print(models.execute_kw(db, uid, password,
                        'res.users', 'search_read',
                        [[['totp_enabled', '=', False]]]
                        , {'fields': ['email', 'name', 'phone']}))

# Ejercicio7
ids = models.execute_kw(db, uid, password,
                        'product.product', 'create',
                        [{'name':'Consola'}])
print(ids)
