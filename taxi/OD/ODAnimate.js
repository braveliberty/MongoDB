
var start_time=$(".start_time").val();
          var day=start_time.split(" ")[0].match(/[\d]$/g);//当前查询的天

          if($(".getoff").attr("click-state")){

            var url="http://127.0.0.1:7999/getoffclusterdata?north="+backcoords['north']+'&east='+backcoords['east']+'&south='+backcoords['south']+'&west='+backcoords['west']+'&day='+day;
            console.log("这是 getoff查询");
          }else{
            var url="http://127.0.0.1:7999/getonclusterdata?north="+backcoords['north']+'&east='+backcoords['east']+'&south='+backcoords['south']+'&west='+backcoords['west']+'&day='+day;

            console.log(url,"这是geton查询");
          }
          
          $.ajax({
              url:url,
              async:true,
              type:"get",
              dataType:'json',
              content:'',
              beforeSend:function(){
                alert("数据响应时间略长，请耐心等待……")
              },
              success:function(data){
                cluster_to_animate(data);
                timeCost(data);
                $(".modal").modal("hide");
              },
              error:function(){
                $(".modal").modal("hide");
                alert("数据请求错误")
              },
              complete:function(){

              }
          })