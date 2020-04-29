function box_html(){
    $(".box").removeClass("yc")
    $(".user").addClass("yc")
    $(".budget").addClass("yc")
    $(".ng").addClass("yc")
    $(".budgetform").addClass("yc")
    $(".merge").addClass("yc")
    $(".detail").addClass("yc")
    $(".maintain").addClass("yc")
    $(".statistic").addClass("yc")
    $(".modifypwd").addClass("yc")
    $(".main_monitor").addClass("yc")
    $(".FA").addClass("yc")
}
//页面上的子菜单的交替
function unbind(){
    $('.unbinding').removeClass("yc")
    $('.models').addClass("yc")
    $('.banded').addClass("yc")
    $('.import_info').addClass("yc")
    $('.alter_parCode').addClass("yc")

    var BoxID = $('#query_BoxID').val()
//    var stage = $('#query_stageID').val()
    var sn = $('#query_SNLink').val()

    if(BoxID.length !=0 ||  sn.length !=0){
        query_model_info();
    }
}
function Box_Info(){
    $('.banded').removeClass("yc")
    $('.unbinding').addClass("yc")
    $('.models').addClass("yc")
    $('.import_info').addClass("yc")
    $('.alter_parCode').addClass("yc")

    var BoxID = $('#all_query_BoxID').val()
    var stage = $('#all_query_stageID').val()
    var sn = $('#all_query_SNLink').val()

    if(BoxID.length !=0 || stage.length !=0 || sn.length !=0){
        all_query_info();
    }

}
function binding(){
    $('.models').removeClass("yc")
    $('.unbinding').addClass("yc")
    $('.banded').addClass("yc")
    $('.import_info').addClass("yc")
    $('.alter_parCode').addClass("yc")
    if($("#txtModelstageID").val() !=""){
        Clear();
    }
}
function Alter_ParCode(){
    $('.alter_parCode').removeClass("yc")
    $('.models').addClass("yc")
    $('.unbinding').addClass("yc")
    $('.banded').addClass("yc")
    $('.import_info').addClass("yc")
    var PartCode = $('#q_PartCode').val()
    var stage = $('#q_stageID').val()
    if(PartCode.length !=0 || stage.length !=0){
        alter_query();
    }


}
function im_info(){
    $('.models').addClass("yc")
    $('.unbinding').addClass("yc")
    $('.banded').addClass("yc")
    $('.alter_parCode').addClass("yc")
    $('.import_info').removeClass("yc")
}

//导入信息models
function import_model(obj){
    data = {'import_Models':obj.value.replace(/^\s+|\s+$/g,"").toUpperCase(),}
    $.ajax({
        'type':'POST',
        'url':'/BoxID/import-models/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                $('#import_mode').empty();
                data_info = result['data']
                for(var a=0; a<data_info.length; a++){
                     var b = a+1
                    var form_modelstageId ='<tr align="left">'
                      +'<td>'+b+'</td>'
                      +'<td>'+data_info[a].ModelStage+'</td>'
                      +'<td>'+data_info[a].PartCode+'</td>'
                      +'<td>'+data_info[a].PartName+'</td>'
                      +'<td>'+data_info[a].RequireQuantity+'</td>'
                      +'<td>'+data_info[a].AlternativeType+'</td>'
                      +'</tr>'
                    $('#import_mode').append(form_modelstageId)
                }
                window.message.showSuccess(result['message'])

            }else{
                alert(result['message'])
                console.log(result['message'])
                console.log(result['data'])
            }
        }
    })
}
function SN_import(obj){
   data = {'import_SNs':obj.value.replace(/^\s+|\s+$/g,"").toUpperCase(),}
    $.ajax({
        'type':'POST',
        'url':'/BoxID/import-SN/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                $('#import_sn').empty();
                data_info = result['data']
                for(var a=0; a<data_info.length; a++){
                     var b = a+1
                    var form_modelstageId ='<tr align="left">'
                      +'<td>'+b+'</td>'
                      +'<td>'+data_info[a].BarCode+'</td>'
                      +'<td>'+data_info[a].PartCode+'</td>'
                      +'</tr>'
                    $('#import_sn').append(form_modelstageId)
                }

            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })
}

//修改box添加方式
//function get_BoxID(){
//    data={}
//    $.ajax({
//        'type':'POST',
//        'url':'/BoxID/Get-Box/',
//        'data':data,
//        success:function(result){
//            if(result['code'] === 200){
//                $('#b_number').empty()
//                box_number = result['data'].BoxId
//
//                var check_item = '<option value="'+box_number+'">'+box_number+'</option>'
//                $('#b_number').append(check_item)
//            }else{
//                alert(result['message'])
//                console.log(result['message'])
//            }
//        }
//    })
//}
//function added_Box(){
//    data = {"BoxId":$("#b_number").val()}
//     $.ajax({
//        'type':'POST',
//        'url':'/BoxID/Add-Box/',
//        'data':data,
//        success:function(result){
//            if(result['code'] === 200){
//                console.log(result)
//                window.message.showSuccess(result['message'])
//
//            }else{
//                alert(result['message'])
//                console.log(result['message'])
//            }
//        }
//    })
//}
//修改成自定义的增加box
function add_Box(obj){
    data = {'import_Box':obj.value.replace(/^\s+|\s+$/g,"").toUpperCase(),}
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/Add-Box/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                $('#import_Box').empty();
                window.message.showSuccess(result['message'])

            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })
}

//这里是从数据表里面捞取相关性的数据
function ModelID(obj){
    data = {'modelstageId':obj.value.toUpperCase(),}
    $.ajax({
        'type':'POST',
        'url':'/BoxID/Model-stage-ID/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                $('#search_model').empty();
                data_info = result['data']
                for(var a=0; a<data_info.length; a++){
                    if(data_info[a].AlternativeType == null){data_info[a].AlternativeType=""}
                    if(data_info[a].BrushNumber == null){data_info[a].BrushNumber=""}
                    if(data_info[a].AlternativePartCode == null){data_info[a].AlternativePartCode=""}
                    if(data_info[a].Status == 'Over'){Status_class="badge-danger"}
                    if(data_info[a].Status == 'Open'){Status_class="badge-warning"}
                    if(data_info[a].Status == 'OK'){Status_class="badge-success"}

                    var form_modelstageId ='<tr align="left">'
                      +'<td>'+data_info[a].Id+'</td>'
                      +'<td>'+data_info[a].ModelStage+'</td>'
                      +'<td>'+data_info[a].PartCode+'</td>'
                      +'<td>'+data_info[a].PartName+'</td>'
                      +'<td>'+data_info[a].RequireQuantity+'</td>'
                      +'<td>'+data_info[a].BrushNumber+'</td>'
                      +'<td>'+data_info[a].BrushSN+'</td>'
                      +'<td>'+data_info[a].AlternativeType+'</td>'
                      +'<td>'+data_info[a].AlternativePartCode+'</td>'
                      +'<td><span class="badge '+Status_class+'">'+data_info[a].Status+'</span></td>'
                    +'</tr>'
                    $('#search_model').append(form_modelstageId)
                    popover_show();
                }
                $("#txtModelstageID").attr("readonly","true");

            }else{
                alert(result['message'])
                $("#txtModelstageID").val("")
                console.log(result['message'])
            }
        }
    })
}

function Box_check(obj){
    data = {'BoxId':obj.value.toUpperCase(),}
    $.ajax({
        'type':'POST',
        'url':'/BoxID/Box-Id-check/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                data_info=result['data']
                if(data_info != ""){
                    $('#search_model').empty();
                    $("#txtModelstageID").val(data_info[0]["ModelStage"])
                    $("#txtModelstageID").attr("readonly","true");
                    for(var a=0; a<data_info.length; a++){
                    if(data_info[a].AlternativeType == null){data_info[a].AlternativeType=""}
                    if(data_info[a].BrushNumber == null){data_info[a].BrushNumber=""}
                    if(data_info[a].AlternativePartCode == null){data_info[a].AlternativePartCode=""}
                    if(data_info[a].Status == 'Over'){Status_class="badge-danger"}
                    if(data_info[a].Status == 'none'){Status_class="badge-danger"}
                    if(data_info[a].Status == 'Open'){Status_class="badge-warning"}
                    if(data_info[a].Status == 'OK'){Status_class="badge-success"}
                    var brushSN = data_info[a].BrushSN
                    if(brushSN && brushSN.length >9 ){
                        var ellipsis = "<font color=\"blue\">...</font>";
                        var sub_brushSN = brushSN.substring(0,9);
                        brushSN_show = "<span data-toggle=\"popover\" data-trigger=\"hover click\" data-content=\""+ brushSN +"\">" + sub_brushSN + ellipsis + "</span>";

                    }else{
                        brushSN_show=brushSN
                    }

                    var form_modelstageId ='<tr align="left">'
                      +'<td>'+data_info[a].Id+'</td>'
                      +'<td>'+data_info[a].ModelStage+'</td>'
                      +'<td>'+data_info[a].PartCode+'</td>'
                      +'<td>'+data_info[a].PartName+'</td>'
                      +'<td>'+data_info[a].RequireQuantity+'</td>'
                      +'<td>'+data_info[a].BrushNumber+'</td>'
                      +'<td>'+brushSN_show+'</td>'
                      +'<td>'+data_info[a].AlternativeType+'</td>'
                      +'<td>'+data_info[a].AlternativePartCode+'</td>'
                      +'<td><span class="badge '+Status_class+'">'+data_info[a].Status+'</span></td>'
                    +'</tr>'
                    $('#search_model').append(form_modelstageId)
                    popover_show();

                    }
                    $("#BoxId").attr("readonly","true");
                }else{
                    $("#txtModelstageID").removeAttr("readonly","false");
                }
//                $("#BoxId").attr("readonly","true");
                window.message.showSuccess(result['message'])

            }else{
                alert(result['message'])
                $("#BoxId").val("")
                console.log(result['message'])
            }
        }
    })
}
//刷入sn信息
function SN_info(obj){
    var modelId = $('#txtModelstageID').val().replace(/^\s+|\s+$/g,"").toUpperCase()
    var boxId = $('#BoxId').val().replace(/^\s+|\s+$/g,"").toUpperCase()
    if(modelId.length == 0){
        alert("please input ModelId Number")
        $('#brushSN').val("")
        $('#BoxId').val("")
        return false;
    }
    if(boxId.length == 0){
        alert("please input BoxId Number")
        $('#brushSN').val("")
        $('#BoxId').val("")
        return false;
    }
    console.log(modelId,obj.value)
    data = {
        'SN':obj.value.toUpperCase(),
        'ModelStage':modelId,
        'BoxId':boxId,

    }
    $.ajax({
        'type':'POST',
        'url':'/BoxID/SN-info/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                window.message.showSuccess(result['message'])
                console.log(result)
                $('#search_model').empty();
                data_info = result['data']
                for(var a=0; a<data_info.length; a++){
                    if(data_info[a].BrushNumber == null){data_info[a].BrushNumber=""}
                    if(data_info[a].AlternativePartCode == null){data_info[a].AlternativePartCode=""}
                    if(data_info[a].Status == 'Over'){Status_class="badge-danger"}
                    if(data_info[a].Status == 'Open'){Status_class="badge-warning"}
                    if(data_info[a].Status == 'none'){Status_class="badge-danger"}
                    if(data_info[a].Status == 'OK'){Status_class="badge-success"}
                    var brushSN = data_info[a].BrushSN
                    if(brushSN && brushSN.length >9 ){
                        var ellipsis = "<font color=\"blue\">...</font>";
                        var sub_brushSN = brushSN.substring(0,9);
                        brushSN_show = "<span data-toggle=\"popover\" data-trigger=\"hover click\" data-content=\""+ brushSN +"\">" + sub_brushSN + ellipsis + "</span>";

                    }else{
                        brushSN_show=brushSN
                    }

                    var form_modelstageId ='<tr align="left">'
                      +'<td>'+data_info[a].Id+'</td>'
                      +'<td>'+data_info[a].ModelStage+'</td>'
                      +'<td>'+data_info[a].PartCode+'</td>'
                      +'<td>'+data_info[a].PartName+'</td>'
                      +'<td>'+data_info[a].RequireQuantity+'</td>'
                      +'<td>'+data_info[a].BrushNumber+'</td>'
                      +'<td>'+brushSN_show+'</td>'
                      +'<td>'+data_info[a].AlternativeType+'</td>'
                      +'<td>'+data_info[a].AlternativePartCode+'</td>'
                      +'<td><span class="badge '+Status_class+'">'+data_info[a].Status+'</span></td>'
                    +'</tr>'
                    $('#search_model').append(form_modelstageId)
                    popover_show();
                }

            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })
}
//清除绑定页面的输入框里面的内容
function Clear(){
    $("#BoxId").val("")
    $("#txtModelstageID").val("")
    $("#search_model").empty()
    $("#BoxId").removeAttr("readonly","false");
    $("#txtModelstageID").removeAttr("readonly","false");
}

//给代用料的查询功能
function alter_query(){
    var PartCode = $('#q_PartCode').val().toUpperCase()
    var ModelStage =$('#q_stageID').val().toUpperCase()

    if(PartCode.length == 0 && ModelStage.length == 0){
        alert("need input one message")
        return false;
    }
    data={
        'PartCode':PartCode,
        'ModelStage':ModelStage,
    }
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/alternative-query/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                $('#Al_ParCode').empty();
                data_info = result['data']
                for(var a=0; a<data_info.length; a++){
//                    if(data_info[a].BrushNumber == null){data_info[a].BrushNumber=""}
                    if(data_info[a].AlternativePartCode == null){data_info[a].AlternativePartCode=""}
                    if(data_info[a].AlternativeType == null){data_info[a].AlternativeType=""}
//                    if(data_info[a].Status == 'Open'){Status_class="badge-danger"}
//                    if(data_info[a].Status == 'OK'){Status_class="badge-success"}

                    var form_modelstageId ='<tr align="left">'
                      +'<td>'
                        +'<span onclick="modify_ParCode($(this));" ><img alt="Add" src="/static/images/icon_modify.gif"></span>'
                        +'<span onclick="delete_ParCode($(this));" data-toggle="modal" data-target="#remove_ParCode"><img  alt="Delete" src="/static/images/icon_del.gif"></span>'
                      +'</td>'
                      +'<td class="yc">'+data_info[a].Id+'</td>'
                      +'<td>'+data_info[a].ModelStage+'</td>'
                      +'<td>'+data_info[a].PartCode+'</td>'
                      +'<td>'+data_info[a].PartName+'</td>'
                      +'<td>'+data_info[a].AlternativeType+'</td>'
//                      +'<td>'+data_info[a].RequireQuantity+'</td>'
//                      +'<td>'+data_info[a].BrushNumber+'</td>'
                      +'<td>'+data_info[a].AlternativePartCode+'</td>'
//                      +'<td><span class="badge '+Status_class+'">'+data_info[a].Status+'</span></td>'
                    +'</tr>'
                    $('#Al_ParCode').append(form_modelstageId)
                    popover_show();
                }



            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })
}
//增加<span class="help-block"></span>".parent().parent().find("td").
function modify_ParCode(obj){
    var model_id = obj.parent().parent().find("td").eq(1).text()
    var ParCode = obj.parent().parent().find("td").eq(6).text()
    $("#modelsId").val(model_id)
    $("#ParCode_html").val(ParCode)
    console.log(model_id,ParCode)
    $("#modify_ParCode").modal("show")
}
function modify_alParCode(){
    var model_id = $('#modelsId').val()
    var add_ParCode = $('#add_alP').val()
    var original_parcode = $('#ParCode_html').val()
    var alter_type = $('#alter_type').val()

    var ParCode=""
    if(add_ParCode.length ==0){
        alert("need value input")
        return false;
    }
    data={
        'model_id':model_id,
        'original_parcode':original_parcode,
        'add_ParCode':add_ParCode,
        'alter_type':alter_type,
    }
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/modify-alterParCode/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                window.message.showSuccess(result['message'])
                alter_query();
            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })

}
//减少
function delete_ParCode(obj){
    var model_id = obj.parent().parent().find("td").eq(1).text()
    var ParCode = obj.parent().parent().find("td").eq(6).text()
    $("#mode_id_del").val(model_id)
    $("#original_parcode").val(ParCode)
    console.log(model_id,ParCode)
    console.log("进入删除")
}

function delete_alParCode(){
    var model_id = $('#mode_id_del').val()
    var del_ParCode = $('#del_parCodes').val()
    var original_parcode = $('#original_parcode').val()

    if(del_ParCode.length ==0){
        alert("delete ParCode can not empty")
        return false;
    }
    data={
        'model_id':model_id,
        'del_ParCode':del_ParCode,
        'original_parcode':original_parcode,
    }
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/delete-alterParCode/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                window.message.showSuccess(result['message'])
                alter_query();
            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })

}
//解绑页面的控制和查询
function query_model_info(){
    var BoxId = $('#query_BoxID').val().toUpperCase()
//    var ModelStageID = $('#query_stageID').val()
    var SN = $('#query_SNLink').val().toUpperCase()
    if(BoxId.length==0 && SN.length ==0){
        alert("need input one value")
        return false;
    }
    data={
        'BoxId':BoxId,
        'SN':SN,

    }
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/unbinding-query/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                data = result["data"]
                $('#unbinding_add_html').empty();
                for(var a=0; a<data.length; a++){
                    if(data[a].Status == 'none'){Status_class="badge-danger"}
                    if(data[a].Status == 'Open'){Status_class="badge-warning"}
                    if(data[a].Status == 'Over'){Status_class="badge-danger"}
                    if(data[a].Status == 'OK'){Status_class="badge-success"}
                    if(data[a].BrushNumber == null){data[a].BrushNumber =""}
                    if(data[a].AlternativePartCode == null){data[a].AlternativePartCode =""}
                    var brushSN = data[a].BrushSN
                    if(brushSN && brushSN.length >9 ){
                        var ellipsis = "<font color=\"blue\">...</font>";
                        var sub_brushSN = brushSN.substring(0,9);
                        brushSN_show = "<span data-toggle=\"popover\" data-trigger=\"hover click\" data-content=\""+ brushSN +"\">" + sub_brushSN + ellipsis + "</span>";

                    }else{
                        brushSN_show=brushSN
                    }

                    if(data[a].Status == 'OK'){
                         var data_info ='<tr>'
                          +'<td>'
                            +'<input type="checkbox" class="input_class" id="" name="" value="true">'
                            +'<label class ="yc" >'+data[a].Id+'</label>'
                          +'</td>'
                          +'<td>'
                            +'<span  onclick="release_box($(this));" data-toggle="modal" data-target="#release_buddy"><img  alt="Delete" src="/static/images/signalink.png"></span>'
                          +'</td>'
                          +'<td>'+data[a].BoxID+'</td>'
                          +'<td>'+data[a].ModelStage+'</td>'
                          +'<td >'+data[a].PartCode+'</td>'
                          +'<td>'+data[a].PartName+'</td>'
                          +'<td>'+data[a].RequireQuantity+'</td>'
                          +'<td>'+data[a].BrushNumber+'</td>'
                          +'<td>'+brushSN_show+'</td>'
                          +'<td>'+data[a].AlternativePartCode+'</td>'
                          +'<td><span class="badge '+Status_class+'">'+data[a].Status+'</span></td>'
                        +'</tr>'
                        $('#unbinding_add_html').append(data_info)
                        popover_show();
                    }
                    if(data[a].Status == 'Open'){
                        var data_info ='<tr>'
                          +'<td>'
                            +'<input type="checkbox" class="input_class" id="" name="" value="true">'
                            +'<label class ="yc" >'+data[a].Id+'</label>'
                          +'</td>'
                          +'<td>'
                            +'<span  onclick="release_box($(this));" data-toggle="modal" data-target="#release_buddy"><img  alt="Delete" src="/static/images/signalink.png"></span>'
                          +'</td>'
                          +'<td>'+data[a].BoxID+'</td>'
                          +'<td>'+data[a].ModelStage+'</td>'
                          +'<td >'+data[a].PartCode+'</td>'
                          +'<td>'+data[a].PartName+'</td>'
                          +'<td>'+data[a].RequireQuantity+'</td>'
                          +'<td>'+data[a].BrushNumber+'</td>'
                          +'<td>'+brushSN_show+'</td>'
                          +'<td>'+data[a].AlternativePartCode+'</td>'
                          +'<td><span class="badge '+Status_class+'">'+data[a].Status+'</span></td>'
                        +'</tr>'
                        $('#unbinding_add_html').append(data_info)
                        popover_show();
                    }
                    if(data[a].Status == 'Over'){
                        var data_info ='<tr>'
                          +'<td>'
                            +'<input type="checkbox" class="input_class" id="" name="" value="true">'
                            +'<label class ="yc" >'+data[a].Id+'</label>'
                          +'</td>'
                          +'<td>'
                            +'<span  onclick="release_box($(this));" data-toggle="modal" data-target="#release_buddy"><img  alt="Delete" src="/static/images/signalink.png"></span>'
                          +'</td>'
                          +'<td>'+data[a].BoxID+'</td>'
                          +'<td>'+data[a].ModelStage+'</td>'
                          +'<td >'+data[a].PartCode+'</td>'
                          +'<td>'+data[a].PartName+'</td>'
                          +'<td>'+data[a].RequireQuantity+'</td>'
                          +'<td style="color:red;">'+data[a].BrushNumber+'</td>'
                          +'<td>'+brushSN_show+'</td>'
                          +'<td>'+data[a].AlternativePartCode+'</td>'
                          +'<td><span class="badge '+Status_class+'">'+data[a].Status+'</span></td>'
                        +'</tr>'
                        $('#unbinding_add_html').append(data_info)
                        popover_show();

                    }
                    if(data[a].Status == 'none'){
                        var data_info ='<tr>'
                          +'<td>'
                            +'<label class ="yc" >'+data[a].Id+'</label>'
                          +'</td>'
                          +'<td>'
                            +'<span  onclick="release_box($(this));" data-toggle="modal" data-target="#release_buddy"><img  alt="Delete" src="/static/images/signalink.png"></span>'
                          +'</td>'
                          +'<td>'+data[a].BoxID+'</td>'
                          +'<td>'+data[a].ModelStage+'</td>'
                          +'<td >'+data[a].PartCode+'</td>'
                          +'<td>'+data[a].PartName+'</td>'
                          +'<td>'+data[a].RequireQuantity+'</td>'
                          +'<td style="color:red;">'+data[a].BrushNumber+'</td>'
                          +'<td style="color:red;">'+brushSN_show+'</td>'
                          +'<td>'+data[a].AlternativePartCode+'</td>'
                          +'<td><span class="badge '+Status_class+'">'+data[a].Status+'</span></td>'
                        +'</tr>'
                        $('#unbinding_add_html').append(data_info)
                        popover_show();

                    }

                }
            }else{
                $('#unbinding_add_html').empty();
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })
}
//解绑调用modal
function release_box(obj){
    var object = obj.parent().parent().find("td")
    var id = object.eq(0).text()
    var modelStageID = object.eq(3).text()
    var partCode = object.eq(4).text()
    var requirement = object.eq(6).text()
    var brushNumber = object.eq(7).text()
    var BrushSN = object.eq(8).find("span").eq(0).attr("data-content")
    if(typeof(BrushSN) =="undefined"){
        BrushSN=object.eq(8).text()
    }
    data={
        'id':id,
        'modelStageID':modelStageID,
        'partCode':partCode,
        'requirement':requirement,
        'brushNumber':brushNumber,
        'BrushSN':BrushSN,
    }
    console.log(data)
    $('#release_Id').val(id)
    $('#release_ModelStageID').val(modelStageID)
    $('#release_part').val(partCode)
    $('#release_brushNumber').val(brushNumber)
    $('#check_Bush_SN').val(BrushSN)
    if(brushNumber ==0 && BrushSN.length==0){
        $("#release_buddy").modal("show")
        alert("no need release items")
        return false;
    }
}
//解绑功能的实现
function release_PartCodes(){
    var id = $('#release_Id').val()
    var release_brushNumber = $('#release_brushNumber').val()
    var check_Bush_SN = $('#check_Bush_SN').val()
    var release_partCode = $('#release_partCode').val()

    if(release_partCode.length ==0){
        alert("need release value")
        return false;
    }
    data={
        'id':id,
        'release_brushNumber':release_brushNumber,
        'check_Bush_SN':check_Bush_SN,
        'release_partCode':release_partCode,
    }
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/release-partCode/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                window.message.showSuccess(result['message'])
                query_model_info();

            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })

}

function unbind_html(){
    var SNS = ""
    $("table input[type=checkbox]:checked").each(function(){
        var sn = $(this).parent().parent().find("td").eq(8).find("span").attr("data-content")
        if(typeof(sn) == "undefined"){
            sn = $(this).parent().parent().find("td").eq(8).text()
        }
        if(sn !=""){
            if(SNS ==""){
                SNS=sn
            }else{
                SNS = SNS+","+sn
            }
        }

    })
    if(SNS.length==0){
        alert("no need release")
        return false;
    }
    console.log(SNS)
    data = {'models_ids':SNS}
    $.ajax({
        'type':'POST',
        'url':'/BoxID/Release-all-partCode/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                window.message.showSuccess(result['message'])
                query_model_info();

            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })

}

//删除调用modal
function delete_box(obj){
    var id = obj.parent().parent().find("td").eq(0).text()
    var modelStageID = obj.parent().parent().find("td").eq(3).text()
    var partCode = obj.parent().parent().find("td").eq(4).text()
//    var requirement = obj.parent().parent().find("td").eq(6).text()
    var brushNumber = obj.parent().parent().find("td").eq(7).text()
    var BrushSN = obj.parent().parent().find("td").eq(8).text()
    data={
        'id':id,
        'modelStageID':modelStageID,
        'partCode':partCode,
        'brushNumber':brushNumber,
        'BrushSN':BrushSN,
    }
    console.log(data)
    $('#remove_Id').val(id)
    $('#remove_ModelStageID').val(modelStageID)
    $('#remove_part').val(partCode)
    if(brushNumber !=0 && BrushSN.length!=0){
        $("#remove_buddy").modal("show")
        alert("first need to release")
        return false;
    }

}
//删除功能的实现
function remove_PartCodes(){
    var id = $('#remove_Id').val()
    var remove_ModelStageID = $('#remove_ModelStageID').val()
    var remove_PartCode = $('#remove_part').val()

    if(id.length ==0){
        alert("need release value")
        return false;
    }
    data={
        'id':id,
        'remove_ModelStageID':remove_ModelStageID,
        'remove_PartCode':remove_PartCode,
    }
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/remove-partCode/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                window.message.showSuccess(result['message'])
                query_model_info();

            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })
}
//修改调用modal插入值
function modify_box(obj){
    var id = obj.parent().parent().find("td").eq(0).text()
    var actual_requirement = obj.parent().parent().find("td").eq(1).text()
    var modelStageID = obj.parent().parent().find("td").eq(3).text()
    var partCode = obj.parent().parent().find("td").eq(4).text()
    var requirement = obj.parent().parent().find("td").eq(6).text()
    var brushNumber = obj.parent().parent().find("td").eq(7).text()
    var BrushSN = obj.parent().parent().find("td").eq(8).text()
    data={
        'id':id,
        'actual_requirement':actual_requirement,
        'modelStageID':modelStageID,
        'partCode':partCode,
        'requirement':requirement,
        'brushNumber':brushNumber,
        'BrushSN':BrushSN,
    }
    console.log(data)
    $('#modify_Id').val(id)
    $('#modify_ModelStageID').val(modelStageID)
    $('#modify_part').val(partCode)
    $('#modify_brushNumber').val(brushNumber)
    $('#modify_brushSN').val(BrushSN)
    $('#modify_actual_re').val(actual_requirement)
    $('#modify_brushSN').val(BrushSN)


}
//修改的功能实现
function modify_PartCodes(){
    var id = $('#modify_Id').val()
    var modify_requirement = $('#modify_requirement').val()

    if(id.length ==0){
        alert("please reload")
        return false;
    }
    data={
        'id':id,
        'modify_requirement':modify_requirement,
    }
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/modify-partCode/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                window.message.showSuccess(result['message'])
                query_model_info();

            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })


}
//一键解绑的功能
function unbinding_modelStage(){
//    $("#unbinding_add_html :checkbox").prop("checked", true);
//    var select_box = $("table input[type=checkbox]:checked")
//    console.log(select_box)
//    var statement_box = []
//    select_box.each(function(){
//        statement_box.push($(this).next().html());
//    })
//
//    console.log(statement_box)
}






//查询绑定管理的信息查询的页面的控制
function all_query_info(){
    var BoxId = $('#all_query_BoxID').val().toUpperCase()
    var ModelStageID = $('#all_query_stageID').val().toUpperCase()
    var SN = $('#all_query_SNLink').val().toUpperCase()
    var check_box = $('#IF_check').prop("checked")
    if(check_box==true){check_box="true"}
    if(check_box==false){check_box="false"}
    if(BoxId.length==0 && ModelStageID.length ==0 && SN.length ==0 && check_box=="false"){
        alert("need input one value")
        return false;
    }
    data={
        'BoxId':BoxId,
        'ModelStageID':ModelStageID,
        'SN':SN,
        'check_box':check_box,
    }
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/info-all-query/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
                console.log(result)
                data = result["data"]
                $('#query_info_data').empty();
                if(check_box =="false"){
                    for(var a=0; a<data.length; a++){
                        if(data[a].Status == 'Over'){Status_class="badge-danger"}
                        if(data[a].Status == 'Open'){Status_class="badge-warning"}
                        if(data[a].Status == 'OK'){Status_class="badge-success"}
                        if(data[a].BrushNumber == null){data[a].BrushNumber =""}
                        if(data[a].AlternativeType == null){data[a].AlternativeType =""}
                        if(data[a].AlternativePartCode == null){data[a].AlternativePartCode =""}
                        var brushSN = data[a].BrushSN
                        if(brushSN && brushSN.length >9 ){
                            var ellipsis = "<font color=\"blue\">...</font>";
                            var sub_brushSN = brushSN.substring(0,9);
                            brushSN_show = "<span data-toggle=\"popover\" data-trigger=\"hover click\" data-content=\""+ brushSN +"\">" + sub_brushSN + ellipsis + "</span>";

                        }else{
                            brushSN_show=brushSN
                        }
                        var data_info ='<tr>'
                          +'<td>'+data[a].BoxID+'</td>'
                          +'<td>'+data[a].ModelStage+'</td>'
                          +'<td>'+data[a].PartCode+'</td>'
                          +'<td>'+data[a].PartName+'</td>'
                          +'<td>'+data[a].RequireQuantity+'</td>'
                          +'<td>'+data[a].BrushNumber+'</td>'
                          +'<td>'+brushSN_show+'</td>'
                          +'<td>'+data[a].AlternativeType+'</td>'
                          +'<td>'+data[a].AlternativePartCode+'</td>'
                          +'<td><span class="badge '+Status_class+'">'+data[a].Status+'</span></td>'
                        +'</tr>'
                        $('#query_info_data').append(data_info)
                    }
                }else{
                    for(var a=0; a<data.length; a++){
                        var data_info ='<tr>'
                          +'<td>'+data[a].BoxId+'</td>'
                          +'<td>'+data[a].ModelStageId+'</td>'
                          +'<td></td>'
                          +'<td></td>'
                          +'<td></td>'
                          +'<td></td>'
                          +'<td></td>'
                          +'<td></td>'
                          +'<td></td>'
                          +'<td></td>'
                        +'</tr>'
                        $('#query_info_data').append(data_info)
                    }
                }
            }else{
                $('#query_info_data').empty();
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })
}
//下载报表的功能的实现
function change_binding(){
    var BoxId = $('#all_query_BoxID').val().toUpperCase()
    var ModelStageID = $('#all_query_stageID').val().toUpperCase()
    var SN = $('#all_query_SNLink').val().toUpperCase()
    var check_box = $('#IF_check').prop("checked")
    if(check_box==true){check_box="true"}
    if(check_box==false){check_box="false"}
    if(BoxId.length==0 && ModelStageID.length ==0 && SN.length ==0 ){
        alert("need input one value")
        return false;
    }
    data={
        'BoxId':BoxId,
        'ModelStageID':ModelStageID,
        'SN':SN,
        'check_box':check_box,
    }
    console.log(data)
    $.ajax({
        'type':'POST',
        'url':'/BoxID/download-binding-infos/',
        'data':data,
        success:function(result){
            if(result['code'] === 200){
//                console.log(result["data"])
                var url=result['data'][0]
                window.location.href=url

            }else{
                alert(result['message'])
                console.log(result['message'])
            }
        }
    })
}