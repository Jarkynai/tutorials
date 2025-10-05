import streamlit as st
import pandas as pd
data = pd.read_html('https://mineconom.gov.kg/ru/direct/158/312')
dataform = pd.concat(data)
# Переименование нескольких столбцов
dataform_renamed = dataform.rename(columns={
    1: 'Наименование',
    2: 'гос орган',
     3: 'Охват проекта',
     4: 'Период реализации',
     5: 'Статус',
     6: 'Донор',
     7: 'Сумма',
     8: 'Сфера'
    
})
dataform_renamed.head(5)
dataform_renamed.tail(5)
dataform_renamed.sort_values(by='Период реализации')
sorted = dataform_renamed.sort_values(by='Период реализации')

st.title('Реестр грантов по данным МЭКР')
st.write('открытые данные')

st.write(sorted.head(5))
filtered = sorted.groupby('Донор').count()
st.write('По донорам',filtered)
filtered.to_csv('by_donor.csv')

filtered2 = dataform_renamed.groupby('Статус').count()
st.write('По статусам', filtered2)
filtered2.to_csv('by_status.csv')

filtered3 = dataform_renamed.groupby('Сфера').count()
st.write('со сферам',filtered3)
filtered3.to_csv('by_field.csv')





