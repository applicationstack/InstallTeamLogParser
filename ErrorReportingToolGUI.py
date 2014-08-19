#GUI for Error Reporting tool. Should pop up when an error log is scanned.
#On Risa's windows machine, have to call C:\Python27\python.exe explicitly for this to work

import sys
import wx
import webbrowser

class ErrorReporting(wx.Frame):
	def __init__(self, *args, **kw):
		super(ErrorReporting, self).__init__(*args, size=(500,500))
		self.ErrorReportingGUI()

	def ErrorReportingGUI(self) :
		ErrorReportingPanel = wx.Panel(self)
	
		KnownErrorsList = open('C:\Users\I841251\Desktop\logparser\KnownErrors.txt', 'r')
		UnknownErrorsList = open('C:\Users\I841251\Desktop\logparser\UnknownErrors.txt', 'r')
		KnownErrorsLines = KnownErrorsList.readlines()
		UnknownErrorsLines = UnknownErrorsList.readlines()
	
		# Set up the font, sizing, and boxes
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		heading = wx.StaticText(self, label='Welcome to the Error Reporting Tool', pos=(140, 15))
		heading.SetFont(font)
		self.SetTitle( 'Error Reporting Tool')
		self.KnownErrorsTxtCtrl = wx.TextCtrl(self, value=str(KnownErrorsLines), pos=(30, 90), size=(150,150), style=wx.TE_MULTILINE)
		self.UnknownErrorsListBox = wx.TextCtrl(self, value=str(UnknownErrorsLines), pos=(270, 90), size=(150,150), style=wx.TE_MULTILINE)
		self.Bind(wx.EVT_LISTBOX, self.OnUnknownErrorsListBox)
		
		#Line for decoration and labels for boxes
		wx.StaticLine(self, pos=(25, 50), size=(300,1))
		KnownErrorsText = wx.StaticText(self, label='Known Errors', pos=(30, 60))
		KnownErrorsText.SetForegroundColour(wx.Colour(34,139,34))
		UnknownErrorsText = wx.StaticText(self, label='Unknown Errors', pos=(270, 60))
		UnknownErrorsText.SetForegroundColour(wx.Colour(255,0,0))
		wx.StaticLine(self, pos=(25, 260), size=(300,1))
	
		# When there are unknown errors present, report them to JIRA
		self.button =wx.Button(self, label="Report to JIRA", pos=(200, 325))
		self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

		self.Centre()
		self.Show(True)

	def OnClick(self,event):
		webbrowser.open('https://sapjira.wdf.sap.corp/secure/')
	def OnUnknownErrorsListBox(self, event):
		selection = self.UnknownErrorsListBox.GetSelection()

def main() :
	er = wx.App()
	ErrorReporting(None)
	er.MainLoop()

main()