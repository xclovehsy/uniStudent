<!-- 新的 -->
<template>
    <view class="container"> 
          <image class="bg-img" src="/static/img/background4.png"></image>
          <view class="content">
		<u--text   size=38 align=center bold text="性格测试报告查询"></u--text><br>
		<u--text   text="请输入您的姓名和电话" size=20></u--text>
		<!-- <u--text size=38 align=center bold text="性格测试报告查询"></u--text>
		<u--text text="请输入您的姓名和电话"  openType="share"  v-show="true" size=20 -->
		</u--text>
		<u--form
				labelPosition="left"
				:model="model1"
				:rules="rules"
				ref="form1"
				:label-style="{'font-size':'16px'}"
		>
			<u-form-item
					label="姓名"
					prop="userInfo.name"
					borderBottom
					ref="item1"
			>
				<u--input
						v-model="model1.userInfo.name"
						border="none"
						shape=circle
						fontSize=60%
						inputAlign=center
						placeholder="请输入姓名"
				></u--input>
			</u-form-item>
			<u-form-item
					label="电话"
					prop="userInfo.stuId"
					borderBottom
					ref="item1"
			>
				<u--input
						v-model="model1.userInfo.stuId"
						border="none"
						shape=circle
						fontSize=60%
						inputAlign=center
						placeholder="请输入电话"
				></u--input>
			</u-form-item>
		</u--form>
		
		<u-button @click="showReport()" type="primary" icon="search" :plain="false" shape="circle" text="查看性格测试报告" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))" ></u-button>
		<!-- <text>{{model1.userInfo}}</text> -->
		<!-- =================================性格报告=================================== -->
		<!-- <u-button></u-button> -->
		<!-- <u--text :show="true"> test</u--text> -->
		<!-- <u--text text="你是一个性格开朗、乐观的人，。。。。\n" openType="share" type="success" v-show="assShow"></u--text> -->
		
		<!-- <text></text>
		<text>一张性格雷达图</text> -->
		<!-- <canvas canvas-id="bQASfDemsxJtNjLTXlnseDWeqoSILkiz" id="bQASfDemsxJtNjLTXlnseDWeqoSILkiz" class="charts" @touchend="tap"/> -->
		<!-- 性格测试结果 ===============================================================================-->
			<!-- 个人信息 -->
			<!-- <u-divider style="margin-left: -10%;margin-right:-10%;"  text="您的性格测试结果如下" :dashed="true" v-show="assShow" textSize="23" textColor="black"  lineColor="black"></u-divider>
			<u--text :text="model1.userInfo.name2" openType="share"  v-show="assShow" size=21 bold></u--text>
			<br><u--text style="padding-left: 1em;" :text="model1.userInfo.addr" openType="share"  v-show="assShow"></u--text>
			<u--text style="padding-left: 1em;":text="model1.userInfo.dis" openType="share"  v-show="assShow"></u--text> -->
			
		<!-- 	
			<text>{{model1.userInfo.name}}</text>
			<text>{{model1.userInfo.stuId}}</text>
			<text>{{model1.userInfo.addr}}</text>
			<text>{{model1.userInfo.dis}}</text> -->
			
			<!-- <br><u--text text="⭐你的性格类型近似于: \n" openType="share" color=black size=22 v-show="assShow"></u--text>
			
			<u--textarea style="padding-left: 2em;" v-model="model1.userInfo.stuType"  v-show="assShow"></u--textarea>
			
			<br><u--text text="⭐你的性格特点近似于: \n" openType="share" color=black size=22 v-show="assShow"></u--text>
			<u--textarea style="padding-left: 2em;padding-right: 2em;" v-model="model1.userInfo.trait"  v-show="assShow" autoHeight></u--textarea>
			 -->
			<u-divider  text="您的性格测试结果如下" :dashed="true" v-show="assShow" textSize="23" textColor="black" lineColor="black"></u-divider>
				<u--text :text="model1.userInfo.name2" openType="share"  v-show="assShow" size=21 bold style="line-height: 300%;
		foont:size 80px;"></u--text>
				<!-- <u--text :text="model1.userInfo.stuId" openType="share"  v-show="assShow"></u--text> -->
				<u--text style="padding-left: 1em;line-height: 300%;
		foont:size 80px;" :text="model1.userInfo.addr" openType="share"  v-show="assShow"></u--text>
				<u--text style="padding-left: 1em;line-height: 300%;
		foont:size 80px;":text="model1.userInfo.dis" openType="share"  v-show="assShow"></u--text>
				
			<!-- 	
				<text>{{model1.userInfo.name}}</text>
				<text>{{model1.userInfo.stuId}}</text>
				<text>{{model1.userInfo.addr}}</text>
				<text>{{model1.userInfo.dis}}</text> -->
				
				<u--text text="⭐你的性格类型是: \n" openType="share" color=black size=22 v-show="assShow" style="line-height: 300%;
		foont:size 80px;"></u--text>
				
				<u--textarea style="padding-left: 2em;" v-model="model1.userInfo.stuType"  v-show="assShow"></u--textarea>
				
				<u--text text="⭐你的性格特点是: \n" openType="share" color=black size=22 v-show="assShow" style="line-height: 300%;
		foont:size 80px;"></u--text>
			
				<u--textarea style="padding-left: 2em;padding-right: 2em;" v-model="model1.userInfo.trait"  v-show="assShow" autoHeight></u--textarea>
			
			<!-- 雷达图===================================================== -->
			<canvas canvas-id="bQASfDemsxJtNjLTXlnseDWeqoSILkiz" id="bQASfDemsxJtNjLTXlnseDWeqoSILkiz"  class="charts"
			@touchend="tap" v-show="assShow"/>
			
			
			
			<!-- 消息弹窗 -->
			<u-popup :show="erroshow" @close="erroClose()" @open="erroOpen()">
				<view>
					<text>{{erroMes}}</text>
				</view>
			</u-popup>
			<!-- <text>{{model1.userInfo}}</text> -->
			</u-cell-group>
			<u-popup
				:safeAreaInsetBottom="true"
				:safeAreaInsetTop="true"
				:mode="popupData.mode"
				:show="popShow"
				:round="popupData.round"
				:overlay="popupData.overlay"
				:borderRadius="popupData.borderRadius"
				:closeable="popupData.closeable"
				:closeOnClickOverlay="popupData.closeOnClickOverlay"
				@close="popClose"
				@open="popOpen"
				bgColor=#ffffff
			>
				<view
					class="u-popup-slot"
					:style="{
						width: ['bottom', 'top'].includes(popupData.mode) ? '750rpx' : '200px',
						marginTop: ['left', 'right'].includes(popupData.mode) ? '480rpx' : '0',
					}"
				>	
					<u--text :text="popMsg" v-show="msgShow" align=center bold style="margin-top: 15%;"  ></u--text>
					<!-- <u-button v-show="buShow" type="primary" icon="checkmark" :plain="false" shape="circle" text="返回" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button> -->
					
					<!-- 返回 -->
					<u-button v-show="returnShow" @click="popClose()" type="primary" style="width: 60%;" icon="arrow-leftward" :plain="false" shape="circle" text="返回填写信息" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button>
					<!-- <u-button @click="clear()" type="primary" icon="close-circle" :plain="true" shape="circle" text="清空" class="custom-style"></u-button> -->
					
					<!-- 上传个人信息界面 -->
					<navigator url="/pages/info/info" open-type="navigate" hover-class="navigator-hover">
						<u-button v-show="uploadShow" @click="popClose()" type="primary" style="width: 60%;" icon="edit-pen" :plain="true" shape="circle" text="上传个人信息" class="custom-style" ></u-button>
					</navigator>
					
					<!-- 跳转到性格测试界面 -->
					<navigator url="/pages/capTest/capTest" open-type="navigate" hover-class="navigator-hover">
						<u-button v-show="CapReportShow" @click="popClose()" type="primary"style="width: 60%;" icon="file-text-fill" :plain="true" shape="circle" text="性格测试" class="custom-style" ></u-button>
						<!-- <u-button icon="edit-pen" type="primary" text="能力测试" shape="circle" class="btn" :plain="true" ></u-button> -->
					</navigator>

				</view>
			</u-popup>
			</view>
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
	
</template>

<script>
import uCharts from '@/js_sdk/u-charts/u-charts.js';
var uChartsInstance = {};
export default {
	data() {
		return {
			cWidth: 750,
			cHeight: 500,
			showSex: false,
			value6:3,
			assShow: false,
			erroshow: false,
			erroMes:"",
			model1: {
				userInfo: {
					name: '',
					stuId: '',
					stuType:'',
					trait:'',
					addr:'',
					dis:'',
					gender: 1,
				},
			},
			// buShow: true,
			popShow: false,
			msgShow: false,
			returnShow:false,
			uploadShow: false,
			CapReportShow: false,
			popupData: {
				overlay: true,
				mode: 'center',
				round: 10,
				closeOnClickOverlay: true
			},
			popMsg: "您所提交的信息有误",
			rules: {
				'userInfo.name': {
					type: 'string',
					required: true,
					message: '请填写姓名',
					trigger: ['blur', 'change']
				},
				
				'userInfo.stuId': [
						{
							required: true, 
							message: '请输入手机号',
							trigger: ['change','blur'],
						},
						{
							// 自定义验证函数，见上说明
							validator: (rule, value, callback) => {
								// 上面有说，返回true表示校验通过，返回false表示不通过
								// uni.$u.test.mobile()就是返回true或者false的
								return uni.$u.test.mobile(value);
							},
							message: '手机号码不正确',
							// 触发器可以同时用blur和change
							trigger: ['change','blur'],
						}
					],
			},
			radio: '',
			switchVal: false
		};
	},
	onReady() {
	  },
	methods: {
		openPopup() {
			this.popupData = {
				overlay: true,
				mode: 'center',
				round: 10,
				closeOnClickOverlay: true
			}
			
			uni.$u.sleep().then(() => {
				this.popShow = !this.popShow
			})
		},
		navigateBack() {
			uni.navigateBack()
		},
		popOpen() {
			// console.log('open');
		},
		popClose() {
			this.popShow = false
			// console.log('close');
		},
		erroOpen() {
		  // console.log('open');
		},
		erroClose() {
		  this.erroshow = false;
		  // console.log('close');
		},
		// 展示性格报告
		showReport(){
			this.assShow = false
			if(this.model1.userInfo.name == '' || this.model1.userInfo.stuId == ''){
				this.popMsg = "请填写个人信息"
				this.msgShow = true
				this.returnShow = true
				this.uploadShow = false
				this.CapReportShow = false
				this.openPopup()
			}else if(this.model1.userInfo.stuId.length != 11){
				this.popMsg = "请填写正确的电话号码"
				this.msgShow = true
				this.returnShow = true
				this.uploadShow = false
				this.CapReportShow = false
				this.openPopup()
			}else{
				uni.request({
							  header: {
										'Content-Type': 'application/x-www-form-urlencoded'
								   }, 
							  url: "http://121.4.95.22:10085/api/capacity/getStuCapAss", //仅为示例，并非真实接口地址。
							   method: 'GET',
								   data: {
									   // stuName:this.model1.userInfo.name,
									   stuId: this.model1.userInfo.stuId,
									   name:this.model1.userInfo.name,
								   },
							   //dataType:'json',
							   success: (res) => {
										console.log(res);
										if(res.data.code == 0){
											this.popMsg = "请填写个人信息"
											this.msgShow = true
											this.returnShow = true
											this.uploadShow = false
											this.CapReportShow = false
											this.openPopup()
										}else if(res.data.code == 1){
											this.popMsg = "您所填写的姓名有误"
											this.msgShow = true
											this.returnShow = true
											this.uploadShow = false
											this.CapReportShow = false
											this.openPopup()
										}else if(res.data.code == 2){
											this.popMsg = "电话有误，请上传个人信息"
											this.msgShow = true
											this.returnShow = true
											this.uploadShow = true
											this.CapReportShow = false
											this.openPopup()
										}else if(res.data.code == 3){
											this.popMsg = "请先进行性格测试"
											this.msgShow = true
											this.returnShow = false
											this.uploadShow = false
											this.CapReportShow = true
											this.openPopup()
										}else if(res.data.code == 4){
											// 成功获取信息
											this.model1.userInfo.name = res.data.stuName
											this.model1.userInfo.name2 ="🌹亲爱的"+res.data.stuName+"，你好！"
											this.model1.userInfo.stuId = res.data.stuId
											this.model1.userInfo.stuType = res.data.data.stuType
											this.model1.userInfo.trait = res.data.data.stuTrait
											this.model1.userInfo.addr ="🗺生源地：" +res.data.stuCity
											this.model1.userInfo.dis ="🎩专业："+ res.data.stuDis
											this.model1.userInfo.gender = res.data.gender;
				//这里的 750 对应 css .charts 的 width
											// this.cWidth = uni.upx2px(750);
											// //这里的 500 对应 css .charts 的 height
											// this.cHeight = uni.upx2px(200);
											this.cWidth = uni.upx2px(750);
											//这里的 500 对应 css .charts 的 height
											this.cHeight = uni.upx2px(500);
											// this.getServerData();
											this.assShow = true;
											this.drawCharts('bQASfDemsxJtNjLTXlnseDWeqoSILkiz', res.data.data.trait);
											
										}else{
											this.popMsg = "其他错误，请联系开发人员"
											this.msgShow = true
											this.returnShow = false
											this.uploadShow = false
											this.CapReportShow = false
											this.openPopup()
										}
										
										
										
										//-----------------------等后端实现------------------------------------------
										// console.log(res.data.data.trait)
										// console.log(res.data.data.trait)
										  
										
								   } 
							   })
			}
			
			
				   
				   
			
		},

		goToCapPlane(){
			uni.navigateTo({
				url: "/pages/CapAssess/CapAssess"
				// icon:'success'
			})
		},

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
		getServerData() {
		      //模拟从服务器获取数据时的延时
		      
		    },
		    drawCharts(id,data){
				if(this.model1.userInfo.gender == 1){
					const ctx = uni.createCanvasContext(id, this);
					uChartsInstance[id] = new uCharts({
					  type: "radar",
					  context: ctx,
					  width: this.cWidth,
					  height: this.cHeight,
					  categories: data.categories,
					  series: data.series,
					  animation: true,
					  background: "#FFFFFF",
					  color: ["#1890FF","#91CB74","#FAC858","#EE6666","#73C0DE","#3CA272","#FC8452","#9A60B4","#ea7ccc"],
					  padding: [5,5,5,5],
					  dataLabel: false,
					  legend: {
					    show: false,
					    position: "right",
					    lineHeight: 25
					  },
					  extra: {
					    radar: {
					      gridType: "circle",
					      gridColor: "#CCCCCC",
					      gridCount: 3,
					      opacity: 0.2,
					      max: 5
					    }
					  }
					});
				}else{
					const ctx = uni.createCanvasContext(id, this);
					uChartsInstance[id] = new uCharts({
					  type: "radar",
					  context: ctx,
					  width: this.cWidth,
					  height: this.cHeight,
					  categories: data.categories,
					  series: data.series,
					  animation: true,
					  background: "#FFFFFF",
					  color: ["#ffaaff","#91CB74","#FAC858","#EE6666","#73C0DE","#3CA272","#FC8452","#9A60B4","#ea7ccc"],
					  padding: [5,5,5,5],
					  dataLabel: false,
					  legend: {
					    show: false,
					    position: "right",
					    lineHeight: 25
					  },
					  extra: {
					    radar: {
					      gridType: "circle",
					      gridColor: "#CCCCCC",
					      gridCount: 3,
					      opacity: 0.2,
					      max: 5
					    }
					  }
					});
				}
				
		      
		    },
		    tap(e){
		      uChartsInstance[e.target.id].touchLegend(e);
		      uChartsInstance[e.target.id].showToolTip(e);
		    }
		  },

};
</script>
<style>
	.u-text{
		font-family: 'Times New Roman', Times, serif;
		font-weight: bold;
		border-radius: 20%;
		box-sizing: border-box;
		border-bottom: 10px;
		border-width: 15px;
	}
	.u-input{
		font-size: 35px;
		height: 50%;
		border-style: dashed;
	}
	.u-form-item{
		padding-left: 5%;
		/* size: 50px; */
		width:80%;
		/* height: 20px; */
	}
	.u-popup-slot {
		width: 200px;
		height: 150px;
		// @include flex;
		justify-content: center;
		align-items: center;
	}
	.custom-style {
			margin-top: 10px;
			color: #ffffff;
			width: 400rpx;
			font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
		}
	.btn {
	    width: 500rpx;
	    height: 72rpx;
	    border: 2rpx solid #f4f4f4;
	    border-radius: 36rpx;
	    /* margin: auto; */
	    background: transparent;
	    font-size: 28rpx;
	    line-height: 72rpx;
	    color: #faf6f4;
		background-color: dodgerblue;
	    
		}
	  .charts{
			margin-bottom: 0%;
			margin-left: -4%;
			margin-right:0%;
	  		width: 440px;
	  		height: 360px;
	  		background-color: #ffffff;
	   }
	   // 以下为 style 区域
	   .bg-img{
	   	position: fixed;
	   	width: 100%;
	   	height: 100%;
	   	top: 0;
	   	left: 0;
	   	z-index: -1;
	   }
	   .content{
	   	font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
	   	padding-left: 5%;
	   	padding-right: 5%;
	   }
</style>