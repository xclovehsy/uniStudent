<template>
    <view class="container"> 
          <image class="bg-img" src="/static/img/background4.png"></image>
          <view class="content">
		<u-divider text="性格测试" textSize="20" style="margin-top: 5%;" lineColor="black" textColor="black"></u-divider>
		<navigator url="/pages/capReport/capReport" open-type="navigate" hover-class="navigator-hover">
			<u-button type="primary" icon="file-text" :plain="false" shape="circle" text="查看性格报告" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button>
		</navigator>
		
		<navigator url="/pages/capTest/capTest" open-type="navigate" hover-class="navigator-hover">
			<u-button type="primary" icon="edit-pen" :plain="true" shape="circle" text="性格测试" class="custom-style"></u-button>
		</navigator>
		
		<u-divider text="欢迎来到弹幕时间" textSize="20" style="margin-top: 30%;" lineColor="black" textColor="black"></u-divider>
		<u--form
				labelPosition="left"
				:model="model1"
				:rules="rules"
				ref="form1"
				:label-style="{'font-size':'16px'}"
		>
			<u-form-item
					label="弹幕"
					prop="userInfo.text"
					borderBottom
					ref="item1"
			>
				<u--input
						v-model="model1.userInfo.text"
						border="none"
						shape=circle
						fontSize=60%
						inputAlign=center
						placeholder="我已出仓,感觉良好"
				></u--input>
			</u-form-item>
			
		</u--form>
		<u-button @click="uploadBarrage()" type="primary" icon="thumb-up" :plain="true" shape="circle" text="发送弹幕" class="custom-style"  ></u-button>
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
		>
			<view
				class="u-popup-slot"
				:style="{
					width: ['bottom', 'top'].includes(popupData.mode) ? '750rpx' : '200px',
					marginTop: ['left', 'right'].includes(popupData.mode) ? '480rpx' : '0',
				}"
			>	
				<u--text :text="popMsg" v-show="msgShow" align=center bold style="margin-top: 15%;"  ></u--text>
				
			</view>
		</u-popup>
		
		<!-- <u-button @click="openPopup()"> test</u-button> -->
		
		<!-- <u-button type="primary" text="查看性格报告"></u-button> -->
		<!-- <u-button type="primary" text="性格测试"></u-button> -->
		
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
			<u-tabbar-item text="性格测试" icon="edit-pen"></u-tabbar-item>
		</u-tabbar>
	</view>
	    </view> 
	</template>

<script>
	export default {
		data() {
			return {
				value6:3,
				model1: {
					userInfo: {
						text: '',
					},
					
				},
				popShow: false,
				msgShow: true,
				popupData: {
					overlay: true,
						overlay: true,
						mode: 'bottom',
						borderRadius: '',
						closeable: true,
						closeOnClickOverlay: true
				},
				popMsg: "您所提交的信息有误",
				rules: {
					'userInfo.text': {
						type: 'string',
						required: true,
						message: '请输入弹幕内容',
						trigger: ['blur', 'change']
					},
					
				},
			}
		},
		methods: {
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
				
			uploadBarrage(){
				this.popMsg = '';
				if(this.model1.userInfo.text == ''){
					this.popMsg = "请输入弹幕内容";
					this.openPopup();
					
				}else{
					uni.request({
					  header: {
								'Content-Type': 'application/x-www-form-urlencoded'
						   }, 
					  url: "http://121.4.95.22:10085/api/student/uploadBarrage", //仅为示例，并非真实接口地址。
					   method: 'GET',
						   data: {
								text: this.model1.userInfo.text,
						   },
					   //dataType:'json',
					   success: (res) => {
								// console.log(res);
								if(res.data.code == 1){
									this.model1.userInfo.text = '';
								}
								this.popMsg = res.data.msg;
								this.openPopup();
						   } 
					   })
				}
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
			}
		}
	}
</script>

<style>
	.custom-style {
		margin-top: 10px;
		color: #ffffff;
		width: 550rpx;
		height: 100rpx;
		/* font-size: 50px; */
		font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
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
	.u-form-item{
		padding-left: 5%;
		/* size: 50px; */
		width:80%;
		/* height: 20px; */
	}
	.u-input{
		font-size: 35px;
		height: 50%;
		border-style: dashed;
	}
	.u-popup-slot {
		width: 200px;
		height: 150px;
		@include flex;
		justify-content: center;
		align-items: center;
	}

</style>
