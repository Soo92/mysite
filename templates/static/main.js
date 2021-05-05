let removeToast;
back_optin_list="회벽, 마루.jpg/청색 대리석.jpg/갈색톤.jpg/검은색 목재.jpg/밝은 나무.jpg/밝은 벽돌 콘크리트.jpg/밝은 콘크리트.jpg/밝은 회색, 마루.jpg/분홍 벽지.jpg/블루 원단.jpg/살구벽지,마루.jpg/살색 원단.jpg/어두운 콘크리트.jpg/자홍색벽지.jpg/청색벽, 소나무 원목.jpg/한지 텍스쳐.jpg/흰벽,밝은마루.jpg/흰벽지,마루.jpg/흰색 나무결(2).jpg/흰색 나무결.jpg"
font_list="A01/A02/A03/A04/A05/A06/A07/A08/A09/A10/B01/B02/B03/B04/B05/B06/B07/B08/B09/B10"


function createRange(node, chars, range) {
    if (!range) {
        range = document.createRange()
        range.selectNode(node);
        range.setStart(node, 0);
    }
    if (chars.count === 0) {
        range.setEnd(node, chars.count);
    } else if (node && chars.count >0) {
        if (node.nodeType === Node.TEXT_NODE) {
            if (node.textContent.length < chars.count) {
                chars.count -= node.textContent.length;
            } else {
                 range.setEnd(node, chars.count);
                 chars.count = 0;
            }
        } else {
            for (var lp = 0; lp < node.childNodes.length; lp++) {
                range = createRange(node.childNodes[lp], chars, range);

                if (chars.count === 0) {
                   break;
                }
            }
        }
   }
   return range;
}

function setCurrentCursorPosition(chars) {
    if (chars >= 0) {
        var selection = window.getSelection();
        range = createRange(document.getElementById("preview_text").parentNode, { count: chars });
        if (range) {
            range.collapse(false);
            selection.removeAllRanges();
            selection.addRange(range);
        }
    }
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
  var input = document.getElementById('ssa');

  const selectedFiles = input.files;
  const list = document.createElement('ul');
  tmp=""
  for(const file of selectedFiles) {
    tmp=tmp+"/"+file.webkitRelativePath.split("/")[1]
  }
}

function copyIt(bID) {
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
  toast("복사됨!")
}

function paste_value(e){
  document.execCommand('insertHTML', false, event.clipboardData.getData('Text'));
  event.preventDefault();
}

function first_enter(){
  tmp=document.getElementById("preview_text")
  if (tmp.spellcheck) {
    tmp.spellcheck=false
    tmp.innerText=""
  } else if (tmp.innerText.trim()=="") {
    tmp.spellcheck=true
    tmp.innerHTML="여기에<br>써보세요"
  }
}


function preview_update(){
  pro_w = document.getElementById('pro_wh').value;

  select = document.getElementById('back_option');
  if(select.length<1) {
    for (const element of back_optin_list.split("/")) {
      var opt = document.createElement('option');
      opt.value = element;
      opt.innerHTML = element.split(".")[0];
      select.appendChild(opt);
      var tmp = document.createElement('img');
      tmp.src="static/background/"+element;
      pre_img = document.getElementById('pre_img');
      pre_img.appendChild(tmp);
    }
    pre_text = document.getElementById('pre_text');
    for (const element of font_list.split("/")) {
      var opt = document.createElement('p');
      opt.style = "font-family:"+element+";font-size:20px;height:auto;margin:0 auto;";
      opt.innerText = element+":ㄱ가간agfG";
      opt.id = "font"+element
      pre_text.appendChild(opt);
    }
  }

  pre_width=document.getElementById("pro_back").width
  pre_height=document.getElementById("pro_back").height

  var sel_text_list = document.getElementById("preview_list")
  var sel_text = document.getElementById("preview_text").innerText
  var sel_HTML = document.getElementById("preview_text").innerHTML
  if (sel_text.length>20) {
    toast("20자씩 나눠서 입력해 주세요")
    sel_text=sel_text.slice(0,20)
    document.getElementById("preview_text").innerText=sel_text
    console.log(setCurrentCursorPosition())
    setCurrentCursorPosition(20)
  }
  if (sel_text.indexOf("؊")>-1) {
    toast("사용할 수 없는 문자입니다")
    sel_text=sel_text.replace("؊","")
    document.getElementById("preview_text").innerText=sel_text
  }
  if (sel_text.search(/\n{3}/)>-1) {
    toast("줄바꿈은 한번만 가능합니다!")
    sel_text=sel_text.replace(/\n{3}/, "\n\n");
    document.getElementById("preview_text").innerText=sel_text
  }
  if (sel_text.search(/\n{2}/)==0) {
    toast("줄바꿈은 한번만 가능합니다")
    sel_text=sel_text.replace(/\n{2}/, "\n");
    document.getElementById("preview_text").innerText=sel_text
  }

  var sel_clr = document.getElementById("pro_color");
  var sel_font = document.getElementById("pro_font");
  var sel_size = document.getElementById("pro_size");
  var sel_back = document.getElementById('back_option');
  var sel_align = document.getElementById('pro_align');
  var sel_deco = document.getElementById('side_deco');

  var t_clr = sel_clr.options[sel_clr.selectedIndex].text
  var t_font = sel_font.options[sel_font.selectedIndex].text
  var t_size = sel_size.options[sel_size.selectedIndex].text
  var t_align = sel_align.options[sel_align.selectedIndex].text

  var f_w = sel_font.value
  var f_h = sel_size.value
  var f_align = sel_align.value
  var f_deco = sel_deco.value;
  if (pro_w=="a") {
    var f_thi = 2
  } else if (pro_w="b") {
    var f_thi = 10
  } else if (pro_w="c") {

  }
  var f_cnt = 20

  var max_w = 450
  var max_h = 400

  if (sel_size.value<50) {    back_scale=1.4
  } else {    back_scale=1  }

  f_scale=1
  tmp=document.getElementById("font"+f_w);
//  tmp.innerText=sel_text.replace(/(\n|\r\n)/g, '');
  aa=tmp.style.fontSize;  bb=tmp.clientHeight;
  f_scale=parseInt(aa)/bb

  document.getElementById("pro_back").style="background-image:url('static/background/"+sel_back.value+"');"
    +"background-size:"+pre_width*back_scale+"px "+pre_height*back_scale+"px;background-position-y:center;text-align:end;margin:0 auto;"

  if (pro_w=="a") {
    arr_clr = sel_clr.value.split(",")
  } else if (pro_w="b") {
    arr_clr=[document.getElementById("pro_color_LED").value,document.getElementById("side_color_on").value,document.getElementById("side_color_off").value]
  } else if (pro_w="c") {

  }
  taper=0
  for (step = 0; step <= f_cnt; step++) {
    pre_style="";f_shwd="";

    if(step==0) {
      f_clr=arr_clr[0]
      tmp=document.getElementById("preview_text")
      if (pro_w=="a") {
        pre_style="background:radial-gradient(farthest-corner at 40% -5%, #"+arr_clr[0]+" 3%, #"+arr_clr[1]+" 5%, #"+arr_clr[2]+" 35%, #"
                  +arr_clr[2]+" 65%, #"+arr_clr[1]+" 99%, #"+arr_clr[0]+" 1000%);"
          +"-webkit-background-clip:text;"
          +"-webkit-text-fill-color:transparent;"
        } else if (pro_w="b") {
          f_shwd="text-shadow:0.5px 0.5px #D9D9D9;"
        }
    } else {
      if (pro_w=="a") {
        if (step==1) {
          f_clr=arr_clr[1]
        } else {
          f_clr=arr_clr[2]
        }
      } else if (pro_w="b") {
        if (step<=(f_cnt*7/20) || (f_cnt*15/20)<=step ) {
          f_clr=arr_clr[2]
        } else {
          f_clr=arr_clr[1]
        }
        if (step<=(f_cnt*15/20)) {
          taper=taper+(1/3)
          // /*f_h/100
        }
        console.log(taper)
        console.log(f_h)
        f_shwd="text-shadow:"
        for (t_v = -taper; t_v<=taper; t_v=t_v+0.1) {
          f_shwd=f_shwd+t_v+"px "+taper+"px #"+f_clr+","
                        +t_v+"px "+-taper+"px #"+f_clr+","
                        +taper+"px "+t_v+"px #"+f_clr+","
                        +-taper+"px "+t_v+"px #"+f_clr
          if(t_v+0.05>=taper) {
            f_shwd=f_shwd+";"
          } else {
            f_shwd=f_shwd+","
          }
        }
      }
      tmpid="side"+(step);
      tmp=document.getElementById(tmpid)
      if(!tmp) {
        tmp = document.createElement('div');
        tmp.id=tmpid
        tmp.className="drcnt preview_3d_text";
        sel_text_list.appendChild(tmp);
      }
      tmp.innerText=sel_text;
    }
//6 10 35 60
    if (step == f_cnt) {
      f_shwd="text-shadow:"+
        f_thi/4+"px "+0.5*f_thi/4+"px "+f_thi*1.1+"px rgba(16,16,16,0.4),"+
        f_thi*2/4+"px "+0.5*f_thi*2/4+"px "+f_thi*1.2+"px rgba(16,16,16,0.2),"+
        f_thi*3/4+"px "+0.5*f_thi*3/4+"px "+f_thi*1.4+"px rgba(16,16,16,0.2),"+
        f_thi*4/4+"px "+0.5*f_thi*4/4+"px "+f_thi*2+"px rgba(16,16,16,0.4);"
    }
    pre_style=pre_style+"width:fit-content;min-width:"+f_h+"px;min-height:"+f_h+"px;max-width:"+max_w+"px;max-height:"+max_h+"px;"
      +""+f_shwd+"color:#"+ f_clr +";font-family:"+f_w+";font-size:"+(f_h*f_scale*back_scale)+"px;text-align:"+f_align+";"
      +"z-index:"+(f_cnt-step)+";left:"+(pre_width/2+step*0.5*f_thi/f_cnt)+"px;top:"+(pre_height/2+step*f_thi/f_cnt)+"px;word-wrap:break-word;"
    if (f_deco=="underL") {
      pre_style=pre_style+"border-bottom:solid;border-width:"+(f_h/6+taper)+"px;border-radius:"+f_h/6+"px;border-color:#"+f_clr+";"
    } else if (f_deco=="borderL") {
      pre_style=pre_style+"border-style:solid;border-width:"+(f_h/6+taper)+"px;border-radius:"+f_h/6+"px;border-color:#"+f_clr+";"
    }
    tmp.style=pre_style;
  }

/*외부 수정 가능하게*/
  var price_total = 0
  var price_KE ={}
  price_KE["4cm"]=1200
  price_KE["5cm"]=1500
  price_KE["6cm"]=2000
  price_KE["8cm"]=3500
  price_KE["10cm"]=4500
  price_KE["15cm"]=7000
  price_KE["20cm"]=9500
  var price_ETC ={}
  price_ETC["4cm"]=2000
  price_ETC["5cm"]=2200
  price_ETC["6cm"]=3000
  price_ETC["8cm"]=4000
  price_ETC["10cm"]=5000
  price_ETC["15cm"]=8000
  price_ETC["20cm"]=10000

  var check_num = /[0-9]/;
  var check_eng = /[a-zA-Z]/;
  var check_spc = /[~!@#$%^&*()_+|<>?:{}]/;
  var check_kor = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;
  var check_n = /\n/;
  var check_s = /\s/;

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
  document.getElementById("btext").innerText=sel_text.replace(/(\n|\r\n)/g, '؊')
/*.replace(/(^\s*)|(\s*$)/gi, "؉").replace(/(\s*)/g, "")*/
  document.getElementById("boption").innerText=t_clr+"/" +sel_font.value+"/" +t_size+"/"+t_align
  document.getElementById("btotal").innerText=price_total.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
  document.getElementById("bcount").innerText=price_total/1200
}
