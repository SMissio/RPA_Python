#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pyautogui as tempopc
import pyautogui as posMouse
import pyautogui as escrever

escrever.alert("O RPA vai iniciar ! Por gentileza aguardar finalização.")

posMouse.click(x=538, y=755)
tempopc.sleep(1)
posMouse.doubleClick(x=311, y=318)
tempopc.sleep(2)
escrever.typewrite('=PROCX([@[Codigo Cliente]];Tabela3[[#Tudo];[Cliente]];Tabela3[[#Tudo];[Total]])')
tempopc.sleep(2)
posMouse.press('enter')
tempopc.sleep(1)
posMouse.click(x=311, y=318)
tempopc.sleep(1)
posMouse.doubleClick(x=346, y=325)
tempopc.sleep(1)
#Segunda Informação
posMouse.doubleClick(x=387, y=316)
tempopc.sleep(2)
escrever.typewrite('=PROCX([@[Codigo Cliente]];Tabela3[Cliente];Tabela3[Especie])')
tempopc.sleep(2)
posMouse.press('enter')
tempopc.sleep(1)
posMouse.click(x=387, y=316)
tempopc.sleep(1)
posMouse.doubleClick(x=420, y=325)
tempopc.sleep(1)
#Terceira Informação
posMouse.doubleClick(x=480, y=315)
tempopc.sleep(2)
escrever.typewrite('=PROCX([@[Codigo Cliente]];Tabela3[Cliente];Tabela3[Valor Gasto])')
tempopc.sleep(2)
posMouse.press('enter')
tempopc.sleep(1)
posMouse.click(x=480, y=315)
tempopc.sleep(1)
posMouse.doubleClick(x=550, y=326)
tempopc.sleep(1)
#Total
posMouse.doubleClick(x=460, y=578)
tempopc.sleep(2)
escrever.typewrite('=SOMA(Tabela1[Valor Total Gasto])')
tempopc.sleep(2)
posMouse.press('enter')
tempopc.sleep(3)
posMouse.click(x=51, y=297)
posMouse.hotkey('ctrl','shift','right')
tempopc.sleep(1)
posMouse.hotkey('ctrl','shift','down')
#Criando Pivo
posMouse.click(x=215, y=46)
tempopc.sleep(3)
posMouse.click(x=23, y=113)
tempopc.sleep(3)
posMouse.click(x=33, y=209)
tempopc.sleep(3)
posMouse.click(x=577, y=491)
tempopc.sleep(1)
posMouse.click(x=696, y=339)
tempopc.sleep(1)
posMouse.click(x=693, y=415)
tempopc.sleep(2)
posMouse.click(x=295, y=296)
tempopc.sleep(2)
posMouse.hotkey('ctrl','shift','down')
tempopc.sleep(2)
posMouse.click(x=120, y=49)
tempopc.sleep(1)
posMouse.click(x=258, y=297)
tempopc.sleep(3)
posMouse.hotkey('ctrl','shift','down')
tempopc.sleep(2)
posMouse.click(x=535, y=107)
tempopc.sleep(2)
#Criar Gráfico
posMouse.click(x=56, y=275)
tempopc.sleep(2)
posMouse.hotkey('ctrl','shift','right')
tempopc.sleep(1)
posMouse.hotkey('ctrl','shift','down')
tempopc.sleep(3)
posMouse.click(x=209, y=50)
tempopc.sleep(3)
posMouse.click(x=261, y=111)
tempopc.sleep(2)
posMouse.click(x=241, y=237)
tempopc.sleep(2)
posMouse.click(x=698, y=642)
tempopc.sleep(2)
posMouse.doubleClick(x=138, y=694)
tempopc.sleep(2)
escrever.typewrite('Grafico')
tempopc.sleep(2)
posMouse.press('enter')
tempopc.sleep(2)
posMouse.click(x=335, y=442,button='right')
tempopc.sleep(3)
posMouse.click(x=560, y=358)
tempopc.sleep(3)
posMouse.click(x=629, y=359)
tempopc.sleep(1)
escrever.alert("O RPA Finalizou.")


# In[ ]:





# In[ ]:




