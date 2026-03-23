import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# إعدادات الصفحة
st.set_page_config(page_title="BOD Simulator", layout="centered")

st.title("🧪 محاكي اختبار الـ BOD التفاعلي")
st.write("أهلاً بك يا هندسة.. تحكم في المدخلات لمشاهدة منحنى استهلاك الأكسجين:")

# القائمة الجانبية
L0 = st.sidebar.slider("الحمل العضوي الابتدائي (L0)", 50, 500, 200)
k = st.sidebar.slider("ثابت سرعة التفاعل (k)", 0.05, 0.5, 0.23)

# الحسابات والرسوم
t = np.linspace(0, 20, 100)
bod_t = L0 * (1 - np.exp(-k * t))

fig, ax = plt.subplots()
ax.plot(t, bod_t, label='BOD Curve', color='blue', linewidth=2)
ax.set_xlabel('Time (Days)')
ax.set_ylabel('Oxygen Consumed (mg/L)')
ax.grid(True)

st.pyplot(fig)
st.success("تم تشغيل المحاكي بنجاح!")
