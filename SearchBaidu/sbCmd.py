#-*- coding:utf-8 -*-

#使用命令行工具作为交互工具

import os
import cmd
import sys
import re
import searchBaidu

class SBCmd(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = ">"   #命令提示符
		self.intro = "==欢迎使用查百度工具=="   #简介和欢迎信息

	def help_quit(self):
		print "退出"
	def do_quit(self,arg):
		sys.exit()

	def help_shell(self):
		print "查看所有命令"
	def do_shell(self,arg):
		commods = ["search","quit","?","!"]
		print ",".join(commods)

	def help_search(self):
		print "百度查询"
	def do_search(self,arg):
		params = arg.split(" ")
		if len(params) == 2:
			if re.match(r".+\.html",params[1]):
				stauts = searchBaidu.search(params[0],params[1])
				if stauts == 1:
					print "抓取成功！文件保存在%s"%params[1]
				else:
					print "出现错误！请重试！"
			else:
				print "输入保存文件必须是.html文件"
		else:
			print "输入参数不足，或者过多！请输入search 关键词 保存文件路径 "


	
if __name__ == '__main__':
	sb = SBCmd()
	sb.cmdloop()