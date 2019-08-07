# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Mar 13 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import numpy as np
from scipy import integrate

#from matplotlib.backends.backend_pdf import PdfPages
import wx.lib.agw.aui as aui
import matplotlib as mpl
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar

##########################################################################
## Constant values
##########################################################################

k_B = 8.61e-5 #[eV/K]
q = 1.6e-19 #[C] 4.803e−10[statC]
A = 1e5
h = 4.135e-15 #[eV s]6.626e34[J s]
c = 3e10 #[cm/s]
eps_0 = 8.8542e-14

##########################################################################
## Initialiaze variables
##########################################################################

D_n, D_p, L_p, L_n, tau_n, tau_p, eps_p, eps_n, N_a, N_d, E_gn, E_gp, N_cp, N_vp, N_cn, N_vn, S_n, S_p, W_n, W_p, X_n, X_p, Ta, S_i = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
data_1, data_2, data_3, data_4 = [], [], [], []
wlengths, rows, N_0 = [], [], []
file_nameR, file_nameT = '', ''
isCheck = True

###########################################################################
## Class PrincipalPanel
###########################################################################

class PrincipalPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1000,900 ), style = wx.TAB_TRAVERSAL|wx.WANTS_CHARS, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

###########################################################################
## Window & text.
###########################################################################

		self.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetMinSize( wx.Size( 1100,800 ) )

		MrLayout = wx.BoxSizer( wx.VERTICAL )


		MrLayout.Add( ( 0, 25), 0, wx.EXPAND, 5 )

		self.Titletext = wx.StaticText( self, wx.ID_ANY, u"Heterojunction Thin Film Solar Cell - Electric Model", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Titletext.Wrap( -1 )

		self.Titletext.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Consolas" ) )
		self.Titletext.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.Titletext.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		MrLayout.Add( self.Titletext, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.TOP, 25 )

		self.Introtext = wx.StaticText( self, wx.ID_ANY, u"In this program we focus on presenting a software developed for theorical calculations of Heterojunction Thin Film Solar Cells (HTFSC) the results includes graphics of Efficiency, FF, Voc and Jsc values in function of the Energy Band Gap and the Thickness of the Absorbent Layer. It's necesary to know the next values for run the simulation, you can consultate the instruction file or write a mail with yours doubts.", wx.DefaultPosition, wx.Size( 750,60 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.Introtext.Wrap( -1 )

		self.Introtext.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.Introtext.SetForegroundColour( wx.Colour( 64, 64, 64 ) )
		self.Introtext.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		MrLayout.Add( self.Introtext, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.Sc_parameters = wx.ScrolledWindow( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.VSCROLL )
		self.Sc_parameters.SetScrollRate( 5, 5 )
		self.Sc_parameters.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.Sc_parameters.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.Sc_parameters.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.Sc_parameters.SetMinSize( wx.Size( -1,600 ) )

		noimage = wx.BoxSizer( wx.VERTICAL )

		cols = wx.BoxSizer( wx.HORIZONTAL )

		col1 = wx.BoxSizer( wx.VERTICAL )

		self.Parametertext = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Parameters.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Parametertext.Wrap( -1 )

		self.Parametertext.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.Parametertext.SetForegroundColour( wx.Colour( 63, 63, 63 ) )
		self.Parametertext.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		col1.Add( self.Parametertext, 0, wx.ALL, 0 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )


		bSizer12.Add( ( 0, 35), 0, wx.ALL|wx.EXPAND, 5 )

		self.parameterText = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Relative permittivity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parameterText.Wrap( -1 )

		self.parameterText.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.parameterText.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.parameterText.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.parameterText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 10 )

		self.parameterText1 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Energy Band Gap [eV]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parameterText1.Wrap( -1 )

		self.parameterText1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.parameterText1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.parameterText1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.parameterText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 10 )

		self.parameterText2 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Effective conduction band  [cm^-3]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parameterText2.Wrap( -1 )

		self.parameterText2.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.parameterText2.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.parameterText2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.parameterText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 10 )

		self.parameterText3 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Effective valence band [cm^-3]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parameterText3.Wrap( -1 )

		self.parameterText3.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.parameterText3.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.parameterText3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.parameterText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 10 )

		self.parameterText4 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Diffusion coeficient of electron / hole  [cm^2 * s^-1]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parameterText4.Wrap( -1 )

		self.parameterText4.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.parameterText4.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.parameterText4.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.parameterText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 10 )

		self.parameterText5 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Surface recombination velocity  [cm/s]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parameterText5.Wrap( -1 )

		self.parameterText5.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.parameterText5.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.parameterText5.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.parameterText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 10 )

		self.parameterText28 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Layer thickness [cm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parameterText28.Wrap( -1 )

		self.parameterText28.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.parameterText28.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.parameterText28.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.parameterText28, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 10 )

		self.parameterText24 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Electron affinity [eV]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parameterText24.Wrap( -1 )

		self.parameterText24.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.parameterText24.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.parameterText24.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.parameterText24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 10 )

		self.parameterText6 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Acceptor / Donor   concentration [cm^-3]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.parameterText6.Wrap( -1 )

		self.parameterText6.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.parameterText6.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.parameterText6.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.parameterText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 10 )

		self.LorTtext = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Electron lifetime [s] or Diffussion length of electron [cm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LorTtext.Wrap( -1 )

		self.LorTtext.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.LorTtext.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.LorTtext.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.LorTtext, 0, wx.ALL, 8 )


		bSizer12.Add( ( 0, 28), 0, wx.ALL|wx.EXPAND, 5 )

		self.Gaptext = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Energy Gap variation [eV]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Gaptext.Wrap( -1 )

		self.Gaptext.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.Gaptext.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.Gaptext.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.Gaptext, 0, wx.ALL, 8 )

		self.Thicktext1 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Thickness variation [cm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Thicktext1.Wrap( -1 )

		self.Thicktext1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.Thicktext1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.Thicktext1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.Thicktext1, 0, wx.ALL, 8 )


		bSizer12.Add( ( 0, 25), 0, wx.ALL|wx.EXPAND, 5 )

		self.avgtext = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Average value of material [ > 0; < 1 ]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.avgtext.Wrap( -1 )

		self.avgtext.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.avgtext.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.avgtext.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer12.Add( self.avgtext, 0, wx.ALL, 8 )

		col1.Add( bSizer12, 1, wx.ALL|wx.EXPAND, 5 )

		cols.Add( col1, 1, wx.EXPAND, 5 )

		col2 = wx.BoxSizer( wx.VERTICAL )

		self.Valuetitle = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Valuetitle.Wrap( -1 )

		self.Valuetitle.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.Valuetitle.SetForegroundColour( wx.Colour( 63, 63, 63 ) )
		self.Valuetitle.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		col2.Add( self.Valuetitle, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )

		gSizer4 = wx.GridSizer( 16, 2, 0, 0 )

		self.Ptype = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"P-type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Ptype.Wrap( -1 )

		self.Ptype.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.Ptype.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.Ptype.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.Ptype, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.Ntype = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"N-type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Ntype.Wrap( -1 )

###########################################################################
## Default parameters
###########################################################################
		self.Ntype.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.Ntype.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.Ntype.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.Ntype, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valeps_p = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"13.6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valeps_p.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valeps_p.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valeps_p.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valeps_p, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.valeps_n = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valeps_n.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valeps_n.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valeps_n.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valeps_n, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valE_gp = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"1.17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valE_gp.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valE_gp.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valE_gp.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valE_gp, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valE_gn = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"2.42", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valE_gn.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valE_gn.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valE_gn.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valE_gn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valN_cp = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"2.2e18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valN_cp.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valN_cp.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valN_cp.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valN_cp, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valN_cn = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"2.2e18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valN_cn.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valN_cn.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valN_cn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valN_vp = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"1.8e19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valN_vp.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valN_vp.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valN_vp.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valN_vp, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valN_vn = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"1.8e19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valN_vn.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valN_vn.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valN_vn.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valN_vn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valD_p = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"0.65", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valD_p.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valD_p.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valD_p.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valD_p, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valD_n = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"1.05", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valD_n.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valD_n.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valD_n.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valD_n, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valS_p = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valS_p.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valS_p.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valS_p.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valS_p, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valS_n = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"1.0e6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valS_n.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valS_n.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valS_n.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valS_n, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valW_p = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"2.0e-4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valW_p.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valW_p.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valW_p.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valW_p, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valW_n = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"0.1e-4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valW_n.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valW_n.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valW_n.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valW_n, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valX_p = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"4.235", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valX_p.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valX_p.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valX_p.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valX_p, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valX_n = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"4.3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valX_n.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valX_n.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valX_n.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valX_n, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valN_a = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"1.0e17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valN_a.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valN_a.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valN_a.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valN_a, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valN_d = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"1.0e17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valN_d.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valN_d.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valN_d.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valN_d, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn1 = wx.RadioButton( self.Sc_parameters, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.m_radioBtn1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_radioBtn1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer181.Add( self.m_radioBtn1, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.m_radioBtn2 = wx.RadioButton( self.Sc_parameters, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn2.SetValue( True )
		self.m_radioBtn2.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_radioBtn2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer181.Add( self.m_radioBtn2, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.valLorT_p = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"8.0e-4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valLorT_p.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valLorT_p.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valLorT_p.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer181.Add( self.valLorT_p, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer4.Add( bSizer181, 0, wx.EXPAND, 5 )

		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )

		self.n_radioBtn3 = wx.RadioButton( self.Sc_parameters, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.n_radioBtn3.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.n_radioBtn3.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer191.Add( self.n_radioBtn3, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.n_radioBtn4 = wx.RadioButton( self.Sc_parameters, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.n_radioBtn4.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.n_radioBtn4.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.n_radioBtn4.SetValue( True )

		bSizer191.Add( self.n_radioBtn4, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.valLorT_n = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"2.9e-6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valLorT_n.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valLorT_n.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valLorT_n.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer191.Add( self.valLorT_n, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer4.Add( bSizer191, 0, wx.EXPAND, 5 )

		self.m_staticText54 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Minimum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		self.m_staticText54.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.m_staticText54.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_staticText54.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.m_staticText54, 0, wx.ALIGN_CENTER, 0 )

		self.m_staticText541 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Maximum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText541.Wrap( -1 )

		self.m_staticText541.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.m_staticText541.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_staticText541.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.m_staticText541, 0, wx.ALIGN_CENTER, 0 )

		self.valE_gpmin = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valE_gpmin.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valE_gpmin.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valE_gpmin.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valE_gpmin, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valE_gpmax = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"2.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valE_gpmax.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valE_gpmax.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valE_gpmax.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valE_gpmax, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valW_pmin = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"0.5e-4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valW_pmin.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valW_pmin.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valW_pmin.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valW_pmin, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.valW_pmax = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"3.0e-4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valW_pmax.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valW_pmax.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valW_pmax.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.valW_pmax, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.Reflectancetext = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Reflectance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Reflectancetext.Wrap( -1 )

		self.Reflectancetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.Reflectancetext.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.Reflectancetext.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.Reflectancetext, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.Transmitancetext = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Transmitance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Transmitancetext.Wrap( -1 )

		self.Transmitancetext.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.Transmitancetext.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.Transmitancetext.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.Transmitancetext, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.importRButton = wx.Button( self.Sc_parameters, wx.ID_ANY, u"Reflectance", wx.DefaultPosition, wx.DefaultSize, 0 )
#		self.valueR = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"0.02", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.importRButton.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.importRButton.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.importRButton.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.importRButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.importTButton = wx.Button( self.Sc_parameters, wx.ID_ANY, u"Transmitance", wx.DefaultPosition, wx.DefaultSize, 0 )
#		self.valueT = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"0.98", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.importTButton.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.importTButton.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.importTButton.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer4.Add( self.importTButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		col2.Add( gSizer4, 1, wx.ALL|wx.EXPAND, 5 )


		cols.Add( col2, 0, wx.ALL|wx.EXPAND, 5 )


		noimage.Add( cols, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox3 = wx.CheckBox( self.Sc_parameters, wx.ID_ANY, u"Interace recombination velocity:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetValue(True)
		bSizer22.Add( self.m_checkBox3, 0, wx.ALL, 8 )

		self.valS_i = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"10e5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valS_i.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valS_i.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valS_i.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer22.Add( self.valS_i, 0, wx.ALL, 5 )

		self.m_staticText632 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Total steps:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText632.Wrap( -1 )

		self.m_staticText632.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.m_staticText632.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_staticText632.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer22.Add( self.m_staticText632, 0, wx.ALL, 8 )

		self.valSteps = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valSteps.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valSteps.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valSteps.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer22.Add( self.valSteps, 0, wx.ALL, 5 )

		self.m_staticText633 = wx.StaticText( self.Sc_parameters, wx.ID_ANY, u"Voltage steps:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText633.Wrap( -1 )

		self.m_staticText633.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.m_staticText633.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_staticText633.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer22.Add( self.m_staticText633, 0, wx.ALL, 8 )

		self.valVib_steps = wx.TextCtrl( self.Sc_parameters, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.valVib_steps.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
		self.valVib_steps.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.valVib_steps.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer22.Add( self.valVib_steps, 0, wx.ALL, 5 )

###########################################################################
## Buttons & images
###########################################################################

		bSizer24.Add( bSizer22, 1, wx.ALIGN_CENTER, 5 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.calculationButton = wx.Button( self.Sc_parameters, wx.ID_ANY, u"Calculate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.calculationButton.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.calculationButton.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.calculationButton.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer25.Add( self.calculationButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.graphicButton = wx.Button( self.Sc_parameters, wx.ID_ANY, u"Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.graphicButton.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.graphicButton.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.graphicButton.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer25.Add( self.graphicButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.exportButton = wx.Button( self.Sc_parameters, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exportButton.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Consolas" ) )
		self.exportButton.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.exportButton.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer25.Add( self.exportButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer24.Add( bSizer25, 0, wx.ALIGN_CENTER, 5 )

		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_gauge1 = wx.Gauge( self.Sc_parameters, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		bSizer161.Add( self.m_gauge1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer24.Add( ( 0, 20), 0, wx.ALL|wx.EXPAND, 5 )
		bSizer24.Add( bSizer161, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer16.Add( bSizer24, 1, wx.EXPAND, 5 )


		noimage.Add( bSizer16, 0, wx.ALL|wx.EXPAND, 0 )


		self.Sc_parameters.SetSizer( noimage )
		self.Sc_parameters.Layout()
		noimage.Fit( self.Sc_parameters )
		bSizer8.Add( self.Sc_parameters, 1, wx.EXPAND, 2 )

		image = wx.BoxSizer( wx.HORIZONTAL )

		self.cell = wx.StaticBitmap( self.m_scrolledWindow2, wx.ID_ANY, wx.Bitmap( u"cell2.PNG", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cell.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		image.Add( self.cell, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 50 )


		bSizer8.Add( image, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL, 0 )


		self.m_scrolledWindow2.SetSizer( bSizer8 )
		self.m_scrolledWindow2.Layout()
		bSizer8.Fit( self.m_scrolledWindow2 )
		MrLayout.Add( self.m_scrolledWindow2, 14, wx.EXPAND |wx.ALL, 5 )


		MrLayout.Add( ( 0, 20), 1, wx.EXPAND, 5 )

		unal = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"UN-Black1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,118 ), 0 )
		self.m_bitmap2.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		unal.Add( self.m_bitmap2, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		MrLayout.Add( unal, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.BOTTOM|wx.EXPAND, 5 )


		self.SetSizer( MrLayout )
		self.Layout()

		# Connect Events
		self.importTButton.Hide()
		self.calculationButton.Hide()
		self.exportButton.Hide()
		self.graphicButton.Hide()
		self.importRButton.Bind( wx.EVT_BUTTON, self.importR)
		self.importTButton.Bind( wx.EVT_BUTTON, self.importT)
		self.calculationButton.Bind( wx.EVT_BUTTON, self.calculateFunc )
		self.graphicButton.Bind( wx.EVT_BUTTON, self.graphs )
		self.exportButton.Bind( wx.EVT_BUTTON, self.export )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class

	def calculateFunc( self, event ):
		cldata()
		self.m_gauge1.SetValue( 0 )
		self.graphicButton.Hide()
		global isCheck
		isCheck = self.m_checkBox3.GetValue()
###########################################################################
## Read: variables & spectrum data 
###########################################################################
		global D_n, D_p, eps_p, eps_n, N_a, N_d, E_gn, E_gp, E_gpmin, E_gpmax, N_cp, N_vp, N_cn, N_vn, S_n, S_p, W_n, W_p, W_pmin, W_pmax, X_n, X_p, Ta, S_i, Steps, Vib_steps, R, T, L_p, tau_p, L_p, tau_p
		global N_0, wlengths, data_1, data_2, data_3, data_4, R, T, wait
		data_1, data_2, data_3, data_4 = [], [], [], []
		D_n = np.float_(self.valD_n.GetLineText(0))
		D_p = np.float_(self.valD_p.GetLineText(0))
		eps_p = np.float_(self.valeps_p.GetLineText(0))
		eps_n = np.float_(self.valeps_n.GetLineText(0))
		N_a = np.float_(self.valN_a.GetLineText(0))
		N_d = np.float_(self.valN_d.GetLineText(0))
		E_gn = np.float_(self.valE_gn.GetLineText(0))
		E_gp = np.float_(self.valE_gp.GetLineText(0))
		E_gpmin = np.float_(self.valE_gpmin.GetLineText(0))
		E_gpmax = np.float_(self.valE_gpmax.GetLineText(0))
		N_cp = np.float_(self.valN_cp.GetLineText(0))
		N_vp = np.float_(self.valN_vp.GetLineText(0))
		N_cn = np.float_(self.valN_cn.GetLineText(0))
		N_vn = np.float_(self.valN_vn.GetLineText(0))
		S_n = np.float_(self.valS_n.GetLineText(0))
		S_p = np.float_(self.valS_p.GetLineText(0))
		W_n = np.float_(self.valW_n.GetLineText(0))
		W_p = np.float_(self.valW_p.GetLineText(0))
		W_pmin = np.float_(self.valW_pmin.GetLineText(0))
		W_pmax = np.float_(self.valW_pmax.GetLineText(0))
		X_n = np.float_(self.valX_n.GetLineText(0))
		X_p = np.float_(self.valX_p.GetLineText(0))
		Ta = np.float_(300)
		S_i = np.float_(self.valS_i.GetLineText(0))
		Steps = int(self.valSteps.GetLineText(0))
		Vib_steps = int(self.valVib_steps.GetLineText(0))
		waiter = 100 / (Steps * 2)
		wait = 0
		L_p, tau_p = checkfp()
		L_n, tau_n = checkfn()
		file_name = LoadFile(self)
		Rneq = np.loadtxt(file_nameR, dtype=float, usecols=(1,), skiprows=1)
		Tneq = np.loadtxt(file_nameT, dtype=float, usecols=(1,), skiprows=1)
		wlengthsneq = np.loadtxt(file_name, dtype=float, usecols=(0,), skiprows=1)
		N_0neq = np.loadtxt(file_name, dtype=float, usecols=(1,), skiprows=1)
		wlengths, N_0, R, T = [], [], [], []
		for i in range(len(Rneq)):
			R.append( Rneq[i] )
			T.append( Tneq[i] )
			wlengths.append( wlengthsneq[i] )
			N_0.append( N_0neq[i] )
		#R = 0.1
		#T = 0.9
###########################################################################
## Simulation
###########################################################################
		wlengths = 1e-7 * np.array(wlengths, dtype='float64') #[cm]
		N_0 = np.array(N_0, dtype='float64') / (1240.0/(wlengths*1e7))
		T = np.array(T, dtype='float64')
		R = np.array(R, dtype='float64')	
		# values for thickness
		thickness = np.linspace(W_pmin, W_pmax, num=Steps, endpoint=True, dtype='float64')
		# values for Gap
		gap = np.linspace(E_gpmin, E_gpmax, num=Steps, endpoint=True, dtype='float64')
		global ni_n, p_0, alpha_n
		ni_n = np.float_(( N_cn * N_vn * np.exp( - E_gn / ( k_B * Ta ) ) )**0.5)
		p_0 = np.float_(ni_n ** 2 / N_d)
		alpha_n = function_alpha(wlengths, E_gn)
		if isCheck:
			global results
			nu_list, Voc_list, FF_list, Jsc_list = [], [], [], []
			nu_slist, Voc_slist, FF_slist, Jsc_slist = [], [], [], []
			for W in thickness:
				wait += waiter
				W_p = W
				results = []
				results.append(one_cell(False))# [V_oc, nu, FF, J_sc], s*[V_oc, nu, FF, J_sc]
				nu_list.append(results[0][0][1])
				Voc_list.append(results[0][0][0])
				Jsc_list.append(results[0][0][-1])
				FF_list.append(results[0][0][2])
				nu_slist.append(results[0][1][1])
				Voc_slist.append(results[0][1][0])
				Jsc_slist.append(results[0][0][-1])
				FF_slist.append(results[0][1][2])
				self.m_gauge1.SetValue( int(wait) )
			data_1 = [np.array(thickness, dtype='float64'), np.array(nu_list, dtype='float64'), np.array(Voc_list, dtype='float64'), np.array(FF_list, dtype='float64'), np.array(Jsc_list, dtype='float64')]
			data_2 = [np.array(thickness, dtype='float64'), np.array(nu_slist, dtype='float64'), np.array(Voc_slist, dtype='float64'), np.array(FF_slist, dtype='float64'), np.array(Jsc_slist, dtype='float64')]
			nu_list, Voc_list, FF_list, Jsc_list = [], [], [], []
			nu_slist, Voc_slist, FF_slist, Jsc_slist = [], [], [], []
			for E in gap:
				wait += waiter
				E_gp = E
				results = []
				results.append(one_cell(False)) # [V_oc, nu, FF, J_sc], s*[V_oc, nu, FF, J_sc]
				nu_list.append(results[0][0][1])
				Voc_list.append(results[0][0][0])
				Jsc_list.append(results[0][0][-1])
				FF_list.append(results[0][0][2])
				nu_slist.append(results[0][1][1])
				Voc_slist.append(results[0][1][0])
				Jsc_slist.append(results[0][1][-1])
				FF_slist.append(results[0][1][2])
				self.m_gauge1.SetValue( int(wait) )
			data_3 = [np.array(gap, dtype='float64'), np.array(nu_slist, dtype='float64'), np.array(Voc_slist, dtype='float64'), np.array(FF_slist, dtype='float64'), np.array(Jsc_slist, dtype='float64')]
			data_4 = [np.array(gap, dtype='float64'), np.array(nu_list, dtype='float64'), np.array(Voc_list, dtype='float64'), np.array(FF_list, dtype='float64'), np.array(Jsc_list, dtype='float64')]
		else:
			nu_list, Voc_list, FF_list, Jsc_list = [], [], [], []
			for W in thickness:
				wait += waiter
				W_p = W
				results = []
				results.append(one_cell(False))
				nu_list.append(results[0][1])
				Voc_list.append(results[0][0])
				Jsc_list.append(results[0][-1])
				FF_list.append(results[0][2])
				self.m_gauge1.SetValue( int(wait) )
			data_1 = [np.array(thickness, dtype='float64'), np.array(nu_list, dtype='float64'), np.array(Voc_list, dtype='float64'), np.array(FF_list, dtype='float64'), np.array(Jsc_list, dtype='float64')]
			nu_list, Voc_list, FF_list, Jsc_list = [], [], [], []
			for E in gap:
				wait += waiter
				E_gp = E
				results = []
				results.append(one_cell(False))# [V_oc, nu, FF, J_sc]
				nu_list.append(results[0][1])
				Voc_list.append(results[0][0])
				Jsc_list.append(results[0][-1])
				FF_list.append(results[0][2])
				self.m_gauge1.SetValue( int(wait) )
			data_4 = [np.array(gap, dtype='float64'), np.array(nu_list, dtype='float64'), np.array(Voc_list, dtype='float64'), np.array(FF_list, dtype='float64'), np.array(Jsc_list, dtype='float64')]

		alldata = svdata([data_1,data_2,data_3,data_4])
		self.graphicButton.Show()
		self.exportButton.Show()
		self.m_gauge1.SetValue( 0 )

	def importR( self, event):
		global file_nameR
		self.m_gauge1.SetValue( 33 )
		file_nameR = LoadFile(self)
		self.importTButton.Show()

	def importT( self, event):
		global file_nameT
		self.m_gauge1.SetValue( 66 )
		file_nameT = LoadFile(self)
		self.calculationButton.Show()

	def graphs( self, event ):		
###########################################################################
## Graphics
###########################################################################
		waiter = 25
		wait = 0
		global isCheck
		isCheck = self.m_checkBox3.GetValue()
		thickness = data_1[0]
		gap = data_4[0]
		if isCheck:
			S_i = float(self.valS_i.GetLineText(0))
			ss_si = np.format_float_scientific(S_i, unique=True)
###########################################################################
## Energy-gap_variation S_i
###########################################################################
			graphframe0 = wx.Frame(None, -1, 'Energy gap - Variation', size=(1024, 768))
			plotter0 = PlotNotebook(graphframe0)
			axes7 = plotter0.add('Short-circuit current density').gca()
			axes7.plot(gap, data_3[4], linewidth=1.2)
			axes7.plot(gap, data_3[4], '.', linewidth=0.8)
			axes7.plot(gap, data_4[4], '--', linewidth=1.2)
			axes7.plot(gap, data_4[4], '*', linewidth=0.8)
			#axes7.legend(loc='best', fontsize =18)
			axes7.set_xlabel('Band gap [eV]', fontsize =18)
			axes7.set_ylabel('$J_{sc}$ [mA]', fontsize =18)
			axes7.set_title('Short-circuit current density', fontsize =30)
			axes7.tick_params(labelsize=18)
			axes7.grid('on')

			axes8 = plotter0.add('Fill factor').gca()
			axes8.plot(gap, data_3[3], linewidth=1.2)
			axes8.plot(gap, data_3[3], '.', linewidth=0.8)
			axes8.plot(gap, data_4[3], '--', linewidth=1.2)
			axes8.plot(gap, data_4[3], '*', linewidth=0.8)
			#axes8.legend(loc='best', fontsize =18)
			axes8.set_xlabel('Band gap [eV]', fontsize =18)
			axes8.set_ylabel('FF [%]', fontsize =18)
			axes8.set_title('Fill factor', fontsize =30)
			axes8.tick_params(labelsize=18)
			axes8.grid('on')

			axes9 = plotter0.add('Open-circuit voltage').gca()
			axes9.plot(gap, data_3[2]*1e3, linewidth=1.2)
			axes9.plot(gap, data_3[2]*1e3, '.', linewidth=0.8)
			axes9.plot(gap, data_4[2]*1e3, '--', linewidth=1.2)
			axes9.plot(gap, data_4[2]*1e3, '*', linewidth=0.8)
			#axes9.legend(loc='best', fontsize =18)
			axes9.set_xlabel('Band gap [eV]', fontsize =18)
			axes9.set_ylabel('$V_{oc}$ [mV]', fontsize =18)
			axes9.set_title('Open-circuit voltage', fontsize =30)
			axes9.tick_params(labelsize=18)
			axes9.grid('on')

			axes0 = plotter0.add('Efficiency').gca()
			axes0.plot(gap, data_3[1], linewidth=1.2)
			axes0.plot(gap, data_3[1], '.', linewidth=0.8)
			axes0.plot(gap, data_4[1], '--', linewidth=1.2)
			axes0.plot(gap, data_4[1], '*', linewidth=0.8)
			#axes0.legend(loc='best', fontsize =18)
			axes0.set_xlabel('Band gap [eV]', fontsize =18)
			axes0.set_ylabel('$\eta$ [%]', fontsize =18)
			axes0.set_title('Efficiency', fontsize =30)
			axes0.tick_params(labelsize=18)
			axes0.grid('on')

			plotter0.Show()
			self.graphicButton.Hide()
			graphframe0.Show()
			wait += waiter
			self.m_gauge1.SetValue( int( wait ) )
###########################################################################
## Thickness_variation S_i
##########################################################################.#
			graphframe1 = wx.Frame(None, -1, 'Thickness Variation', size=(1024, 768))
			thickness = np.linspace(float(self.valW_pmin.GetLineText(0)), float(self.valW_pmax.GetLineText(0)), num=Steps, endpoint=True, dtype='float64')
			thickness = data_1[0]
			gap = data_4[0]
			plotter1 = PlotNotebook(graphframe1)

			axes1 = plotter1.add('Short-circuit current density').gca()
			axes1.plot(thickness*1e7, data_1[4], linewidth=1.2)
			axes1.plot(thickness*1e7, data_2[4], '--', linewidth=1.2)
			axes1.plot(thickness*1e7, data_2[4], '.', linewidth=0.8)
			axes1.plot(thickness*1e7, data_1[4], '*', linewidth=0.8)
			#axes1.legend(loc='best', fontsize =18)
			axes1.set_xlabel('Thickness [nm]', fontsize =18)
			axes1.set_ylabel('$J_{sc}$ [mA]', fontsize =18)
			axes1.set_title('Short-circuit current density', fontsize =30)
			axes1.tick_params(labelsize=18)
			axes1.grid('on')

			axes2 = plotter1.add('Fill factor').gca()
			axes2.plot(thickness*1e7, data_1[3], linewidth=1.2)
			axes2.plot(thickness*1e7, data_2[3], '--', linewidth=1.2)
			axes2.plot(thickness*1e7, data_2[3], '.', linewidth=0.8)
			axes2.plot(thickness*1e7, data_1[3], '*', linewidth=0.8)
			#axes2.legend(loc='best', fontsize =18)
			axes2.set_xlabel('Thickness [nm]', fontsize =18)
			axes2.set_ylabel('FF [%]', fontsize =18)
			axes2.set_title('Fill factor', fontsize =30)
			axes2.tick_params(labelsize=18)
			axes2.grid('on')

			axes3 = plotter1.add('Open-circuit voltage').gca()
			axes3.plot(thickness*1e7, data_1[2]*1e3, linewidth=1.2)
			axes3.plot(thickness*1e7, data_2[2]*1e3, '--', linewidth=1.2)
			axes3.plot(thickness*1e7, data_2[2]*1e3, '.', linewidth=0.8)
			axes3.plot(thickness*1e7, data_1[2]*1e3, '*', linewidth=0.8)
			#axes3.legend(loc='best', fontsize =18)
			axes3.set_xlabel('Thickness [nm]', fontsize =18)
			axes3.set_ylabel('$V_{oc}$ [mV]', fontsize =18)
			axes3.set_title('Open-circuit voltage', fontsize =30)
			axes3.tick_params(labelsize=18)
			axes3.grid('on')

			axes4 = plotter1.add('Efficiency').gca()
			axes4.plot(thickness*1e7, data_1[1], linewidth=1.2)
			axes4.plot(thickness*1e7, data_2[1], '--', linewidth=1.2)
			axes4.plot(thickness*1e7, data_2[1], '.', linewidth=0.8)
			axes4.plot(thickness*1e7, data_1[1], '*', linewidth=0.8)
			#axes4.legend(loc='best', fontsize =18)
			axes4.set_xlabel('Thickness [nm]', fontsize =18)
			axes4.set_ylabel('$\eta$ [%]', fontsize =18)
			axes4.set_title('Efficiency', fontsize =30)
			axes4.tick_params(labelsize=18)
			axes4.grid('on')

			plotter1.Show()
			graphframe1.Show()
			wait += waiter
			self.m_gauge1.SetValue( int( wait ) )
		else:
			graphframe0 = wx.Frame(None, -1, 'Energy gap - Variation', size=(1024, 768))
			plotter0 = PlotNotebook(graphframe0)
###########################################################################
## Energy-gap_variation
###########################################################################
			axes7 = plotter0.add('Short-circuit current density').gca()
			axes7.plot(gap, data_4[4], '--', linewidth=1.2)
			axes7.plot(gap, data_4[4], '*', linewidth=0.8)
			#axes7.legend(loc='best', fontsize =18)
			axes7.set_xlabel('Band gap [eV]', fontsize =18)
			axes7.set_ylabel('$J_{sc}$ [mA]', fontsize =18)
			axes7.set_title('Short-circuit current density', fontsize =30)
			axes7.tick_params(labelsize=18)
			axes7.grid('on')

			axes8 = plotter0.add('Fill factor').gca()
			axes8.plot(gap, data_4[3], '--', linewidth=1.2)
			axes8.plot(gap, data_4[3], '*', linewidth=0.8)
			#axes8.legend(loc='best', fontsize =18)
			axes8.set_xlabel('Band gap [eV]', fontsize =18)
			axes8.set_ylabel('FF [%]', fontsize =18)
			axes8.set_title('Fill factor', fontsize =30)
			axes8.tick_params(labelsize=18)
			axes8.grid('on')

			axes9 = plotter0.add('Open-circuit voltage').gca()
			axes9.plot(gap, data_4[2]*1e3, '--', linewidth=1.2)
			axes9.plot(gap, data_4[2]*1e3, '*', linewidth=0.8)
			#axes9.legend(loc='best', fontsize =18)
			axes9.set_xlabel('Band gap [eV]', fontsize =18)
			axes9.set_ylabel('$V_{oc}$ [mV]', fontsize =18)
			axes9.set_title('Open-circuit voltage', fontsize =30)
			axes9.tick_params(labelsize=18)
			axes9.grid('on')

			axes0 = plotter0.add('Efficiency').gca()
			axes0.plot(gap, data_4[1], '--', linewidth=1.2)
			axes0.plot(gap, data_4[1], '*', linewidth=0.8)
			#axes0.legend(loc='best', fontsize =18)
			axes0.set_xlabel('Band gap [eV]', fontsize =18)
			axes0.set_ylabel('$\eta$ [%]', fontsize =18)
			axes0.set_title('Efficiency', fontsize =30)
			axes0.tick_params(labelsize=18)
			axes0.grid('on')

			plotter0.Show()
			self.graphicButton.Hide()
			graphframe0.Show()
			wait += waiter
			self.m_gauge1.SetValue( int( wait ) )
###########################################################################
## Thickness_variation
##########################################################################.#
			graphframe1 = wx.Frame(None, -1, 'Thickness Variation', size=(1024, 768))
			thickness = np.linspace(float(self.valW_pmin.GetLineText(0)), float(self.valW_pmax.GetLineText(0)), num=Steps, endpoint=True, dtype='float64')
			thickness = data_1[0]
			gap = data_4[0]
			plotter1 = PlotNotebook(graphframe1)

			axes1 = plotter1.add('Short-circuit current density').gca()
			axes1.plot(thickness*1e7, data_1[4], linewidth=1.2)
			axes1.plot(thickness*1e7, data_1[4], '*', linewidth=0.8)
			#axes1.legend(loc='best', fontsize =18)
			axes1.set_xlabel('Thickness [nm]', fontsize =18)
			axes1.set_ylabel('$J_{sc}$ [mA]', fontsize =18)
			axes1.set_title('Short-circuit current density', fontsize =30)
			axes1.tick_params(labelsize=18)
			axes1.grid('on')

			axes2 = plotter1.add('Fill factor').gca()
			axes2.plot(thickness*1e7, data_1[3], linewidth=1.2)
			axes2.plot(thickness*1e7, data_1[3], '*', linewidth=0.8)
			#axes2.legend(loc='best', fontsize =18)
			axes2.set_xlabel('Thickness [nm]', fontsize =18)
			axes2.set_ylabel('FF [%]', fontsize =18)
			axes2.set_title('Fill factor', fontsize =30)
			axes2.tick_params(labelsize=18)
			axes2.grid('on')

			axes3 = plotter1.add('Open-circuit voltage').gca()
			axes3.plot(thickness*1e7, data_1[2]*1e3, linewidth=1.2)
			axes3.plot(thickness*1e7, data_1[2]*1e3, '*', linewidth=0.8)
			#axes3.legend(loc='best', fontsize =18)
			axes3.set_xlabel('Thickness [nm]', fontsize =18)
			axes3.set_ylabel('$V_{oc}$ [mV]', fontsize =18)
			axes3.set_title('Open-circuit voltage', fontsize =30)
			axes3.tick_params(labelsize=18)
			axes3.grid('on')

			axes4 = plotter1.add('Efficiency').gca()
			axes4.plot(thickness*1e7, data_1[1], linewidth=1.2)
			axes4.plot(thickness*1e7, data_1[1], '*', linewidth=0.8)
			#axes4.legend(loc='best', fontsize =18)
			axes4.set_xlabel('Thickness [nm]', fontsize =18)
			axes4.set_ylabel('$\eta$ [%]', fontsize =18)
			axes4.set_title('Efficiency', fontsize =30)
			axes4.tick_params(labelsize=18)
			axes4.grid('on')

			plotter1.Show()
			graphframe1.Show()
			wait += waiter
			self.m_gauge1.SetValue( int( wait ) )
#######################################################################
# QE and JV whitout variation
###########################################################################
		graphframe2 = wx.Frame(None, -1, 'JV of input data & QE', size=(1024, 768))
		thickness = np.linspace(float(self.valW_pmin.GetLineText(0)), float(self.valW_pmax.GetLineText(0)), num=Steps, endpoint=True, dtype='float64')
		gap = np.linspace(float(self.valE_gpmin.GetLineText(0)), float(self.valE_gpmax.GetLineText(0)), num=Steps, endpoint=True, dtype='float64')
		plotter2 = PlotNotebook(graphframe2)

		W_p = np.float_(self.valW_p.GetLineText(0))
		E_gp = np.float_(self.valE_gp.GetLineText(0))

		EQE0 = fdJ_ph(0) / N_0
		IQE0 = EQE0 / ( 1 - R)
		wlengthsQE = []
		EQE = [0.0]
		IQE = [0.0]

		for i in range(len(EQE0)):
			if EQE0[i] == 0:
				if EQE0[i-1] != [0]:
					wlengthsQE.append(wlengths[i+1]*1e7)
					IQE.append(0.0)
					EQE.append(0.0)
				pass
			else:
				if len(wlengthsQE) == 0:
					wlengthsQE.append((wlengths[i]*1e7)-1)
				wlengthsQE.append(wlengths[i]*1e7)
				IQE.append(IQE0[i])
				EQE.append(EQE0[i])
		wait += waiter
		self.m_gauge1.SetValue( int( wait ) )

		axes5 = plotter2.add('Quantum Efficciency').gca()
		axes5.plot(wlengthsQE, EQE, label='EQE', linewidth=1.2)
		axes5.plot(wlengthsQE, IQE, '--', label='IQE', linewidth=1.2)
		#axes5.legend(loc='best', fontsize =18)
		axes5.set_xlabel('Wave length [nm]', fontsize =18)
		axes5.set_ylabel('QE', fontsize =18)
		axes5.set_title('Quantum Efficciency', fontsize =30)
		axes5.tick_params(labelsize=18)
		axes5.grid('on')

		if isCheck:
			v1, J1, v2, J2  = one_cell(True)
			v1, J1 = np.array(v1, dtype='float64'), np.array(J1, dtype='float64')
			v2, J2 = np.array(v2, dtype='float64'), np.array(J2, dtype='float64')
			
			axes6 = plotter2.add('Current density (Input parameters)').gca()
			axes6.plot(v1, J1, linewidth=1.2)
			axes6.plot(v2, J2, '--', linewidth=1.2)
			#axes6.legend(loc='best', fontsize =18)
			axes6.set_xlabel('Voltage [V]', fontsize =18)
			axes6.set_ylabel('Current density [mA/cm²]', fontsize =18)
			axes6.set_title('Current density (Input parameters)', fontsize =30)
			axes6.tick_params(labelsize=18)
			axes6.grid('on') 
		else:
			v1, J1  = one_cell(True)
			v1, J1 = np.array(v1, dtype='float64'), np.array(J1, dtype='float64')
			
			axes6 = plotter2.add('Current density (Input parameters)').gca()
			axes6.plot(v1, J1, linewidth=1.2)
			#axes6.legend(loc='best', fontsize =18)
			axes6.set_xlabel('Voltage [V]', fontsize =18)
			axes6.set_ylabel('Current density [mA/cm²]', fontsize =18)
			axes6.set_title('Current density (Input parameters)', fontsize =30)
			axes6.tick_params(labelsize=18)
			axes6.grid('on') 

		plotter2.Show()
		graphframe2.Show()
		wait += waiter
		self.m_gauge1.SetValue( int( wait ) )
		self.m_gauge1.SetValue( 0 )

	def export( self, event ):		
###########################################################################
## Export
###########################################################################
		global isCheck
		isCheck = self.m_checkBox3.GetValue()
		if isCheck:
			exp_data1 = np.stack((data_1), axis=-1)
			np.savetxt('result-data1.txt', exp_data1)
			exp_data2 = np.stack((data_2), axis=-1)
			np.savetxt('result-data2.txt', exp_data2)
			exp_data3 = np.stack((data_2), axis=-1)
			np.savetxt('result-data3.txt', exp_data3)
			exp_data4 = np.stack((data_2), axis=-1)
			np.savetxt('result-data4.txt', exp_data4)
		else:
			exp_data1 = np.stack((data_1), axis=-1)
			np.savetxt('result-data1.txt', exp_data1)
			exp_data4 = np.stack((data_2), axis=-1)
			np.savetxt('result-data4.txt', exp_data4)


class Plot(wx.Panel):
	def __init__(self, parent, id=-1, dpi=None, **kwargs):
		wx.Panel.__init__(self, parent, id=id, **kwargs)
		self.figure = mpl.figure.Figure(dpi=dpi, figsize=(14, 10))
		self.canvas = FigureCanvas(self, -1, self.figure)
		self.toolbar = NavigationToolbar(self.canvas)
		self.toolbar.Realize()

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.canvas, 1, wx.EXPAND)
		sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
		self.SetSizer(sizer)


class PlotNotebook(wx.Panel):
	def __init__(self, parent, id=-1):
		wx.Panel.__init__(self, parent, id=id)
		self.nb = aui.AuiNotebook(self, id=id, pos=(0,0), size=(800,1000))
		sizer = wx.BoxSizer()
		sizer.Add(self.nb, 1, wx.EXPAND)
		self.SetSizer(sizer)

	def add(self, name="plot"):
		page = Plot(self.nb)
		self.nb.AddPage(page, name)
		return page.figure

###########################################################################
## Load file with FileDialog
###########################################################################

def LoadFile(self):

		#app = wx.PySimpleApp(0)
		dir = "/home"
		save_dlg = wx.FileDialog(self, message='Choose Files to be Imported', defaultDir=dir, defaultFile= '', wildcard="Text files (*.txt)|*.txt", 
			style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		if save_dlg.ShowModal() == wx.ID_OK:
			path = save_dlg.GetPath()
		save_dlg.Destroy()
		return path


def checkfp():
	a = PrincipalPane.m_radioBtn1.GetValue()
	if a:
		t = np.float_(PrincipalPane.valLorT_p.GetLineText(0))
		l = ( t * np.float_(PrincipalPane.valD_p.GetLineText(0)) ) ** 0.5 
		return l, t
	elif PrincipalPane.m_radioBtn2.GetValue():
	 	l = np.float_(PrincipalPane.valLorT_p.GetLineText(0))
	 	t = l ** 2 / np.float_(PrincipalPane.valD_p.GetLineText(0))
	 	return l, t	

def checkfn():
	a = PrincipalPane.n_radioBtn3.GetValue()
	if a:	
		t = np.float_(PrincipalPane.valLorT_n.GetLineText(0))
		l = ( t * np.float_(PrincipalPane.valD_n.GetLineText(0)) ) ** 0.5 
		return l, t
	elif PrincipalPane.n_radioBtn4.GetValue():
		l = np.float_(PrincipalPane.valLorT_n.GetLineText(0))
		t =  l ** 2 / np.float_(PrincipalPane.valD_n.GetLineText(0))
		return l, t

###########################################################################
# Some functions 4 calculations
###########################################################################

def function_alpha(wlengths, E_g):
	ans = []
	for wlength in wlengths:
		if h*c/(wlength) <= E_g:
			ans.append(0.0)
		else:
			ans.append( A * ( ( h*c/(wlength) - E_g ) )**0.5 )
	ans = np.array(ans, dtype='float64')
	if E_g != E_gn:
		global alpha_p
		alpha_p = ans
	return ans

def svdata(listdata):
	ans = listdata[0]
	global data_1
	data_1 = ans
	ans = listdata[1]
	global data_2
	data_2 = ans
	ans = listdata[2]
	global data_3
	data_3 = ans
	ans = listdata[3]
	global data_4
	data_4 = ans
	return listdata

def cldata():
	global D_n, D_p, eps_p, eps_n, N_a, N_d, E_gn, E_gp, E_gpmin, E_gpmax, N_cp, N_vp, N_cn, N_vn, S_n, S_p, W_n, W_p, W_pmin, W_pmax, X_n, X_p, Ta, S_i, Steps, Vib_steps, R, T, L_p, tau_p, L_p, tau_p
	global N_0, wlengths
	D_n, D_p, L_p, L_n, tau_n, tau_p, eps_p, eps_n, N_a, N_d, E_gn, E_gp, N_cp, N_vp, N_cn, N_vn, S_n, S_p, W_n, W_p, X_n, X_p, Ta, S_i = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
	wlengths, N_0 = [], []
	global data_1
	data_1 = []
	global data_2
	data_2 = []
	global data_3
	data_3 = []
	global data_4
	data_4 = []
	global R, T
	R, T = [], []

def Voc(x1,y1,x2,y2):
	ans = -(y2 - (( y2 - y1 ) / ( x2 - x1 )) * x2)/(( y2 - y1 ) / ( x2 - x1 ))
	return ans

def fV_ib(E):
	ans = ( ( E - E_gn ) / 2 ) + ( k_B * Ta * np.log( (N_a * N_d) / (ni_p * ni_n) ) ) - ( 0.5 * k_B * Ta * np.log( (N_cp * N_vn) / (N_cn * N_vp) ) ) + ( X_p - X_n )
	global V_ib
	V_ib = ans
	return ans

###########################################################################
# Photocurrent equations
###########################################################################

# [All contributions & integration]

def fdJ_ph(V):
	x_p = ( ( 2 * eps_p * eps_n * N_d * eps_0 * ( V_ib - V ) ) / ( N_a * q * ( eps_n * N_d + eps_p * N_a ) ) )**0.5
	if x_p >= W_p:   # x_p value > W_p
		x_p = W_p 

	x_n = ( ( 2 * eps_p * eps_n * eps_0 * N_a * ( V_ib - V ) ) / ( N_d * q * ( eps_n * N_d + eps_p * N_a ) ) )**0.5
	if x_n >= W_n:   # x_n value > W_n
		x_n = W_n
###########################################################################
# Photocurrent equations
###########################################################################
	dJ_p = []
	a = N_0 * (1 - R) * T * alpha_n * L_p / ( ( ( alpha_n ** 2 * L_p ** 2 ) - 1 ) )
	b = ( S_p * L_p / D_p ) + alpha_n * L_p - np.exp( - alpha_n * ( W_n - x_n) ) * ( ( S_p * L_p / D_p) * np.cosh( ( W_n - x_n ) / L_p ) + np.sinh( ( W_n -x_n ) / L_p ) )
	c = ( S_p * L_p / D_p ) * np.sinh( ( W_n - x_n ) / L_p ) + np.cosh( ( W_n - x_n ) / L_p )
	d = alpha_n * L_p * np.exp( - alpha_n * (W_n - x_n) )
	dJ_p = a * ( b / c - d)

	dJ_n = []
	a = N_0 * (1 - R) * T * alpha_p * L_n * np.exp( - (alpha_n * W_n + alpha_p * x_p) )  /  ( alpha_p**2 * L_n**2 - 1 )
	b = ( S_n * L_n / D_n ) * ( np.cosh( ( W_p - x_p ) / L_n ) - np.exp( - alpha_p * ( W_p - x_p ) ) ) + np.sinh( ( W_p - x_p ) / L_n ) + alpha_p * L_n * np.exp( - alpha_p * ( W_p - x_p ) )
	c = ( S_n * L_n / D_n ) * np.sinh( ( W_p - x_p ) / L_n ) + np.cosh( ( W_p - x_p ) / L_n )
	d = alpha_p * L_n
	dJ_n = a * ( d - b / c )

	dJ_scr = []
	dJ_scr = N_0 * (1 - R) * T * np.exp( - alpha_n * ( W_n - x_n ) ) * ( ( 1 - np.exp( - alpha_n * x_n ) ) + np.exp( - alpha_n * x_n ) * ( 1 - np.exp( - alpha_p * x_p ) ) )

	dJ_RCEp = []
	dJ_RCEp = N_0 * T * ( 1 - R) * np.exp( - alpha_n * W_n - alpha_p * ( 2 * W_p - x_p ) ) * ( 1 - np.exp( - alpha_p * x_p ) )

	dJ_RCEn = []
	dJ_RCEn = N_0 * T * ( 1 - R) * np.exp( - alpha_n * W_n - alpha_p * 2 * W_p ) * ( 1 - np.exp( - alpha_n ) )

	dJ_abs = []
	a = N_0 * T * ( 1 - R) * alpha_p * ( L_n / ( alpha_p ** 2 * L_n ** 2 - 1 ) ) * np.exp( - alpha_n * W_n - alpha_p * W_p )
	b = alpha_p * L_n
	c = S_n * L_n / D_n * ( np.cosh( ( W_p -x_p ) / L_n ) - np.exp( - alpha_p * ( W_p - x_p) )) + np.sinh( ( W_p -x_p ) / L_n ) + alpha_p * L_n * np.exp( - alpha_p * ( W_p - x_p ) )
	d = S_n * L_n / D_n * np.sinh( ( W_p - x_p ) / L_n ) + np.cosh( ( W_p - x_p ) / L_n )
	dJ_abs = a * ( b - c / d)


	dJ_win = []
	a = N_0 * T * ( 1 - R) * alpha_n * L_p / ( alpha_n ** 2 * L_p ** 2 - 1 ) * np.exp( - alpha_n * ( W_n + x_n ) - alpha_p * ( 2 * W_p ) )
	b = S_p * L_p / D_p * ( np.cosh( ( W_n - x_n ) / L_p ) - np.exp( -alpha_n * ( W_n - x_n ) ) ) + np.sinh( ( W_n - x_n ) / L_p ) + alpha_n * L_p * np.exp( alpha_n * ( W_n - x_n ) )
	c = S_p * L_p / D_p * np.sinh( ( W_n - x_n ) / L_p ) + np.cosh( ( W_n - x_n ) / L_p )
	dJ_win = a * ( alpha_n * L_p - b/c )

	ans = []
	ans = dJ_p + dJ_n + dJ_scr + dJ_RCEp + (dJ_RCEn)  + dJ_abs + dJ_win
	return ans 


def Jc(V):
    x_p = ( ( 2 * eps_p * eps_n * N_d * eps_0 * ( V_ib - V ) ) / ( N_a * q * ( eps_n * N_d + eps_p * N_a ) ) )**0.5
    if x_p >= W_p:   # x_p value > W_p
        x_p = W_p 

    x_n = ( ( 2 * eps_p * eps_n * eps_0 * N_a * ( V_ib - V ) ) / ( N_d * q * ( eps_n * N_d + eps_p * N_a ) ) )**0.5
    if x_n >= W_n:   # x_n value > W_n
        x_n = W_n
###########################################################################
# Photocurrent equations
###########################################################################
    dJ_ph = []
    dJ_ph.append(fdJ_ph(V))
    J_ph = 0
    J_ph = integrate.simps(dJ_ph, wlengths*1e7, even='avg') * (1 / 10) #scipy.integrate.fixed_quad(func, a, b, args=(), n=5) -https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.fixed_quad.html#scipy.integrate.fixed_quad-
###########################################################################
# Dark photocurrent equations
###########################################################################
    J_0p = 0.0
    a = q * D_p * p_0 / L_p
    b = ( S_p * L_p / D_p ) * np.cosh( ( W_n - x_n ) / L_p ) + np.sinh( ( W_n - x_n ) / L_p )
    c = ( S_p * L_p / D_p ) * np.sinh( ( W_n - x_n ) / L_p ) + np.cosh( ( W_n - x_n ) / L_p )
    J_0p = a * ( b / c ) * 1000

    J_0n = 0.0
    a = q * D_n * n_0 / L_n
    b = ( S_n * L_n / D_n ) * np.cosh( ( W_p - x_p ) / L_n ) + np.sinh( ( W_p - x_p ) / L_n )
    c = ( S_n * L_n / D_n ) * np.sinh( ( W_p - x_p ) / L_n ) + np.cosh( ( W_p - x_p ) / L_n )
    J_0n = a * ( b / c ) * 1000


    J_00 = 0.0
    J_00 = q * 1000 * ( x_n * ni_n / tau_p + x_p * ni_p / tau_n )

    J_000 = 0.0
    J_000 = q * 1000 * S_i * ( ( ( ( N_cp * N_vp ) / ( N_cn * N_vn ) ) ** 0.5 ) * ni_n + ni_p )

    Jdark = 0.0
    Jdark = ( J_0p + J_0n ) * ( np.exp( V / ( k_B * Ta ) ) - 1 ) + ( J_00 + J_000 ) * ( np.exp( V / ( 2 * k_B * Ta ) ) - 1 ) 

    return J_ph - Jdark

def one_cell(valgraph):
    # DEPENDIENTE:
    global ni_p, n_0, alpha_p, V_ib, voltage, isCheck, S_i
    ni_p = ( N_cp * N_vp * np.exp( - E_gp / ( k_B * Ta ) ) )**0.5
    n_0 = ni_p ** 2 / N_a
    isCheck = PrincipalPane.m_checkBox3.GetValue()
    alpha_p = function_alpha(wlengths, E_gp)
    V_ib = fV_ib(E_gp)
    voltage = np.linspace(0,V_ib,num=Vib_steps, dtype='float64')
    if isCheck:
        V_oc1, nu1, J_sc1, FF1, V_oc2, nu2, J_sc2, FF2 = np.zeros(8, dtype='float64')
        v1, J1, v2, J2  = [], [], [], []
        for i in voltage:
            S_i = 0.0
            j1 = Jc(i)
            if j1 <= 0:
                pass
            else:
                J1.append(j1)
                v1.append(i)
            S_i = float(PrincipalPane.valS_i.GetLineText(0))
            j2 = Jc(i)
            if j2 <= 0:
                pass
            else:
                J2.append(j2)
                v2.append(i)
        V_oc1 += np.float_(Voc( v1[-2], J1[-2], v1[-1], J1[-1] ))
        v1.append(V_oc1)
        J1.append(0.0)
        v1, J1 = np.array(v1, dtype='float64'), np.array(J1, dtype='float64')
        V_oc2 += np.float_(Voc( v2[-2], J2[-2], v2[-1], J2[-1] ))
        v2.append(V_oc2)
        J2.append(0.0)
        v2, J2 = np.array(v2, dtype='float64'), np.array(J2, dtype='float64')
        if valgraph:
            return  [v1, J1, v2, J2]
        else:
            nu1 += max(J1*v1)
            J_sc1 += max(J1)
            FF1 += 100*nu1/(V_oc1*J_sc1)
            nu2 += max(J2*v2)
            J_sc2 += max(J2)
            FF2 += 100*nu2/(V_oc2*J_sc2)
            return [V_oc1, nu1, FF1, J_sc1], [V_oc2, nu2, FF2, J_sc2]
    else:
        V_oc, nu, J_sc, FF = np.zeros(4, dtype='float64')
        S_i = 0.0
        v, J = [], []
        for i in voltage:
            j = Jc(i)
            if j <= 0:
                pass
            else:
                J.append(j)
                v.append(i)
        V_oc += np.float_(Voc( v[-2], J[-2], v[-1], J[-1] ))
        v.append(V_oc)
        J.append(0.0)
        v, J = np.array(v, dtype='float64'), np.array(J, dtype='float64')
        if valgraph:
            return [v, J]
        else:
            nu += max(J*v)
            J_sc += max(J)
            FF += 100*nu/(V_oc*J_sc)
            return [V_oc, nu, FF, J_sc]

app = wx.App()
frame = wx.Frame(None, -1, 'SOLAR - HET', pos=(0,0), size=(-1,-1))
frame.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ) )
frame.SetSizeHints( wx.Size( 1300,650 ), wx.Size( -1,-1 ) )
PrincipalPane = PrincipalPanel(frame)
frame.Show()
app.MainLoop()