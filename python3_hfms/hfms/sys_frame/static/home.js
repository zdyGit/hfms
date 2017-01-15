if(typeof menumanager != "object")
	menumanager = {}

function Createmenumanager(){
	var mf = {
		"Getmenulist":function(rootid){

		},
		"Openurl":function(title,url){
			if ($('#maintab').tabs('exists', title)){
					$('#maintab').tabs('select', title);
				} else {
					var content = '<iframe scrolling="auto" frameborder="0"  src="'+url+'" style="width:100%;height:100%;"></iframe>';
					$('#maintab').tabs('add',{
						title:title,
						content:content,
						closable:true
					});
				}
		}


	}
	return mf
}

$(function(){
	menumanager = Createmenumanager()
})
