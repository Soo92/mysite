
function showTextFile() {
  var input = document.getElementById('ssa');

  const selectedFiles = input.files;
  const list = document.createElement('ul');
  tmp=""
  for(const file of selectedFiles) {
    tmp=tmp+"/"+file.webkitRelativePath.split("/")[1]
  }
  console.log(tmp)
}

function preview_update()
{
  select = document.getElementById('back_option');
  if(select.length<1) {
    back_optin_list="회벽, 마루.jpg/청색 대리석.jpg/갈색톤.jpg/검은색 목재.jpg/밝은 나무.jpg/밝은 벽돌 콘크리트.jpg/밝은 콘크리트.jpg/밝은 회색, 마루.jpg/분홍 벽지.jpg/블루 원단.jpg/살구벽지,마루.jpg/살색 원단.jpg/어두운 콘크리트.jpg/자홍색벽지.jpg/청색벽, 소나무 원목.jpg/한지 텍스쳐.jpg/흰벽,밝은마루.jpg/흰벽지,마루.jpg/흰색 나무결(2).jpg/흰색 나무결.jpg"
    for (const element of back_optin_list.split("/")) {
      var opt = document.createElement('option');
      opt.value = element;
      opt.innerHTML = element.split(".")[0];
      select.appendChild(opt);
    }
  }

  var sel_text = document.getElementById("preview_text").innerText
  var text_cnt = sel_text.replace(/(^\s*)|(\s*$)/gi, "").replace(/(\s*)/g, "").length
  if (text_cnt>20) {
    toast("20자씩 나눠서 입력해 주세요")
    document.getElementById("preview_text").innerText=sel_text.slice(0,20)
  }
  var sel_clr = document.getElementById("pro_color");
  var sel_font = document.getElementById("pro_font");
  var sel_size = document.getElementById("pro_size");
  var sel_back = document.getElementById('back_option');

  var t_clr = sel_clr.options[sel_clr.selectedIndex].text
  var t_font = sel_font.options[sel_font.selectedIndex].text
  var t_size = sel_size.options[sel_size.selectedIndex].text

  var arr_clr = sel_clr.value.split(",")
  var f_clr = arr_clr[0]
  var f_w = sel_font.value
  var f_h = (sel_size.value*7)
  var f_thi = 5
  var f_shwd = "0.5px 1px 0px #" + arr_clr[1]

  for (step = 2; step <= f_thi; step++) {
    f_shwd=f_shwd + ","+ step/2 +"px " + step + "px 0px #" +  arr_clr[2]
  }
  f_shwd=f_shwd +
  ","+f_thi/2+"px " +(4 + step*1)+ "px 6px rgba(16,16,16,0.4),"+
  f_thi/2+"px " +(8 + step*1)+ "px 10px rgba(16,16,16,0.2),"+
  f_thi/2+"px " +(11 + step*1)+ "px 35px rgba(16,16,16,0.2),"+
  f_thi/2+"px " +(16 + step*1)+ "px 60px rgba(16,16,16,0.4);"

  f_scale=1
  tmzzp=document.getElementById("pre_text").children
  var i;
  for (i = 0; i < tmzzp.length; i++) {
    aa=tmzzp[i].style.fontSize
    bb=tmzzp[i].clientHeight
    if(tmzzp[i].style.fontFamily==f_w){
      f_scale=parseInt(aa)/bb
      console.log(f_scale)
      break
    }
  }

  pre_width="600"
  pre_height="400"
  if (sel_size.value<10) {
    back_scale=1.2
  } else {
    back_scale=1
  }

  pre_style="width:fit-content;min-width:"+f_h+"px;min-height:"+f_h+"px;max-width:"+pre_width+"px;max-height:"+pre_height+"px;"
    +"text-shadow:"+f_shwd+"color:#"+ f_clr +";font-family:"+f_w+";font-size:"+f_h*f_scale+"px;margin:0 auto;text-align:center;"
  if (document.getElementById("preview_text").clientHeight >= pre_height) {
    pre_style=pre_style+"overflow:auto;"
  }
  document.getElementById("preview_text").style=pre_style
  document.getElementById("pro_back").style="background-image:url('static/background/"+sel_back.value+"');background-color:#868e96;"
    +"background-size:"+pre_width*back_scale+"px "+pre_height*back_scale+"px;background-position-y:center;"

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

  o_cnt=0;e_cnt=0;k_cnt=0;f_cnt=0;
  for (i = 0; i < sel_text.length; i++) {
    tmp=sel_text.charAt(i)
    tmp_price=0
    if (check_kor.test(tmp)){
      k_cnt=k_cnt+1
      tmp_price=price_KE[t_size]
    } else if (check_eng.test(tmp)){
      e_cnt=e_cnt+1
      tmp_price=price_KE[t_size]
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
  document.getElementById("btext").innerText=sel_text.replace(/(^\s*)|(\s*$)/gi, "").replace(/(\s*)/g, "")
  document.getElementById("boption").innerText=t_clr+"/" +t_font+"/" +t_size
  document.getElementById("btotal").innerText=price_total
  document.getElementById("bcount").innerText=price_total/1200
}

let removeToast;

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
