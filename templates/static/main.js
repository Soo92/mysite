let removeToast;
back_optin_list="검은색 목재.jpg/청색 대리석.jpg/갈색톤.jpg/밝은 나무.jpg/밝은 벽돌.jpg/밝은 콘크리트.jpg/밝은 회색, 마루.jpg/분홍 벽지.jpg/블루 원단.jpg/살구벽지,마루.jpg/살색 원단.jpg/어두운 콘크리트.jpg/자홍색벽지.jpg/청색벽,소나무.jpg/한지 텍스쳐.jpg/흰벽,밝은마루.jpg/흰색 나무결.jpg/흰색 나무결2.jpg";
font_list="A01/A02/A03/A04/A05/A06/A07/A08/A09/A10/B01/B02/B03/B04/B05/B06/B07/B08/B09/B10/C01/C02/C03/C04/C05/C06/C07/D01/D02";

flag_font=false;
dbg_cnt=0;

price_arr={};

price_K={};	price_E={};	price_ETC={};	price_s={};	price_n={};	price_border={};	price_line={};	price_mirror={};	price_color={};
price_K['10cm']=35000;	price_E['10cm']=35000;	price_ETC['10cm']=45000;	price_s['10cm']=0;	price_n['10cm']=0;	price_border['10cm']=0;	price_line['10cm']=-5000;	price_mirror['10cm']=0;	price_color['10cm']=0;
price_K['20cm']=45000;	price_E['20cm']=45000;	price_ETC['20cm']=50000;	price_s['20cm']=0;	price_n['20cm']=0;	price_border['20cm']=0;	price_line['20cm']=-10000;	price_mirror['20cm']=0;	price_color['20cm']=0;
price_K['30cm']=50000;	price_E['30cm']=50000;	price_ETC['30cm']=60000;	price_s['30cm']=0;	price_n['30cm']=0;	price_border['30cm']=0;	price_line['30cm']=-10000;	price_mirror['30cm']=0;	price_color['30cm']=0;
price_arr['c']={price_K,price_E,price_ETC,price_s,price_n,price_border,price_line,price_mirror,price_color}

price_K={};	price_E={};	price_ETC={};	price_s={};	price_n={};	price_border={};	price_line={};	price_mirror={};	price_color={};
price_K['4cm']=400;	price_E['4cm']=400;	price_ETC['4cm']=800;	price_s['4cm']=400;	price_n['4cm']=400;	price_border['4cm']=0;	price_line['4cm']=0;	price_mirror['4cm']=0;	price_color['4cm']=0;
price_K['6cm']=500;	price_E['6cm']=500;	price_ETC['6cm']=1000;	price_s['6cm']=500;	price_n['6cm']=500;	price_border['6cm']=0;	price_line['6cm']=0;	price_mirror['6cm']=0;	price_color['6cm']=0;
price_K['8cm']=500;	price_E['8cm']=500;	price_ETC['8cm']=1000;	price_s['8cm']=500;	price_n['8cm']=500;	price_border['8cm']=0;	price_line['8cm']=0;	price_mirror['8cm']=0;	price_color['8cm']=0;
price_K['10cm']=700;	price_E['10cm']=700;	price_ETC['10cm']=1400;	price_s['10cm']=700;	price_n['10cm']=700;	price_border['10cm']=0;	price_line['10cm']=0;	price_mirror['10cm']=0;	price_color['10cm']=0;
price_K['15cm']=1000;	price_E['15cm']=1000;	price_ETC['15cm']=2000;	price_s['15cm']=1000;	price_n['15cm']=1000;	price_border['15cm']=0;	price_line['15cm']=0;	price_mirror['15cm']=0;	price_color['15cm']=0;
price_K['20cm']=1500;	price_E['20cm']=1500;	price_ETC['20cm']=3000;	price_s['20cm']=1500;	price_n['20cm']=1500;	price_border['20cm']=0;	price_line['20cm']=0;	price_mirror['20cm']=0;	price_color['20cm']=0;
price_arr['e']={price_K,price_E,price_ETC,price_s,price_n,price_border,price_line,price_mirror,price_color}

price_K={};	price_E={};	price_ETC={};	price_s={};	price_n={};	price_border={};	price_line={};	price_mirror={};	price_color={};
price_K['4cm']=1200;	price_E['4cm']=1200;	price_ETC['4cm']=2000;	price_s['4cm']=1200;	price_n['4cm']=1200;	price_border['4cm']=0;	price_line['4cm']=0;	price_mirror['4cm']=500;	price_color['4cm']=0;
price_K['5cm']=1500;	price_E['5cm']=1500;	price_ETC['5cm']=2200;	price_s['5cm']=1500;	price_n['5cm']=1500;	price_border['5cm']=0;	price_line['5cm']=0;	price_mirror['5cm']=500;	price_color['5cm']=0;
price_K['6cm']=2000;	price_E['6cm']=2000;	price_ETC['6cm']=3000;	price_s['6cm']=2000;	price_n['6cm']=2000;	price_border['6cm']=0;	price_line['6cm']=0;	price_mirror['6cm']=500;	price_color['6cm']=0;
price_K['8cm']=2500;	price_E['8cm']=2500;	price_ETC['8cm']=4000;	price_s['8cm']=2500;	price_n['8cm']=2500;	price_border['8cm']=0;	price_line['8cm']=0;	price_mirror['8cm']=500;	price_color['8cm']=0;
price_K['10cm']=3500;	price_E['10cm']=3500;	price_ETC['10cm']=5000;	price_s['10cm']=3500;	price_n['10cm']=3500;	price_border['10cm']=0;	price_line['10cm']=0;	price_mirror['10cm']=500;	price_color['10cm']=0;
price_K['15cm']=4500;	price_E['15cm']=4500;	price_ETC['15cm']=8000;	price_s['15cm']=4500;	price_n['15cm']=4500;	price_border['15cm']=0;	price_line['15cm']=0;	price_mirror['15cm']=1000;	price_color['15cm']=0;
price_K['20cm']=7000;	price_E['20cm']=7000;	price_ETC['20cm']=10000;	price_s['20cm']=7000;	price_n['20cm']=7000;	price_border['20cm']=0;	price_line['20cm']=0;	price_mirror['20cm']=1000;	price_color['20cm']=0;
price_arr['a3t']={price_K,price_E,price_ETC,price_s,price_n,price_border,price_line,price_mirror,price_color}

price_K={};	price_E={};	price_ETC={};	price_s={};	price_n={};	price_border={};	price_line={};	price_mirror={};	price_color={};
price_K['4cm']=2500;	price_E['4cm']=2500;	price_ETC['4cm']=3000;	price_s['4cm']=2500;	price_n['4cm']=2500;	price_border['4cm']=0;	price_line['4cm']=0;	price_mirror['4cm']=500;	price_color['4cm']=0;
price_K['5cm']=2500;	price_E['5cm']=2500;	price_ETC['5cm']=3500;	price_s['5cm']=2500;	price_n['5cm']=2500;	price_border['5cm']=0;	price_line['5cm']=0;	price_mirror['5cm']=500;	price_color['5cm']=0;
price_K['6cm']=3000;	price_E['6cm']=3000;	price_ETC['6cm']=5000;	price_s['6cm']=3000;	price_n['6cm']=3000;	price_border['6cm']=0;	price_line['6cm']=0;	price_mirror['6cm']=500;	price_color['6cm']=0;
price_K['8cm']=4000;	price_E['8cm']=4000;	price_ETC['8cm']=5500;	price_s['8cm']=4000;	price_n['8cm']=4000;	price_border['8cm']=0;	price_line['8cm']=0;	price_mirror['8cm']=500;	price_color['8cm']=0;
price_K['10cm']=4500;	price_E['10cm']=4500;	price_ETC['10cm']=6000;	price_s['10cm']=4500;	price_n['10cm']=4500;	price_border['10cm']=0;	price_line['10cm']=0;	price_mirror['10cm']=500;	price_color['10cm']=0;
price_K['15cm']=6500;	price_E['15cm']=6500;	price_ETC['15cm']=9500;	price_s['15cm']=6500;	price_n['15cm']=6500;	price_border['15cm']=0;	price_line['15cm']=0;	price_mirror['15cm']=1000;	price_color['15cm']=0;
price_K['20cm']=9000;	price_E['20cm']=9000;	price_ETC['20cm']=12000;	price_s['20cm']=9000;	price_n['20cm']=9000;	price_border['20cm']=0;	price_line['20cm']=0;	price_mirror['20cm']=1000;	price_color['20cm']=0;
price_arr['a5t']={price_K,price_E,price_ETC,price_s,price_n,price_border,price_line,price_mirror,price_color}

price_K={};	price_E={};	price_ETC={};	price_s={};	price_n={};	price_border={};	price_line={};	price_mirror={};	price_color={};
price_K['10cm']=30000;	price_E['10cm']=25000;	price_ETC['10cm']=30000;	price_s['10cm']=0;	price_n['10cm']=25000;	price_border['10cm']=25000;	price_line['10cm']='??';	price_mirror['10cm']='??';	price_color['10cm']=0;
price_K['15cm']=35000;	price_E['15cm']=30000;	price_ETC['15cm']=35000;	price_s['15cm']=0;	price_n['15cm']=30000;	price_border['15cm']=30000;	price_line['15cm']='??';	price_mirror['15cm']='??';	price_color['15cm']=0;
price_K['20cm']=45000;	price_E['20cm']=40000;	price_ETC['20cm']=45000;	price_s['20cm']=0;	price_n['20cm']=40000;	price_border['20cm']=40000;	price_line['20cm']='??';	price_mirror['20cm']='??';	price_color['20cm']=0;
price_arr['b']={price_K,price_E,price_ETC,price_s,price_n,price_border,price_line,price_mirror,price_color}

price_K={};	price_E={};	price_ETC={};	price_s={};	price_n={};	price_border={};	price_line={};	price_mirror={};	price_color={};
price_K['10cm']=4000;	price_E['10cm']=4000;	price_ETC['10cm']=5000;	price_s['10cm']=0;	price_n['10cm']=0;	price_border['10cm']=0;	price_line['10cm']=0;	price_mirror['10cm']=0;	price_color['10cm']=1000;
price_K['15cm']=4500;	price_E['15cm']=4500;	price_ETC['15cm']=5300;	price_s['15cm']=0;	price_n['15cm']=0;	price_border['15cm']=0;	price_line['15cm']=0;	price_mirror['15cm']=0;	price_color['15cm']=1000;
price_K['20cm']=4800;	price_E['20cm']=4800;	price_ETC['20cm']=5800;	price_s['20cm']=0;	price_n['20cm']=0;	price_border['20cm']=0;	price_line['20cm']=0;	price_mirror['20cm']=0;	price_color['20cm']=1000;
price_K['25cm']=5000;	price_E['25cm']=5000;	price_ETC['25cm']=5900;	price_s['25cm']=0;	price_n['25cm']=0;	price_border['25cm']=0;	price_line['25cm']=0;	price_mirror['25cm']=0;	price_color['25cm']=1000;
price_K['30cm']=5400;	price_E['30cm']=5400;	price_ETC['30cm']=6000;	price_s['30cm']=0;	price_n['30cm']=0;	price_border['30cm']=0;	price_line['30cm']=0;	price_mirror['30cm']=0;	price_color['30cm']=1000;
price_K['35cm']=8000;	price_E['35cm']=8000;	price_ETC['35cm']=8000;	price_s['35cm']=0;	price_n['35cm']=0;	price_border['35cm']=0;	price_line['35cm']=0;	price_mirror['35cm']=0;	price_color['35cm']=1500;
price_K['40cm']=8500;	price_E['40cm']=8500;	price_ETC['40cm']=11000;	price_s['40cm']=0;	price_n['40cm']=0;	price_border['40cm']=0;	price_line['40cm']=0;	price_mirror['40cm']=0;	price_color['40cm']=2000;
price_K['45cm']=11000;	price_E['45cm']=11000;	price_ETC['45cm']=13000;	price_s['45cm']=0;	price_n['45cm']=0;	price_border['45cm']=0;	price_line['45cm']=0;	price_mirror['45cm']=0;	price_color['45cm']=2000;
price_K['50cm']=15000;	price_E['50cm']=15000;	price_ETC['50cm']=18000;	price_s['50cm']=0;	price_n['50cm']=0;	price_border['50cm']=0;	price_line['50cm']=0;	price_mirror['50cm']=0;	price_color['50cm']=2000;
price_arr['d10t']={price_K,price_E,price_ETC,price_s,price_n,price_border,price_line,price_mirror,price_color}

price_K={};	price_E={};	price_ETC={};	price_s={};	price_n={};	price_border={};	price_line={};	price_mirror={};	price_color={};
price_K['20cm']=5000;	price_E['20cm']=5000;	price_ETC['20cm']=5800;	price_s['20cm']=0;	price_n['20cm']=0;	price_border['20cm']=0;	price_line['20cm']=0;	price_mirror['20cm']=0;	price_color['20cm']=1000;
price_K['25cm']=6000;	price_E['25cm']=6000;	price_ETC['25cm']=6200;	price_s['25cm']=0;	price_n['25cm']=0;	price_border['25cm']=0;	price_line['25cm']=0;	price_mirror['25cm']=0;	price_color['25cm']=1000;
price_K['30cm']=7000;	price_E['30cm']=7000;	price_ETC['30cm']=6800;	price_s['30cm']=0;	price_n['30cm']=0;	price_border['30cm']=0;	price_line['30cm']=0;	price_mirror['30cm']=0;	price_color['30cm']=1000;
price_K['35cm']=8000;	price_E['35cm']=8000;	price_ETC['35cm']=8500;	price_s['35cm']=0;	price_n['35cm']=0;	price_border['35cm']=0;	price_line['35cm']=0;	price_mirror['35cm']=0;	price_color['35cm']=1500;
price_K['40cm']=11000;	price_E['40cm']=11000;	price_ETC['40cm']=11000;	price_s['40cm']=0;	price_n['40cm']=0;	price_border['40cm']=0;	price_line['40cm']=0;	price_mirror['40cm']=0;	price_color['40cm']=2000;
price_K['45cm']=14000;	price_E['45cm']=14000;	price_ETC['45cm']=14000;	price_s['45cm']=0;	price_n['45cm']=0;	price_border['45cm']=0;	price_line['45cm']=0;	price_mirror['45cm']=0;	price_color['45cm']=2000;
price_K['50cm']=17000;	price_E['50cm']=17000;	price_ETC['50cm']=18500;	price_s['50cm']=0;	price_n['50cm']=0;	price_border['50cm']=0;	price_line['50cm']=0;	price_mirror['50cm']=0;	price_color['50cm']=2000;
price_arr['d20t']={price_K,price_E,price_ETC,price_s,price_n,price_border,price_line,price_mirror,price_color}

price_K={};	price_E={};	price_ETC={};	price_s={};	price_n={};	price_border={};	price_line={};	price_mirror={};	price_color={};
price_K['30cm']=6000;	price_E['30cm']=5000;	price_ETC['30cm']=7500;	price_s['30cm']=0;	price_n['30cm']=0;	price_border['30cm']=0;	price_line['30cm']=0;	price_mirror['30cm']=0;	price_color['30cm']=1000;
price_K['35cm']=8000;	price_E['35cm']=6000;	price_ETC['35cm']=9500;	price_s['35cm']=0;	price_n['35cm']=0;	price_border['35cm']=0;	price_line['35cm']=0;	price_mirror['35cm']=0;	price_color['35cm']=1500;
price_K['40cm']=9000;	price_E['40cm']=7000;	price_ETC['40cm']=11000;	price_s['40cm']=0;	price_n['40cm']=0;	price_border['40cm']=0;	price_line['40cm']=0;	price_mirror['40cm']=0;	price_color['40cm']=2000;
price_K['45cm']=11500;	price_E['45cm']=8000;	price_ETC['45cm']=13000;	price_s['45cm']=0;	price_n['45cm']=0;	price_border['45cm']=0;	price_line['45cm']=0;	price_mirror['45cm']=0;	price_color['45cm']=2000;
price_K['50cm']=16000;	price_E['50cm']=11000;	price_ETC['50cm']=18000;	price_s['50cm']=0;	price_n['50cm']=0;	price_border['50cm']=0;	price_line['50cm']=0;	price_mirror['50cm']=0;	price_color['50cm']=2000;
price_arr['d30t']={price_K,price_E,price_ETC,price_s,price_n,price_border,price_line,price_mirror,price_color}

price_wh = {};
price_wh["a3t"]=1200;price_wh["a5t"]=1200;price_wh["b"]=5000;price_wh["c"]=5000;price_wh["e"]=500;
price_wh["d10t"]=1200;price_wh["d20t"]=1200;price_wh["d30t"]=1200;
price_wh["f10t"]=1200;price_wh["f20t"]=1200;price_wh["f30t"]=1200;
maxWH = {};
maxWH["a"]=[900,800]; maxWH["b"]=[550,550]; maxWH["c"]=[99999,99999]; maxWH["d"]=[99999,99999]; maxWH["e"]=[99999,99999]; maxWH["f"]=[99999,99999];
max_h=0;max_w=0;

window.addEventListener('load', function() {
  // console.log(self);
  // console.log(self.parent);
  if ( self !== top ) {
    // console.log("iframe");
    // console.log(self.opener);
    // console.log(parent);
    // console.log(self.opener);
    // console.log(parent);
    // opener.parent.Msg();
    // parent.Msg();
  //    console.log(parent);
  //    alert(window.location.href);
  } else {
    // console.log("nono")
  }
});

function show_debug(){
  dbg_cnt=dbg_cnt+1;
  if (dbg_cnt>10) {
    tmp=document.getElementById("dev_down");
    tmp.hidden=false;
  }
}

function cut_line(){
  tmp=document.getElementById("preview_text");
  pre_test = document.getElementById('pre_text2');
  pre_test.style="width:fit-content;height:fit-content;font-family:"+f_w+";font-size:"+font_size+"px;text-align:"+f_align+";"
                +"word-wrap:break-word;max-width:"+max_w+"px;"// +"max-height:"+max_h+"px;"
  pre_text.innerText=tmp.innerText;
  text_list=show_text.split(/؊|؉|\n/);
  pre_h=pre_text.clientHeight;

  while (pre_h>max_h) {
    text_list.splice(text_list.length-1, 1)
    pre_text.innerText=text_list.join('\n').trim()
    pre_h=pre_text.clientHeight;
    console.log(pre_text.innerText)
    if (pre_h<=max_h) {
      toast("자동 견적은 한번에 "+maxWH[pro_w][1]*0.1+"cm 까지 가능합니다!")
      tmp.innerText=pre_text.innerText;
      show_text=tmp.innerText;
      break;
    }
  }

  pre_test2 = document.getElementById('pre_text3');
  pre_test2.innerHTML=sel_HTML;
  pre_test2.style="width:fit-content;height:fit-content;font-family:"+f_w+";font-size:"+font_size+"px;text-align:"+f_align+";"
                +"word-wrap:break-word;max-width:"+max_w+"px;"// +"max-height:"+max_h+"px;"
  pre_scale=1
  pre_scale_h=pre_height/(pre_test2.clientHeight*1.1);
  pre_scale_w=pre_width/(pre_test2.clientWidth*1.1);
  if(pre_height<pre_test2.clientHeight && pre_scale>pre_scale_h) {
    pre_scale=pre_scale_h
  }
  if(pre_width<pre_test2.clientWidth && pre_scale>pre_scale_w) {
    pre_scale=pre_scale_w
  }
  back_scale=back_scale*pre_scale
}

function sel_last(){
contentEditableElement=document.getElementById("preview_text");
var range,selection;
if(document.createRange)//Firefox, Chrome, Opera, Safari, IE 9+
{
  range = document.createRange();//Create a range (a range is a like the selection but invisible)
  range.selectNodeContents(contentEditableElement);//Select the entire contents of the element with the range
  range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
  selection = window.getSelection();//get the selection object (allows you to change selection)
  selection.removeAllRanges();//remove any selections already made
  selection.addRange(range);//make the range you have just created the visible selection
}
else if(document.selection)//IE 8 and lower
{
  range = document.body.createTextRange();//Create a range (a range is a like the selection but invisible)
  range.moveToElementText(contentEditableElement);//Select the entire contents of the element with the range
  range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
  range.select();//Select the range (make it the visible selection
}
}

function sel_sel(nod,x){
  var sel = window.getSelection()
  var rng = sel.getRangeAt(0)

  // console.log(nod,x)
  // console.log(rng,sel)
  sel.collapse(nod,x)
  sel = window.getSelection()
  // range.collapse(true)
  // rng = sel.getRangeAt(0)
  // console.log(nod,x)
  // console.log(rng,sel)
  // rng.setStart(nod, x)
  // rng.collapse(true)
  //
  // sel.removeAllRanges()
  // sel.addRange(rng)
}

function check_sel(){
  // sel=window.getSelection();
  // range=sel.getRangeAt(0);
  //
  // x_size=sel.rangeLength;
  // x_pos=range.startOffset;
  // end_pos=range.endOffset;
  // conten_s=range.startContainer;
  // conten_l=range.endContainer;
  // last_pos=range.endContainer.length;
  // last_pos1=range.startContainer.length;
  //
  // cur_node=sel.focusNode;
  // cur_pos=sel.focusOffset;

  // console.log(x_pos,end_pos,conten_s,conten_l,last_pos,last_pos1)
  // tmp=document.getElementById("preview_text");
  // document.getElementById('pre_text3').innerText=(tmp.innerText);
  // document.getElementById('pre_text4').innerText=(tmp.innerHTML);
  // document.getElementById('pre_text5').innerText=($(tmp).html());
  // document.getElementById('pre_text6').innerText=($(tmp).text());
}

document.fonts.ready.then(function () {
  preview_init();
  preview_update();
  toast("문구와 옵션을 변경해\n미리 제품을 확인해 보세요!")
  flag_font=true;

  $('#preview_text').keyup(function(e) {

    // check_sel
//      sel.setPosition(range.endContainer,19);
    check_sel();
    preview_update();
  })
  $('#preview_text').keydown(function(e) {
//    console.log(e.keyCode)

      sel=window.getSelection();
      range=sel.getRangeAt(0);
      x_pos=range.startOffset;
      last_pos=range.endContainer.length;
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
  document.execCommand('insertHTML', false, event.clipboardData.getData('Text').replace(/(\n|\r\n)/g, '').replaceAll('؊', '<br>').replaceAll('؉', '<br>'));
  event.preventDefault();
}

function first_enter(){
  tmp=document.getElementById("preview_text")
  if (tmp.innerText.trim()=="") {
    tmp.spellcheck=true
  } else if (tmp.spellcheck) {
    tmp.spellcheck=false
    tmp.innerText=""
    sel_text=""
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

function font_pop(){
  if (flag_font) {
    toast("일부 특수문자는\n지원하지 않을 수 있습니다.")
    flag_font=false;
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
  padding_l=10
  padding_t=4
  tmp.css("padding-left",padding_l)
  tmp.css("padding-top",padding_t)
  tmp.width(w-padding_l)
  tmp.height(h-padding_t)

  trg=tmp.siblings("a:visible");
  if(trg.length>0) {
    if (!trg.hasClass('clicked')) {
      select_itm('#pro_font',trg.first());
    } else {
      trg=tmp.siblings("a.clicked:visible");
      select_itm('#pro_font',trg.first());
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

  f_list=$('.dropdown > .dropbtn > span')
  f_list.each(function () {
    init=$(this).text()
    m_w=$(this).parent().width();
    tmp=$(this).parent().siblings('.dropdown-content').children('a');
    for (i = 0; i < tmp.length; i++) {
      if (tmp[i].innerText==$(this).data("select") && ($(tmp[i]).attr("class")==undefined||$(tmp[i]).attr("class").indexOf("clicked")<1)) {
        $(tmp[i]).addClass("clicked")
      }
      $(this).text(tmp[i].innerText);
      // console.log($(this).text(),$(this).height());
      if(m_w<$(this).parent().width()) {        m_w=$(this).parent().width();      }
    }
    $(this).text(init);
    $(this).parent().width(m_w);
  });

  pro_w = document.getElementById('pro_wh').value;
  if (pro_w.length>1) {
    pro_w="a"
    $("#dev_down").show()
  }
  pro_list=$('.for')
  pro_list.each(function () {
    if ($(this).attr('class').indexOf("hidden")<0) {
      $(this).addClass("hidden")
    }
    tmp=$(this).attr('class').split(" ");
    for (step = 0; step < tmp.length; step++) {
      if (tmp[step]==(pro_w) && $(this).attr('class').indexOf("hidden")>-1) {
        $(this).removeClass("hidden")
        break;
      }
    };
  });

  aa = document.getElementById('back_dr');
  pre_img = document.getElementById('pre_img');
  if($(aa).children().length==0) {
    element=back_optin_list.split("/")[0];
    document.getElementById('pro_back').setAttribute("style","background:url('static/background/"+element+"') 50% 50%;");

    bb = document.getElementById('back_img');
    bb.innerText=element.split(".")[0];
    bb.setAttribute("data-value",element);
    bb.setAttribute("data-select",element.split(".")[0]);
    for (const element of back_optin_list.split("/")) {
      tmp = document.createElement('img');
      tmp.src="static/background/"+element;
      pre_img.appendChild(tmp);

      aac = document.createElement('a');
      aac.innerText=element.split(".")[0];
      aac.setAttribute("class","dropbtn");
      aac.setAttribute("style","float:left;background-image:url('static/background/"+element+"');background-size:200%;background-position:bottom;width:48px;height:30px;font-size:0px;");
      aac.setAttribute("data-value",element);
      aac.setAttribute("onclick","select_itm(back_img,this);preview_update()");
      aa.appendChild(aac);
    }
    tmp = document.createElement('img');
    tmp.src="static/background/sys_1.gif";
    pre_img.appendChild(tmp);
    tmp = document.createElement('img');
    tmp.src="static/background/sys_2.gif";
    pre_img.appendChild(tmp);
  }

  pre1 = document.getElementById('pre_text');
  for (const element of font_list.split("/")) {
    opt=document.getElementById("font"+element)
    if(!opt) {
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
  sel_text=tmp.innerText

  check_num = /[0-9]/;
  check_eng = /[a-zA-Z]/;
  check_spc = /[~!@#$%^&*()_+|<>?:{}]/;
  check_kor = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;
  check_n = /\n/;
  check_s = /\s/;

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
  if (pro_w=="d") {
    tmp_flag=true;
    tmp_size=$("#pro_size").data("select");
    pro_list=$('#size_list').children()
    t_thk = $(".thi:visible").data("value")
    pro_list.each(function () {
      if ($(this).attr('class').indexOf("hidden")<0) {
        $(this).addClass("hidden")
      }
      tmpc=$(this).attr('class').split(" ");
      for (step = 0; step < tmpc.length; step++) {
        if (tmpc[step]==(pro_w+t_thk) && $(this).attr('class').indexOf("hidden")>-1) {
          if($(this).text()==tmp_size) {
            tmp_flag=false;
          }
          $(this).removeClass("hidden")
          break;
        }
      };
    });
    if(tmp_flag) {
      "a",$('#size_list').children(':not(.hidden)').first().click();
    }
  }

  pre_width=document.getElementById("pro_back").width
  pre_height=document.getElementById("pro_back").height
  sel_text_list = document.getElementById("preview_list")
  sel_text = tmp.innerText
  sel_HTML = tmp.innerHTML

  sel_thk = $(".thi:visible");
  sel_clr = $(".pro_color:visible");
  sel_font = $("#pro_font");
  sel_size = $("#pro_size");
  sel_back = $('#back_img');
  sel_align = $('#pro_align');
  sel_deco = $('#side_deco');
  sel_main_LED = $("#pro_color_LED");

  t_thk = sel_thk.data("value")
  if (t_thk==undefined) {t_thk=""}
  t_side_gomu = $("#gomu").data("select");
  t_side_gomu_c = $("#gomu2").data("select");
  t_clr = sel_clr.data("select")
  if (t_clr==undefined) {t_clr=""}
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

  pre_w="fit-content";
  pre_h="fit-content";

  if (f_s<6) {    back_scale=1.8
  } else if (f_s<8) {  back_scale=1.4
  } else if (f_s<15) {  back_scale=1.2
  } else {    back_scale=1  }

  if(pro_w=="b") {
    back_scale=back_scale*1.4
  }

  show_text=sel_text;
  max_w = maxWH[pro_w][0]*back_scale/2
  max_h = maxWH[pro_w][1]*back_scale/2

  font_s = document.getElementById('pre_text');
  if($(font_s).children().length==0) {
    preview_init();
  }
  f_scale=$("#font"+f_w).data("scale")
  if(f_scale==undefined) {
    preview_init();
    f_scale=$("#font"+f_w).data("scale")
  }
  font_size=(f_h*f_scale*back_scale)
  pre_scale=1;
  cut_text();
  cut_line();

  font_size=(f_h*f_scale*back_scale)

  sel_text=tmp.innerText
  cut_text();

  if (sel_text.indexOf("؊")>-1 || sel_text.indexOf("؉")>-1) {
    toast("사용할 수 없는 문자입니다!")
    sel_text=sel_text.replaceAll("؊","").replaceAll("؉","")
    tmp.innerText=sel_text.trim()
  }
  if (show_text.length>19) {
    toast("20자씩 나눠서 입력해주세요!")
    sel_text=sel_text.slice(0,20-(show_text.match(/؉/g) || []).length)
    show_text=show_text.slice(0,20)
    tmp.innerText=sel_text.trim()
  }
  tmp=document.getElementById("preview_text");


  sel_text = tmp.innerText
  sel_HTML = tmp.innerHTML

  f_light = $("#pro_light").text().indexOf("OFF")>0
  f_main_LED = $("#pro_color_LED").data("value")
  f_side_LED = $("#side_color_on").data("value");
  f_side_back = $("#side_color_off").data("value");
  f_side_gomu = $("#gomu").data("value");

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

  if (t_thk=="") {
    if (pro_w=="a") {
      f_thi = 2
    } else if (pro_w=="b") {
      f_thi = 10
    } else if (pro_w=="c") {
      f_thi = 6
    } else if (pro_w=="d") {
      f_thi = 5
    } else if (pro_w=="e") {
      f_thi = 0
    }
  } else {
    f_thi=t_thk.replaceAll("t","")*2/6
  }
  f_cnt = 20
  let root = document.documentElement;

  if(back_scale<1) {
    back_scale=1;
  }
  if(f_light) {
    pre_back="background: linear-gradient(to top, rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.25)), url('static/background/"+f_b+"') 50% 50%;"
      +"background-size:"+100*back_scale+"% "+100*back_scale+"%;  background-position-x:center;background-position-y:bottom;"
    root.style.setProperty('--bopa',0.1);
  } else {
    pre_back="background:url('static/background/"+f_b+"') 50% 50%;"
      +"background-size:"+100*back_scale+"% "+100*back_scale+"%;background-position-x:center;background-position-y:bottom;"
    f_main_LED="ffffff"
    root.style.setProperty('--bopa',0.2);
  }
  document.getElementById("pro_back").style=pre_back

  if (pro_w=="a") {
    arr_clr = sel_clr.data("value").split(",")
  } else if (pro_w=="b") {
    if (f_side) {
      arr_clr=[f_main_LED,f_side_LED,f_side_back]
    } else {
      arr_clr=[f_main_LED,f_side_back,f_side_back]
    }
  } else if (pro_w=="c") {
    arr_clr = sel_clr.data("value").split(",")
  } else if (pro_w=="d") {
    if(t_clr.indexOf("도장")<0) {
      arr_clr = sel_clr.data("value").split(",")
      arr_clr[3]=f_side_gomu
      $(".gomu_menu").show()
      $(".gomu2_menu").hide()
    } else {
      arr_clr = $("#gomu2").data("value").split(",")
      arr_clr[1]=f_light_down(arr_clr[1],2)
      $(".gomu_menu").hide()
      $(".gomu2_menu").show()
    }
  } else if (pro_w=="e") {
    arr_clr = sel_clr.data("value").split(",")
  } else if (pro_w=="f") {
    arr_clr = sel_clr.data("value").split(",")
  }
  taper=0
  for (step = 0; step <= f_cnt; step++) {
    pre_style="";f_shwd="";

    if(step==0) {
      tmp=document.getElementById("preview_text")
      f_clr=arr_clr[0]
      if (pro_w=="a" || pro_w=="f") {
        pre_style="background:radial-gradient(farthest-corner at 40% -5%, #"+arr_clr[0]+" 3%, #"+arr_clr[1]+" 5%, #"+arr_clr[2]+" 35%, #"
                  +arr_clr[2]+" 65%, #"+arr_clr[1]+" 99%, #"+arr_clr[0]+" 1000%);"
          +"-webkit-background-clip:text;"
          +"-webkit-text-fill-color:transparent;"
      } else if (pro_w=="b") {
        f_shwd="text-shadow:0.5px 0.5px #fefefe"
        if (f_light) {
          f_shwd=f_shwd+",0px 0px 10px #"+f_clr
        } else if (f_clr=="ffffff") {
          f_clr="fcfcfc"
        }
        f_shwd=f_shwd+";"
      } else if (pro_w=="d") {

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
      if (pro_w=="a" || pro_w=="d" || pro_w=="f") {
        if (step==1) {
          f_clr=arr_clr[1]
        } else {
          f_clr=arr_clr[arr_clr.length-1]
        }
      } else if (pro_w=="b") {
        if (step<=(f_cnt*15/20)) {
          taper=taper+(1/6)
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
          } else if(!f_light&&f_side_LED=="ffffff") {
            f_clr="fcfcfc"
          }
        }
        f_clr=f_clr+""
        if(f_light){
          dep_tmp=f_cnt/2-Math.abs(step-f_cnt/2)
          if (f_side_LED!="none") {
            f_shwd=f_shwd+"0px 0px "+dep_tmp/4+5+"px #"+arr_clr[0]+","
            f_sub_clr=f_light_down(f_clr,1.25-(dep_tmp/40))
            f_clr=f_light_down(f_clr,1.3-(dep_tmp/40))
          } else {
            f_sub_clr=f_light_down(f_clr,3)
            f_clr=f_light_down(f_clr,2)
          }
        } else {
          f_sub_clr=f_light_down(f_clr,1.5)
        }
        for (t_v = -taper; t_v<=taper; t_v=t_v+0.1) {
          f_shwd=f_shwd
                        +t_v+"px "+taper+"px #"+f_sub_clr+","
                        +t_v+"px "+-taper+"px #"+f_clr+","
                        +taper+"px "+t_v+"px #"+f_clr+","
                        +-taper+"px "+t_v+"px #"+f_clr+","
        }
        f_shwd=f_shwd+taper+"px "+taper+"px red;"
      } else if (pro_w=="c") {
        tmp_text=""
        for (i = sel_text.length-1; i >-1; i--) {
          sel_prt=sel_text.charAt(i);
          if(check_n.test(sel_prt)) {
            tmp_text="<br/>"+tmp_text
          } else if(check_s.test(sel_prt)) {
            tmp_text="<div class='footN'>&nbsp;</div>"+tmp_text
          } else if (step==f_cnt) {
            tmp_text="<div class='foote'>"+sel_text.charAt(i)+"</div>"+tmp_text
          } else {
            tmp_text="<div class='foot'>"+sel_text.charAt(i)+"</div>"+tmp_text
          }
        }
        root.style.setProperty('--bclr',"#"+f_clr);
        pre_w=document.getElementById("preview_text").clientWidth+5+"px";
        pre_h=document.getElementById("preview_text").clientHeight+5+"px";
        tmp.opacity=0;
        tmp.innerHTML=tmp_text;
      }
    }
//6 10 35 60
    if (step == f_cnt) {
      if (f_shwd=="") {
        f_shwd="text-shadow:"
      } else {
        f_shwd=f_shwd.replaceAll(";",",")
      }
      if(pro_w=="c") {
        f_shwd=f_shwd+
        "0px 8px rgba(16,16,16,0.5);"
        pre_h="fit-content"
        pre_w="fit-content"
      } else {
        f_shwd=f_shwd+
        f_thi/4+"px "+0.5*f_thi/4+"px "+f_thi*1.1+"px rgba(16,16,16,0.4),"+
        f_thi*2/4+"px "+0.5*f_thi*2/4+"px "+f_thi*1.2+"px rgba(16,16,16,0.2),"+
        f_thi*3/4+"px "+0.5*f_thi*3/4+"px "+f_thi*1.4+"px rgba(16,16,16,0.2),"+
        f_thi*4/4+"px "+0.5*f_thi*4/4+"px "+f_thi*2+"px rgba(16,16,16,0.4);"
      }
    }
    pre_style=pre_style+"width:"+pre_w+";height:"+pre_h+";min-width:"+f_h+"px;min-height:"+f_h*pre_scale+"px;"
      +""+f_shwd+"color:#"+ f_clr +";font-family:"+f_w+";font-size:"+font_size+"px;text-align:"+f_align+";"
      +"z-index:"+(f_cnt-step)+";left:"+(pre_width/2+step*0.5*f_thi/f_cnt)+"px;top:"+(pre_height/2+step*f_thi/f_cnt)+"px;position:absolute;"
      +"word-wrap:break-word;max-height:"+max_h+"px;max-width:"+max_w+"px;overflow:hidden;"
    if (f_deco=="underL") {
      pre_style=pre_style+"text-decoration: underline;"
    } else if (f_deco=="borderL") {
      if (step==0) {
        f_sub_clr=f_clr
      } else if(step>0) {
        if(f_light) {
          // f_sub_clr=f_light_down(f_clr,1.2)
        } else {
          // f_sub_clr=f_light_down(f_clr,1.5)
        }
      }
      pre_style=pre_style+"border-style:solid;border-width:"+(f_h/6+taper)+"px;border-radius:"+f_h/6+"px;border-color:#"+f_clr+";border-color:#"+f_clr+";border-bottom:solid "+(f_h/6+taper)+"px #"+f_sub_clr+";"
    }
    tmp.style=pre_style;
  }

/*외부 수정 가능하게*/
  price_total = 0

  o_cnt=0;e_cnt=0;k_cnt=0;f_cnt=0;
  n_cnt=0;s_cnt=0;bx_cnt=0;by_cnt=0;
  for (i = 0; i < sel_text.length; i++) {
    tmp=sel_text.charAt(i)
    if (check_kor.test(tmp)){
      k_cnt=k_cnt+1;f_cnt=f_cnt+1;
    } else if (check_eng.test(tmp)){
      e_cnt=e_cnt+1;f_cnt=f_cnt+1;
    } else if (check_n.test(tmp)) {
      n_cnt=n_cnt+1;f_cnt=f_cnt+1;
    } else if (check_s.test(tmp)) {
      s_cnt=s_cnt+1;
    } else if (check_num.test(tmp) || check_spc.test(tmp) || tmp.trim()!=""){
      o_cnt=o_cnt+1;
    }
  }
  if(pro_w=="b" && f_deco=="borderL") {
    y_sel_text=show_text.split(/؊|؉|\n/)
    by_cnt=y_sel_text.length;
    for (y=0; y<y_sel_text.length; y++) {
      tmp_y=y_sel_text[y]
      tmp_x_cnt=parseInt((y_sel_text[y].split(" ").length-1)/2)
      tmp_x_cnt2=y_sel_text[y].replaceAll(/\s+/g,"").length
      if((tmp_x_cnt+tmp_x_cnt2)>bx_cnt) {
        bx_cnt=tmp_x_cnt+tmp_x_cnt2;
      }
    }
    n_cnt=parseInt(n_cnt/2)
  }
  s_cnt=parseInt(s_cnt/3)

  tmp_w=pro_w+t_thk
  price_total=
    price_arr[tmp_w]["price_K"][t_size]   *   k_cnt +
    price_arr[tmp_w]["price_E"][t_size]   *   e_cnt +
    price_arr[tmp_w]["price_ETC"][t_size] *   o_cnt +
    price_arr[tmp_w]["price_s"][t_size]   *   s_cnt +
    price_arr[tmp_w]["price_n"][t_size]   *   n_cnt +
    price_arr[tmp_w]["price_border"][t_size]   *   (bx_cnt*2+by_cnt*2)/4
  if (t_clr.search("미러")>-1) {
    price_total=price_total + price_arr[tmp_w]["price_mirror"][t_size]*f_cnt
  }
  if (pro_w=="d" && t_clr.search("도장")>-1) {
    price_total=price_total+price_arr[tmp_w]["price_color"][t_size]*f_cnt
  }
  if (price_total%price_wh[tmp_w]!=0) {
    price_total=price_total+(price_wh[tmp_w]-price_total%price_wh[tmp_w])
  }

  if (pro_w=="b") {
    t_clr_slt=t_main_LED[0]+t_side_LED[0]+t_side_back[0]
  } else if(pro_w=="d") {
    if(t_clr.search("도장")>-1) {
      t_clr_slt=t_clr.split(" ")[1].charAt(0)+t_side_gomu_c.charAt(0)
    } else {
      t_clr_slt=t_clr.split(" ")[1].charAt(0)+t_side_gomu.charAt(0)
    }
  } else {
    t_clr_slt=t_clr.split(" ")[0]
  }
  document.getElementById("btext").innerText=show_text.replace(/(\n|\r\n)/g, '؊')
  document.getElementById("boption").innerText=f_w+"/" +t_clr_slt+"/" +t_size+"/"+t_align+"/"+t_deco.charAt(0)+"/"+t_thk
  document.getElementById("btotal").innerText=price_total.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
  document.getElementById("bcount").innerText=price_total/price_wh[tmp_w]
}

function f_light_down(clrz,valz){
  return (parseInt(parseInt(clrz.slice(0,1),16)/valz)).toString(16)
    +(parseInt(parseInt(clrz.slice(2,3),16)/valz)).toString(16)
    +(parseInt(parseInt(clrz.slice(4,5),16)/valz)).toString(16)
}

function cut_text(){
  tmp=document.getElementById("preview_text");
  text_list=tmp.innerText.split('\n');
  for (var y = text_list.length-1; y > -1; y--) {
    pre_text=document.getElementById('pre_text2');
    pre_text.style="width:fit-content;height:fit-content;font-family:"+f_w+";font-size:"+font_size+"px;text-align:"+f_align+";"
                  +"word-wrap:break-word;max-width:"+max_w+"px;"// +"max-height:"+max_h+"px;"
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
        text_list[y]=insert(text_list[y], y_rec[i], '؉');
      }
      show_text=text_list.join('\n');
      show_text=show_text.trim();
      if (show_text.length>19) {
        sel_text=sel_text.slice(0,show_text.length-(show_text.match(/؉/g) || []).length)
        show_text=show_text.slice(0,20)
      }
    }
  }
}
