<template>
	<view style="background-image: url(static/img/background3.png);">
		<br><text style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;font-size: 28px;display: flex;flex-direction: column;
		align-items: center;
		margin: auto;">新生入学“四步走”</text><br>
		<image style="width: 90px;height: 30px;display: flex;flex-direction: column;margin: auto;align-items: center;" src="/static/img/laba3.png"></image>
		<br><image  class="content" src="/static/img/schoolInfoimg3.png"  @click="dianji(0)" ></image>
		<view >
			<br><text class="title">步骤①：</text>
			<br>
			<text class='text-area'>找到自己学院的新生接待处，领取相关物资</text>
			<br></br>			
			<image class= "content" src="../../static/img/schoolInfoimg.png" @click="dianji(1)"></image>
			<br></br>
		</view>
		<view >
			<text class="title">步骤②</text>
			<br>
			<text class='text-area'>前往学生事务中心领军训物资</text>
			<br></br>
			<image class= "content" src="../../static/img/schoolInfoimg4.png" @click="dianji(2)"></image>
			<br></br>
		</view>
		<view>
			<text class="title">步骤③</text>
			<br>
			<text class='text-area'>到校医院进行入学体检</text>
			<br></br>
			<image class= "content" src="/static/img/stuGuide1.png"@click="dianji(3)"></image>
			<br></br>
		</view>
		<view>
			<text class="title">步骤④</text>
			<br>
			<text class='text-area'>到辅导员办公室办理注册手续</text>
			<br></br>
			<image class= "content" src="/static/img/stuGuide2.png"@click="dianji(4)"></image>
			<br></br>
		</view>
		
		<!-- 底部导航栏 -->
		<u-tabbar
				:value="value6"
				@change="name => value6 = name"
				:fixed="true"
				:placeholder="true"
				:safeAreaInsetBottom="true"
			>
				<u-tabbar-item text="首页" icon="home" @click='goToMainPlane()' ></u-tabbar-item>
				<u-tabbar-item text="数据总览" icon="search" @click='goToDataPlane()' ></u-tabbar-item>
				<u-tabbar-item text="报道流程" icon="map" ></u-tabbar-item>
				<u-tabbar-item text="性格测试" icon="edit-pen" @click='goToCapPlane()'></u-tabbar-item>
			</u-tabbar>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				value6: 2,
			}
		},
		methods: {
			// value6:0,
			dianji(index) {
				uni.previewImage({
					urls: ["/static/img/schoolInfoimg3.png","/static/img/schoolInfoimg.png",
					"/static/img/schoolInfoimg4.png","/static/img/stuGuide1.png",
					"/static/img/stuGuide2.png"],
					//需要预览的图片http链接列表，多张的时候，url直接写在后面就行了
					current: index, // 当前显示图片的http链接，默认是第一个
					
				})
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
	.content {
		
		display: flex;
		flex-direction: column;
		align-items: center;
		margin: auto;
		border-radius: 8%;

	}
	.text-area {
		/* font-style: oblique; */
	    font-style: unset; 
		white-space: pre-wrap;
		display: flex;
		flex-direction: column;
		align-items: center;
		margin: auto;
		
	}

	.title {
		font-size: 25px;
		color: black;
		display: flex;
		flex-direction: column;
		align-items: center;
		margin: auto;
	}
</style>
