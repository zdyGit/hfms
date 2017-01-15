var setting = {
	view:{
		selectedMulti:false
	},
	data:{
		simpleData:{
			enable:true,
			idKey:"id",
			pIdKey:"pid",
			rootPid:0
		}
	},
	callback:{
		onDblClick:function(treeid,treenode){
			alert("双击")
		} 
	}
}

var data = [
	{id:1,pid:0,open:true,name:"root"},
	{id:2,pid:1,name:"test"},
	{id:3,pid:1,name:"test"},
	{id:4,pid:1,name:"test"},
	{id:5,pid:3,name:"test"},
	{id:6,pid:3,name:"test"}
]

$(function(){
	console.log("test")
	$.fn.zTree.init($("#menutree"),setting,data)
})
