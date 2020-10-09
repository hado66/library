from django.test import TestCase

# Create your tests here.
a = []

b = [{}, {1: 3}, {9: [1, 2, 3]}]

a = a+b
print(a)
