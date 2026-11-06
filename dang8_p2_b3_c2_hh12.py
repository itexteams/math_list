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


def bt_dang8_p2_b3_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến (Random m để tạo nhiều bài toán khác nhau)
            # Gọi vận tốc tại H là m. Để số liệu đẹp, ta random m trong một tập hợp.
            m = random.choice([10, 15, 20, 25, 30])
            # C là hằng số tự do trong hàm E(v)
            C = m**2 + random.randint(300, 500)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian với hệ trục $Oxyz$ với đơn vị trên mỗi trục tính bằng kilomet, một khinh khí cầu bay thẳng theo hướng từ điểm $A(3;8;0)$ đến điểm $B(-3;-2;15)$ với tốc độ $v$ (km/h). Biết rằng, năng lượng của khinh khí cầu để có thể di chuyển với tốc độ $v$ là $E(v)=v^2-%sv+%s(J)$.
            Do phải tránh vùng an toàn là một mặt cầu $(S)$ tâm $I$ có phương trình $(x-2)^2+(y-0,5)^2+(z-6)^2=25$ nên khinh khí cầu bay lệch một góc $\\alpha$ so với $AB$ trong mặt phẳng $(IAB)$. Tại một điểm $H$ gần tâm mặt cầu nhất thì vận tốc $v_H$ đạt mức năng lượng thấp nhất và thỏa mãn $v_H=v_0\\cos \\alpha - AH$.'''                
                             %(latex(2*m), latex(C)
                                 ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Vận tốc của khinh khí cầu tại vị trí $H$ là $%s$ (km/h)' % latex(m)
            nb_da_1_s = 'Vận tốc của khinh khí cầu tại vị trí $H$ là $%s$ (km/h)' % latex(m + random.randint(5, 10))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Để năng lượng thấp nhất, ta xét $E'(v)=2v-%s$. $E'(v)=0 \\Leftrightarrow v=%s$ (km/h). \\\\
            Vậy tại điểm $H$ thì vận tốc $v_H=%s$ (km/h) để đạt mức năng lượng thấp nhất.'''
                        %(latex(2*m), latex(m), latex(m)))

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
            th_da_1_d = '\\True Khoảng cách từ tâm mặt cầu $(S)$ đến đường thẳng $AB$ là $3,5$ km' 
            th_da_1_s = 'Khoảng cách từ tâm mặt cầu $(S)$ đến đường thẳng $AB$ là $4,5$ km'   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $\\overrightarrow{AB}=(-6;-10;15) \\Rightarrow |\\overrightarrow{AB}|=\\sqrt{(-6)^2+(-10)^2+15^2}=19$ và $\\overrightarrow{AI}=(-1;-7,5;6)$ \\\\
            Tích có hướng: $\\left[\\overrightarrow{AI},\\overrightarrow{AB}\\right]=(52,5;21;35) \\Rightarrow \\left|\\left[\\overrightarrow{AI},\\overrightarrow{AB}\\right]\\right|=\\sqrt{(52,5)^2+21^2+35^2}=\\frac{133}{2}$ \\\\
            Khoảng cách từ tâm $I$ đến đường thẳng $AB$ là: \\\\
            $d(I,AB)=\\frac{\\left|\\left[\\overrightarrow{AI},\\overrightarrow{AB}\\right]\\right|}{|\\overrightarrow{AB}|}=\\frac{\\frac{133}{2}}{19}=3,5$ (km).''')

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
            vd_da_1_d = '\\True Để giá trị $v_0$ nhỏ nhất thì góc lệch $\\alpha$ thỏa mãn $\\sin \\alpha = %s$' %(latex(Rational(7, 2*m)))  
            vd_da_1_s = 'Để giá trị $v_0$ nhỏ nhất thì góc lệch $\\alpha$ thỏa mãn $\\sin \\alpha = \\frac{1}{5}$' 
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Trong mặt phẳng $(IAB)$ gọi $\\beta$ là góc $\\widehat{IAB}$ thì $\\cos \\beta = \\frac{\\overrightarrow{AI}\\cdot\\overrightarrow{AB}}{|\\overrightarrow{AI}|\\cdot|\\overrightarrow{AB}|} = \\frac{9}{AI}$ và $\\sin \\beta = \\frac{3,5}{AI}$ \\\\
            Gọi $\\alpha$ là góc lệch của đường bay mới $AH$ so với $AB$ thì $H$ là điểm trên đường bay mới gần $I$ nhất nên $\\Delta AIH$ vuông tại $H$ \\\\
            Vậy $AH = AI\\cdot\\cos \\widehat{IAH}$. \\\\
            Để tránh mặt cầu (nằm cùng phía với $I$) thì góc giữa $AH$ và $AI$ là $\\varphi = \\alpha + \\beta$ \\\\
            Khi đó $AH = AI\\cdot\\cos (\\alpha + \\beta) = AI\\cdot(\\cos \\alpha \\cos \\beta - \\sin \\alpha \\sin \\beta) = 9\\cos \\alpha - 3,5\\sin \\alpha$. \\\\
            Theo đề bài: $v_H=v_0\\cos \\alpha - AH \\Leftrightarrow %s=v_0\\cos \\alpha - (9\\cos \\alpha - 3,5\\sin \\alpha)$ \\\\
            $\\Rightarrow v_0=\\frac{%s}{\\cos \\alpha}+9-3,5\\tan \\alpha \\Rightarrow v'_0(\\alpha)=\\frac{%s\\sin \\alpha - 3,5}{\\cos^2\\alpha}$ \\\\
            Cho $v'_0(\\alpha)=0 \\Leftrightarrow %s\\sin \\alpha - 3,5=0 \\Leftrightarrow \\sin \\alpha = %s$.'''  
                       %(latex(m), latex(m), latex(m), latex(m), latex(Rational(7, 2*m))
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
            vdc_da_1_d = '\\True Giá trị nhỏ nhất của $v_0$ là $9+\\frac{\\sqrt{%s}}{2}$' %(latex(4*m**2 - 49)) 
            vdc_da_1_s = 'Giá trị nhỏ nhất của $v_0$ là $9+\\frac{\\sqrt{%s}}{4}$' %(latex(4*m**2 - 49)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Khi $\\sin \\alpha = \\frac{7}{%s}$ thì $\\cos \\alpha = \\frac{\\sqrt{%s}}{%s}$ và $\\tan \\alpha = \\frac{7}{\\sqrt{%s}}$ \\\\
            $v_{0 Min} = \\frac{%s}{\\cos \\alpha} + 9 - 3,5\\tan \\alpha = \\frac{%s}{\\frac{\\sqrt{%s}}{%s}} + 9 - 3,5\\cdot\\frac{7}{\\sqrt{%s}} = 9 + \\frac{\\sqrt{%s}}{2}$.'''
                       %(latex(2*m), latex(4*m**2 - 49), latex(2*m), latex(4*m**2 - 49),
                         latex(m), latex(m), latex(4*m**2 - 49), latex(2*m), latex(4*m**2 - 49), latex(4*m**2 - 49)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

