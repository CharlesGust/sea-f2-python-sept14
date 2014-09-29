class Element(object):


    tag = 'HTML'
    indent = '    '
    # content = ''

    def __init__(self, content = None): #initializer
        if content is not None:  #Check for none
            self.content = [str(content)]  # Making a list to append (knowing append in future)
        else:
            self.content = []  #

    #def write(self):

    def append(self, new_content):
        ''' Add some new content to the element '''
        self.content.append(new_content)  # Now you can append content using this method

    def render(self, file_out, ind = ""):
        ''' render the contet to the given file like object '''
        file_out.write(ind + "<"+ self.tag+">" + ind + self.indent)
        file_out.write( "\n" + ind + self.indent).join(self.content) )
        file_out.write("\n" + ind + "<"/+self.tag + ">")


#e = Element()
#e.content
#e.indent
#e.Element['this is some content']
#e.append('some additional content')
