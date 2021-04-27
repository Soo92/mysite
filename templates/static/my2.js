function preview_update()
{
  var sel_text = document.getElementById("preview_text").innerText
  var sel_clr = document.getElementById("pro_color");
  var sel_font = document.getElementById("pro_font");
  var sel_size = document.getElementById("pro_size");

  var t_clr = sel_clr.options[sel_clr.selectedIndex].text
  var t_font = sel_font.options[sel_font.selectedIndex].text
  var t_size = sel_size.options[sel_size.selectedIndex].text

  var arr_clr = sel_clr.value.split(",")
  var f_clr = arr_clr[0]
  var f_w = sel_font.value
  var f_size = (60 + sel_size.value*2)
  var f_thi = 8
  var f_shwd = "1px 2px 0px #" + arr_clr[1]

  for (step = 2; step <= f_thi; step++) {
    f_shwd=f_shwd + ","+ step/2 +"px " + step + "px 0px #" +  arr_clr[2]
  }
  f_shwd=f_shwd +
  ","+f_thi/2+"px " +(4 + step*1)+ "px 6px rgba(16,16,16,0.4),"+
  f_thi/2+"px " +(8 + step*1)+ "px 10px rgba(16,16,16,0.2),"+
  f_thi/2+"px " +(11 + step*1)+ "px 35px rgba(16,16,16,0.2),"+
  f_thi/2+"px " +(16 + step*1)+ "px 60px rgba(16,16,16,0.4);"

  document.getElementById("preview_text").style="text-shadow:"+f_shwd+"text-align:center;color:#"+ f_clr +";font-family:"+f_w+";font-size:"+f_size+"px;font-weight:bold;"
  document.getElementById("pro_back").style="background-color:#868e96"
  document.getElementById("boption").innerText= sel_text+"/" +t_clr+"/" +t_font+"/" +t_size

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

  o_cnt=0;e_cnt=0;k_cnt=0;
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

    if (t_clr.search("미러")>0) {
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
  document.getElementById("btotal").innerText=price_total
  document.getElementById("bcount").innerText=price_total/1200
}
