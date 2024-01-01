import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Arun Joshi, Senior Data Scientist
##### *Resume* 
''')

image = Image.open('dp.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Supply chain professional, with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong in problem solving as demonstrated by extensive projects such in decarbonising ocean logistic network.
- Strong track record in developmnet of data products to manage vessel performance.
''')


#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.youtube.com/@arunj6639/videos" target="_blank">Arun Joshi</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Decarbonization Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Supply Chain and Logistic** (MBA), *SPJAIN School of Global Management*, Sydney/Dubai/Singapore',
'2015-2016')
st.markdown('''
- GPA: `3.2`
- Summer intership project at Sydney entitled `Improving the safety track record in the Distribution Center`.
- Conducted market entry reserach project in Dubai for a reatil company by doing competitors analysis covering price and services.
''')

txt('**Bachelors of Engineering** (Marine Technology), *Birla Institute of Technology and Science,*, Mesra',
'2005-2009')
st.markdown('''
- GPA: `8.4`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Advance Analytics Specialist**, Maersk Line, Mumbai',
'2021-Present')
st.markdown('''
- Managing a vessel reporting data product with help of `10` data engineers, power bi specialist and sme to ensure KPIs are strategically achieved as per IMO guidelines, namely EEOI and CII report on monthly basis. 
- Actively lead cost initiative projects that can have potential impact of 30 million dollar.
''')

#####################
st.markdown('''
## BI Tools
''')
txt4('Ocean Decarb Dashboard', 'A tool to drive performance management of ocean and drive the decarb agenda', 'https://app.powerbi.com/groups/')
txt4('CII Predictor', 'A CII tool to predict carbon intensity index of a vessel based on improvement factors year on year', 'https://allthewaycii.streamlit.app/')
txt4('EEOI Impact', 'An IP tool to calculate the emission reduction by replacement of old vessel with new one','https://gogreen-investment.streamlit.app/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `DAX - Power BI`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/akj129/')
txt2('GitHub', 'https://github.com/Rigava')


