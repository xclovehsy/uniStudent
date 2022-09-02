<template>
    <view class="container"> 
          <image class="bg-img" src="/static/img/background4.png"></image>
          <view class="content">
			  
			  
		<u--text size=38 align=center bold text="霍兰德性格测试"></u--text>
		<u--text :text="stuNameWel"  openType="share"  v-show="true" size=20 
></u--text>
		<!-- 表单收集信息 -->
		<u--form
				labelPosition="left"
				:model="model1"
				:rules="rules"
				ref="form1"
				:label-style="{'font-size':'16px'}"
		>
			<u-form-item
					label="电话: "
					prop="userInfo.stuId"
					borderBottom=true
					ref="item1"
					
			>
				<u--input
						v-model="model1.userInfo.stuId"
						border="none"
						@blur = "getStuInfor()"
						placeholder="例:  1533055××××"
						shape=circle
						fontSize=60%
						inputAlign=center
				></u--input>
			</u-form-item>
		</u--form >
		
		
		
		<!-- 十八个问卷============================================================ -->
		<!-- 十八个问卷============================================================ -->
		<!-- 十八个问卷============================================================ -->
		<!-- 十八个问卷============================================================ -->
		
		
		<u--text text="快来填写下面的性格测试吧!"  openType="share"  v-show="true" size=25 
		align=center color=#000000></u--text>
		<u--text  class="content" type="info"  size=19 bold text="🎉问题1.周末没事干时喜欢和朋友出去玩的"></u--text>
		<u-rate :count="5"  v-model="model1.userInfo.data.value1" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🧑‍🤝‍🧑问题2.和一群没那么熟的人在一起时，我能一起很好的聊天"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value2" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info"size=19 bold text="🎎问题3.我很擅长和陌生人沟通"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value3" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🙋问题4.我愿意积极争当班干部"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value4" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🙌问题5.我会觉得我更胜任某个职位"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value5"size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🤳问题6.我喜欢不时夸赞一下自己取得的成就"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value6" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="👩问题7.我乐于按照父母和老师的安排做事"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value7"size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="👨‍🏭问题8.我愿意从事工资相对较少但相对稳定的职业"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value8" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="💬问题9.和别人交流时，我总是听取别人的观点"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value9" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🔧问题10.我喜欢使用钳子，螺丝刀，万用表等工具"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value10" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="💴问题11.如果掌握一门精湛的手艺并能以此赚到足够多的钱，我感到很满足"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value11" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🔎问题12.我小时候经常把问题拆开，把里面看个究竟"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value12" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🤵问题13.我的理想是当一名科学家"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value13" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🤔问题14.我做题时常常有了思路就跳过"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value14" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🧑‍💻问题15.我喜欢抽象思维的工作，不喜欢动手的工作"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value15" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🎬问题16.看情感影片时，我经常红了眼眶"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value16" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🤣问题17.当接受新任务后，我喜欢以自己独特的方式完成它"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value17" size=25 gutter="26"></u-rate>
		<u--text class="content"   type="info" size=19 bold text="🎶问题18.我常陶醉于音乐之中"></u--text>
		<u-rate :count="5" v-model="model1.userInfo.data.value18" size=25 gutter="26"></u-rate><br>
		
		
		<!-- test -->
		<!-- <text>{{model1}}</text> -->
		
		<u-button @click="showReport()" type="primary" icon="checkmark" :plain="false" shape="circle" text="点我性格测试哟" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))" ></u-button>
				
		<u-button @click="clear()" type="primary" icon="close-circle" :plain="true" shape="circle" text="重新填写" class="custom-style"></u-button>
		
		
		
		<!-- 性格测试结果 ===============================================================================-->
		<!-- 个人信息 -->
		<u-divider  text="您的性格测试结果如下" :dashed="true" v-show="assShow" textSize="23" textColor="black" lineColor="black"></u-divider>
		<u--text :text="model1.userInfo.name2" openType="share"  v-show="assShow" size=21 bold></u--text>
		<!-- <u--text :text="model1.userInfo.stuId" openType="share"  v-show="assShow"></u--text> -->
		<u--text style="padding-left: 1em;" :text="model1.userInfo.addr" openType="share"  v-show="assShow"></u--text>
		<u--text style="padding-left: 1em;":text="model1.userInfo.dis" openType="share"  v-show="assShow"></u--text>
		
	<!-- 	
		<text>{{model1.userInfo.name}}</text>
		<text>{{model1.userInfo.stuId}}</text>
		<text>{{model1.userInfo.addr}}</text>
		<text>{{model1.userInfo.dis}}</text> -->
		
		<u--text text="⭐你的性格类型是: \n" openType="share" color=black size=22 v-show="assShow"></u--text>
		
		<u--textarea style="padding-left: 2em;" v-model="model1.userInfo.stuType"  v-show="assShow"></u--textarea>
		
		<u--text text="⭐你的性格特点是: \n" openType="share" color=black size=22 v-show="assShow"></u--text>

		<u--textarea style="padding-left: 2em;padding-right: 2em;" v-model="model1.userInfo.trait"  v-show="assShow" autoHeight></u--textarea>
		
		<!-- 雷达图===================================================== -->
		<canvas canvas-id="bQASfDemsxJtNjLTXlnseDWeqoSILkiz" id="bQASfDemsxJtNjLTXlnseDWeqoSILkiz" class="charts" @touchend="tap" v-show="assShow"/>
		<!-- <canvas canvas-id="bQASfDemsxJtNjLTXlnseDWeqoSILkiz" id="bQASfDemsxJtNjLTXlnseDWeqoSILkiz"  class="charts"@touchend="tap" v-show="assShow"/> -->
		<!-- <text>{{model1.userInfo}}</text> -->
		<br><br>
		
		
		
		
		<!-- 学生信息查找失败 -->
		<!-- <u-popup :show="erroShow" @close="erroClose()" @open="erroOpen()">
			<view>
				<text>{{msg}}</text>
			</view>
		</u-popup> -->
		<!-- <u-button @click="erroShow = true">打开</u-button> -->
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
				<u--text :text="popMsg" v-show="msgShow" align=center bold ></u--text>
				<!-- <u-button v-show="buShow" type="primary" icon="checkmark" :plain="false" shape="circle" text="返回" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button> -->
				<u-button v-show="returnShow" @click="popClose()" type="primary" style="width: 60%;" icon="arrow-leftward" :plain="false" shape="circle" text="返回填写信息" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button>
				<!-- <u-button @click="clear()" type="primary" icon="close-circle" :plain="true" shape="circle" text="清空" class="custom-style"></u-button> -->
				<navigator url="/pages/info/info" open-type="navigate" hover-class="navigator-hover">
					<u-button v-show="uploadShow" @click="popClose()" type="primary" style="width: 60%;" icon="edit-pen" :plain="true" shape="circle" text="上传个人信息" class="custom-style" ></u-button>
				</navigator>
			</view>
		</u-popup>
		
		<!-- <u-button @click="openPopup()"> test</u-button> -->
		
		</view>
		<!-- 底部导航栏 -->
		<u-tabbar
			:value="value6"
			@change="name => value6 = name"
			:fixed="true"
			:placeholder="true"
			:safeAreaInsetBottom="true"
		>
			<u-tabbar-item text="首页" icon="home" @click='goToMainPlane()'></u-tabbar-item>
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
				stuNameWel: "请输入您的电话号码:",
				statusCode : false,
				cWidth: 750,
				cHeight: 500,
				// showSex: false,
				value6:3,
				assShow: false,
				erroShow: false,
				msg:'',
				// confirmType:'',
				// traitShow: true,
				model1: {
					userInfo: {
						name: '',
						stuId: '',
						data:{
							value1: 0,
							value2: 0,
							value3: 0,
							value4: 0,
							value5: 0,
							value6: 0,
							value7: 0,
							value8: 0,
							value9: 0,
							value10: 0,
							value11: 0,
							value12: 0,
							value13: 0,
							value14: 0,
							value15: 0,
							value16: 0,
							value17: 0,
							value18: 0,
						},
						stuType:'',
						trait:'',
						addr:'',
						dis:'',
						gender:0,
					},
				},
				// 弹窗的属性
				popShow: false,
				msgShow: true,
				returnShow:false,
				uploadShow: true,
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
					'userInfo.stuId':  [
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
			}
		},
		methods: {
			// erroOpen() {
			//   // console.log('open');
			// },
			// erroClose() {
			//   this.erroShow = false
			//   // console.log('close');
			//   uni.navigateTo({
			//   	url: "/pages/info/info"
			//   	// icon:'success'
			//   })
			// },
			getStuInfor(){
				this.assShow = false;
				this.statusCode = false;
				if(this.model1.userInfo.stuId == ''){
					this.popMsg = "请填写电话号码"
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
					// this.CapReportShow = false
					this.openPopup()
				}else{
					// console.log("test")
					uni.request({
						  header: {
									'Content-Type': 'application/x-www-form-urlencoded'
							   }, 
						  url: "http://121.4.95.22:10085/api/capacity/getStuInfo", //仅为示例，并非真实接口地址。
						   method: 'GET',
							   data: {
									stuId:this.model1.userInfo.stuId,
							   },
						   //dataType:'json',
						   success: (res) => {
									// console.log(res);
									// alert(res.data.message);
									// console.log(res)
									if(res.data.code == 1){
										// 数据库中有该学生
										this.statusCode = true;
										this.model1.userInfo.name = res.data.name
										this.model1.userInfo.name2 ="🌹亲爱的"+res.data.name+"，你好！"
										this.stuNameWel = "欢迎 " + res.data.name + " 参与性格测试"
										this.model1.msg = res.data.msg
									}else{
										this.popMsg = "电话有误，或上传个人信息"
										this.msgShow = true
										this.returnShow = true
										this.uploadShow = true
										// this.CapReportShow = false
										this.openPopup()
										// 数据库中没有该学生
										// this.msg = res.data.msg
										// this.stuNameWel = "请先填写个人信息"
										// this.erroShow = true
									}
									
							   } 
						   })
				}
				
			},
			clear(){
				this.model1.userInfo.data = {
							value1: 0,
							value2: 0,
							value3: 0,
							value4: 0,
							value5: 0,
							value6: 0,
							value7: 0,
							value8: 0,
							value9: 0,
							value10: 0,
							value11: 0,
							value12: 0,
							value13: 0,
							value14: 0,
							value15: 0,
							value16: 0,
							value17: 0,
							value18: 0,
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
			
			
			// 展示性格报告
			showReport(){
				if(this.statusCode == false){
					this.popMsg = "请先填写电话号码"
					this.msgShow = true
					this.returnShow = true
					this.uploadShow = false
					// this.CapReportShow = false
					this.openPopup()
				}else{
					//这里的 750 对应 css .charts 的 width
					this.cWidth = uni.upx2px(750);
					//这里的 500 对应 css .charts 的 height
					this.cHeight = uni.upx2px(500);
					this.getServerDataAndDrawRadix();
					this.assShow = true;
					
				}
				
			},
			getServerDataAndDrawRadix() {
				
				uni.request({
				  header: {
							'Content-Type': 'application/x-www-form-urlencoded'
					   }, 
				  url: "http://121.4.95.22:10085/api/capacity/CapAss", //仅为示例，并非真实接口地址。
				   method: 'GET',
					   data: {
							stuId:this.model1.userInfo.stuId,
							value1: this.model1.userInfo.data.value1,
							value2: this.model1.userInfo.data.value2,
							value3: this.model1.userInfo.data.value3,
							value4: this.model1.userInfo.data.value4,
							value5: this.model1.userInfo.data.value5,
							value6: this.model1.userInfo.data.value6,
							value7: this.model1.userInfo.data.value7,
							value8: this.model1.userInfo.data.value8,
							value9: this.model1.userInfo.data.value9,
							value10: this.model1.userInfo.data.value10,
							value11: this.model1.userInfo.data.value11,
							value12: this.model1.userInfo.data.value12,
							value13: this.model1.userInfo.data.value13,
							value14: this.model1.userInfo.data.value14,
							value15: this.model1.userInfo.data.value15,
							value16: this.model1.userInfo.data.value16,
							value17: this.model1.userInfo.data.value17,
							value18: this.model1.userInfo.data.value18,
					   },

				   success: (res) => {
							// console.log("test")
							// console.log(res.data)
							// console.log(res.)
							// console.log(res.data.data.stuType)
							console.log("test===========")
							console.log(res.data)
							this.model1.userInfo.trait =res.data.data.stuTrait
							this.model1.userInfo.stuType = res.data.data.stuType
							this.model1.userInfo.addr ="🗺生源地："+res.data.stuCity
							this.model1.userInfo.dis = "🎩专业："+res.data.stuDis
							this.model1.userInfo.gender = res.data.gender
							
							// this.drawCharts('bQASfDemsxJtNjLTXlnseDWeqoSILkiz', res);
							// console.log(res.data.data.trait.categories)
							// console.log(res.data.data.trait.series[0].data)
							// this.data = {
							//     categories: res.data.data.trait.categories,
							//     series: [
							//       {
							//         name: "性格",
							//         data: res.data.data.trait.series[0].data,
							//       }
							//     ]
						 //  };
						 
						  this.drawCharts('bQASfDemsxJtNjLTXlnseDWeqoSILkiz', res.data.data.trait);
					   } 
				   })
			      //模拟从服务器获取数据时的延时
			      // setTimeout(() => {
			      //   //模拟服务器返回数据，如果数据格式和标准格式不同，需自行按下面的格式拼接
			      //   let res = {
			      //       categories: ["维度1","维度2","维度3","维度4","维度5","维度6"],
			      //       series: [
			      //         {
			      //           name: "成交量1",
			      //           data: [90,110,165,195,187,172]
			      //         },
			      //         {
			      //           name: "成交量2",
			      //           data: [190,210,105,35,27,102]
			      //         }
			      //       ]
			      //     };
			      //   this.drawCharts('bQASfDemsxJtNjLTXlnseDWeqoSILkiz', res);
			      // }, 500);
			    },
			    drawCharts(id,data){
			      const ctx = uni.createCanvasContext(id, this);
				  if(this.model1.userInfo.gender == 1){
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
			    },
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
			  
		}
	}
</script>

<style>
	.content{
		font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
		line-height: 300%;
		foont:size 80px;
		padding-left: 5%;
		padding-right: 5%;
	}
	.u-text{
		font-family: 'Times New Roman', Times, serif;
		font-weight: bold;
		border-radius: 20%;
		box-sizing: border-box;
		border-bottom: 10px;
		border-width: 15px;
	}
	.u-rate{
		padding-left: 5%;
		size: 28rpx;
	}
	.btn {
	    width: 500rpx;
	    height: 72rpx;
	    border: 2rpx solid #188af4;
	    border-radius: 36rpx;
	    /* margin: auto; */
	    background: transparent;
	    font-size: 28rpx;
	    line-height: 72rpx;
	    color: #faf6f4;
		background-color: dodgerblue;
		}
	.btn2{
		width: 500rpx;
		height: 72rpx;
		border: 2rpx solid #2984f4;
		border-radius: 36rpx;
		background: transparent;
		font-size: 28rpx;
		line-height: 72rpx;
		color: deepskyblue;
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
	.custom-style {
			margin-top: 10px;
			color: #ffffff;
			width: 400rpx;
			font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
		}
	 .charts{
		 margin-bottom: 0%;
		 margin-left: -5%;
		 margin-right:0%;
		width: 410px;
		height: 320px;
		background-color: #ffffff;
		/* margin: auto auto; */
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
	  .u-popup-slot {
	  	width: 200px;
	  	height: 150px;
	  	// @include flex;
	  	justify-content: center;
	  	align-items: center;
	  }
</style>
