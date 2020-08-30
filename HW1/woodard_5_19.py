#Darrian Woodard
#1593984

# FIXME (1):
services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12
}
print('Davy'+"'"+'s auto shop services')
for key, value in services.items():
    print(key, '-- $' + str(value))

#FIXME (2)
service1 = input('\nSelect first service:\n')
service2 = input('Select second service:\n')

#FIXME (3)
print('\nDavy'+"'"+'s auto shop invoice')


if service2 == '-':
    service2 = "No service"
    print('\nService 1:', service1 + ', $' + str(services[service1]))
    print('Service 2:', service2)
    print('\nTotal: $' + str(services[service1]))

elif service1 == '-':
    service1 = "No service"
    print('\nService 1:', service1)
    print('Service 2:', service2 + ', $' + str(services[service2]))
    print('\nTotal: $' + str(services[service2]))
else:
    print('\nService 1:', service1 + ', $' + str(services[service1]))
    print('Service 2:', service2 + ', $' + str(services[service2]))
    total = services[service2] + services[service1]
    print('\nTotal: $' + str(total))