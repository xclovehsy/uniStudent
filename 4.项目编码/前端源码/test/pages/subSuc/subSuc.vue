<template>
    <view class="container"> 
          <image class="bg-img" src="/static/img/background12.png"></image>
          <view class="content">
			  
			  
		<image class="imgcontent" src='/static/img/successLogo.png' style="height: 240px;width: 240px;"></image><br>
		<view>
			
			
			<navigator url="/pages/schoolInfo/schoolInfo" open-type="navigate" hover-class="navigator-hover">
				<u-button icon="home" type="primary" text="查看学校信息" class="btn" shape="circle" color="linear-gradient(to right, rgb(15, 104, 211), rgb(18, 116, 245))"></u-button>
			</navigator>
			<navigator url="/pages/capTest/capTest" open-type="navigate" hover-class="navigator-hover">
				<!-- <u-button icon="edit-pen" type="primary" text="能力测试"  shape="circle" class="btn" color="linear-gradient(to right, rgb(15, 104, 211), rgb(18, 116, 245))"></u-button> -->
				<u-button icon="edit-pen" type="primary" text="能力测试" shape="circle" class="btn" :plain="true" ></u-button>
			</navigator>
			
			<!-- <navigator url="/pages/info/info" open-type="navigate" hover-class="navigator-hover">
				<u-button icon="order" type="primary" text="返回信息收集界面" shape="circle" class="btn" :plain="true" ></u-button>
			</navigator> -->
<!-- 			<u-button type="primary" icon="checkmark" :plain="false" shape="circle" text="返回信息收集界面" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button>

			<u-button type="primary" icon="close-circle" :plain="true" shape="circle" text="查看学校信息" class="custom-style"></u-button>

			<u-button type="primary" icon="checkmark" :plain="false" shape="circle" text="能力测试" class="custom-style" color="linear-gradient(to right, rgb(14, 87, 182), rgb(18, 116, 245))"></u-button> -->

			
		</view>

		<!-- <u-button type="primary" text="新生引导"></u-button> -->
		</view>
	    </view> 
	</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style >
	// 以下为 style 区域
	.bg-img{
		position: fixed;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		z-index: -1;
	}
	.imgcontent{
			display: flex;
			flex-direction: column;
			align-items: center;
			margin: auto;
			top: 50px;
	}
	.u-hairline-border:after{
	    border: none;
	}
	.btn {
	    /* width: 500rpx; */
	    height: 85rpx;
	    /* border: 2rpx solid #f4f3f3; */
	    /* border-radius: 36rpx; */
	    /* margin: auto; */
	    /* background: transparent; */
	    font-size: 28rpx;
	    line-height: 72rpx;
		/* color:white; */
	    /* color: #0268FA; */
		margin-top: 3%;
		top: 60px;
		/* background-color: dodgerblue; */
		
/* 		margin-top: 10px;
		color: #ffffff; */
		width: 400rpx;
		font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
	}
	
</style>
