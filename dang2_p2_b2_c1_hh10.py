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


def bt_dang2_p2_b2_c1_hh10(self):
            # Khai báo biến
            lis0=[10,15,20,25,30,35,40,45,50,55,60,65]
            goc1=random.choice(lis0)
            goc1_rad=goc1 * pi / 180

            goc2=random.choice(lis0)
            goc2_rad=goc2 * pi / 180

            goc3=180-goc1-goc2
            goc3_rad=goc3 * pi / 180

            lis1=[2,3,4,5,6,7,8,9]
            a=random.choice(lis1)
            b=random.choice(lis1)
            c=random.choice(lis1)

            kq1=round(c*sin(goc1_rad)/sin(goc2_rad),1)
            kq1s1=round(kq1+0.1,1)
            kq1s2=round(kq1+0.2,1)
            kq1s3=round(kq1-0.1,1)

            kq2=round(c*sin(goc1_rad)/sin(goc3_rad),1)
            kq2s1=round(kq2+0.1,1)
            kq2s2=round(kq2+0.2,1)
            kq2s3=round(kq2-0.1,1)

            kq3=round(c/(2*sin(goc3_rad)),1)
            kq3s1=round(kq3+0.1,1)
            kq3s2=round(kq3+0.2,1)
            kq3s3=round(kq3-0.1,1)
            # Nội dung câu hỏi
            noidungcauhoi = '''Cho tam giác $ABC$ có $\\widehat{C} = %s^\\circ, \\widehat{A} = %s^\\circ$ và $BC=%s$$zzz$\n''' %(latex(goc1),latex(goc2),latex(c))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Độ dài cạnh $CA\\approx %s$'%(latex(kq2))
            nb_da_1_s = 'Độ dài cạnh $CA \\approx %s$'%(latex(kq2+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Độ dài cạnh $CA \\approx %s$'%(latex(kq2))
            nb_da_2_s = 'Độ dài cạnh $CA \\approx %s$'%(latex(kq2+2))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Góc $\\widehat{A} = 180^\\circ - \\widehat{B} - \\widehat{C} = 180^\\circ -%s^\\circ -%s^\\circ = %s^\\circ$$zzz$\\\\ \n'
                    'Áp dụng định lí sin cho tam giác $ABC$, ta có \\\\ \n'
                    '$\\dfrac{CA}{\\sin B} = \\dfrac{BC}{\\sin A}$ suy ra $CA = \\dfrac{BC \\sin B}{\\sin A} = \\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx  %s$$zzz$'
                    %(latex(goc1),latex(goc2),latex(180-goc1-goc2),
                    latex(c), latex(goc1), latex(180-goc1-goc2),latex(kq2)
                    ))
            loigiai_nb_2 = ('Góc $\\widehat{A} = 180^\\circ - \\widehat{B} - \\widehat{C} = 180^\\circ -%s^\\circ -%s^\\circ = %s^\\circ$$zzz$\\\\ \n'
                    'Áp dụng định lí sin cho tam giác $ABC$, ta có \\\\ \n'
                    '$\\dfrac{CA}{\\sin B} = \\dfrac{BC}{\\sin A}$ suy ra $CA = \\dfrac{BC \\sin B}{\\sin A} = \\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx  %s$$zzz$'
                    %(latex(goc1),latex(goc2),latex(180-goc1-goc2),
                    latex(c), latex(goc1), latex(180-goc1-goc2),latex(kq2)
                    ))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Diện tích tam giác $ABC\\approx %s$'%(latex(round(0.5*c*kq2*sin(goc2_rad),1)))
            th_da_1_s = 'Diện tích tam giác $ABC\\approx %s$'%(latex(round(0.5*c*kq2*sin(goc2_rad)+1,1)))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Diện tích tam giác $ABC\\approx %s$'%(latex(round(0.5*c*kq2*sin(goc2_rad),1)))
            th_da_2_s = 'Diện tích tam giác $ABC\\approx %s$'%(latex(round(0.5*c*kq2*sin(goc2_rad)+2,1)))
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Góc $\\widehat{B} = 180^\\circ - \\widehat{C} - \\widehat{A} = 180^\\circ -%s^\\circ -%s^\\circ = %s^\\circ$$zzz$\\\\ \n'
                    'Áp dụng định lí sin cho tam giác $ABC$, ta có \\\\ \n'
                    '$\\dfrac{AB}{\\sin C} = \\dfrac{CA}{\\sin B}$ suy ra $AB = \\dfrac{CA \\sin C}{\\sin B} = \\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx  %s$$zzz$ \\\\ \n'
                    'Diện tích tam giác là \\\\ \n'
                    '$S=\\dfrac{1}{2}bc \\sin A = \\dfrac{1}{2}AC \\cdot AB \\cdot \\sin A = \\dfrac{1}{2} \\cdot %s \\cdot %s \\cdot \\sin %s^\\circ \\approx  %s$$zzz$'
                    %(latex(goc1),latex(goc2),latex(180-goc1-goc2),
                    latex(c), latex(goc1), latex(180-goc1-goc2),latex(kq2),
                    latex(c),latex(kq2), latex(goc2), latex(round(0.5*c*kq2*sin(goc2_rad),1))
                    ))
            loigiai_th_2 = ('Góc $\\widehat{B} = 180^\\circ - \\widehat{C} - \\widehat{A} = 180^\\circ -%s^\\circ -%s^\\circ = %s^\\circ$$zzz$\\\\ \n'
                    'Áp dụng định lí sin cho tam giác $ABC$, ta có \\\\ \n'
                    '$\\dfrac{AB}{\\sin C} = \\dfrac{CA}{\\sin B}$ suy ra $AB = \\dfrac{CA \\sin C}{\\sin B} = \\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx  %s$$zzz$ \\\\ \n'
                    'Diện tích tam giác là \\\\ \n'
                    '$S=\\dfrac{1}{2}bc \\sin A = \\dfrac{1}{2}AC \\cdot AB \\cdot \\sin A = \\dfrac{1}{2} \\cdot %s \\cdot %s \\cdot \\sin %s^\\circ \\approx  %s$$zzz$'
                    %(latex(goc1),latex(goc2),latex(180-goc1-goc2),
                    latex(c), latex(goc1), latex(180-goc1-goc2),latex(kq2),
                    latex(c),latex(kq2), latex(goc2), latex(round(0.5*c*kq2*sin(goc2_rad),1))
                    ))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Bán kính đường tròn ngoại tiếp tam giác $ABC$ là $R \\approx %s$' %(latex(kq3))
            vd_da_1_s = 'Bán kính đường tròn ngoại tiếp tam giác $ABC$ là $R \\approx %s$' %(latex(kq3+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Bán kính đường tròn nội tiếp tam giác $ABC$ là $r\\approx%s$' %(latex(round(c*kq2*sin(goc2_rad)/(c+kq2+c*sin(goc2_rad)/sin(goc3_rad)),1)))
            vd_da_2_s = 'Bán kính đường tròn nội tiếp tam giác $ABC$ là $r\\approx%s$' %(latex(round(c*kq2*sin(goc2_rad)/(c+kq2+c*sin(goc2_rad)/sin(goc3_rad))+1,1)))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Góc $\\widehat{B} = 180^\\circ - \\widehat{C} - \\widehat{A} = 180^\\circ -%s^\\circ -%s^\\circ = %s^\\circ$$zzz$\\\\ \n'
                    'Áp dụng định lí sin cho tam giác $ABC$, ta có \\\\ \n'
                    '$\\dfrac{CA}{\\sin B} = 2R$ suy ra $R=\\dfrac{CA}{2 \\sin B} =\\dfrac{%s}{2 \\sin %s^\\circ} \\approx  %s$$zzz$'
                    %(latex(goc1),latex(goc2),latex(180-goc1-goc2),
                    latex(c),latex(180-goc1-goc2),latex(kq3)
                    ))
            loigiai_vd_2 = ('Góc $\\widehat{B} = %s^\\circ$ Diện tích tam giác là $S\\approx  %s$$zzz$\\\\ \n'
                    'Áp dụng định lí sin cho tam giác $ABC$, ta có \\\\ \n' 
                    '$\\dfrac{AB}{\\sin C} = \\dfrac{CA}{\\sin B}$ suy ra $AB = \\dfrac{CA \\sin C}{\\sin B} = \\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx  %s$$zzz$ \\\\ \n'
                    '$\\dfrac{BC}{\\sin A} = \\dfrac{CA}{\\sin B}$ suy ra $BC = \\dfrac{CA \\sin A}{\\sin B} = \\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx  %s$$zzz$ \\\\ \n'
                    'Bán kính đường tròn nội tiếp tam giác là\\\\ \n'
                    '$S=pr \\Rightarrow r=\\dfrac{S}{p} = \\dfrac{2S}{CA+AB+BC} = \\dfrac{2 \\cdot %s}{%s+%s+%s} \\approx %s$$zzz$'
                    %(latex(180-goc1-goc2),
                    latex(round(0.5*c*kq2*sin(goc2_rad),1)),
                    latex(c), latex(goc1), latex(180-goc1-goc2),latex(kq2), #cạnh AB
                    latex(c), latex(goc2), latex(180-goc1-goc2),latex(round(c*sin(goc2_rad)/sin(goc3_rad),1)),   #Cạnh BC            

                    latex(round(0.5*c*kq2*sin(goc2_rad),1)),latex(c),latex(kq2),latex(round(c*sin(goc2_rad)/sin(goc3_rad),1)), latex(round(c*kq2*sin(goc2_rad)/(c+kq2+c*sin(goc2_rad)/sin(goc3_rad)),1))
                    ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Đường cao của tam giác $h_a \\approx %s$' %(latex(round(c*kq2*sin(goc2_rad)/(c*sin(goc2_rad)/sin(goc3_rad)),1)))
            vdc_da_1_s = 'Đường cao của tam giác $h_a \\approx %s$' %(latex(round(c*kq2*sin(goc2_rad)/(c*sin(goc2_rad)/sin(goc3_rad))+1,1)))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Đường cao của tam giác $h_b \\approx %s$' %(latex(round(c*kq2*sin(goc2_rad)/(c),1)))
            vdc_da_2_s = 'Đường cao của tam giác $h_b \\approx %s$' %(latex(round(c*kq2*sin(goc2_rad)/(c)+1,1)))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            vdc_da_3_d = '\\True Đường cao của tam giác $h_c \\approx %s$' %(latex(round(c*kq2*sin(goc2_rad)/(kq2),1)))
            vdc_da_3_s = 'Đường cao của tam giác $h_c \\approx %s$' %(latex(round(c*kq2*sin(goc2_rad)/(c)+1,1)))
            list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
            vdc_da_3=random.choice(list_vdc_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2, vdc_da_3]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Diện tích tam giác là $S \\approx  %s$$zzz$ \\\\ \n'
                    'Đường cao $h_a$ của tam giác là\\\\ \n'
                    '$S=\\dfrac{1}{2}ah_a \\Rightarrow h_a=\\dfrac{2S}{a} = \\dfrac{2S}{BC} = \\dfrac{2 \\cdot %s}{%s} \\approx %s$$zzz$'
                    %(latex(round(0.5*c*kq2*sin(goc2_rad),1)),
                    latex(round(0.5*c*kq2*sin(goc2_rad),1)),latex(round(c*sin(goc2_rad)/sin(goc3_rad),1)), latex(round(c*kq2*sin(goc2_rad)/(c*sin(goc2_rad)/sin(goc3_rad)),1))
                    ))
            loigiai_vdc_2 = ('Diện tích tam giác là $S \\approx  %s$$zzz$ \\\\ \n'
                    'Đường cao $h_b$ của tam giác là\\\\ \n'
                    '$S=\\dfrac{1}{2}bh_b \\Rightarrow h_b=\\dfrac{2S}{b} = \\dfrac{2S}{AC} = \\dfrac{2 \\cdot %s}{%s} \\approx %s$$zzz$'
                    %(latex(round(0.5*c*kq2*sin(goc2_rad),1)),
                    latex(round(0.5*c*kq2*sin(goc2_rad),1)),latex(c), latex(round(c*kq2*sin(goc2_rad)/(c),1))
                    ))
            loigiai_vdc_3 = ('Diện tích tam giác là $S \\approx  %s$$zzz$ \\\\ \n'
                    'Đường cao $h_c$ của tam giác là\\\\ \n'
                    '$S=\\dfrac{1}{2}ch_c \\Rightarrow h_c=\\dfrac{2S}{c} = \\dfrac{2S}{AB} = \\dfrac{2 \\cdot %s}{%s} \\approx %s$$zzz$'
                    %(latex(round(0.5*c*kq2*sin(goc2_rad),1)),
                    latex(round(0.5*c*kq2*sin(goc2_rad),1)),latex(kq2), latex(round(c*kq2*sin(goc2_rad)/(kq2),1))
                    ))



            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2, loigiai_vdc_3]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zzz$','.').replace('{,}0','')
            return content   

