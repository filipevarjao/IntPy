# support/stdfunc.py
#
# Copyright 2008 Rafael Menezes Barreto <rmb3@cin.ufpe.br,
# rafaelbarreto87@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.


"""Rigorous IEEE 754 standard functions module

Given the fact that the math module of Python doesn't provide standard
functions totally conformant with IEEE 754, we implement ourselves a conformant
one.

It was developed in CIn/UFPE (Brazil) by Rafael Menezes Barreto
<rmb3@cin.ufpe.br, rafaelbarreto87@gmail.com> as part of the IntPy package and
it's free software.

Modifi by Filipe R. G. Varjão
<frgv@cin.ufpe.br, varjaofilipe@gmail.com>
"""


from intpy.support import rounding 
from intpy import*
import math


def acos(self, other=None):
# Return arc cosine of interval

	if other != None:
		intv = IReal(self, other)
	else:
		if type(self) == float or type(self) == str:
			intv = IReal(self)
		else:
			intv = self
 
	if math.acos(intv.inf) > math.acos(intv.sup):
		inf = max(intv.inf, intv.sup)
		sup = min(intv.inf, intv.sup)
	else:
		inf = intv.inf
		sup = intv.sup

	ireal.rounding.set_mode(1)

	ireal.rounding.set_mode(-1)
	ireal.rounding.set_mode(-1)

	new_inf = math.acos(inf)
	ireal.rounding.set_mode(1)
	new_sup = IReal(math.acos(sup))
	new_sup = new_sup.sup

	temp = new_inf
	return IReal(min(temp,new_sup), '%.15f' % new_sup)


def asin(self, other=None):
 # Return arc sine of interval

	if other != None:
		intv = IReal(self, other)
	else:
		if type(self) == float or type(self) == str:
			intv = IReal(self)
		else:
			intv = self
 
	if math.asin(intv.inf) > math.asin(intv.sup):
		inf = max(intv.inf, intv.sup)
		sup = min(intv.inf, intv.sup)
	else:
		inf = intv.inf
		sup = intv.sup


	ireal.rounding.set_mode(1)

	ireal.rounding.set_mode(-1)
	ireal.rounding.set_mode(-1)

	new_inf = math.asin(inf)
	ireal.rounding.set_mode(1)
	new_sup = IReal(math.asin(sup))
	new_sup = new_sup.sup
 
	temp = new_inf
	return IReal(min(temp,new_sup), '%.15f' % new_sup)

	
def atan(self, other=None):
# Return arc sine of interval

	if other != None:
		intv = IReal(self, other)
	else:
		if type(self) == float or type(self) == str:
  			intv = IReal(self)
		else:
			intv = self
 
	if math.atan(intv.inf) > math.atan(intv.sup):
		inf = max(intv.inf, intv.sup)
		sup = min(intv.inf, intv.sup)
	else:
		inf = intv.inf
		sup = intv.sup


	ireal.rounding.set_mode(1)

	ireal.rounding.set_mode(-1)
	ireal.rounding.set_mode(-1)

	new_inf = math.atan(inf)
	ireal.rounding.set_mode(1)
	new_sup = max(float(IReal('%.16f' % math.atan(sup)).sup), float(IReal('%.19f' % math.atan(sup)).sup))
 
	temp = new_inf
	return IReal(min(temp,new_sup), new_sup)


def cos(self, other=None):
# Return cosine of interval

	if other != None:
		intv = IReal(self, other)
	else:
		if type(self) == float or type(self) == str:
			intv = IReal(self)
		else:
			intv = self

	if intv in IReal(0, math.pi):
		if math.cos(intv.inf) > math.cos(intv.sup):
			inf = max(intv.inf, intv.sup)
			sup = min(intv.inf, intv.sup)
		else:
			inf = intv.inf
			sup = intv.sup


		ireal.rounding.set_mode(1)
	
		ireal.rounding.set_mode(-1)
		ireal.rounding.set_mode(-1)

		new_inf = math.cos(inf)
		ireal.rounding.set_mode(1)
		new_sup = IReal(math.cos(sup))
		new_sup = new_sup.sup

	else:
 		return  "Your interval should be between [0, PI]"

	if new_inf <= 6.1230317691118863e-17:
		new_inf = 0
	temp = new_inf

	return IReal(min(temp,new_sup), '%.15f' % new_sup)


def cosh(self, other=None):
# Return hyperbolic cosine of interval

	if other != None:
		intv = IReal(self, other)
	else:
		if type(self) == float or type(self) == str:
			intv = IReal(self)
		else:
			intv = self
 
	if math.cosh(intv.inf) > math.cosh(intv.sup):
		inf = max(intv.inf, intv.sup)
		sup = min(intv.inf, intv.sup)
	else:
		inf = intv.inf
		sup = intv.sup

	if 0 in intv:
		inf = 0

	ireal.rounding.set_mode(1)

	ireal.rounding.set_mode(-1)
	ireal.rounding.set_mode(-1)

	new_inf = math.cosh(inf)
	ireal.rounding.set_mode(1)
	new_sup = max(float(IReal('%.16f' % math.cosh(sup)).sup), float(IReal('%.20f' % math.cosh(sup)).sup))

	return IReal(new_inf, new_sup)


def exp(self, other=None):
# Return exponencial of interval

	if other != None:
		intv = IReal(self, other)
	else:
		if type(self) == float or type(self) == str:
			intv = IReal(self)
		else:
			intv = self
 
	ireal.rounding.set_mode(1)

	ireal.rounding.set_mode(-1)
	ireal.rounding.set_mode(-1)

	new_inf = math.exp(intv.inf)
	ireal.rounding.set_mode(1)
	new_sup = IReal(math.exp(intv.sup))
	new_sup = new_sup.sup

	temp = new_inf
	return IReal(min(temp,new_sup),  '%.15f' % new_sup)

	
def log(self, base=None):
# Return base x or e logarithm of interval

	if base == None:
		base = math.e

	else:
  		if type(self) == float or type(self) == str:
   			intv = IReal(self)
  		else:
   			intv = self
 
	ireal.rounding.set_mode(1)

	ireal.rounding.set_mode(-1)
 	ireal.rounding.set_mode(-1)

 	new_inf = math.log(intv.inf, base)
 	ireal.rounding.set_mode(1)
 	new_sup = math.log(intv.sup, base)

 	temp = new_inf
 	return IReal(min(temp,new_sup),  '%.15f' % new_sup)

	
def pow(self, y=None):
# Return raised to the power y of interval

 	if y == None:
  		return "exponent undefined"
 	else:
  		if type(self) == float or type(self) == str:
   			intv = IReal(self)
  		else:
   			intv = self

	temp = intv.inf
	if 0 in intv and y%2 == 0:
		temp = 0
 	ireal.rounding.set_mode(1)

 	ireal.rounding.set_mode(-1)
 	ireal.rounding.set_mode(-1)

 	new_inf = math.pow(intv.inf, y)
 	ireal.rounding.set_mode(1)
 	new_sup = math.pow(intv.sup, y)
 
 	return IReal(min(temp,new_sup),  '%.15f' % new_sup)

	
def sin(self, other=None):
# Return sine of interval

 	if other != None:
  		intv = IReal(self, other)
 	else:
  		if type(self) == float or type(self) == str:
   			intv = IReal(self)
  		else:
   			intv = self
 
 	if intv in IReal(-math.pi/2, math.pi/2):
		if math.sin(intv.inf) > math.sin(intv.sup):
			inf = max(intv.inf, intv.sup)
			sup = min(intv.inf, intv.sup)
		else:
			inf = intv.inf
			sup = intv.sup


		ireal.rounding.set_mode(1)

		ireal.rounding.set_mode(-1)
		ireal.rounding.set_mode(-1)

		new_inf = math.sin(inf)
		ireal.rounding.set_mode(1)
		new_sup = float(IReal('%.15f' % math.sin(sup)).sup)

 
	else:
 		return  "Your interval should be between [-PI/2, PI/2]"

	temp = new_inf
	return IReal(min(temp,new_sup), new_sup)


def sinh(self, other=None):
# Return hiperbolic sine of interval

 	if other != None:
  		intv = IReal(self, other)
 	else:
  		if type(self) == float or type(self) == str:
	   		intv = IReal(self)
  		else:
   			intv = self
 
 	if math.sinh(intv.inf) > math.sinh(intv.sup):
		inf = max(intv.inf, intv.sup)
		sup = min(intv.inf, intv.sup)
	else:
		inf = intv.inf
		sup = intv.sup


	ireal.rounding.set_mode(1)

 	ireal.rounding.set_mode(-1)
 	ireal.rounding.set_mode(-1)
 
 	new_inf = math.sinh(inf)
 	ireal.rounding.set_mode(1)
	new_sup = max(float(IReal('%.16f' % math.sinh(sup)).sup), float(IReal('%.20f' % math.sinh(sup)).sup))

 	return IReal(new_inf, new_sup)


def sqrt(self, other=None):
# Return hiperbolic sine of interval

 	if other != None:
  		intv = IReal(self, other)
 	else:
  		if type(self) == float or type(self) == str:
   			intv = IReal(self)
  		else:
   			intv = self
 
 	if math.sqrt(intv.inf) > math.sqrt(intv.sup):
		inf = max(intv.inf, intv.sup)
		sup = min(intv.inf, intv.sup)
	else:
		inf = intv.inf
		sup = intv.sup


	ireal.rounding.set_mode(1)

 	ireal.rounding.set_mode(-1)
 	ireal.rounding.set_mode(-1)

 	new_inf = math.sqrt(inf)
 	ireal.rounding.set_mode(1)
	new_sup = IReal(math.sqrt(sup))
	new_sup = new_sup.sup

 	temp = new_inf
 	return IReal(min(temp,new_sup), '%.15f' % new_sup)


def tan(self, other=None):
# Return tangent of interval

 	if other != None:
  		intv = IReal(self, other)
 	else:
  		if type(self) == float or type(self) == str:
   			intv = IReal(self)
  		else:
   			intv = self
 
 	if intv in IReal(-math.pi/2, math.pi/2) and not(-math.pi/2) in intv and not(math.pi/2) in intv:
		if math.tan(intv.inf) > math.tan(intv.sup):
			inf = max(intv.inf, intv.sup)
			sup = min(intv.inf, intv.sup)
		else:
			inf = intv.inf
			sup = intv.sup


		ireal.rounding.set_mode(1)

		ireal.rounding.set_mode(-1)
		ireal.rounding.set_mode(-1)

		new_inf = math.tan(inf)
		ireal.rounding.set_mode(1)
		new_sup = float(IReal('%.16f' % math.tan(sup)).sup)

	else:
		return  "Not Defined"

 	return IReal(new_inf, new_sup)

	
def tanh(self, other=None):
# Return hyperbolic tangent of interval
	
 	if other != None:
  		intv = IReal(self, other)
 	else:
  		if type(self) == float or type(self) == str:
   			intv = IReal(self)
  		else:
   			intv = self
 
 	if math.tanh(intv.inf) > math.tanh(intv.sup):
		inf = max(intv.inf, intv.sup)
		sup = min(intv.inf, intv.sup)
	else:
		inf = intv.inf
		sup = intv.sup


 	ireal.rounding.set_mode(1)

 	ireal.rounding.set_mode(-1)
 	ireal.rounding.set_mode(-1)

 	new_inf = math.tanh(inf)
 	ireal.rounding.set_mode(1)
	new_sup = max(float(IReal('%.16f' % math.tanh(sup)).sup), float(IReal('%.19f' % math.tanh(sup)).sup))

 	return IReal(new_inf, new_sup)
