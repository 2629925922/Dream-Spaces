        // function getBase64(){
        //     //通过构造函数来创建的 img 实例，在赋予 src 值后就会立刻下载图片，相比 createElement() 创建 <img> 省去了 append()，也就避免了文档冗余和污染
        //     var Img = new Image(),
        //         dataURL='';
        //     Img.src="C:\Users\Think\Desktop\文件\web开发\测试项目\制梦翻译\images";
        //     Img.onload=function(){ //要先确保图片完整获取到，这是个异步事件
        //         var canvas = document.createElement('canvas'), //创建canvas元素
        //             width=Img.width, //确保canvas的尺寸和图片一样
        //             height=Img.height;
        //         canvas.width=width;
        //         canvas.height=height;
        //         canvas.getContext('2d').drawImage(Img,0,0,width,height); //将图片绘制到canvas中
        //         dataURL=canvas.toDataURL('image/jpeg'); //转换图片为dataURL
        //     };
        // }
        function getbase64(url)
        {
            var img = new Image();
            var dataurl = '';
            img.src = url;
            img.onload=function () {
                var canvas = document.getElementById('canvas');
                var imgs = document.getElementById('imgs');
                canvas.width = img.width;
                canvas.height = img.height;
                canvas.getContext('2d').drawImage(img,0,0,width,height);
                dataurl = canvas.toDataURL('image/jpeg');
            }
        }


        function sajax()
        {
            var xmlhttp;
            if (window.XMLHttpRequest) {
	            xmlhttp=new XMLHttpRequest();
	        } else
            {
	            xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	        }
            xmlhttp.onreadystatechange=function () {
                if(xmlhttp.readyState == 4 && xmlhttp.status == 200)
                {
                    document.getElementById("mytext").innerHTML=xmlhttp.responseText;
                }
            }
            var values = document.getElementById('word').value;
            xmlhttp.open('GET','/fanyi/'+values,true);
            xmlhttp.send();
        }