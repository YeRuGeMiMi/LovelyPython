#-*- coding:utf-8 -*-

#使用命令行工具作为交互工具

import os
import cmd
import sys

class SBCmd(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self);

	def help_EOF(self):
		print "退出";
	def do_EOF(self):
		sys.exit();

	