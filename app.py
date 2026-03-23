import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# إعداد واجهة المستخدم
st.set_page_config(page_title="BOD Simulator", layout="centered")
st.title("🧪 محاكي اختبار الـ BOD التفاعلي")
st.markdown("---")
st.write("أهلاً بك يا هندسة.. استخدم الأشرطة الجانبية لتغيير المدخلات ومراقبة المنحنى:")

# المدخلات في القائمة الجانبية
st.sidebar.header("إعدادات المختبر")
L0 = st.sidebar.slider("الحمل العضوي الابتدائي (L0) - mg/L", 50, 500, 200)
k = st.sidebar.slider("ثابت سرعة التفاعل (k) - per day", 0.05, 0.5, 0.23)

# معادلة الـ BOD
t = np.linspace(0, 20, 100)
bod_t = L0 * (1 - np.exp(-k * t))

# رسم المنحنى
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, bod_t, label=f'k = {k}', color='#1f77b4', linewidth=2.5)
ax.fill_between(t, bod_t, color='#1f77b4', alpha=0.1)

# إعدادات الرسم البياني
ax.set_xlabel('Time (Days)', fontsize=12)
ax.set_ylabel('BOD (mg/L)', fontsize=12)
ax.set_title('BOD Exertion Over Time', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# عرض الرسم في الموقع
st.pyplot(fig)

# نتيجة سريعة للطلاب
bod_5 = int(L0 * (1 - np.exp(-k * 5)))
st.info(f"💡 النتيجة: عند اليوم الخامس، استهلاك الأكسجين (BOD5) يساوي تقريباً: {bod_5} mg/L")
