let removeToast;
back_optin_list="갈색톤.jpg/검은색 목재.jpg/밝은 나무.jpg/밝은 벽돌 콘크리트.jpg/밝은 콘크리트.jpg/밝은 회색, 마루.jpg/분홍 벽지.jpg/블루 원단.jpg/살구벽지,마루.jpg/살색 원단.jpg/어두운 콘크리트.jpg/자홍색벽지.jpg/청색 대리석.jpg/청색벽, 소나무 원목.jpg/한지 텍스쳐.jpg/흰벽,밝은마루.jpg/흰색 나무결 (2).jpg/흰색 나무결.jpg"
font_list="A01/A02/A03/A04/A05/A06/A07/A08/A09/A10/B01/B02/B03/B04/B05/B06/B07/B08/B09/B10/C01/C02/C03/C04/C05/C06/C07/D01/D02"

price_KE ={}
price_KE["4cm"]=1200
price_KE["5cm"]=1500
price_KE["6cm"]=2000
price_KE["8cm"]=3500
price_KE["10cm"]=4500
price_KE["15cm"]=7000
price_KE["20cm"]=9500
price_ETC ={}
price_ETC["4cm"]=2000
price_ETC["5cm"]=2200
price_ETC["6cm"]=3000
price_ETC["8cm"]=4000
price_ETC["10cm"]=5000
price_ETC["15cm"]=8000
price_ETC["20cm"]=10000

maxWH = {}
maxWH["a"]=[900,800]
maxWH["b"]=[550,550]
maxWH["C"]=[900,600]

window.addEventListener('load', function() {
  if ( self !== top ) {
//    console.log("iframe");
//    console.log(parent);
  //    alert(window.location.href);
  } else {
//    console.log("nono")
  }
})

function cut_line(){
  tmp=document.getElementById("preview_text");
  sel_text=tmp.innerText
  if (sel_text.indexOf("؊")>-1) {
    toast("사용할 수 없는 문자입니다!")
    sel_text=sel_text.replace("؊","")
    tmp.innerText=sel_text
  }
  if (sel_text.length>20) {
    toast("20자씩 나눠서 입력해주세요!")
    sel_text=sel_text.slice(0,20)
    tmp.innerText=sel_text
  }
  text_list=tmp.innerText.split('\n');
  for (var y = text_list.length-1; y > -1; y--) {
    pre_text=document.getElementById('pre_text2');
    pre_text.innerText=text_list[y];
    text_t=text_list[y];
    pre_h=pre_text.clientHeight;
    y_rec=[]
    for (var i = text_t.length-1; i > 0; i--) {
      pre_text.innerText=text_t.slice(0,i);
      if (pre_text.clientHeight<pre_h) {
        pre_h=pre_text.clientHeight;
        y_rec.push(i);
      }
    }
    if (y_rec.length>0) {
      for (i=0; i<y_rec.length; i++) {
        text_list[y]=insert(text_t, y_rec[i], '\n');
      }
      tmp.innerText=text_list.join('\n')
    }
  }
  pre_text.innerText=tmp.innerText;
  text_list=pre_text.innerText.split('\n');
  pre_h=pre_text.clientHeight;
  while (pre_h>max_h) {
    text_list.splice(text_list.length-1, 1)
    pre_text.innerText=text_list.join('\n')
    pre_h=pre_text.clientHeight;
    if (pre_h<=max_h) {
      toast("자동 견적은 최대 "+max_h*2+"mm 까지 가능합니다!")
      tmp.innerText=text_list.join('\n')
      break;
    }
  }
}

document.fonts.ready.then(function () {
  preview_init();
  preview_update();
  toast("문구를 써보고\n제품을 미리 확인해보세요!")

  $('#preview_text').keyup(function(e) {
    sel=window.getSelection();
    range=sel.getRangeAt(0);
    x_size=sel.rangeLength;
    x_pos=range.startOffset;
    last_pos=range.endOffset;

    sel=window.getSelection();
    range=sel.getRangeAt(0);
    x_size=sel.rangeLength;
    x_pos=range.startOffset;
//      sel.setPosition(range.endContainer,19);
    preview_update();
  })
  $('#preview_text').keydown(function(e) {
//    console.log(e.keyCode)
      x_pos=window.getSelection().getRangeAt(0).startOffset;
      last_pos=window.getSelection().getRangeAt(0).endContainer.length;
      end_pos=window.getSelection().getRangeAt(0).endOffset;
      last_pos1=window.getSelection().getRangeAt(0).startContainer.length;
      y_height=this.clientHeight;
      y_width=this.clientWidth;
      y_left=this.clientLeft;
      y_top=this.clientTop;

      // tmp=document.getElementById("preview_text");
      // document.getElementById('pre_text3').innerText=(tmp.innerText);
      // document.getElementById('pre_text4').innerText=(tmp.innerHTML);
      // document.getElementById('pre_text5').innerText=($(tmp).html());
      // document.getElementById('pre_text6').innerText=($(tmp).text());

      if (e.keyCode === 13 && (last_pos==undefined || x_pos!=last_pos)) {
          // insert 2 br tags (if only one br tag is inserted the cursor won't go to the next line)
          document.execCommand('insertHTML', false, '<br/>');
          // prevent the default behaviour of return key pressed
          return false;
      }
      preview_update();
  });
});

function insert(str, index, value) {
    return str.substring(0, index) + value + str.substring(index);
}

function toast(string) {
    const toast = document.getElementById("toast");

    toast.classList.contains("reveal") ?
        (clearTimeout(removeToast), removeToast = setTimeout(function () {
            document.getElementById("toast").classList.remove("reveal")
        }, 1000)) :
        removeToast = setTimeout(function () {
            document.getElementById("toast").classList.remove("reveal")
        }, 1000)
    toast.classList.add("reveal"),
        toast.innerText = string
}

function showTextFile() {
  input = document.getElementById('ssa');

  const selectedFiles = input.files;
  const list = document.createElement('ul');
  tmp=""
  for(const file of selectedFiles) {
    tmp=tmp+"/"+file.webkitRelativePath.split("/")[1]
  }
  console.log(tmp)
}

function copyIt(title,bID) {
  copied=document.getElementById(bID);
  copyText=document.getElementById(bID).innerText.trim();
  if (window.clipboardData) {
    window.clipboardData.setData("Text", copyText);
  } else {
    tmp = document.createElement('input');
    copied.appendChild(tmp);
    tmp.value=copyText;
    tmp.select();
    document.execCommand("copy");
    tmp.remove();
  }
  toast(title+" 복사했습니다!\n> " + copyText)
}

function paste_value(e){
  document.execCommand('insertHTML', false, event.clipboardData.getData('Text').replace(/(\n|\r\n)/g, ''));
  event.preventDefault();
}

function first_enter(){
  tmp=document.getElementById("preview_text")
  if (tmp.spellcheck) {
    tmp.spellcheck=false
    tmp.innerText=""
  } else if (tmp.innerText.trim()=="") {
    tmp.spellcheck=true
  }
}

function select_prev() {
  tmp=$('#back_dr').children();
  tmp2=$('#back_img');
  flag=false;
  $(tmp.get().reverse()).each(function (index) {
    if(flag) {
      tmp2.data("value",$(this).data("value"));
      tmp2.data("select",$(this).text());
      tmp2.text($(this).text());
      select_clicked(tmp2,this);
      return false;
    }
    if ($(this).text()==$(tmp2).text()) {
      flag=true;
      if(index==tmp.length-1){
        tmp2.data("value",tmp.last().data("value"));
        tmp2.data("select",tmp.last().text());
        tmp2.text(tmp.last().text());
        select_clicked(tmp2,tmp.last());
      }
    }
  })
}

function select_next() {
  tmp=$('#back_dr').children();
  tmp2=$('#back_img');
  flag=false;
  tmp.each(function (index) {
    if(flag) {
      tmp2.data("value",$(this).data("value"));
      tmp2.data("select",$(this).text());
      tmp2.text($(this).text());
      select_clicked(tmp2,this);
      return false;
    }
    if ($(this).text()==$(tmp2).text()) {
      flag=true;
      if(index==tmp.length-1){
        tmp2.data("value",tmp.first().data("value"));
        tmp2.data("select",tmp.first().text());
        tmp2.text(tmp.first().text());
        select_clicked(tmp2,tmp.first());
      }
    }
  })
}

function select_itm(t,e) {
  $(t).data("value",$(e).data("value"));
  $(t).data("select",$(e).text());
  $(t).text($(e).text());
  select_clicked(t,e);
}

function select_clicked(t,e){
  if ($(e).attr("class")==undefined||$(e).attr("class").indexOf("clicked")<1) {
     $(e).addClass("clicked")
   }
   tmp=$(e).siblings(":not([style*='display: none'])")
   tmp.each(function () {
     if ($(this).attr("class")!=undefined&&$(this).attr('class').indexOf("clicked")>-1) {
       $(this).removeClass('clicked')
     }
   });
}

function change_light(e) {
  if ($(e).text().indexOf("OFF")<0) {
    $(e).text('조명 OFF');
  } else {
    $(e).text('조명 ON');
  }
}

function change_font(wh,e) {
  f_wh=wh;
  if ($(e).attr("class")==undefined||$(e).attr("class").indexOf("clicked")<1) {
    $(e).addClass("clicked")
  }
  tmp=$(e).siblings()
  tmp.each(function () {
    if ($(this).attr('class').indexOf("clicked")>-1) {
      $(this).removeClass('clicked')
    }
  });

  tmp=$("#font_list")
  tmp.siblings("a").each(function () {
    if ($(this).data("value").indexOf(wh)==0) {
      $(this).show()
    } else {
      $(this).hide()
    }
  });

  w=tmp.parent().width();
  h=$("#font_dummy").height();
  padding=5
  tmp.css("padding",padding)
  tmp.width(w-padding*2)
  tmp.height(h-padding*2)

  trg=tmp.siblings("a:visible");
  if(trg.length>0) {
    if (!trg.hasClass('clicked')) {
      select_itm('#pro_font',trg.first());
      console.log("dd")
    } else {
      trg=tmp.siblings("a.clicked:visible");
      select_itm('#pro_font',trg.first());
      console.log("ddee")
    }
  }
}

function align_change(){
  aaadfb = document.getElementById('pro_aaa').value;
  tmp=document.getElementById('preview_text')
  $(tmp).css("white-space",aaadfb)
  console.log("--------------------"+aaadfb);
  console.log(tmp.innerText.split("\n"));
  console.log(tmp.innerText);
  console.log(tmp.innerHTML);
  console.log($(tmp).html());
  console.log($(tmp).text());
}

function align2_change(){
  aaadfb = document.getElementById('pro_bbb').value;
  tmp=document.getElementById('preview_text')
  $(tmp).css("word-wrap",aaadfb)
  console.log("--------------------"+aaadfb);
  console.log(tmp.innerText);
  for (var i = 0; i < tmp.innerText.length; i++) {
    console.log(tmp.innerText.charAt(i));
  }
  console.log(tmp.innerHTML);
  console.log($(tmp).html());
  console.log($(tmp).text());
}

function font_resize(){
  sel_size = $("#pro_size");
  f_s = sel_size.data("value")
  f_h = f_s*5
  $("#pre_text").children("p").each(function () {
    $(this).css('font-size',f_h+"px");
    $(this).text($('#preview_text').text());

    bb=$(this).height();
    tmp_scale=f_h/bb;

    $(this).data("scale",tmp_scale)
    $(this).css('font-size',f_h*tmp_scale+"px");

    sub=$("#sub"+$(this).attr('id'));
    sub.css('font-size',f_h*tmp_scale+"px");
  });
}

function preview_init(){
  f_wh='A'; f_scale=1;

  pro_w = document.getElementById('pro_wh').value;
document.getElementById('pro_aaa')
  pro_list=$('.for')
  pro_list.each(function () {
    if ($(this).attr('class').indexOf("hidden")<0) {
      $(this).addClass("hidden")
    }
    tmp=$(this).attr('class').split(" ");
    for (step = 0; step < tmp.length; step++) {
      if (tmp[step].indexOf(pro_w)>-1 && $(this).attr('class').indexOf("hidden")>-1) {
        $(this).removeClass("hidden")
        break;
      }
    };
  });

  f_list=$('.dropdown > .dropbtn > span')
  f_list.each(function () {
    init=$(this).text()
    m_h=$(this).parent().height();
    m_w=$(this).parent().width();
    tmp=$(this).parent().siblings('.dropdown-content').children('a');
    for (i = 0; i < tmp.length; i++) {
      if (tmp[i].innerText==$(this).data("select") && ($(tmp[i]).attr("class")==undefined||$(tmp[i]).attr("class").indexOf("clicked")<1)) {
        $(tmp[i]).addClass("clicked")
      }
      $(this).text(tmp[i].innerText);
      if(m_h<$(this).parent().height()) {        m_h=$(this).parent().height();      }
      if(m_w<$(this).parent().width()) {        m_w=$(this).parent().width();      }
    }
    $(this).text(init);
    $(this).parent().height(m_h);
    $(this).parent().width(m_w);
  });


  aa = document.getElementById('back_dr');
  if($(aa).children().length==0) {
    element=back_optin_list.split("/")[0];
    bb = document.getElementById('back_img');
    bb.innerText=element.split(".")[0];
    bb.setAttribute("data-value",element);
    bb.setAttribute("data-select",element.split(".")[0]);
    for (const element of back_optin_list.split("/")) {
      tmp = document.createElement('img');
      tmp.src="static/background/"+element;
      pre_img = document.getElementById('pre_img');
      pre_img.appendChild(tmp);

      aac = document.createElement('a');
      aac.innerText=element.split(".")[0];
      aac.setAttribute("class","dropbtn");
      aac.setAttribute("style","float:left;background-image:url('static/background/"+element+"');width:48px;height:30px;font-size:0px;");
      aac.setAttribute("data-value",element);
      aac.setAttribute("onclick","select_itm(back_img,this);preview_update()");
      aa.appendChild(aac);
    }
    pre1 = document.getElementById('pre_text');
    for (const element of font_list.split("/")) {
      opt = document.createElement('p');
      opt.id = "font"+element;
      opt.style = "font-family:"+element+";font-size:20px;height:auto;width:fit-content;margin:0;";
      opt.innerText = element+":ㄱ가간agfG";
      opt.setAttribute("data-scale",1);
      pre1.appendChild(opt);
    }
  }
}

function preview_update(){
  tmp=document.getElementById("preview_text")
  if (tmp.spellcheck) {
    if(f_wh=="A") {
      tmp.innerHTML="여기에<br>써보세요"
    } else if (f_wh=="B") {
      tmp.innerHTML="WRITE<br>HERE"
    } else if (f_wh=="C") {
      tmp.innerHTML="ここで<br>書いてみましょう"
    } else if (f_wh=="D") {
      tmp.innerHTML="这里<br>尝试一下"
    }
    font_resize();
  }

  pre_width=document.getElementById("pro_back").width
  pre_height=document.getElementById("pro_back").height
  sel_text_list = document.getElementById("preview_list")
  sel_text = tmp.innerText
  sel_HTML = tmp.innerHTML

  sel_clr = $("#pro_color");
  sel_font = $("#pro_font");
  sel_size = $("#pro_size");
  sel_back = $('#back_img');
  sel_align = $('#pro_align');
  sel_deco = $('#side_deco');
  sel_main_LED = $("#pro_color_LED");

  t_clr = sel_clr.data("select")
  t_main_LED = sel_main_LED.data("select")
  t_side_LED = $("#side_color_on").data("select");
  t_side_back = $("#side_color_off").data("select");
  t_font = sel_font.data("select")
  t_size = sel_size.data("select")
  t_align = sel_align.data("select")
  t_deco = sel_deco.data("select")

  f_b = sel_back.data("value")
  f_w = sel_font.data("value")
  f_s = sel_size.data("value")
  f_h = f_s*5
  f_align = sel_align.data("value")
  f_deco = sel_deco.data("value");

  if (f_s<8) {    back_scale=1.4
  } else if (f_s<15) {  back_scale=1.2
  } else {    back_scale=1  }

  f_scale=$("#font"+f_w).data("scale")
  font_size=(f_h*f_scale*back_scale)

  max_w = maxWH[pro_w][0]*back_scale/2
  max_h = maxWH[pro_w][1]*back_scale/2
  pre_test = document.getElementById('pre_text2');
  pre_test.style="width:fit-content;height:fit-content;font-family:"+f_w+";font-size:"+font_size+"px;text-align:"+f_align+";"
                +"word-wrap:break-word;max-width:"+max_w+"px;"// +"max-height:"+max_h+"px;"
  cut_line();
  sel_text = tmp.innerText
  sel_HTML = tmp.innerHTML

  f_light = $("#pro_light").text().indexOf("OFF")>0
  f_main_LED = $("#pro_color_LED").data("value")
  f_side_LED = $("#side_color_on").data("value");
  f_side_back = $("#side_color_off").data("value");

  if (f_side_LED =="none") {
    f_side = false
  } else {
    f_side = true
  }

  tmp=$("#side_color_on").parent().siblings().find('a')
  tmp.each(function () {
    $(this).show()
  });
  if (f_main_LED!="ffffff") {
    if (f_side_LED!="none"&&f_side_LED!="ffffff"&&f_side_LED!=f_main_LED){
      $("#side_color_on").data("value",f_main_LED);
      $("#side_color_on").data("select",t_main_LED);
      $("#side_color_on").text(t_main_LED);
      f_side_LED = $("#side_color_on").data("value");
    }
    tmp.each(function () {
      item=$(this).data("value");
      if (item!="none"&&item!="ffffff"&&item!=f_main_LED) {
        $(this).hide()
      } else {
        $(this).show()
      }
    });
  }

  if (pro_w=="a") {
    f_thi = 2
  } else if (pro_w="b") {
    f_thi = 10
  } else if (pro_w="c") {

  }
  f_cnt = 20

  if(f_light) {
    pre_back="background: linear-gradient(to top, rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.25)), url('static/background/"+f_b+"');"
      +"background-size:"+pre_width*back_scale+"px "+pre_height*back_scale+"px;background-position-y:center;text-align:end;margin:0 auto;transition-duration:2s;"
  } else {
    pre_back="background:url('static/background/"+f_b+"');"
      +"background-size:"+pre_width*back_scale+"px "+pre_height*back_scale+"px;background-position-y:center;text-align:end;margin:0 auto;transition-duration:2s;"
    f_main_LED="ffffff"
  }
  document.getElementById("pro_back").style=pre_back

  if (pro_w=="a") {
    arr_clr = sel_clr.data("value").split(",")
  } else if (pro_w="b") {
    if (f_side) {
      arr_clr=[f_main_LED,f_side_LED,f_side_back]
    } else {
      arr_clr=[f_main_LED,f_side_back,f_side_back]
    }
  } else if (pro_w="c") {

  }
  taper=0
  for (step = 0; step <= f_cnt; step++) {
    pre_style="";f_shwd="";

    if(step==0) {
      tmp=document.getElementById("preview_text")
      f_clr=arr_clr[0]
      if (pro_w=="a") {
        pre_style="background:radial-gradient(farthest-corner at 40% -5%, #"+arr_clr[0]+" 3%, #"+arr_clr[1]+" 5%, #"+arr_clr[2]+" 35%, #"
                  +arr_clr[2]+" 65%, #"+arr_clr[1]+" 99%, #"+arr_clr[0]+" 1000%);"
          +"-webkit-background-clip:text;"
          +"-webkit-text-fill-color:transparent;"
        } else if (pro_w="b") {
          f_shwd="text-shadow:0.5px 0.5px gray"
          if (f_light) {
            f_shwd=f_shwd+",0px 0px 5px #"+f_clr
          }
          f_shwd=f_shwd+";"
        }
    } else {
      tmpid="side"+(step);
      tmp=document.getElementById(tmpid)
      if(!tmp) {
        tmp = document.createElement('div');
        tmp.id=tmpid
        tmp.className="drcnt preview_3d_text";
        sel_text_list.appendChild(tmp);
      }
      tmp.innerText=sel_text;
      if (pro_w=="a") {
        if (step==1) {
          f_clr=arr_clr[1]
        } else {
          f_clr=arr_clr[2]
        }
      } else if (pro_w="b") {
        if (step<=(f_cnt*15/20)) {
          taper=taper+(1/3)
        }

        f_shwd="text-shadow:"
        if (step<=(f_cnt*7/20) || (f_cnt*15/20)<=step ) {
          f_clr=arr_clr[2]
        } else {
          f_clr=arr_clr[1]
          if (f_light&&f_side_LED!="none") {
            f_clr=arr_clr[0]
            if(f_main_LED=="ffffff") {
              f_clr=arr_clr[1]
            }
            f_shwd=f_shwd+"0px 0px "+taper+5+"px #"+f_clr+","
          }
        }
        for (t_v = -taper; t_v<=taper; t_v=t_v+0.1) {
          f_shwd=f_shwd+t_v+"px "+taper+"px #"+f_clr+","
                        +t_v+"px "+-taper+"px #"+f_clr+","
                        +taper+"px "+t_v+"px #"+f_clr+","
                        +-taper+"px "+t_v+"px #"+f_clr+","
        }
        f_shwd=f_shwd+taper+"px "+taper+"px red;"
      }
    }
//6 10 35 60
    if (step == f_cnt) {
      f_shwd="text-shadow:"+
        f_thi/4+"px "+0.5*f_thi/4+"px "+f_thi*1.1+"px rgba(16,16,16,0.4),"+
        f_thi*2/4+"px "+0.5*f_thi*2/4+"px "+f_thi*1.2+"px rgba(16,16,16,0.2),"+
        f_thi*3/4+"px "+0.5*f_thi*3/4+"px "+f_thi*1.4+"px rgba(16,16,16,0.2),"+
        f_thi*4/4+"px "+0.5*f_thi*4/4+"px "+f_thi*2+"px rgba(16,16,16,0.4);"
    }
    pre_style=pre_style+"width:fit-content;height:fit-content;min-width:"+f_h+"px;min-height:"+f_h+"px;"
      +""+f_shwd+"color:#"+ f_clr +";font-family:"+f_w+";font-size:"+font_size+"px;text-align:"+f_align+";"
      +"z-index:"+(f_cnt-step)+";left:"+(pre_width/2+step*0.5*f_thi/f_cnt)+"px;top:"+(pre_height/2+step*f_thi/f_cnt)+"px;position:absolute;"
      +"word-wrap:break-word;max-height:"+max_h+"px;max-width:"+max_w+"px;"
    if (f_deco=="underL") {
      pre_style=pre_style+"text-decoration: underline;"
    } else if (f_deco=="borderL") {
      pre_style=pre_style+"border-style:solid;border-width:"+(f_h/6+taper)+"px;border-radius:"+f_h/6+"px;border-color:#"+f_clr+";"
    }
    tmp.style=pre_style;
  }

/*외부 수정 가능하게*/
  price_total = 0

  check_num = /[0-9]/;
  check_eng = /[a-zA-Z]/;
  check_spc = /[~!@#$%^&*()_+|<>?:{}]/;
  check_kor = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;
  check_n = /\n/;
  check_s = /\s/;

  o_cnt=0;e_cnt=0;k_cnt=0;f_cnt=0;
  n_cnt=0;s_cnt=0;
  for (i = 0; i < sel_text.length; i++) {
    tmp=sel_text.charAt(i)
    tmp_price=0
    if (check_kor.test(tmp)){
      k_cnt=k_cnt+1
      tmp_price=price_KE[t_size]
    } else if (check_eng.test(tmp)){
      e_cnt=e_cnt+1
      tmp_price=price_KE[t_size]
    } else if (check_n.test(tmp)) {
      n_cnt=n_cnt+1
      tmp_price=price_KE[t_size]
    } else if (check_s.test(tmp)) {
      s_cnt=s_cnt+1
      if (s_cnt%3==0) {
        tmp_price=price_KE[t_size]
      }
    } else if (check_num.test(tmp) || check_spc.test(tmp) || tmp.trim()!=""){
      o_cnt=o_cnt+1
      tmp_price=price_ETC[t_size]
    }

    if (t_clr.search("미러")>-1) {
      if (tmp_price<=2000) {
        tmp_price=tmp_price+200
      } else if (tmp_price<5000) {
        tmp_price=tmp_price+300
      } else if (tmp_price<8000) {
        tmp_price=tmp_price+400
      } else {
        tmp_price=tmp_price+500
      }
    }
    price_total=price_total+tmp_price
  }
  if (price_total%1200!=0) {
    price_total=price_total+(1200-price_total%1200)
  }
  if(pro_w=="a") {
    t_clr_slt=t_clr.split(" ")[0]
  } else if (pro_w=="b") {
    t_clr_slt=t_main_LED[0]+t_side_LED[0]+t_side_back[0]
  } else if (pro_w=="c") {
    t_clr_slt=t_clr
  }
  document.getElementById("btext").innerText=sel_text.replace(/(\n|\r\n)/g, '؊')
  document.getElementById("boption").innerText=t_clr_slt+"/" +f_w+"/" +t_size+"/"+t_align+"/"+t_deco
  document.getElementById("btotal").innerText=price_total.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
  document.getElementById("bcount").innerText=price_total/1200
}
