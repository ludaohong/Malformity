#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure
from common.entities import Hash
from canari.maltego.entities import Domain
from common.vt import bsearch
from canari.maltego.message import UIMessage

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2013, Malformity Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Keith Gilbert - @digital4rensics'
__email__ = 'Keith@digital4rensics.com'
__status__ = 'Development'

__all__ = [
    'dotransform',
]

@configure(
    label='Domain Search - VirusTotal [Private]',
    description='Searches VirusTotal for samples based on a domain',
    uuids=[ 'malformity.v1.VT_Priv_Domain2Hash' ],
    inputs=[ ( 'VirusTotal', Domain ) ],
    debug=True
)

def dotransform(request, response):
    data = bsearch(request.value)
    try:
    	if data['response_code'] == 1:
    		results = data['hashes']
    		for result in results:
    			response += Hash(result)
    except:
    	response += UIMessage(data['verbose_msg'])
    
    return response