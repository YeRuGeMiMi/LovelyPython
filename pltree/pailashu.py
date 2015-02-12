#coding:utf-8

#author:yfl
#date:2015-02-11
#取数据库中内容，画出树桩图

import MySQLdb
import pygraphviz as pgv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#取数据库数据
def getAll():
	sql = "select tree.id,m.username from pl_repconsume_tree tree left join pl_members m on tree.uid=m.uid order by tree.id"

	try:
		conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='pl',port=3306,charset='utf8')
		cur = conn.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		cur.close()
	except MySQLdb.Error, e:
		print "MySqlError"

	return result



#结果集转字典
def tulpToMap(prs):
	d = {}
	for vo in prs:
		d[vo[0]] = vo

	return d

#画图
def draw_plshu():
	r_tulp = getAll()
	r_map = tulpToMap(r_tulp)
	A = pgv.AGraph(directed=True,strict=True)
	for item in r_tulp:
		l_next = 2*item[0]
		r_next = 2*item[0]+1
		node = "("+str(item[0])+")"+item[1]
				
		if r_map.has_key(l_next):
			l_node = "("+str(r_map[l_next][0])+")"+r_map[l_next][1]
			A.add_edge(node,l_node)
		if r_map.has_key(r_next):
			r_node = "("+str(r_map[r_next][0])+")"+r_map[r_next][1]
			A.add_edge(node,r_node)

		A.graph_attr['epsilon']='0.001'
		A.write('pl003.dot')
		A.layout('dot')
		A.draw('pl003.svg')

if __name__ == '__main__':
	draw_plshu()
	