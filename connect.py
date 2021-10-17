from contracts.documents import AddressParser
from os import listdir
import json
import sys


parser = AddressParser()
parser.connect_with_tables('C:/Users/alway/PycharmProjects/ExtractData/tables')