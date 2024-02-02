class Organization(dict):
    def __init__(self, **kwargs):
        base = {
            'image': [],
            'name': 'BtpStore',
            'description': '',
            'city': 'Yaoundé',
            'region': 'Centre-Cameroun',
            'zip_code': 59000,
            'fonder': {
                'name': 'Jiomekong',
                'surname': 'Azanzi',
                'title': 'Founder, SEO'
            }
        }
        if kwargs:
            organization = {**organization, **kwargs}
        self.update({'organization': base})

organization = Organization()

def organization_context_processor(request):
    return {'organization': organization}