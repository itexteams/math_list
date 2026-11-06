import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang4_p2_b2_c1_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                def round_SA(a): 
                    # Kiểm tra nếu a là số nguyên
                    if a == int(a):
                        return "", int(a)

                    # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
                    str_a = f"{a:.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
                    integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân

                    # Xác định cách làm tròn
                    if len(integer_part) > 2:
                        number = Decimal(float(a)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                        cirle = "(làm tròn kết quả đến hàng đơn vị)"
                    elif len(integer_part) == 2 and len(decimal_part) > 1:
                        number = Decimal(float(a)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        cirle = "(làm tròn kết quả đến hàng phần chục)"
                    elif len(decimal_part) <= 2:
                        number = str_a  # Không cần làm tròn thêm
                        cirle = ""
                    else:
                        number = Decimal(float(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                        cirle = "(làm tròn kết quả đến hàng phần trăm)"

                    # Chuyển dấu chấm thành dấu phẩy (nếu có)
                    return cirle, str(number).replace('.', ',')
                # Khai báo biến
                lis0=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]
                goc1=random.choice(lis0)
                lis0.remove(goc1)
                goc2=random.choice(lis0)
                goc3=180-goc1-goc2
                d=randint(8,25)
                lis2=['A','B','C']
                g1=random.choice(lis2)
                lis2.remove(g1)
                g2=random.choice(lis2)
                lis2.remove(g2)
                g3=random.choice(lis2)
                a=str(g1)+str(g2)
                b=str(g3)+str(g2)
                c=str(g3)+str(g1)
                s3=math.sin(math.radians(goc3))
                s1=math.sin(math.radians(goc1))
                s2=math.sin(math.radians(goc2))

                b1=round_SA((d*s1)/s3)[1]
                b11=round_SA((d*s1)/s3)[0]
                b1s=round_SA((d*s1)/s3+1)[1]

                c1=round_SA((d*s2)/s3)[1]
                c11=round_SA((d*s2)/s3)[0]
                c1s=round_SA((d*s2)/s3+2)[1]

                r1=round_SA(d/(2*s3))[0]
                r=round_SA(d/(2*s3))[1]
                rs=round_SA(d/(s3))[1]



                # Nội dung câu hỏi
                noidungcauhoi =  '''Cho tam giác $ABC$ có $\\widehat{%s} = %s^\\circ, \\widehat{%s} = %s^\\circ$ và $%s=%s.$\n''' %(g1,latex(goc1),g2,latex(goc2),a,latex(d))
                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True Số đo của góc $\\widehat{%s}=%s^\\circ$'%(g3,latex(goc3))
                nb_da_1_s = ' Số đo của góc $\\widehat{%s}=%s^\\circ$'%(g3,latex(goc3-2))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Vì tổng ba góc trong tam giác bằng $180^{\\circ}$ nên ta có\\\\ \n'
                                '\\hspace*{1cm} $\\widehat{%s}=180^{\\circ}-(\\widehat{%s}+\\widehat{%s})=180^{\\circ}-(%s^{\\circ}+%s^{\\circ})=%s^{\\circ}.$'
                     %(latex(g3),latex(g1),latex(g2),latex(goc1),latex(goc2),latex(goc3))
                            )


                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Độ dài cạnh $%s=%s$ %s'%(b,latex(b1),b11)
                th_da_1_s ='Độ dài cạnh $%s=%s$ %s'%(b,latex(b1s),b11)
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Áp dụng định lí $\\sin$ ta có\\\\ \n'
                                '$\\dfrac{%s}{\\sin %s}=\\dfrac{%s}{\\sin %s} \\Leftrightarrow %s=\\dfrac{%s\\cdot \\sin %s}{\\sin %s}=\\dfrac{%s\\cdot \\sin %s^{\\circ}}{\\sin %s^{\\circ}}=%s$.'
                                %(b,g1,a,g3,b,a,g1,g3,latex(d),goc1,goc3,b1
                            ))


                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Độ dài cạnh $%s=%s$ %s'%(c,latex(c1),c11)
                vd_da_1_s =  'Độ dài cạnh $%s=%s$ %s'%(c,latex(c1s),c11)
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)



                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Áp dụng định lí $\\sin$ ta có\\\\ \n'
                                '$\\dfrac{%s}{\\sin %s}=\\dfrac{%s}{\\sin %s} \\Leftrightarrow %s=\\dfrac{%s\\cdot \\sin %s}{\\sin %s}=\\dfrac{%s\\cdot \\sin %s^{\\circ}}{\\sin %s^{\\circ}}=%s$.'
                                %(c,g2,a,g3,c,a,g2,g3,latex(d),goc2,goc3,c1
                            ))


                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d ='\\True Độ dài bán kính đường tròn ngoại tiếp tam giác $ABC$ là $R=%s$ %s'%(latex(r),r1)
                vdc_da_1_s = ' Độ dài bán kính đường tròn ngoại tiếp tam giác $ABC$ là $R=%s$ %s'%(latex(rs),r1)
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Áp dụng định lí $\\sin$ ta có\\\\ \n'
                                '$\\dfrac{%s}{\\sin %s}=2R \\Leftrightarrow R=\\dfrac{%s}{2\\sin %s}=\\dfrac{%s}{2\\sin %s^{\\circ}}=%s$.'
                                %(a,g3,a,g3,latex(d),goc3,latex(r)
                            ))
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content 

