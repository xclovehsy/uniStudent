(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-stuGuide-stuGuide"],{1234:function(i,n,t){"use strict";t.r(n);var e=t("b909"),o=t.n(e);for(var c in e)"default"!==c&&function(i){t.d(n,i,(function(){return e[i]}))}(c);n["default"]=o.a},1298:function(i,n,t){"use strict";t.r(n);var e=t("433e"),o=t.n(e);for(var c in e)"default"!==c&&function(i){t.d(n,i,(function(){return e[i]}))}(c);n["default"]=o.a},"2a16":function(i,n,t){"use strict";Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var e={props:{}};n.default=e},3151:function(i,n,t){var e=t("24fb");n=e(!1),n.push([i.i,'@charset "UTF-8";\r\n/**\r\n * 这里是uni-app内置的常用样式变量\r\n *\r\n * uni-app 官方扩展插件及插件市场（https://ext.dcloud.net.cn）上很多三方插件均使用了这些样式变量\r\n * 如果你是插件开发者，建议你使用scss预处理，并在插件代码中直接使用这些变量（无需 import 这个文件），方便用户通过搭积木的方式开发整体风格一致的App\r\n *\r\n */\r\n/**\r\n * 如果你是App开发者（插件使用者），你可以通过修改这些变量来定制自己的插件主题，实现自定义主题功能\r\n *\r\n * 如果你的项目同样使用了scss预处理，你也可以直接在你的 scss 代码中使用如下变量，同时无需 import 这个文件\r\n */\r\n/* 颜色变量 */\r\n/* uni.scss */\r\n/* 行为相关颜色 */\r\n/* 文字基本颜色 */\r\n/* 背景颜色 */\r\n/* 边框颜色 */\r\n/* 尺寸变量 */\r\n/* 文字尺寸 */\r\n/* 图片尺寸 */\r\n/* Border Radius */\r\n/* 水平间距 */\r\n/* 垂直间距 */\r\n/* 透明度 */\r\n/* 文章场景相关 */uni-view[data-v-59765974], uni-scroll-view[data-v-59765974], uni-swiper-item[data-v-59765974]{display:flex;flex-direction:column;flex-shrink:0;flex-grow:0;flex-basis:auto;align-items:stretch;align-content:flex-start}@font-face{font-family:uicon-iconfont;src:url(https://at.alicdn.com/t/font_2225171_8kdcwk4po24.ttf) format("truetype")}.u-icon[data-v-59765974]{display:flex;align-items:center}.u-icon--left[data-v-59765974]{flex-direction:row-reverse;align-items:center}.u-icon--right[data-v-59765974]{flex-direction:row;align-items:center}.u-icon--top[data-v-59765974]{flex-direction:column-reverse;justify-content:center}.u-icon--bottom[data-v-59765974]{flex-direction:column;justify-content:center}.u-icon__icon[data-v-59765974]{font-family:uicon-iconfont;position:relative;display:flex;flex-direction:row;align-items:center}.u-icon__icon--primary[data-v-59765974]{color:#3c9cff}.u-icon__icon--success[data-v-59765974]{color:#5ac725}.u-icon__icon--error[data-v-59765974]{color:#f56c6c}.u-icon__icon--warning[data-v-59765974]{color:#f9ae3d}.u-icon__icon--info[data-v-59765974]{color:#909399}.u-icon__img[data-v-59765974]{height:auto;will-change:transform}.u-icon__label[data-v-59765974]{line-height:1}',""]),i.exports=n},3801:function(i,n,t){var e=t("e890");"string"===typeof e&&(e=[[i.i,e,""]]),e.locals&&(i.exports=e.locals);var o=t("4f06").default;o("5f28f3ed",e,!0,{sourceMap:!1,shadowMode:!1})},"40c7":function(i,n,t){i.exports=t.p+"static/img/schoolInfoimg4.f3a261b9.png"},"433e":function(i,n,t){"use strict";var e=t("4ea4");t("caad"),t("c975"),t("2532"),Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var o=e(t("48d3")),c=e(t("ce15")),u={name:"u-icon",data:function(){return{}},mixins:[uni.$u.mpMixin,uni.$u.mixin,c.default],computed:{uClasses:function(){var i=[];return i.push(this.customPrefix+"-"+this.name),this.color&&uni.$u.config.type.includes(this.color)&&i.push("u-icon__icon--"+this.color),i},iconStyle:function(){var i={};return i={fontSize:uni.$u.addUnit(this.size),lineHeight:uni.$u.addUnit(this.size),fontWeight:this.bold?"bold":"normal",top:uni.$u.addUnit(this.top)},this.color&&!uni.$u.config.type.includes(this.color)&&(i.color=this.color),i},isImg:function(){return-1!==this.name.indexOf("/")},imgStyle:function(){var i={};return i.width=this.width?uni.$u.addUnit(this.width):uni.$u.addUnit(this.size),i.height=this.height?uni.$u.addUnit(this.height):uni.$u.addUnit(this.size),i},icon:function(){return o.default["uicon-"+this.name]||this.name}},methods:{clickHandler:function(i){this.$emit("click",this.index),this.stop&&this.preventEvent(i)}}};n.default=u},"48d3":function(i,n,t){"use strict";Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var e={"uicon-level":"","uicon-column-line":"","uicon-checkbox-mark":"","uicon-folder":"","uicon-movie":"","uicon-star-fill":"","uicon-star":"","uicon-phone-fill":"","uicon-phone":"","uicon-apple-fill":"","uicon-chrome-circle-fill":"","uicon-backspace":"","uicon-attach":"","uicon-cut":"","uicon-empty-car":"","uicon-empty-coupon":"","uicon-empty-address":"","uicon-empty-favor":"","uicon-empty-permission":"","uicon-empty-news":"","uicon-empty-search":"","uicon-github-circle-fill":"","uicon-rmb":"","uicon-person-delete-fill":"","uicon-reload":"","uicon-order":"","uicon-server-man":"","uicon-search":"","uicon-fingerprint":"","uicon-more-dot-fill":"","uicon-scan":"","uicon-share-square":"","uicon-map":"","uicon-map-fill":"","uicon-tags":"","uicon-tags-fill":"","uicon-bookmark-fill":"","uicon-bookmark":"","uicon-eye":"","uicon-eye-fill":"","uicon-mic":"","uicon-mic-off":"","uicon-calendar":"","uicon-calendar-fill":"","uicon-trash":"","uicon-trash-fill":"","uicon-play-left":"","uicon-play-right":"","uicon-minus":"","uicon-plus":"","uicon-info":"","uicon-info-circle":"","uicon-info-circle-fill":"","uicon-question":"","uicon-error":"","uicon-close":"","uicon-checkmark":"","uicon-android-circle-fill":"","uicon-android-fill":"","uicon-ie":"","uicon-IE-circle-fill":"","uicon-google":"","uicon-google-circle-fill":"","uicon-setting-fill":"","uicon-setting":"","uicon-minus-square-fill":"","uicon-plus-square-fill":"","uicon-heart":"","uicon-heart-fill":"","uicon-camera":"","uicon-camera-fill":"","uicon-more-circle":"","uicon-more-circle-fill":"","uicon-chat":"","uicon-chat-fill":"","uicon-bag-fill":"","uicon-bag":"","uicon-error-circle-fill":"","uicon-error-circle":"","uicon-close-circle":"","uicon-close-circle-fill":"","uicon-checkmark-circle":"","uicon-checkmark-circle-fill":"","uicon-question-circle-fill":"","uicon-question-circle":"","uicon-share":"","uicon-share-fill":"","uicon-shopping-cart":"","uicon-shopping-cart-fill":"","uicon-bell":"","uicon-bell-fill":"","uicon-list":"","uicon-list-dot":"","uicon-zhihu":"","uicon-zhihu-circle-fill":"","uicon-zhifubao":"","uicon-zhifubao-circle-fill":"","uicon-weixin-circle-fill":"","uicon-weixin-fill":"","uicon-twitter-circle-fill":"","uicon-twitter":"","uicon-taobao-circle-fill":"","uicon-taobao":"","uicon-weibo-circle-fill":"","uicon-weibo":"","uicon-qq-fill":"","uicon-qq-circle-fill":"","uicon-moments-circel-fill":"","uicon-moments":"","uicon-qzone":"","uicon-qzone-circle-fill":"","uicon-baidu-circle-fill":"","uicon-baidu":"","uicon-facebook-circle-fill":"","uicon-facebook":"","uicon-car":"","uicon-car-fill":"","uicon-warning-fill":"","uicon-warning":"","uicon-clock-fill":"","uicon-clock":"","uicon-edit-pen":"","uicon-edit-pen-fill":"","uicon-email":"","uicon-email-fill":"","uicon-minus-circle":"","uicon-minus-circle-fill":"","uicon-plus-circle":"","uicon-plus-circle-fill":"","uicon-file-text":"","uicon-file-text-fill":"","uicon-pushpin":"","uicon-pushpin-fill":"","uicon-grid":"","uicon-grid-fill":"","uicon-play-circle":"","uicon-play-circle-fill":"","uicon-pause-circle-fill":"","uicon-pause":"","uicon-pause-circle":"","uicon-eye-off":"","uicon-eye-off-outline":"","uicon-gift-fill":"","uicon-gift":"","uicon-rmb-circle-fill":"","uicon-rmb-circle":"","uicon-kefu-ermai":"","uicon-server-fill":"","uicon-coupon-fill":"","uicon-coupon":"","uicon-integral":"","uicon-integral-fill":"","uicon-home-fill":"","uicon-home":"","uicon-hourglass-half-fill":"","uicon-hourglass":"","uicon-account":"","uicon-plus-people-fill":"","uicon-minus-people-fill":"","uicon-account-fill":"","uicon-thumb-down-fill":"","uicon-thumb-down":"","uicon-thumb-up":"","uicon-thumb-up-fill":"","uicon-lock-fill":"","uicon-lock-open":"","uicon-lock-opened-fill":"","uicon-lock":"","uicon-red-packet-fill":"","uicon-photo-fill":"","uicon-photo":"","uicon-volume-off-fill":"","uicon-volume-off":"","uicon-volume-fill":"","uicon-volume":"","uicon-red-packet":"","uicon-download":"","uicon-arrow-up-fill":"","uicon-arrow-down-fill":"","uicon-play-left-fill":"","uicon-play-right-fill":"","uicon-rewind-left-fill":"","uicon-rewind-right-fill":"","uicon-arrow-downward":"","uicon-arrow-leftward":"","uicon-arrow-rightward":"","uicon-arrow-upward":"","uicon-arrow-down":"","uicon-arrow-right":"","uicon-arrow-left":"","uicon-arrow-up":"","uicon-skip-back-left":"","uicon-skip-forward-right":"","uicon-rewind-right":"","uicon-rewind-left":"","uicon-arrow-right-double":"","uicon-arrow-left-double":"","uicon-wifi-off":"","uicon-wifi":"","uicon-empty-data":"","uicon-empty-history":"","uicon-empty-list":"","uicon-empty-page":"","uicon-empty-order":"","uicon-man":"","uicon-woman":"","uicon-man-add":"","uicon-man-add-fill":"","uicon-man-delete":"","uicon-man-delete-fill":"","uicon-zh":"","uicon-en":""};n.default=e},"54dd":function(i,n,t){var e=t("9e9f");"string"===typeof e&&(e=[[i.i,e,""]]),e.locals&&(i.exports=e.locals);var o=t("4f06").default;o("154428f5",e,!0,{sourceMap:!1,shadowMode:!1})},5738:function(i,n,t){"use strict";var e;t.d(n,"b",(function(){return o})),t.d(n,"c",(function(){return c})),t.d(n,"a",(function(){return e}));var o=function(){var i=this,n=i.$createElement,t=i._self._c||n;return t("v-uni-view",{staticClass:"u-icon",class:["u-icon--"+i.labelPos],on:{click:function(n){arguments[0]=n=i.$handleEvent(n),i.clickHandler.apply(void 0,arguments)}}},[i.isImg?t("v-uni-image",{staticClass:"u-icon__img",style:[i.imgStyle,i.$u.addStyle(i.customStyle)],attrs:{src:i.name,mode:i.imgMode}}):t("v-uni-text",{staticClass:"u-icon__icon",class:i.uClasses,style:[i.iconStyle,i.$u.addStyle(i.customStyle)],attrs:{"hover-class":i.hoverClass}},[i._v(i._s(i.icon))]),""!==i.label?t("v-uni-text",{staticClass:"u-icon__label",style:{color:i.labelColor,fontSize:i.$u.addUnit(i.labelSize),marginLeft:"right"==i.labelPos?i.$u.addUnit(i.space):0,marginTop:"bottom"==i.labelPos?i.$u.addUnit(i.space):0,marginRight:"left"==i.labelPos?i.$u.addUnit(i.space):0,marginBottom:"top"==i.labelPos?i.$u.addUnit(i.space):0}},[i._v(i._s(i.label))]):i._e()],1)},c=[]},6249:function(i,n,t){"use strict";t.r(n);var e=t("c0e1"),o=t.n(e);for(var c in e)"default"!==c&&function(i){t.d(n,i,(function(){return e[i]}))}(c);n["default"]=o.a},"65b6":function(i,n,t){"use strict";var e;t.d(n,"b",(function(){return o})),t.d(n,"c",(function(){return c})),t.d(n,"a",(function(){return e}));var o=function(){var i=this,n=i.$createElement,t=i._self._c||n;return t("v-uni-view",{staticClass:"u-safe-bottom",class:[!i.isNvue&&"u-safe-area-inset-bottom"],style:[i.style]})},c=[]},"67ae":function(i,n,t){"use strict";t.r(n);var e=t("5738"),o=t("1298");for(var c in o)"default"!==c&&function(i){t.d(n,i,(function(){return o[i]}))}(c);t("7578");var u,a=t("f0c5"),l=Object(a["a"])(o["default"],e["b"],e["c"],!1,null,"59765974",null,!1,e["a"],u);n["default"]=l.exports},"73fd":function(i,n,t){"use strict";var e=t("3801"),o=t.n(e);o.a},7542:function(i,n,t){"use strict";t.r(n);var e=t("7bf5"),o=t("6249");for(var c in o)"default"!==c&&function(i){t.d(n,i,(function(){return o[i]}))}(c);t("c1c4");var u,a=t("f0c5"),l=Object(a["a"])(o["default"],e["b"],e["c"],!1,null,"608cedb6",null,!1,e["a"],u);n["default"]=l.exports},7578:function(i,n,t){"use strict";var e=t("f358"),o=t.n(e);o.a},"7bf5":function(i,n,t){"use strict";t.d(n,"b",(function(){return o})),t.d(n,"c",(function(){return c})),t.d(n,"a",(function(){return e}));var e={uTabbar:t("77dc").default,uTabbarItem:t("b7ef").default},o=function(){var i=this,n=i.$createElement,e=i._self._c||n;return e("v-uni-view",{staticStyle:{"background-image":"url(static/img/background3.png)"}},[e("br"),e("v-uni-text",{staticStyle:{"font-family":"'Segoe UI', Tahoma, Geneva, Verdana, sans-serif","font-size":"28px",display:"flex","flex-direction":"column","align-items":"center",margin:"auto"}},[i._v("新生入学“四步走”")]),e("br"),e("v-uni-image",{staticStyle:{width:"90px",height:"30px",display:"flex","flex-direction":"column",margin:"auto","align-items":"center"},attrs:{src:"/static/img/laba3.png"}}),e("br"),e("v-uni-image",{staticClass:"content",attrs:{src:"/static/img/schoolInfoimg3.png"},on:{click:function(n){arguments[0]=n=i.$handleEvent(n),i.dianji(0)}}}),e("v-uni-view",[e("br"),e("v-uni-text",{staticClass:"title"},[i._v("步骤①：")]),e("br"),e("v-uni-text",{staticClass:"text-area"},[i._v("找到自己学院的新生接待处，领取相关物资")]),e("br"),e("br"),e("v-uni-image",{staticClass:"content",attrs:{src:t("c3f2")},on:{click:function(n){arguments[0]=n=i.$handleEvent(n),i.dianji(1)}}}),e("br"),e("br")],1),e("v-uni-view",[e("v-uni-text",{staticClass:"title"},[i._v("步骤②")]),e("br"),e("v-uni-text",{staticClass:"text-area"},[i._v("前往学生事务中心领军训物资")]),e("br"),e("br"),e("v-uni-image",{staticClass:"content",attrs:{src:t("40c7")},on:{click:function(n){arguments[0]=n=i.$handleEvent(n),i.dianji(2)}}}),e("br"),e("br")],1),e("v-uni-view",[e("v-uni-text",{staticClass:"title"},[i._v("步骤③")]),e("br"),e("v-uni-text",{staticClass:"text-area"},[i._v("到校医院进行入学体检")]),e("br"),e("br"),e("v-uni-image",{staticClass:"content",attrs:{src:"/static/img/stuGuide1.png"},on:{click:function(n){arguments[0]=n=i.$handleEvent(n),i.dianji(3)}}}),e("br"),e("br")],1),e("v-uni-view",[e("v-uni-text",{staticClass:"title"},[i._v("步骤④")]),e("br"),e("v-uni-text",{staticClass:"text-area"},[i._v("到辅导员办公室办理注册手续")]),e("br"),e("br"),e("v-uni-image",{staticClass:"content",attrs:{src:"/static/img/stuGuide2.png"},on:{click:function(n){arguments[0]=n=i.$handleEvent(n),i.dianji(4)}}}),e("br"),e("br")],1),e("u-tabbar",{attrs:{value:i.value6,fixed:!0,placeholder:!0,safeAreaInsetBottom:!0},on:{change:function(n){arguments[0]=n=i.$handleEvent(n),function(n){return i.value6=n}.apply(void 0,arguments)}}},[e("u-tabbar-item",{attrs:{text:"首页",icon:"home"},on:{click:function(n){arguments[0]=n=i.$handleEvent(n),i.goToMainPlane()}}}),e("u-tabbar-item",{attrs:{text:"数据总览",icon:"search"},on:{click:function(n){arguments[0]=n=i.$handleEvent(n),i.goToDataPlane()}}}),e("u-tabbar-item",{attrs:{text:"报道流程",icon:"map"}}),e("u-tabbar-item",{attrs:{text:"性格测试",icon:"edit-pen"},on:{click:function(n){arguments[0]=n=i.$handleEvent(n),i.goToCapPlane()}}})],1)],1)},c=[]},"9e9f":function(i,n,t){var e=t("24fb");n=e(!1),n.push([i.i,".content[data-v-608cedb6]{display:flex;flex-direction:column;align-items:center;margin:auto;border-radius:8%}.text-area[data-v-608cedb6]{\n\t/* font-style: oblique; */font-style:unset;white-space:pre-wrap;display:flex;flex-direction:column;align-items:center;margin:auto}.title[data-v-608cedb6]{font-size:25px;color:#000;display:flex;flex-direction:column;align-items:center;margin:auto}",""]),i.exports=n},b909:function(i,n,t){"use strict";var e=t("4ea4");Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var o=e(t("2a16")),c={name:"u-safe-bottom",mixins:[uni.$u.mpMixin,uni.$u.mixin,o.default],data:function(){return{safeAreaBottomHeight:0,isNvue:!1}},computed:{style:function(){var i={};return uni.$u.deepMerge(i,uni.$u.addStyle(this.customStyle))}},mounted:function(){}};n.default=c},c0e1:function(i,n,t){"use strict";Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var e={data:function(){return{value6:2}},methods:{dianji:function(i){uni.previewImage({urls:["/static/img/schoolInfoimg3.png","/static/img/schoolInfoimg.png","/static/img/schoolInfoimg4.png","/static/img/stuGuide1.png","/static/img/stuGuide2.png"],current:i})},goToCapPlane:function(){uni.navigateTo({url:"/pages/CapAssess/CapAssess"})},goToDataPlane:function(){uni.navigateTo({url:"/pages/plane/plane"})},goToRegPlane:function(){uni.navigateTo({url:"/pages/stuGuide/stuGuide"})},goToMainPlane:function(){uni.navigateTo({url:"/pages/schoolInfo/schoolInfo"})}}};n.default=e},c1c4:function(i,n,t){"use strict";var e=t("54dd"),o=t.n(e);o.a},c3f2:function(i,n,t){i.exports=t.p+"static/img/schoolInfoimg.b69ae7e7.png"},ce15:function(i,n,t){"use strict";t("a9e3"),Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var e={props:{name:{type:String,default:uni.$u.props.icon.name},color:{type:String,default:uni.$u.props.icon.color},size:{type:[String,Number],default:uni.$u.props.icon.size},bold:{type:Boolean,default:uni.$u.props.icon.bold},index:{type:[String,Number],default:uni.$u.props.icon.index},hoverClass:{type:String,default:uni.$u.props.icon.hoverClass},customPrefix:{type:String,default:uni.$u.props.icon.customPrefix},label:{type:[String,Number],default:uni.$u.props.icon.label},labelPos:{type:String,default:uni.$u.props.icon.labelPos},labelSize:{type:[String,Number],default:uni.$u.props.icon.labelSize},labelColor:{type:String,default:uni.$u.props.icon.labelColor},space:{type:[String,Number],default:uni.$u.props.icon.space},imgMode:{type:String,default:uni.$u.props.icon.imgMode},width:{type:[String,Number],default:uni.$u.props.icon.width},height:{type:[String,Number],default:uni.$u.props.icon.height},top:{type:[String,Number],default:uni.$u.props.icon.top},stop:{type:Boolean,default:uni.$u.props.icon.stop}}};n.default=e},db46:function(i,n,t){"use strict";t.r(n);var e=t("65b6"),o=t("1234");for(var c in o)"default"!==c&&function(i){t.d(n,i,(function(){return o[i]}))}(c);t("73fd");var u,a=t("f0c5"),l=Object(a["a"])(o["default"],e["b"],e["c"],!1,null,"59ae07f8",null,!1,e["a"],u);n["default"]=l.exports},e890:function(i,n,t){var e=t("24fb");n=e(!1),n.push([i.i,'@charset "UTF-8";\r\n/**\r\n * 这里是uni-app内置的常用样式变量\r\n *\r\n * uni-app 官方扩展插件及插件市场（https://ext.dcloud.net.cn）上很多三方插件均使用了这些样式变量\r\n * 如果你是插件开发者，建议你使用scss预处理，并在插件代码中直接使用这些变量（无需 import 这个文件），方便用户通过搭积木的方式开发整体风格一致的App\r\n *\r\n */\r\n/**\r\n * 如果你是App开发者（插件使用者），你可以通过修改这些变量来定制自己的插件主题，实现自定义主题功能\r\n *\r\n * 如果你的项目同样使用了scss预处理，你也可以直接在你的 scss 代码中使用如下变量，同时无需 import 这个文件\r\n */\r\n/* 颜色变量 */\r\n/* uni.scss */\r\n/* 行为相关颜色 */\r\n/* 文字基本颜色 */\r\n/* 背景颜色 */\r\n/* 边框颜色 */\r\n/* 尺寸变量 */\r\n/* 文字尺寸 */\r\n/* 图片尺寸 */\r\n/* Border Radius */\r\n/* 水平间距 */\r\n/* 垂直间距 */\r\n/* 透明度 */\r\n/* 文章场景相关 */.u-safe-bottom[data-v-59ae07f8]{width:100%}',""]),i.exports=n},f358:function(i,n,t){var e=t("3151");"string"===typeof e&&(e=[[i.i,e,""]]),e.locals&&(i.exports=e.locals);var o=t("4f06").default;o("3da46e04",e,!0,{sourceMap:!1,shadowMode:!1})}}]);