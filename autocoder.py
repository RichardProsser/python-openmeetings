"""
Parse API docs from OpenMeetings source and create corresponding .py files.

So far, this generates client-side code only; server-side (Jython) mods TBD

Each doc is in HTML (generated), with the following skeletal structure:
    <div class="method">            Container a for a method specification
    <p>                             Description
    <p>                             Return Type

    #'Params' are optional
    <p>                             Params
        # Each param grouped via <tr>
        <td>                        Type
        <td>                        Fieldname
        <td>                        Description
    #OR
    <i>No Params</i>
    #

    <a>                             REST Sample Call/URL
    
N.B.:
    OpenMeetings API is not really RESTful - just GET in every case!
    Data returned in SOAP format.

"""
import os
from bs4 import BeautifulSoup
from urllib2 import urlopen, HTTPError
from itertools import islice


root_url = 'http://openmeetings.apache.org/'
available_webservices = root_url + 'SoapRestAPI.html'


def get_data(url):
    " Returns HTML contents at given URL"
    try:
        data = urlopen(url)
    except HTTPError, e:
        print 'A problem occured. Please try again.'
        return

    return BeautifulSoup(data)


def generate(target, service):

    url = root_url + service + '.html'
    soup = get_data(url)

    module = "%s.py" % service
    
    INDENT = 4

    fn = dict()   # 'Global' place-holders to build Python function
    
    ##filename = path.join(target, module)
    filename = module
    print "Building %s" % filename
    
    file_handle = open(filename, 'w')
    
    ############
    ## Functions        
    
    def output(data, indent=0):
        # Could use format() here but this is easier!
        fill = ' ' * indent
        for line in data.split('\n'):
            ##print fill + line
            file_handle.write(fill + line + '\n')

    # Processors
    def process_methods(doc):

        def init(section):
            fn['sig'] = ""
            fn['doc'] = ""
            fn['call'] = ""

            ##print "section = %s" % section

        def build(s, section='doc'):
            fn[section] += s + '\n'

        def process_header(method):
            fmt_sig = """def {fn_name}({fn_args}):"""
            fmt_call = """return call("{fn_name}"{fn_args})"""
            header = method.find_next('i').string
            items = header.split()
            _name = items[0]
            items = items[2:-1]    # Drop brackets and function name

            _args = ", ".join(islice(items, 1, None, 3))
            build(fmt_sig.format(fn_name=_name, fn_args=_args), 'sig')

            _args = ", " + _args if len(_args) > 0 else ""
            build(fmt_call.format(fn_name=_name, fn_args=_args), 'call')

        def process_subheader(method):
            # BS find_next() does not work as expected so use find_all()
            subheader = method.find_all('p', limit=2)
            build(subheader[0].text.strip())   # Description

            build("")
            build(subheader[1].text.strip())   # Return type
            
        def process_params(method):
            
            def process_param(param):
                items = param.find_all('td')
                try:
                    build(items[0].text.strip())    # Type
                    build(items[1].text.strip())    # Fieldname
                    build(items[2].text.strip())    # Description
                except AttributeError:
                    # Ignore errors due to empty text!
                    pass
                build("")

            build("")
            build("# Parameters:")

            # Params may not be present
            table = method.find('table')
            if table is not None:
                for row in table.find_all('tr')[1:]:     # Skip <th> row
                    process_param(row)
            else:
                build("No Params")

        def process_sample(method):
            build("")
            build("# Sample Call/URL:")
            build(method.find('a', href=True)['href'])

    
        def produce_output():
            output(fn['sig'])
            output('"""', INDENT)                 # Triple quote
            output(fn['doc'], INDENT)
            output('"""', INDENT)                 # Triple quote

            output(fn['call'], INDENT)
            
        for div in doc.find_all('div', class_='method'):
            init(div)
            process_header(div)
            process_subheader(div)
            process_params(div)
            process_sample(div)

            produce_output()


    # Static output                        
    output('"""')                 # Triple quote
    output("Generated Python API code, for %s" % service)
    output('"""')                 # Triple quote

    output('')
    output('from . import call')
    output('')

    # Dynamic output
    process_methods(soup)
    
    file_handle.close()
    
    
def generate_all(mode):

    # Form list of services to be processed
    # N.B.: document is badly formed (<a> within <blockquote>)!
    soup = get_data(available_webservices)
    bq = soup.find("blockquote").contents[1]

    services = [a.text.strip() for a in bq.find_all('a')]

    for service in services:
        generate('client', service)


    

if __name__ == '__main__':
    generate_all('client')
