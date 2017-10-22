import sublime
import sublime_plugin
import os

class GetfilepathforgitcommitCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if len(self.view.file_name()) > 0:
			#print(os.path.dirname(os.path.realpath(self.view.file_name())))
			filepath = os.path.realpath(self.view.file_name())
			#print(filepath)
			filepath = filepath.replace("\\", "/")
			if '/src' in filepath:
				modified_filepath = '/src' + filepath.split("/src",1)[1] 
				print(modified_filepath)
				sublime.set_clipboard(modified_filepath)
				sublime.status_message("copied file path: %s" %modified_filepath)
			
