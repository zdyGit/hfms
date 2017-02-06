$(function(){
	$("#dg").datagrid({
        	singleSelect:true,
        	title:"所有账户",
		fitColumns:false,
		nowrap:false,
		rowStyler:function(index,row){
			if(index%2==1){
				return "background-color:#FFF5EE;"
			}
			else{
				return "background-color:#E0EEEE;"
			}
		}
	})
})
