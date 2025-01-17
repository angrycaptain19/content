

URL_RES_JSON = {
    'results': [{'confidence': 50, 'display_text': 'http://www.malware.com',
                 'files': [{'confidence': 50, 'display_text': '934a72f37d861097c85dc3c2e16bca3c',
                            'key': '934a72f37d861097c85dc3c2e16bca3c', 'last_seen': '2020-10-07T20:26:30.000Z',
                            'relationship': 'contactsC2At', 'relationship_created_on': '2020-10-07T20:04:51.000Z',
                            'relationship_last_published': '2020-10-07T20:04:51.000Z', 'type': 'file',
                            'uuid': '8498bf4f-53e0-4cc0-aa44-10917eeec78c',
                            'sha1': '842ccc77b6ea22b4ef17ee6278819b4393051103',
                            'sha256': 'd2b7f1f38705374306c3a7775158933e4963c88a05bedad60078e3fb514c444d',
                            'href': '/rest/fundamental/v0/8498bf4f-53e0-4cc0-aa44-10917eeec78c'},
                           {'confidence': 50, 'display_text': '8d648dc2e1c5ebc383b5f62acefc6875',
                            'key': '8d648dc2e1c5ebc383b5f62acefc6875', 'last_seen': '2020-10-06T00:59:33.000Z',
                            'relationship': 'contactsC2At', 'relationship_created_on': '2020-10-05T23:51:53.000Z',
                            'relationship_last_published': '2016-09-10T01:05:09.000Z', 'type': 'file',
                            'uuid': '9fea5b89-2ff8-4881-849c-6bbee6d80320',
                            'sha1': 'd026df22ad7c9773b12d99795d7a15b3a31d83b0',
                            'sha256': '022728d858c0206adca9ee32ba92e190723d6d42207dd1872657030f19bc27b2',
                            'href': '/rest/fundamental/v0/9fea5b89-2ff8-4881-849c-6bbee6d80320'},
                           {'confidence': 50, 'display_text': '218dfd9d968892d7ae7960fb4a85de35',
                            'key': '218dfd9d968892d7ae7960fb4a85de35', 'last_seen': '2020-10-18T15:24:12.000Z',
                            'malware_family': ['JavaScript Downloader'], 'relationship': 'contactsC2At',
                            'relationship_created_on': '2020-10-18T14:49:36.000Z',
                            'relationship_last_published': '2020-10-18T14:49:36.000Z', 'type': 'file',
                            'uuid': 'b96a5814-bf98-4ad9-9980-7632f5c6a20f',
                            'sha1': 'd47c7a84d72b64f6f690a422e004fee4bc892eab',
                            'sha256': 'bc75daf4592c8aace308f72a6393927e2ae174784cbdaba1b6b641b60aa2c84d',
                            'href': '/rest/fundamental/v0/b96a5814-bf98-4ad9-9980-7632f5c6a20f'}],
                 'index_timestamp': '2020-10-26T09:29:54.600Z',
                 'key': 'http://www.malware.com',
                 'last_modified': '2020-10-18T15:25:00.000Z',
                 'last_published': '2020-10-05T23:51:53.000Z', 'last_seen': '2020-10-06T00:59:33.000Z',
                 'last_seen_as': ['MALWARE_C2'], 'malware_family': ['JavaScript Downloader'],
                 'replication_id': 1603034700680000002,
                 'seen_at': [{'confidence': 50,
                              'display_text': 'JavaScript Downloader', 'key': 'JavaScript Downloader',
                              'last_seen': '2020-10-18T15:24:12.000Z', 'relationship': 'seenAt',
                              'relationship_created_on': '2020-10-18T14:49:36.000Z',
                              'relationship_last_published': '2020-10-18T14:49:36.000Z',
                              'type': 'malware_family', 'uuid': 'f1b2bae6-6909-4303-9584-d91e156a13f7',
                              'href': '/rest/fundamental/v0/f1b2bae6-6909-4303-9584-d91e156a13f7'}],
                 'severity': 3,
                 'threat_types': ['Cyber Crime'],
                 'type': 'url',
                 'uuid': '60a2ef03-8650-490b-9542-0f8cc21e5c6d',
                 'arguments': [], 'path': ['nuklyuql']}], 'total_size': 1, 'page': 1, 'page_size': 25, 'more': False}

URL_INTEL_JSON = {'results': [
    {
        'key': 'http://www.malware.com',
        'title': 'my intelligence alert',
        'type': 'intelligence_alert',
        'uuid': '60a2ef03-8650-490b-9542-0f8cc21e5c6d'
    },
    {
        'key': 'http://www.malware.com',
        'title': 'my intelligence report',
        'type': 'intelligence_report',
        'uuid': '70a2ef03-8650-490b-9542-0f8cc21e5c6d'
    }
],
    'total_size': 2,
    'page': 1,
    'page_size': 25,
    'more': False
}

IP_RES_JSON = {
    'results':
        [{'confidence': 100, 'display_text': '0.0.0.0',
          'files': [{'display_text': 'bf0fea133818387cca7eaef5a52c0aed', 'key': 'bf0fea133818387cca7eaef5a52c0aed',
                     'relationship': 'contactsC2At', 'relationship_created_on': '2018-06-06T13:13:37.000Z',
                     'relationship_last_published': '2018-06-06T13:13:37.000Z', 'type': 'file',
                     'uuid': 'ec1af5a4-afe1-4580-b51b-f6f3c7609c75', 'sha1': '0a30b5b24196e503c4a21dcfd1447b28a39af314',
                     'sha256': 'dd7e69e14c88972ac173132b90b3f4bfb2d1faec15cca256a256dd3a12b6e75d',
                     'href': '/rest/fundamental/v0/ec1af5a4-afe1-4580-b51b-f6f3c7609c75'},
                    {'display_text': '1535acbcae591b0d03ef7518cb56883e', 'key': '1535acbcae591b0d03ef7518cb56883e',
                     'relationship': 'contactsC2At', 'relationship_created_on': '2018-01-04T01:10:32.000Z',
                     'relationship_last_published': '2018-01-04T01:10:32.000Z', 'type': 'file',
                     'uuid': 'ff8cbab2-d81d-4839-9045-d566282ef4b9', 'sha1': '36b5e59a01e7f244d4a3bbb539e57aa468115dc8',
                     'sha256': '6fcf4592f9261d5734fb3b8534f6839ab65f68fd9ff14a9005225135e743226c',
                     'href': '/rest/fundamental/v0/ff8cbab2-d81d-4839-9045-d566282ef4b9'}],
          'index_timestamp': '2020-10-22T08:00:43.518Z',
          'key': '0.0.0.0',
          'last_modified': '2020-10-08T20:55:58.000Z',
          'last_published': '2018-01-04T15:22:25.000Z',
          'last_seen_as': ['MALWARE_DOWNLOAD', 'MALWARE_C2'],
          'malware_family': [], 'replication_id': 1602190558122000000,
          'severity': 4,
          'threat_types': ['Cyber Espionage'],
          'type': 'ip',
          'uuid': 'e5d40481-bea4-4d33-95d2-e029cff28084',
          'ip_int': 3105436253, 'ip_type': '4'}],
    'total_size': 1,
    'page': 1,
    'page_size': 25,
    'more': False}

IP_INTEL_JSON = {'results': [
    {
        'key': '0.0.0.0',
        'title': 'my intelligence alert',
        'type': 'intelligence_alert',
        'uuid': 'e5d40481-bea4-4d33-95d2-e029cff28084'
    },
    {
        'key': '0.0.0.0',
        'title': 'my intelligence report',
        'type': 'intelligence_report',
        'uuid': 'f5d40481-bea4-4d33-95d2-e029cff28084'
    }
],
    'total_size': 2,
    'page': 1,
    'page_size': 25,
    'more': False
}

DOMAIN_RES_JSON = {
    'results': [
        {
            'confidence': 100,
            'display_text': 'mydomain.com',
            'key': 'mydomain.com',
            'last_published': '2021-08-12T19:12:58.000Z',
            'last_seen_as': [
                'MALWARE_C2'
            ],
            'malware_family': [
                'CobaltStrike'
            ],
            'severity': 3,
            'threat_types': [
                'Cyber Espionage',
                'Cyber Crime'
            ],
            'type': 'domain',
            'uuid': '461b5ba2-d4fe-4b5c-ac68-35b6636c6edf'
        }
    ],
    'total_size': 1,
    'page': 1,
    'page_size': 25,
    'more': False
}

DOMAIN_INTEL_JSON = {'results': [
    {
        'key': 'mydomain.com',
        'title': 'my intelligence alert',
        'type': 'intelligence_alert',
        'uuid': '461b5ba2-d4fe-4b5c-ac68-35b6636c6edf'
    },
    {
        'key': 'mydomain.com',
        'title': 'my intelligence report',
        'type': 'intelligence_report',
        'uuid': '561b5ba2-d4fe-4b5c-ac68-35b6636c6edf'
    }
],
    'total_size': 2,
    'page': 1,
    'page_size': 25,
    'more': False
}



UUID_RES_JSON={
            'confidence': 100,
            'display_text': 'mydomain.com',
            'key': 'mydomain.com',
            'last_published': '2021-08-12T19:12:58.000Z',
            'last_seen_as': [
                'MALWARE_C2'
            ],
            'malware_family': [
                'CobaltStrike'
            ],
            'severity': 3,
            'threat_types': [
                'Cyber Espionage',
                'Cyber Crime'
            ],
            'type': 'domain',
            'uuid': '461b5ba2-d4fe-4b5c-ac68-35b6636c6edf'
        }
