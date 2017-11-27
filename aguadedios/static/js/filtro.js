$(document).ready(function(){
$("select[name=filtros]").change(function(){
    var sel = $('select[name=filtros]').val();
    if(sel==0){
      location.href = "http://localhost:8000/empresas/list/"
    }else{
      var url = "http://localhost:8000/empresas/filter/";
      location.href = url + $('select[name=filtros]').val();
    }
        });
});
