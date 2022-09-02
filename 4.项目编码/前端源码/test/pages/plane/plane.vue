<template>
    <view class="container"> 
          <image class="bg-img" src="/static/img/background11.png"></image>
          <view class="content">
	<!-- <u-navbar
		title="数据总览"
		@rightClick="rightClick"
		:autoBack="true"
	>
	</u-navbar> -->
	<!-- <view class="navWrap" ref="nav">
		
	</view> -->
	  

	  <!-- <u-tabs :list="tabList" @click="tabClick"></u-tabs>-->
	  <view>
		  <u-divider text="报道人数占比" :hairline="true" textSize="20" textColor="#2979ff"lineColor="#060903"></u-divider>
		  <canvas canvas-id="UcgsrwojWzgflwgxVeXCpQnXpqLcLvWh" id="UcgsrwojWzgflwgxVeXCpQnXpqLcLvWh" class="charts" @touchend="tap"/>
	  </view>
	  <!-- <u--text type="primary" text="报道人数占比"></u--text>
	  <canvas canvas-id="UcgsrwojWzgflwgxVeXCpQnXpqLcLvWh" id="UcgsrwojWzgflwgxVeXCpQnXpqLcLvWh" class="charts" @touchend="tap"/> -->
	  <view>
		  <br><u-divider text="男女比例" :hairline="true" textSize="20" textColor="#2979ff"lineColor="#060903"></u-divider>
		  <canvas canvas-id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" class="charts" @touchend="tap"/>
	  </view>
	  
	  <!-- <u--text type="primary" text="男女比例"></u--text> -->
	  <!-- <canvas canvas-id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" class="charts" @touchend="tap"/> -->
	  <view>
		  <br><u-divider text="专业分布" :hairline="true" textSize="20" textColor="#2979ff"lineColor="#060903"></u-divider>
		  <canvas canvas-id="XzxvROqabbihGSldBgnVRYHQqsgFuizE" id="XzxvROqabbihGSldBgnVRYHQqsgFuizE" class="charts" @touchend="tap"/>
	  </view>
	  <!-- <u--text type="primary" text="专业分布"></u--text> -->
    <!-- <canvas canvas-id="XzxvROqabbihGSldBgnVRYHQqsgFuizE" id="XzxvROqabbihGSldBgnVRYHQqsgFuizE" class="charts" @touchend="tap"/> -->
	<!-- <button>test</button> -->
	
	<view>
		<br><u-divider text="地区排行" :hairline="true" textSize="20" textColor="#2979ff"lineColor="#060903"></u-divider>
		<!-- <canvas canvas-id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" class="charts" @touchend="tap"/> -->
		<canvas canvas-id="proCount" id="proCount" class="charts" @touchend="tap"/>
	</view>
	<!-- <u--text type="primary" text="地区排行"></u--text> -->
	<!-- <canvas canvas-id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" id="GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL" class="charts" @touchend="tap"/> -->
	<!-- <canvas canvas-id="proCount" id="proCount" class="charts" @touchend="tap"/> -->
  
	<br><u-divider  :dot="true" :hairline="true" textSize="20" textColor="#2979ff"lineColor="#060903"></u-divider>
	<!-- 底部导航栏 -->
	<u-tabbar
		:value="value6"
		@change="name => value6 = name"
		:fixed="true"
		:placeholder="true"
		:safeAreaInsetBottom="true"
	>
		<u-tabbar-item text="首页" icon="home" @click='goToMainPlane()'></u-tabbar-item>
		<u-tabbar-item text="数据总览" icon="search" ></u-tabbar-item>
		<u-tabbar-item text="报道流程" icon="map" @click='goToRegPlane()'></u-tabbar-item>
		<u-tabbar-item text="性格测试" icon="edit-pen" @click='goToCapPlane()'></u-tabbar-item>
	</u-tabbar>
  </view>
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
	  value6: 1,
	  
	  item:1,
    };
  },
  // rightClick(){
	 //  console.log("back")
  // },
 
	//滚动到指定位置
	// uni.pageScrollTo({
	// 	scrollTop:500,
	// 	selector:uCharts
	// 	duration: 300,
	// });
  
  onReady() {
    //这里的 750 对应 css .charts 的 width
    this.cWidth = uni.upx2px(750);
    //这里的 500 对应 css .charts 的 height
    this.cHeight = uni.upx2px(500);
    this.getServerData();
  },
  methods: {
	  // goToRegPlane(){
		 //  console.log("go to regplane")
	  // },
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
	  // 导航栏
	  // rightClick() {
		 //  console.log('rightClick');
	  // },
	  // leftClick() {
		 //  console.log('leftClick');
	  // },
    getServerData() {
		
		// 获取专业男女人数排行数据
		uni.request({
			  header: {
						'Content-Type': 'application/x-www-form-urlencoded'
				   }, 
			  url: "http://121.4.95.22:10085/api/plane/disCountMWS", //仅为示例，并非真实接口地址。
			   method: 'GET',
				   data: {
				   },
			   //dataType:'json',
			   success: (res) => {
						// console.log(res.data)
						
						// this.data = {
						// 	categories: ["2016","2017","2018","2019","2020","2021"],
						// 	series: [
						// 	  {
						// 		name: "目标值",
						// 		data: [35,36,31,33,13,34]
						// 	  },
						// 	  {
						// 		name: "完成量",
						// 		data: [18,27,21,24,6,28]
						// 	  }
						// 	]
						//   };
						//   console.log(this.data)
						this.drawDisCountWMCharts('XzxvROqabbihGSldBgnVRYHQqsgFuizE', res.data);
				   } 
			   })
		// 获取报道饼图数据
		uni.request({
			  header: {
						'Content-Type': 'application/x-www-form-urlencoded'
				   }, 
			  url: "http://121.4.95.22:10085/api/plane/isResCount", //仅为示例，并非真实接口地址。
			   method: 'GET',
				   data: {
				   },
			   success: (res) => {
						this.data = {
							series: [
							  {
							    data: [{"name":"已报道","value":res.data.countRes},{"name":"未报到","value":res.data.countNoRes},]
							  }
							]
						}
		
						this.drawWMProCharts('UcgsrwojWzgflwgxVeXCpQnXpqLcLvWh', this.data);
					
				   } 
			   })
			   
			   
	   // 获取男女比例数据
	   uni.request({
		  header: {
					'Content-Type': 'application/x-www-form-urlencoded'
			   }, 
		  url: "http://121.4.95.22:10085/api/plane/getCountOfMWS", //仅为示例，并非真实接口地址。
		   method: 'GET',
			   data: {
			   },
		   //dataType:'json',
		   success: (res) => {
					console.log(res.data)
					this.data = {
						series: [
						  {
							data: [{"name":"男生人数","value":res.data.countM},{"name":"女生人数","value":res.data.countW},]
						  }
						]
					}
					console.log(this.data)
					this.drawCountWMCircleCharts('GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL', this.data);
			   } 
		   })
		   
		   
		    // 获取省份数据
		   uni.request({
		   	  header: {
		   				'Content-Type': 'application/x-www-form-urlencoded'
		   		   }, 
		   	  url: "http://121.4.95.22:10085/api/plane/getProCount", //仅为示例，并非真实接口地址。
		   	   method: 'GET',
		   		   data: {
		   		   },
		   	   //dataType:'json',
		   	   success: (res) => {
		   				console.log(res.data)
		   				this.data = {
		   					categories: res.data.categories,
		   					series: [
		   					  {
		   						name: "省份",
		   						data: res.data.series.data,
		   					  },
		   					]
		   				  };
		   				console.log(this.data)
		   				// this.drawCharts('GcHfmrEVQjGUuYvtmfJOaIzMbLMfnnBL', this.data);
		   				this.proCountDrawCharts('proCount', this.data);
		   		   } 
		   	   })
    },
	
	// 男女比例图样式
	drawWMProCharts(id,data){
	  const ctx = uni.createCanvasContext(id, this);
	  uChartsInstance[id] = new uCharts({
	    type: "pie",
	    context: ctx,
	    width: this.cWidth,
	    height: this.cHeight,
	    series: data.series,
	    animation: true,
	    background: "#FFFFFF",
	    color: ["#67acff","#d6d6d6","#FAC858","#EE6666","#73C0DE","#3CA272","#FC8452","#9A60B4","#ea7ccc"],
	    padding: [5,5,5,5],
	    extra: {
	      pie: {
	        activeOpacity: 0.5,
	        activeRadius: 10,
	        offsetAngle: 0,
	        labelWidth: 15,
	        border: false,
	        borderWidth: 3,
	        borderColor: "#FFFFFF"
	      }
	    }
	  });
	},
	
	
	// 男女比例环图样式
	drawCountWMCircleCharts(id,data){
	  const ctx = uni.createCanvasContext(id, this);
	  uChartsInstance[id] = new uCharts({
	    type: "ring",
	    context: ctx,
	    width: this.cWidth,
	    height: this.cHeight,
	    series: data.series,
	    animation: true,
	    timing: "easeOut",
	    duration: 1000,
	    rotate: false,
	    rotateLock: false,
	    background: "#FFFFFF",
	    color: ["#67acff","#f188c4","#91CB74","#FAC858","#73C0DE","#3CA272","#FC8452","#9A60B4","#ea7ccc"],
	    padding: [5,5,5,5],
	    fontSize: 13,
	    fontColor: "#666666",
	    dataLabel: true,
	    dataPointShape: true,
	    dataPointShapeType: "solid",
	    touchMoveLimit: 60,
	    enableScroll: false,
	    enableMarkLine: false,
	    legend: {
	      show: true,
	      position: "bottom",
	      lineHeight: 25,
	      float: "center",
	      padding: 5,
	      margin: 5,
	      backgroundColor: "rgba(0,0,0,0)",
	      borderColor: "rgba(0,0,0,0)",
	      borderWidth: 0,
	      fontSize: 13,
	      fontColor: "#666666",
	      hiddenColor: "#CECECE",
	      itemGap: 10
	    },
	    title: {
	      name: "男女比例",
		  
	      fontSize: 15,
	      color: "#666666",
	      offsetX: 0,
	      offsetY: 0
	    },
	    subtitle: {
	      name: "",
	      fontSize: 25,
	      color: "#7cb5ec",
	      offsetX: 0,
	      offsetY: 0
	    },
	    extra: {
	      ring: {
	        ringWidth: 30,
	        activeOpacity: 0.5,
	        activeRadius: 10,
	        offsetAngle: 0,
	        labelWidth: 15,
	        border: true,
	        borderWidth: 3,
	        borderColor: "#FFFFFF",
	        centerColor: "#FFFFFF",
	        customRadius: 0,
	        linearType: "none"
	      },
	      tooltip: {
	        showBox: true,
	        showArrow: true,
	        showCategory: false,
	        borderWidth: 0,
	        borderRadius: 0,
	        borderColor: "#000000",
	        borderOpacity: 0.7,
	        bgColor: "#000000",
	        bgOpacity: 0.7,
	        gridType: "solid",
	        dashLength: 4,
	        gridColor: "#CCCCCC",
	        fontColor: "#FFFFFF",
	        splitLine: true,
	        horizentalLine: false,
	        xAxisLabel: false,
	        yAxisLabel: false,
	        labelBgColor: "#FFFFFF",
	        labelBgOpacity: 0.7,
	        labelFontColor: "#666666"
	      }
	    }
	  });
	},
	
	
	
	//专业男女人数排行图样式
    drawDisCountWMCharts(id,data){
      const ctx = uni.createCanvasContext(id, this);
      uChartsInstance[id] = new uCharts({
        type: "column",
        context: ctx,
        width: this.cWidth,
        height: this.cHeight,
        categories: data.categories,
        series: data.series,
        animation: true,
        timing: "easeOut",
        duration: 1000,
        rotate: false,
        rotateLock: false,
        background: "#FFFFFF",
        color: ["#67acff","#f188c4","#FAC858","#EE6666","#73C0DE","#3CA272","#FC8452","#9A60B4","#ea7ccc"],
        padding: [15,15,0,5],
        fontSize: 8,
        fontColor: "#666666",
        dataLabel: true,
        dataPointShape: true,
        dataPointShapeType: "solid",
        touchMoveLimit: 60,
        enableScroll: false,
        enableMarkLine: false,
        legend: {
          show: true,
          position: "bottom",
          float: "center",
          padding: 5,
          margin: 5,
          backgroundColor: "rgba(0,0,0,0)",
          borderColor: "rgba(0,0,0,0)",
          borderWidth: 0,
          fontSize: 13,
          fontColor: "#666666",
          lineHeight: 11,
          hiddenColor: "#CECECE",
          itemGap: 10
        },
        xAxis: {
          disableGrid: true,
          disabled: false,
          axisLine: true,
          axisLineColor: "#CCCCCC",
          calibration: false,
          fontColor: "#666666",
          fontSize: 13,
          rotateLabel: false,
          rotateAngle: 45,
          itemCount: 5,
          boundaryGap: "center",
          splitNumber: 5,
          gridColor: "#CCCCCC",
          gridType: "solid",
          dashLength: 4,
          gridEval: 1,
          scrollShow: false,
          scrollAlign: "left",
          scrollColor: "#A6A6A6",
          scrollBackgroundColor: "#EFEBEF",
          formatter: ""
        },
        yAxis: {
          data: [
            {
              min: 0
            }
          ],
          disabled: false,
          disableGrid: false,
          splitNumber: 5,
          gridType: "solid",
          dashLength: 8,
          gridColor: "#CCCCCC",
          padding: 10,
          showTitle: false
        },
        extra: {
          column: {
            type: "group",
            width: 30,
            activeBgColor: "#000000",
            activeBgOpacity: 0.08,
            seriesGap: 2,
            categoryGap: 3,
            barBorderCircle: false,
            linearType: "none",
            linearOpacity: 1,
            colorStop: 0,
            meterBorder: 1,
            meterFillColor: "#FFFFFF"
          },
          tooltip: {
            showBox: true,
            showArrow: true,
            showCategory: false,
            borderWidth: 0,
            borderRadius: 0,
            borderColor: "#000000",
            borderOpacity: 0.7,
            bgColor: "#000000",
            bgOpacity: 0.7,
            gridType: "solid",
            dashLength: 4,
            gridColor: "#CCCCCC",
            fontColor: "#FFFFFF",
            splitLine: true,
            horizentalLine: false,
            xAxisLabel: false,
            yAxisLabel: false,
            labelBgColor: "#FFFFFF",
            labelBgOpacity: 0.7,
            labelFontColor: "#666666"
          },
          markLine: {
            type: "solid",
            dashLength: 4,
            data: []
          }
        }
      });
    },
	
	//省份图样式
	proCountDrawCharts(id,data){
	  const ctx = uni.createCanvasContext(id, this);
	  uChartsInstance[id] = new uCharts({
	    type: "bar",
	    context: ctx,
	    width: this.cWidth,
	    height: this.cHeight,
	    categories: data.categories,
	    series: data.series,
	    animation: true,
	    timing: "easeOut",
	    duration: 1000,
	    rotate: false,
	    rotateLock: false,
	    background: "#FFFFFF",
	    color: ["#67acff","#91CB74","#FAC858","#EE6666","#73C0DE","#3CA272","#FC8452","#9A60B4","#ea7ccc"],
	    padding: [10,30,0,5],
	    fontSize: 8,
	    fontColor: "#666666",
	    dataLabel: true,
	    dataPointShape: true,
	    dataPointShapeType: "solid",
	    touchMoveLimit: 60,
	    enableScroll: false,
	    enableMarkLine: false,
	    legend: {
	      show: true,
	      position: "bottom",
	      float: "center",
	      padding: 5,
	      margin: 5,
	      backgroundColor: "rgba(0,0,0,0)",
	      borderColor: "rgba(0,0,0,0)",
	      borderWidth: 0,
	      fontSize: 13,
	      fontColor: "#666666",
	      lineHeight: 11,
	      hiddenColor: "#CECECE",
	      itemGap: 10
	    },
	    xAxis: {
	      boundaryGap: "justify",
	      disableGrid: false,
	      min: 0,
	      axisLine: false,
	      disabled: false,
	      axisLineColor: "#CCCCCC",
	      calibration: false,
	      fontColor: "#666666",
	      fontSize: 13,
	      rotateLabel: false,
	      rotateAngle: 45,
	      itemCount: 5,
	      splitNumber: 5,
	      gridColor: "#CCCCCC",
	      gridType: "solid",
	      dashLength: 4,
	      gridEval: 1,
	      scrollShow: false,
	      scrollAlign: "left",
	      scrollColor: "#A6A6A6",
	      scrollBackgroundColor: "#EFEBEF",
	      formatter: ""
	    },
	    yAxis: {
	      disabled: false,
	      disableGrid: false,
	      splitNumber: 5,
	      gridType: "solid",
	      dashLength: 8,
	      gridColor: "#CCCCCC",
	      padding: 10,
	      showTitle: false,
	      data: []
	    },
	    extra: {
	      bar: {
	        type: "group",
	        width: 20,
	        meterBorde: 1,
	        meterFillColor: "#FFFFFF",
	        activeBgColor: "#000000",
	        activeBgOpacity: 0.08,
	        seriesGap: 2,
	        categoryGap: 3,
	        barBorderCircle: false,
	        linearType: "none",
	        linearOpacity: 1,
	        colorStop: 0
	      },
	      tooltip: {
	        showBox: true,
	        showArrow: true,
	        showCategory: false,
	        borderWidth: 0,
	        borderRadius: 0,
	        borderColor: "#000000",
	        borderOpacity: 0.7,
	        bgColor: "#000000",
	        bgOpacity: 0.7,
	        gridType: "solid",
	        dashLength: 4,
	        gridColor: "#CCCCCC",
	        fontColor: "#FFFFFF",
	        splitLine: true,
	        horizentalLine: false,
	        xAxisLabel: false,
	        yAxisLabel: false,
	        labelBgColor: "#FFFFFF",
	        labelBgOpacity: 0.7,
	        labelFontColor: "#666666"
	      },
	      markLine: {
	        type: "solid",
	        dashLength: 4,
	        data: []
	      }
	    }
	  });
	},
    tap(e){
      uChartsInstance[e.target.id].touchLegend(e);
      uChartsInstance[e.target.id].showToolTip(e);
    }
  }
};
</script>

<style scoped>
  .charts{
    width: 750rpx;
    height: 500rpx;
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
</style>