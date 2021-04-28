function preview_update()
{
  var f_clr = document.my_b.pro_color.value
  var f_side_on = document.my_b.side_on.checked
  var f_clr_side_on = document.my_b.side_color_on.value
  var f_clr_side_off = document.my_b.side_color_off.value
  var f_size = (60 + document.my_b.pro_size.value*1)
  var f_w = document.my_b.pro_font.value
  var f_thi = 20
  var f_shwd = "1px 1px "+(10+document.my_b.pro_size.value*1)+"px #" + f_clr
  var f_back = document.my_b.selected_back.value

  if(f_clr!="ffffff" & f_side_on) {
    document.my_b.side_color_on.hidden=f_side_on
  } else {
    document.my_b.side_color_on.hidden=!f_side_on
  }
  document.my_b.side_color_off.hidden=f_side_on

  for (step = 2; step <= f_thi; step++) {
    if (f_side_on) {
      if(step<f_thi/4 || step>f_thi*6/8 ) {
        tmp_clr =  "ffffff"
      } else {
        if (document.my_b.side_color_on.hidden) {
          tmp_clr =  f_clr
        } else {
          tmp_clr =  f_clr_side_on
        }
      }
    } else {
      tmp_clr = f_clr_side_off
    }
    if(step<f_thi*6/8 ) {
      st=-1*step
      fi=1*step
    } else {
      st=-f_thi*6/8
      fi=f_thi*6/8
    }
    for (step2=st; step2<=fi; step2=step2+0.1){
      f_shwd=f_shwd + ","+ step2 +"px " + step + "px 0px #" + tmp_clr
    }
  }
  f_shwd=f_shwd +
  ",0px " +(4 + step*1)+ "px 6px rgba(16,16,16,0.4),"+
  "0px " +(8 + step*1)+ "px 10px rgba(16,16,16,0.2),"+
  "0px " +(11 + step*1)+ "px 35px rgba(16,16,16,0.2),"+
  "0px " +(16 + step*1)+ "px 60px rgba(16,16,16,0.4);"

  document.getElementById("preview_text").style="text-shadow:"+f_shwd+"text-align:center;color:#"+ f_clr +";font-family:"+f_w+";font-size:"+f_size+"px;font-weight:bold;"
  if (f_back==0)  {
    document.getElementById("pro_back").style="background-color:#212529"
  } else if(f_back==1) {
    document.getElementById("pro_back").style="background-image:url('static/background/brick_wall.jpg')"
  } else if(f_back==2) {
    document.getElementById("pro_back").style="background-image:url('static/background/window1.jpg');background-size: 450px;background-repeat:no-repeat"
  } else if(f_back==3) {
    document.getElementById("pro_back").style="background-image:url('static/background/window2.jpg');background-size: 450px;background-repeat:no-repeat"
  }
}
