import shodan 
import argparse

def parse_arguments():
    """create the arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-A", "--API", help="Your api key")
    parser.add_argument("-S", "--SEEK", help="Your search terms")
    return parser.parse_args()

def search_shodan(search, apikey):
    if apikey:
        API_KEY = apikey
    else:
        API_KEY = '''

    api = shodan.Shodan(API_KEY)
    ips_and_ports = []

    #get IPs from Shodan Search
    try:
        results = api.search(search, page=1)
        total_results = results['total']
        print '[++] Total results: {0}'.format(total_results)
        print '[++] First page:'
        for x in results ['matches']:
            ip = x['ip_str']
            port = x['port']
            ip_port = '{0}:{1}'.format(ip,port)
            print '     ', ip_port

    except Exception as e:
        print '[!!] OOPS! Shodan search error:', e 
