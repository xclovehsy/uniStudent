<template>
    <view class="container"> 
          <image class="bg-img" src="/static/img/background10.png"></image>
          <view class="content">
		<u--image src="/static/img/schoolLogo.png" width=500rpx height=80rpx></u--image>
		<!-- <text>学校信息界面</text> -->
		
		
		<!-- 轮播图ucharts -->
		<u-swiper
		            :list="roll_images"
		            indicator
		            indicatorMode="line"
		            circular
					height=180
		    ></u-swiper>
			
		<!-- tab页 -->
		<u-tabs :list="tabList" @click="tabClick"></u-tabs>
		
		
		<u-notice-bar :text="noticeText" mode="closable"></u-notice-bar>
		<!-- 切换的内容 -->
		<view class="textStyle">
		<!-- <view style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;font margin-right: 5%;margin-left: 5%;text-indent: 2em;"> -->
			<u--image v-if="current==0" style="margin-left: -7%;" width=660rpx height=130rpx src="/static/img/Infor.gif" ></u--image>
			<u--text lineHeight=40 size=33rpx v-if="current==0" text="重庆财经学院（原重庆工商大学融智学院）成立于2001年，2003年经教育部批准为全日制普通本科层次的独立学院，2011年增列为学士学位授权单位，2016年获批为重庆市第二批整体向应用型转变试点高校。"
			 ></u--text>
			 <u--text lineHeight=40 size=33rpx v-if="current==0" text="2020年经教育部批准转设为独立设置的非营利性民办普通本科高等学校。2021年获批为重庆市新增硕士学位授予立项建设单位。"
			  ></u--text>
			  <u--image v-if="current==0" style="margin-left: -5%;" width=660rpx height=330rpx src="/static/img/Infor2.png" ></u--image>
		</view>
		
		
		<view class="textStyle" >
			<u--text v-if="current==1" lineHeight=40 size=40rpx  style="margin-left: 0%;text-indent: 0em;" text="学科门类"></u--text>
			<u-line v-if="current==1" color="blue" style="margin-right: -10%;margin-left: 0%;" ></u-line>
			<u--text lineHeight=40 size=33rpx v-if="current==1" text="学校现有全日制在校本科生14000余人，有经济学、管理学、工学、文学和艺术学5个学科门类，有重庆市高等学校“十四五”市级重点学科金融学科。十四五期间，学校将全力打造1+2+2重点学科体系，支撑应用型学科生态体系建设。"
			 ></u--text>
			 <u--image v-if="current==1" style="margin-left: -10%;" width=760rpx height=530rpx src="/static/img/disciplines.png" ></u--image>
			<u--text v-if="current==1" lineHeight=40 size=40rpx  style="margin-left: 0%;text-indent: 0em;margin-top: 50rpx;" text="学科专业"></u--text>
			<u-line v-if="current==1" color="blue" style="margin-right: -10%;margin-left: 0%;" ></u-line>
			<u--text lineHeight=40 size=33rpx v-if="current==1" text="学校开设有41个全日制本科专业，其中金融学和会计学2个专业是国家一流专业建设点，金融学、会计学、经济学、物流管理、会展经济与管理、软件工程、土地资源管理等7个专业是重庆市一流专业建设点；经济学、金融学、物流管理、会计学和软件工程5 个专业是重庆市特色专业；金融学学科专业群是重庆市特色学科专业群。"
			  ></u--text>
			<u--image v-if="current==1" style="margin-left: -17%;" width=820rpx height=360rpx src="/static/img/softDiscipline.png" ></u--image>
		</view>
		
		<view class="textStyle" >
			<u--text v-if="current==2" lineHeight=40 size=40rpx  style="margin-left: 0%;text-indent: 0em;" text="综合新闻"></u--text>
			<u-line v-if="current==2" color="blue" style="margin-right: -10%;margin-left: 0%;" ></u-line>
			 <u--text lineHeight=40 size=40rpx style="margin-left: 0%;text-indent: 1em; margin-top: 50rpx;" v-if="current==2"  mode="link" text="【喜报】金奖突破：我校在第八届中国国际“互联网+”大学生创新创业大赛重庆赛区决赛中斩获“2金4银6铜" href="http://www.cfec.edu.cn/info/1053/21114.htm" ></u--text>
			<u--text lineHeight=40 size=40rpx  style="margin-left: 0%;text-indent: 1em;  margin-top: 50rpx;" v-if="current==2"  mode="link" text="【喜报】我校新增1个国家级一流本科专业建设点和1个省级一流本科专业建设点\n" href="http://www.cfec.edu.cn/info/1053/20793.htm" ></u--text>
			<u--text lineHeight=40 size=40rpx  style="margin-left: 0%;text-indent: 1em; margin-top: 50rpx;"v-if="current==2"  mode="link" text="【喜报】我校喜获2项重庆市重大决策咨询研究课题\n" href="http://www.cfec.edu.cn/info/1053/20667.htm" ></u--text>
			<u--text lineHeight=40 size=40rpx  style="margin-left: 0%;text-indent: 1em; margin-top: 50rpx;" v-if="current==2"  mode="link" text="【喜报】新突破：我校两项成果获2021年重庆市教学成果奖\n" href="http://www.cfec.edu.cn/info/1053/20577.htm" ></u--text>
		</view>
		<view class="textStyle" >
			<u--text v-if="current==3" lineHeight=40 size=40rpx  style="margin-top: 0%;text-indent: 0em;" text="教学院部"></u--text>
			<u-line v-if="current==3" color="blue" style="margin-right: -10%;margin-left: 0%;" ></u-line>
			<u--text size=30rpx lineHeight=25 style="margin-top: -5%;" v-if="current==3"  text="
				金融学院023-88968673
				会计学院 023-88968674
				经济学院023-88968669
				新媒体艺术学院 023-88968703
				物流工程学院023-88968663
				财富管理学院023-88968676
				公共管理学院023-88968665
				数字经济学院023-88968671
				讯飞人工智能学院023-88968710
				马克思主义学院023-88968794
				国际商学院023-88968693"
				
			 ></u--text>
			 <u--text v-if="current==3" lineHeight=40 size=40rpx  style="margin-left: 0%;text-indent: 0em; margin-top: 50rpx;" text="管理服务"></u--text>
			 <u-line v-if="current==3" color="blue" style="margin-right: -10%;margin-left: 0%;" ></u-line>
			 <u--text size=30rpx lineHeight=25 style="margin-top: -5%;" v-if="current==3" text="
				党政办公室023-88968651
				党委宣传部023-88968793
				   纪委办公室023-88968718
				   党群工作部023-88968718
				   国际合作与交流处023-88968693
				   继续教育学院023-88968692
				   组织人事部023-88968685
				   科研处023-88968689
				   教务处023-88968702
				   招生就业处023-88968679
				   财务处023-88968653
				   学生工作部023-88968681
				   教师发展中心023-88968798
				   信息化办公室023-88968699
				   图书馆023-88968661
				   学生工作部（保卫处）023-86999110
				   后勤保障中心023-88968684"
				   ></u--text>
		</view>
		<view class="textStyle">
			<u--text v-if="current==4" lineHeight=40 size=40rpx  style="margin-left: 0%;text-indent: 0em;" text="青春“三下乡”"></u--text>
			<u-line v-if="current==4" color="blue" style="margin-right: -10%;margin-left: 0%;" ></u-line>
			<u--text lineHeight=40 size=33rpx v-if="current==4" text="近日，重庆财经学院公共管理学院2022年暑期“三下乡”社会实践团来到重庆市巴南区鱼洞街道金竹村开展为期六天的社会实践活动。"></u--text>
			<u--image v-if="current==4" style=" margin-left:-2%;" width=620rpx height=560rpx src="/static/img/threego.png" ></u--image>
			
			<u--text v-if="current==4" lineHeight=40 size=40rpx  style="margin-left: 0%;text-indent: 0em; margin-top: 50rpx;" text="“书香战疫情 阅读伴成长”读书月"></u--text>
			<u-line v-if="current==4" color="blue" style="margin-right: -10%;margin-left: 0%; " ></u-line>
			<u--text lineHeight=40 size=33rpx v-if="current==4" text="在第27个“世界读书日”到来之际，我校图书馆举办了重庆财经学院“书香战疫情阅读伴成长”2022年读书月系列活动。"></u--text>
			<u--image v-if="current==4" style=" margin-left:-2%;" width=620rpx height=360rpx src="/static/img/readImg.png" ></u--image>
		</view>
		
		<!-- 消息 -->
		<u-loadmore 
						loadmoreText="请前往官网获取更多信息"
						color="#6f6f6f"
						lineColor="#6f6f6f"
						line
		    />
		
		<!-- <u-text>unistudent unite students， unite hearts 团结同学，团结心灵</u-text> -->
		<!-- 底部导航栏 -->
		<u-tabbar
			:value="value6"
			@change="name => value6 = name"
			:fixed="true"
			:placeholder="true"
			:safeAreaInsetBottom="true"
		>
			<u-tabbar-item text="首页" icon="home" ></u-tabbar-item>
			<u-tabbar-item text="数据总览" icon="search" @click='goToDataPlane()'></u-tabbar-item>
			<u-tabbar-item text="报道流程" icon="map" @click='goToRegPlane()'></u-tabbar-item>
			<u-tabbar-item text="性格测试" icon="edit-pen" @click='goToCapPlane()'></u-tabbar-item>
		</u-tabbar>
		
	</view>
	    </view> 
	</template>

<script>
	export default {
		data() {
			return {
				value6: 0,
				noticeText: "欢迎来到重庆财经学院",
				tabList: [{
					name: '校园概况',
				}, {
					name: '专业介绍',
				}, {
					name: '新闻资讯'
				}, {
					name: '机构设置'
				}, {
					name: '学子风采'
				}],
				current:0,
				
				roll_images: [
					'/static/img/schoolInfoimg.png',
					'/static/img/schoolInfoimg2.png',
					'/static/img/schoolInfoimg3.png',
					'/static/img/schoolInfoimg4.png',
				],
			}
		},
		methods: {

			tabClick(item) {
				
				this.current=item.index;
			},
			
			goToCapPlane(){
				uni.navigateTo({
					url: "/pages/CapAssess/CapAssess"
					// icon:'success'
				})
			},
			// tabClick(item) {
			// 	console.log('item', item);
			// },
			
			goToDataPlane(){
				// console.log("dataplane")
				uni.navigateTo({
					url: "/pages/plane/plane"
					// icon:'success'
				})
			},
			goToRegPlane(){
				// console.log('go to regPlane')
				uni.navigateTo({
					url: "/pages/stuGuide/stuGuide"
					// icon:'success'
				})
			},
			goToMainPlane(){
				// console.log('go to regPlane')
				uni.navigateTo({
					url: "/pages/schoolInfo/schoolInfo"
					// icon:'success'
				})
			},


			
			
		}
	}
</script>

<style>
// 以下为 style 区域
	.bg-img{
		position: fixed;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		z-index: -1;
	}
	.textStyle{
		font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; 
		margin-right: 10%;
		margin-left: 10%;
		text-indent: 2em;
		foont:size 80px;
	}

</style>
