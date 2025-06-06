import streamlit as st
import streamlit as st
import pandas as pd

st.title("🍔 南宁美食探索")
st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")
st.header("📍 南宁美食地图")
st.map(pd.DataFrame({
    "latitude": [22.808992, 22.840197, 22.845501, 22.772335, 22.868989],
    "longitude": [108.268760, 108.216749, 108.231694, 108.458017, 108.300983]
    }))

# 定义数据,以便创建数据框
# 餐厅数据
restaurants = pd.DataFrame({
    "餐厅": ["九京客北京烤鸭", "意式风味牛排饭", "意面叔叔", "窑鸡王", "港味记滑蛋饭茶餐厅"],
    "类型": ["中餐", "快餐", "西餐", "中餐", "自助餐"],
    "评分": [4.7, 4.9, 4.8, 4.9, 4.7],
    "人均消费(元)": [15, 30, 25, 20, 50],
    "位置X": [22.808992, 22.840197, 22.845501, 22.772335, 22.868989],
    "位置Y": [108.268760, 108.216749, 108.231694, 108.458017, 108.300983]
})
# 根据上面创建的data，创建数据框
df = pd.DataFrame(restaurants)

st.header("💰不同类型餐厅价格")
# 通过width、height和use_container_width指定折线图的宽度和高度
st.line_chart(df, x='类型',y='人均消费(元)')

st.header("⭐餐厅评分")
st.bar_chart(df, x='餐厅',y='评分')

data = pd.DataFrame({
    '月份': ['1月', '2月', '3月', '4月', '5月','6月','7月','8月','9月','10月','11月','12月'],
    '九京客北京烤鸭':[200, 150, 180, 190, 220, 210, 190, 200, 160, 170, 175, 140],
    '意式风味牛排饭':[120, 160, 123, 130, 125, 140, 150, 180 ,197, 150, 160, 170],
    '意面叔叔':[110, 100, 160,190, 220, 210, 190, 200, 160, 170, 175, 140],
    '窑鸡王':[130, 160, 123, 190, 220, 210, 190, 200, 160, 170, 175, 140],
    '港味记滑蛋饭茶餐厅':[140, 100, 160, 190, 220, 210, 190, 200, 160, 170, 175, 140],
})
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
st.header("⭐价格走势折线图")
st.line_chart(df,x='月份',y=['九京客北京烤鸭','意式风味牛排饭','意面叔叔','窑鸡王','港味记滑蛋饭茶餐厅'])

st.header("🍽️餐厅详情")
select=st.selectbox('选择餐厅查看详情：',['九京客北京烤鸭','意式风味牛排饭','意面叔叔','窑鸡王','港味记滑蛋饭茶餐厅'],)
if select=='九京客北京烤鸭':
    st.subheader('九京客北京烤鸭')
    st.text('评分')
    st.header('4.7/5.0')
    st.text('人均消费')
    st.header('27元')
    st.subheader('当前拥挤程度')
    st.progress(80, text="80％拥挤")
if select=='意式风味牛排饭':
    st.subheader('意式风味牛排饭')
    st.text('评分')
    st.header('4.9/5.0')
    st.text('人均消费')
    st.header('25元')
    st.subheader('当前拥挤程度')
    st.progress(76, text="76％拥挤")
if select=='意面叔叔':
    st.subheader('意面叔叔')
    st.text('评分')
    st.header('4.8/5.0')
    st.text('人均消费')
    st.header('18元')
    st.subheader('当前拥挤程度')
    st.progress(65, text="65％拥挤")
if select=='窑鸡王':
    st.subheader('窑鸡王')
    st.text('评分')
    st.header('4.9/5.0')
    st.text('人均消费')
    st.header('23元')
    st.subheader('当前拥挤程度')
    st.progress(84, text="84％拥挤")
if select=='港味记滑蛋饭茶餐厅':
    st.subheader('港味记滑蛋饭茶餐厅')
    st.text('评分')
    st.header('4.7/5.0')
    st.text('人均消费')
    st.header('24元')
    st.subheader('当前拥挤程度')
    st.progress(91, text="91％拥挤")


st.header("今日午餐推荐")
if st.button('帮我选午餐'):
    st.write('今日推荐：九京客北京烤鸭')
