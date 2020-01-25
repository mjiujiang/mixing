/*!
 * Cropper v3.0.0
 */

layui.config({
    base: '/static/cropper/' //layui自定义layui组件目录
}).define(['jquery','layer','cropper'],function (exports) {
    var $ = layui.jquery
        ,layer = layui.layer;
    var obj = {
        render: function(e){
            var self = this,
                elem = e.elem,
                saveW = e.saveW,
                saveH = e.saveH,
                aspectRatio = e.aspectRatio,
                area = e.area,
                url = e.url,
                done = e.done;
            var data = e.data;
            var html = "<link rel=\"stylesheet\" href=\"/static/cropper/cropper.css\">\n" +
                "<link rel=\"stylesheet\" href=\"/static/layui/css/layui.css\">\n" +
                "<div class=\"layui-fluid showImgEdit\" style=\"display: none\">\n" +
                "    <div class=\"layui-form-item\" style=\"margin-top:10px;\">\n" +
                "        <div class=\"layui-input-inline layui-btn-container\" style=\"width: auto;\">\n" +
                "            <label for=\"cropper_avatarImgUpload\" class=\"layui-btn layui-btn-primary\">\n" +
                "                <i class=\"layui-icon\">&#xe67c;</i>选择图片\n" +
                "            </label>\n" +
                "            <input class=\"layui-upload-file\" id=\"cropper_avatarImgUpload\" type=\"file\" value=\"选择图片\" name=\"file\">\n" +
                "        </div>\n" +
                "        <div class=\"layui-form-mid layui-word-aux\">"+e.tips+"</div>\n" +
                "    </div>\n" +
                "    <div class=\"layui-row layui-col-space15\">\n" +
                "        <div class=\"layui-col-xs9\">\n" +
                "            <div class=\"readyimg\" style=\"height:450px;background-color: rgb(247, 247, 247);\">\n" +
                "                <img src=\"\" >\n" +
                "            </div>\n" +
                "        </div>\n" +
                "        <div class=\"layui-col-xs3\">\n" +
                "            <div class=\"img-preview\" style=\"width:200px;height:200px;overflow:hidden\">\n" +
                "            </div>\n" +
                "        </div>\n" +
                "    </div>\n" +
                "    <div class=\"layui-row layui-col-space15\">\n" +
                "        <div class=\"layui-col-xs9\">\n" +
                "            <div class=\"layui-row\">\n" +
                "                <div class=\"layui-col-xs6\">\n" +
                "                    <button type=\"button\" class=\"layui-btn layui-icon layui-icon-left\" cropper-event=\"rotate\" data-option=\"-15\" title=\"Rotate -90 degrees\"> 向左旋转</button>\n" +
                "                    <button type=\"button\" class=\"layui-btn layui-icon layui-icon-right\" cropper-event=\"rotate\" data-option=\"15\" title=\"Rotate 90 degrees\"> 向右旋转</button>\n" +
                "                </div>\n" +
                "                <div class=\"layui-col-xs5\" style=\"text-align: right;\">\n" +
                "                    <button type=\"button\" class=\"layui-btn\" cropper-event=\"move\" title=\"移动\"></button>\n" +
                "                    <button type=\"button\" class=\"layui-btn\" title=\"放大图片\"></button>\n" +
                "                    <button type=\"button\" class=\"layui-btn\" title=\"缩小图片\"></button>\n" +
                "                    <button type=\"button\" class=\"layui-btn layui-icon layui-icon-refresh\" cropper-event=\"reset\" title=\"重置图片\"></button>\n" +
                "                </div>\n" +
                "            </div>\n" +
                "        </div>\n" +
                "        <div class=\"layui-col-xs3\">\n" +
                "            <button class=\"layui-btn layui-btn-fluid\" cropper-event=\"confirmSave\" type=\"button\"> 保存修改</button>\n" +
                "        </div>\n" +
                "    </div>\n" +
                "\n" +
            "</div>";
            $('body').append(html);

            var content = $('.showImgEdit')
                ,image = $(".showImgEdit .readyimg img")
                ,preview = '.showImgEdit .img-preview'
                ,file = $(".showImgEdit input[name='file']")
                , options = {aspectRatio: aspectRatio,preview: preview,viewMode:1};

            $(elem).on('click',function () {
                layer.open({
                    type: 1
                    , content: content
                    , area: area
                    , success: function () {
                        image.cropper(options);
                    }
                    , cancel: function (index) {
                        layer.close(index);
                        image.cropper('destroy');
                    }
                });
            });
            $(".layui-btn").on('click',function () {
                var event = $(this).attr("cropper-event");
                //监听确认保存图像
                if (event === 'confirmSave') {
                    image.cropper("getCroppedCanvas",{
                        width: saveW,
                        height: saveH
                    }).toBlob(function(blob){
                        var formData = new FormData();
                        var timestamp = Date.parse(new Date());
                        formData.append('file',blob, timestamp+'.jpg');
                        for (var p in data) {
                            formData.append(p, data[p])
                        }
                        $.ajax({
                            method:"post",
                            url: url, //用于文件上传的服务器端请求地址
                            data: formData,
                            processData: false,
                            contentType: false,
                            success:function(result){
                                if(result.code == 0) {
                                    layer.msg(result.msg,{icon: 1});
                                    layer.closeAll('page');
                                    return done(result);
                                } else if(result.code) {
                                    layer.alert(result.msg,{icon: 2});
                                } else {
                                    layer.alert('未知错误',{icon: 2});
                                }
                            }
                        });
                    });
                    //监听旋转
                } else if(event === 'rotate') {
                    var option = $(this).attr('data-option')
                    image.cropper('rotate', option)
                    //重设图片
                } else if(event === 'reset') {
                    image.cropper('reset')
                } else if (event === 'move') {
                    image.cropper('move')
                }
                //文件选择
                file.change(function () {
                    var r= new FileReader();
                    var f=this.files[0];
                    r.readAsDataURL(f);
                    r.onload=function (e) {
                        image.cropper('destroy').attr('src', this.result).cropper(options);
                    };
                });
            });
        }

    };
    exports('croppers', obj);
});