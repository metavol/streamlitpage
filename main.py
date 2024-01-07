import streamlit as st

st.title('Streamlit 入門')

# st.write('progress bar show')
# 'Start!!'
# latest_iteration = st.empty()
# bar = st.progress(int(0))

# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i+1)
#     time.sleep(0.03)

# 'Done'




left_column, right_column = st.columns(2)
btn = left_column.button('右カラムに文字を表示')
if btn:
    right_column.write('ここは右カラムです')

# if st.checkbox('Show Image'):
#     img = Image.open('img.jpg')
#     st.image(img, caption='Hokudai', use_column_width=True)

option = left_column.selectbox(
    'あなたが好きな数字を教えてください',
    range(1,11)
)

'You like ', option, 'です'

yh = st.text_input('your hobby')

'Your hobby is ', yh

con = st.slider('Your condition', 0,100,50)

'Your condition is ', con

exp = st.expander('問い合わせ')
exp.write('Hello')
# img = Image.open('img.jpg')
# exp.image(img)

