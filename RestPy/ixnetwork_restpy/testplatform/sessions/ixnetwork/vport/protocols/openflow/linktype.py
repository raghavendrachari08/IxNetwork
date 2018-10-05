
# Copyright 1997 - 2018 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
    
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LinkType(Base):
	"""The LinkType class encapsulates a required linkType node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the LinkType property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'linkType'

	def __init__(self, parent):
		super(LinkType, self).__init__(parent)

	@property
	def OfppfCopper(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('ofppfCopper')
	@OfppfCopper.setter
	def OfppfCopper(self, value):
		self._set_attribute('ofppfCopper', value)

	@property
	def OfppfFiber(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('ofppfFiber')
	@OfppfFiber.setter
	def OfppfFiber(self, value):
		self._set_attribute('ofppfFiber', value)