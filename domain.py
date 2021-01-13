from urllib.parse import urlparse

#get domain name (example.com)
def get_domain_name(url):
    """
        This function gets the last two name section of the website
        eg: www.m.thenewboston.com
        extract only "thenewboston.com"
    """
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

#get sub domain name (name.example.com)
def get_sub_domain_name(url):
    """
    Tip: when working with networks or server, websites,
    remember to include try catch exceptions.
    This function parse in the url data and return network location.
    """
    try :
        #parse in using urlparse (python function) and return network location
        return urlparse(url).netloc
    except:
        return ''




#testing this module.
#print(get_sub_domain_name('https://singapore.locanto.sg/ID_2498192936/Full-Stack-Software-Developer.html'))