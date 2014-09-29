#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):
   	tag = 'html'
   	indent = '    '

	def __init__(self, content = None):

		if content is None:
			self.content_list = []
		else:

			self.content_list = [content]

   	def render(self, file_out, ind = ""):
   		"""render the content to file object"""
   		file_out.write("<" + self.tag + ">")
   		file_out.write("\n".join(self.content_list))
   		file_out.write("</" + self.tag +">")

   	def append(self, newcontent):
   		""" add something within the html element"""
   		self.content_list.append(newcontent)


