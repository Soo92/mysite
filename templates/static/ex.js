function textTo3D() {
  f_text=document.getElementById("preview_text").innerhtml
  f_size=20
  f_thi=20
  f_clr_main = "red"
  f_side_on = "blue"
  f_clr_side_on = "green"
  f_clr_side_off = "yellow"
  f_back = "#000000"

  x1=0
  x2=0
  y1=depth/3
  y2=depth*2/3

  for (step = 1; step <= f_thi; step++) {
    in_content=in_content+
    "<div id='preview_text' contenteditable='true' spellcheck='false'>여기에문구as</div>"
  }
  document.getElementById("pre_back").innerhtml=in_content

  document.getElementById("preview_text").style="text-shadow:"+f_shwd+"text-align:center;color:#"+
    f_clr +";font-family:"+f_w+";font-size:"+f_size+"px;font-weight:bold;"


}
