
//타입별 단가표
function chmm(nType,nTick,nSize)
{

	var arrType = nType.split(".");
	//document.myform.p_price.value = arrVal[0];	//단가
	var tempPriceTable = '';

	switch(nTick)
	{
		case "2mm":
		switch(true)
		{
			case 3 <= nSize && nSize <= 5:tempPriceTable = ('700,1500,1500');break;
			case 5 < nSize && nSize <= 10:tempPriceTable = ('1200,2500,2500');break;
			case 10 < nSize && nSize <= 15:tempPriceTable = ('1600,3500,3500');break;
		}
		break;
	}
	var arrPriceTable = tempPriceTable.split(",");
	switch(arrType[0])
	{
		case 'A':document.myform.p_price.value = arrPriceTable[0];break;
	}
}

//수치에 3자리마다 콤마찍는 함수
function setComma(str)
{
	str = "" + str + "";
	var retValue = "";

	for(i=0;i<str.length;i++)
	{
		if(i>0&&(i%3)==0&&str.length>3)
		{
			retValue = str.charAt(str.length -i -1) + "," + retValue;
		}
		else
		{
			retValue = str.charAt(str.length -i -1) + retValue;
		}
	}
	return retValue;
}

//결과값 반내림 함수
function roundXL(n, digits) {
	if (digits >= 0) return parseFloat(n.toFixed(digits)); // 소수부 반올림

	digits = Math.pow(10, digits); // 정수부 반올림
	var t = Math.floor(n * digits) / digits;

	return parseFloat(t.toFixed(0));
}

// 공백을 없앤다.
function no_blank(data)
{
	var tmp = '';
	var comma = ' ';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//쌍따음표 삭제
function no_ssddam(data)
{
	var tmp = '';
	var comma = '\"';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//따음표 삭제
function no_ddam(data)
{
	var tmp = '';
	var comma = '\'';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}


// 각괄호 삭제
function no_gagualho(data)
{
	var tmp = '';
	var comma = '[';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

// 반각괄호 삭제
function no_bgagualho(data)
{
	var tmp = '';
	var comma = ']';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

// 포괄호 삭제
function no_pogualho(data)
{
	var tmp = '';
	var comma = '{';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

// 반포괄호 삭제
function no_bpogualho(data)
{
	var tmp = '';
	var comma = '}';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

// 꺽쇠괄호 삭제
function no_tgualho(data)
{
	var tmp = '';
	var comma = '<';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

// 반꺽쇠괄호 삭제
function no_btgualho(data)
{
	var tmp = '';
	var comma = '>';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

// ^ 삭제
function no_smile(data)
{
	var tmp = '';
	var comma = '^';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//  ~ 삭제
function no_mulbar(data)
{
	var tmp = '';
	var comma = '~';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

// | 삭제
function no_serobar(data)
{
	var tmp = '';
	var comma = '|';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//쩜 삭제
function no_point(data)
{
	var tmp = '';
	var comma = '.';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//콤마 삭제
function no_comma(data)
{
	var tmp = '';
	var comma = ',';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//하이픈 삭제
function no_middlebar(data)
{
	var tmp = '';
	var comma = '-';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//언더바 삭제
function no_underbar(data)
{
	var tmp = '';
	var comma = '_';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//슬러시 삭제
function no_slash(data)
{
	var tmp = '';
	var comma = '/';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//땡땡이 삭제
function no_ddang(data)
{
	var tmp = '';
	var comma = ':';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//땀땡이 삭제
function no_ddamddang(data)
{
	var tmp = '';
	var comma = '\;';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

//괄호 삭제
function no_gualho(data)
{
	var tmp = '';
	var comma = '(';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

// 반괄호  삭제
function no_bgualho(data)
{
	var tmp = '';
	var comma = ')';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) != comma)
		tmp += data.charAt(i);
	}
	return tmp;
}

// 쌍따음표 갯수
function cnt_ssddam(data)
{
	var tmp = 0;
	var comma = '"';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 따음표 갯수
function cnt_ddam(data)
{
	var tmp = 0;
	var comma = '\'';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 각괄호 갯수
function cnt_gagualho(data)
{
	var tmp = 0;
	var comma = '[';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 반각괄호 갯수
function cnt_bgagualho(data)
{
	var tmp = 0;
	var comma = ']';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 포괄호 갯수
function cnt_pogualho(data)
{
	var tmp = 0;
	var comma = '{';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 반포괄호 갯수
function cnt_bpogualho(data)
{
	var tmp = 0;
	var comma = '}';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 꺽쇠괄호 갯수
function cnt_tgualho(data)
{
	var tmp = 0;
	var comma = '<';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}


// 반꺽쇠괄호 갯수
function cnt_btgualho(data)
{
	var tmp = 0;
	var comma = '>';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 괄호갯수
function cnt_gualho(data)
{
	var tmp = 0;
	var comma = '(';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 반괄호  갯수
function cnt_bgualho(data)
{
	var tmp = 0;
	var comma = ')';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// ^ 갯수
function cnt_smile(data)
{
	var tmp = 0;
	var comma = '^';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// ~ 갯수
function cnt_mulbar(data)
{
	var tmp = 0;
	var comma = '~';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// | 갯수
function cnt_serobar(data)
{
	var tmp = 0;
	var comma = '|';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}


// 점 갯수
function cnt_point(data)
{
	var tmp = 0;
	var comma = '.';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 콤마 갯수
function cnt_comma(data)
{
	var tmp = 0;
	var comma = ',';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 하이픈 갯수
function cnt_middlebar(data)
{
	var tmp = 0;
	var comma = '-';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 언더바 갯수
function cnt_underbar(data)
{
	var tmp = 0;
	var comma = '_';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 슬래시 갯수
function cnt_slash(data)
{
	var tmp = 0;
	var comma = '/';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 땡땡이 갯수
function cnt_ddang(data)
{
	var tmp = 0;
	var comma = ':';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

// 땀땡이 갯수
function cnt_ddamddang(data)
{
	var tmp = 0;
	var comma = '\;';
	var i;

	for (i=0; i<data.length; i++)
	{
		if (data.charAt(i) == comma)
		tmp += 1;
	}
	return tmp;
}

//계산함수
function w_sum()
{
	pmnsize = eval(document.myform.p_mnsize.value);		//최소세로
	pmxsize = eval(document.myform.p_mxsize.value);		//최대세로
	plistcnt = eval(document.myform.p_listcnt.value);		//리스트갯수

	ptick = document.myform.pro_tick.value;		//두께
	pcolor = document.myform.pro_color.value;		//색상
	//prbcolor = document.myform.pro_rbcolor.value;		//색상
	pfont = document.myform.pro_font.value;	//서체
	psize = eval(document.myform.pro_size.value);	//높이
	ptext = document.myform.pro_text.value;	//내용
	pcount = document.myform.pro_count.value;	//세트수량


	if(plistcnt == 16)
	{
		alert('견적은 15개 까지만 가능 합니다.\n삭제 후 다시 시도하시거나 \n견적내용을 보내시고 추가로 작성바랍니다.');
		return;
	}

	if(document.myform.pro_tick.value == '')
	{
		alert('아크릴두께를 선택 하십시오.');
		document.myform.pro_tick.focus();
		return;
	}
	if(document.myform.pro_color.value == '')
	{
		alert('아크릴색상을 선택 하십시오.');
		document.myform.pro_color.focus();
		return;
	}
	if(document.myform.pro_font.value == '')
	{
		alert('글자서체를 선택 하십시오.');
		document.myform.pro_font.focus();
		return;

	}
	if(document.myform.pro_size.value == '')
	{
		alert('글자사이즈(높이)를 입력하여 주십시오.');
		document.myform.pro_size.focus();
		return;
	}
	if(document.myform.pro_count.value == '')
	{
		alert('작업 셋트 수량을 입력하여 주십시오.');
		document.myform.pro_count.focus();
		return;
	}
	if(document.myform.pro_tick.value == '2mm')
	{
		if(eval(document.myform.pro_size.value) < 3 || eval(document.myform.pro_size.value) > 15)
		{
			alert('아크릴두께 2mm 제품은 작업배송간에 파손이 잦아 15cm이하 사이즈만 제작.발송 가능합니다.');
			document.myform.pro_size.focus();
			return;
		}
	}

	if(document.myform.pro_tick.value == '3mm')
	{
		if(eval(document.myform.pro_size.value) < 3 || eval(document.myform.pro_size.value) > 25)
		{
			alert('아크릴두께 3mm 제품은 작업배송간에 파손이 잦아 25cm이하 사이즈만 제작.발송 가능합니다.');
			document.myform.pro_size.focus();
			return;
		}
	}

	if(document.myform.pro_tick.value == '5mm')
	{
		if(eval(document.myform.pro_size.value) < 3 || eval(document.myform.pro_size.value) > 40)
		{
			alert('아크릴두께 5mm 제품은 대형사이즈 작업배송간에 파손이 잦아 40cm이하 사이즈만 제작.발송 가능합니다.');
			document.myform.pro_size.focus();
			return;
		}
	}

	if(document.myform.pro_tick.value == '8mm')
	{
		if(eval(document.myform.pro_size.value) < 3 || eval(document.myform.pro_size.value) > 45)
		{
			alert('아크릴두께 8mm 제품은 대형사이즈 작업배송간에 파손이 잦아 45cm이하 사이즈만 제작.발송 가능합니다.');
			document.myform.pro_size.focus();
			return;
		}
	}

	if(psize < pmnsize)
	{
		alert("최소사이즈는 "+pmnsize+"cm 입니다.");
		document.myform.pro_size.focus();
		return;
	}
	if(psize > pmxsize)
	{
		alert("최대사이즈는 "+pmxsize+"cm 입니다.");
		document.myform.pro_size.focus();
		return;
	}
	if(document.myform.pro_text.value == '')
	{
		alert('글자내용을 입력하여 주십시오.');
		document.myform.pro_text.focus();
		return;
	}

	//단가 확인
	chmm(pcolor,ptick,psize);
	pprice = document.myform.p_price.value;	//가격

	var lenText = 0;
	var tempText = '';
	var tempcnt_ssddam = 0;
	var tempcnt_ddam = 0;
	var tempcnt_gagualho = 0;
	var tempcnt_bgagualho = 0;
	var tempcnt_pogualho = 0;
	var tempcnt_bpogualho = 0;
	var tempcnt_smile = 0;
	var tempcnt_mulbar = 0;
	var tempcnt_serobar = 0;
	var tempcnt_tgualho = 0;
	var tempcnt_btgualho = 0;
	var tempcnt_gualho = 0;
	var tempcnt_bgualho = 0;
	var tempcnt_point = 0;
	var tempcnt_comma = 0;
	var tempcnt_middlebar = 0;
	var tempcnt_underbar = 0;
	var tempcnt_slash = 0;
	var tempcnt_ddang = 0;
	var tempcnt_ddamddang = 0;

	tempText = no_blank(ptext);  //공백제거

	//.,-_ 특수문자 가격조정을 위해 갯수 확인
	tempcnt_ssddam = cnt_ssddam(tempText);
	tempcnt_ddam = cnt_ddam(tempText);
	tempcnt_gagualho = cnt_gagualho(tempText);
	tempcnt_bgagualho = cnt_bgagualho(tempText);
	tempcnt_pogualho = cnt_pogualho(tempText);
	tempcnt_bpogualho = cnt_bpogualho(tempText);
	tempcnt_smile = cnt_smile(tempText);
	tempcnt_mulbar = cnt_mulbar(tempText);
	tempcnt_serobar = cnt_serobar(tempText);
	tempcnt_tgualho = cnt_tgualho(tempText);
	tempcnt_btgualho = cnt_btgualho(tempText);
	tempcnt_gualho = cnt_gualho(tempText);
	tempcnt_bgualho = cnt_bgualho(tempText);
	tempcnt_point = cnt_point(tempText);
	tempcnt_comma = cnt_comma(tempText);
	tempcnt_middlebar = cnt_middlebar(tempText);
	tempcnt_underbar = cnt_underbar(tempText);
	tempcnt_slash = cnt_slash(tempText);
	tempcnt_ddang = cnt_ddang(tempText);
	tempcnt_ddamddang = cnt_ddamddang(tempText);




	lenText = tempText.length;		//글자수 체크

	tempText = no_gualho(tempText);  //괄호 제거
	tempText = no_bgualho(tempText);  //반괄호 제거
	tempText = no_ssddam(tempText);  //쌍따음표 제거
	tempText = no_ddam(tempText);  //따음표 제거
	tempText = no_gagualho(tempText); // 각괄호 제거
	tempText = no_bgagualho(tempText); // 반각괄호 제거
	tempText = no_pogualho(tempText); // 포괄호 제거
	tempText = no_bpogualho(tempText); // 반포괄호 제거
	tempText = no_smile(tempText); // ^ 제거
	tempText = no_mulbar(tempText); // ~ 제거
	tempText = no_serobar(tempText); // | 제거
	tempText = no_tgualho(tempText); // 꺽쇠괄호 제거
	tempText = no_btgualho(tempText); // 반꺽쇠괄호 제거
	tempText = no_point(tempText);  //쩜 제거
	tempText = no_comma(tempText);  //콤마 제거
	tempText = no_middlebar(tempText);  //하이픈 제거
	tempText = no_underbar(tempText);  //언더바 제거
	tempText = no_slash(tempText);  //슬래시 제거
	tempText = no_ddang(tempText);  //땡땡이 제거
	tempText = no_ddamddang(tempText);  //땀땡이 제거

	//글자별로 숫자,영문,한글 / 한자 및 기타언어 구문하여 계산
	var i;

	psum = 0;
	for (i=0; i<tempText.length; i++)
	{
		//alert(tempText.charCodeAt(i));
		switch(true)
		{
			case 33 <= tempText.charCodeAt(i) && tempText.charCodeAt(i) <= 300:psum=psum+(pprice*1);break;
			case 44032 <= tempText.charCodeAt(i) && tempText.charCodeAt(i) <= 55203:psum=psum+(pprice*1);break;
			case 12593 <= tempText.charCodeAt(i) && tempText.charCodeAt(i) <= 12643:psum=psum+(pprice*1);break;
			default:psum=psum+(pprice*1.3);break;
		}
		//break;
	}
	console.log(psum)
	psum = psum + (pprice * ((tempcnt_point + tempcnt_comma + tempcnt_ddam) / 4  + (tempcnt_gualho + tempcnt_bgualho + tempcnt_pogualho + tempcnt_bpogualho + tempcnt_gagualho + tempcnt_bgagualho + tempcnt_tgualho + tempcnt_btgualho + tempcnt_smile + tempcnt_mulbar + tempcnt_serobar + tempcnt_middlebar + tempcnt_underbar + tempcnt_ssddam + tempcnt_slash + tempcnt_ddang + tempcnt_ddamddang) / 2));
	console.log(psum)
	psum = psum * pcount;
	console.log(psum)

	pqty = lenText;	//수량

	//<!--   삭제옵션  여기부터 -->
	var currentlist = 1;

	//
	for(i=1;i<16;i++)
	{
		tempsptick_nn = eval("document.all.sptick"+i);
		if(tempsptick_nn.innerHTML == '')
		{
			currentlist = i;
			break;
		}
	}

	//화면상에 계산된값을 뿌려주기위한 준비
	spptm  = document.myform.ptm.value;
	sptick_nn = eval("document.all.sptick"+currentlist);
	spcolor_nn = eval("document.all.spcolor"+currentlist);
	spfont_nn = eval("document.all.spfont"+currentlist);
	spsize_nn = eval("document.all.spsize"+currentlist);
	sptext_nn = eval("document.all.sptext"+currentlist);
	spprice_nn = eval("document.all.spprice"+currentlist);
	spqty_nn = eval("document.all.spqty"+currentlist);
	spcnt_nn = eval("document.all.spcnt"+currentlist);
	spsum_nn = eval("document.all.spsum"+currentlist);
	spdel_nn = eval("document.all.spdel"+currentlist);

	var arrcolorname = pcolor.split(".");

	//화면상에 계산된값을 뿌리기
	sptick_nn.innerHTML = ptick;
	spcolor_nn.innerHTML = arrcolorname[1];
	//sprbcolor_nn.innerHTML = prbcolor;
	spfont_nn.innerHTML = pfont;
	spsize_nn.innerHTML = psize;
	sptext_nn.innerHTML = ptext;
	//spprice_nn.innerHTML = pprice;
	spqty_nn.innerHTML = pcount;		//세트수량
	spcnt_nn.innerHTML = pqty;			//글자갯수
	spsum_nn.innerHTML = setComma(psum);
	tempHtml =  "<a href='##'><img src='static/icon_del.png' border=0 onClick='delline(this)' name='del_" + currentlist + "'></a>";			// 이미지 경로임
	spdel_nn.innerHTML = tempHtml;
	//tt_sum = eval(spptm)+eval(psum);   //소계 합산
	var tt_sum2 = 0;
	for(i=1;i<16;i++)
	{
		//alert("for:" + tt_sum2);
		tempspsum_nn = eval("document.all.spsum"+i);
		//alert(tempspsum_nn.innerHTML);
		if(tempspsum_nn.innerHTML != '')
		{
			tt_sum2 = tt_sum2 + eval(no_comma(tempspsum_nn.innerHTML));
			//alert("if:" + tt_sum2);
		}
	}
	document.all.spst.innerHTML = setComma(tt_sum2);		//합계값 화면상에 뿌리기
	document.all.spcount.innerHTML = setComma(roundXL(tt_sum2,-3)/1000);		// 주문수량 화면상에 뿌리기 - 내림 (-3은 자리수 000)
	document.myform.ptm.value = tt_sum2;		//총 합계금액 임시 저장

	if(plistcnt < 16)
	{
		document.myform.p_listcnt.value = eval(plistcnt)+1;   //리스트 갯수 저장
	}
}
function html_auto_br(obj)
{
	if (obj.checked) {
		result = confirm("자동 줄바꿈을 하시겠습니까?\n\n자동 줄바꿈은 게시물 내용중 줄바뀐 곳을<br>태그로 변환하는 기능입니다.");
		if (result)
		obj.value = "html2";
		else
		obj.value = "html1";
	}
	else
	obj.value = "";
}

//producturl = "";

//alert(parentname);

//producturl = "<br><br><a href='http://itempage3.auction.co.kr/DetailView.aspx?itemNo=A529976553&frm3=V2' target='_new'><img src='./img/icon_del.png' border='0'></a>";


//게시판 카테고리 구분
document.getElementById("ca_name").value = "아크릴스카시";

var stemp = "";
var stemp3 = "";
stemp = stemp + document.all.splist.innerHTML;

//alert(stemp);

document.getElementById("spst2").value = document.all.spst.innerHTML;
document.getElementById("spcount2").value = document.all.spcount.innerHTML;
