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


def bt_dang9_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Nghiên cứu đề bài và thiết lập thông số ngẫu nhiên
            # a_val: độ dài cạnh đáy (hình vuông)
            # l_val: độ dài cạnh bên
            a_val = random.choice([210, 220, 230, 240, 250])
            l_val = random.choice([210, 215, 219, 225, 230])

            # Đảm bảo điều kiện hình chóp tồn tại (l > a*sqrt(2)/2)
            while l_val <= (a_val * math.sqrt(2) / 2):
                l_val += 10

            # Tính toán các giá trị
            # 1. Chiều cao SO
            so_val = math.sqrt(l_val**2 - (a_val**2) / 2)
            so_str = str(round(so_val, 2)).replace('.', ',')

            # 2. Góc giữa cạnh bên SC và cạnh đáy AB
            # Vì AB // CD nên góc (SC, AB) = góc (SC, CD)
            # Trong tam giác SCD cân tại S, gọi M là trung điểm CD -> cos(SCD) = (a/2) / l
            cos_alpha = a_val / (2 * l_val)
            alpha_val = math.degrees(math.acos(cos_alpha))
            alpha_str = str(round(alpha_val, 1)).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''\\immini{Kim tự tháp Cheops là kim tự tháp lớn nhất trong các kim tự tháp ở Ai Cập. Kim tự tháp có dạng hình chóp với đáy là hình vuông có cạnh dài khoảng $%s m$, các cạnh bên bằng nhau và dài khoảng $%s m$. Kim tự tháp Cheops được mô phỏng bởi hình chóp $S.ABCD$ với $O$ là giao điểm của hai đường chéo $AC$ và $BD$.}''' 
                             r'''{\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
                             		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (183.47,120.69) -- (337.47,121.4) ;
                             		\draw [line width=1]    (106.47,175.69) -- (260.47,176.4) ;
                             		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (183.47,120.69) -- (106.47,175.69) ;
                             		\draw [line width=1]    (337.47,121.4) -- (260.47,176.4) ;
                             		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (183.47,120.69) -- (260.47,176.4) ;
                             		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (106.47,175.69) -- (337.47,121.4) ;
                             		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (221.97,148.54) -- (220.47,32.4) ;
                             		\draw [line width=1]    (106.47,175.69) -- (220.47,32.4) ;
                             		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (183.47,120.69) -- (220.47,32.4) ; 
                             		\draw [line width=1]    (260.47,176.4) -- (220.47,32.4) ;
                             		\draw [line width=1]    (220.47,32.4) -- (337.47,121.4) ;
                             		\draw (164.47,99.04) node [anchor=north west][inner sep=0.75pt]    {$A$};
                             		\draw (90,172) node [anchor=north west][inner sep=0.75pt]    {$B$};
                             		\draw (260.47,176.4) node [anchor=north west][inner sep=0.75pt]    {$C$};
                             		\draw (214,11) node [anchor=north west][inner sep=0.75pt]    {$S$};
                             		\draw (208,149) node [anchor=north west][inner sep=0.75pt]    {$O$};
                             		\draw (338.68,103.54) node [anchor=north west][inner sep=0.75pt]    {$D$};
                             	\end{tikzpicture}}'''%(a_val, l_val))

            # --- Mệnh đề (a) ---
            alpha_wrong = str(round(alpha_val + random.uniform(5, 10), 1)).replace('.', ',')
            a_true = '\\True Góc tạo bởi cạnh bên $SC$ và cạnh đáy $AB$ của kim tự tháp (gần đúng) là $%s^\\circ$' % alpha_str
            a_false = 'Góc tạo bởi cạnh bên $SC$ và cạnh đáy $AB$ của kim tự tháp (gần đúng) là $%s^\\circ$' % alpha_wrong
            list_a = [a_true, a_false]
            nb_da_1 = random.choice(list_a)
            loigiai_nb_1 = ('''Vì $AB // CD$ nên góc giữa $SC$ và $AB$ bằng góc giữa $SC$ và $CD$. \\\\ Xét $\\triangle SCD$ có $SC=SD=%s, CD=%s$. \\\\ Áp dụng định lí hàm số cosin: \\\\ $\\cos \\widehat{SCD} = \\frac{SC^2+CD^2-SD^2}{2 \\cdot SC \\cdot CD} = \\frac{CD}{2 \\cdot SC} = \\frac{%s}{2 \\cdot %s}$. Suy ra $\\widehat{SCD} \\approx %s^\\circ$.''' 
                            %(l_val, a_val, a_val, l_val, alpha_str))

            # --- Mệnh đề (b) ---
            b_true = '\\True Đường thẳng $SO$ vuông góc với mặt phẳng đáy $(ABCD)$'
            b_false = 'Đường thẳng $SO$ không vuông góc với mặt phẳng đáy $(ABCD)$'
            list_b = [b_true, b_false]
            th_da_1 = random.choice(list_b)
            loigiai_th_1 = ('''Vì hình chóp $S.ABCD$ có đáy là hình vuông và các cạnh bên bằng nhau ($SA=SB=SC=SD$) nên $S$ cách đều các đỉnh $A, B, C, D$. Do đó, hình chiếu của $S$ lên mặt đáy trùng với tâm $O$ của hình vuông $ABCD$. Vậy $SO \\perp (ABCD)$.''')

            # --- Mệnh đề (c) ---
            c_true = '\\True Đường thẳng $SO$ vuông góc với cạnh đáy $AB$ và $BC$'
            c_false = 'Đường thẳng $SO$ song song với cạnh đáy $AB$ và $BC$'
            list_c = [c_true, c_false]
            vd_da_1 = random.choice(list_c)
            loigiai_vd_1 = ('''Vì $SO \\perp (ABCD)$ mà $AB, BC$ nằm trong mặt phẳng $(ABCD)$ nên $SO \\perp AB$ và $SO \\perp BC$.''')

            # --- Mệnh đề (d) ---
            so_wrong = str(round(so_val - 10.5, 2)).replace('.', ',')
            d_true = '\\True Biết rằng độ dài $SO$ chính là chiều cao của kim tự tháp Cheops, ta tính được $SO \\approx %s m$' % so_str
            d_false = 'Biết rằng độ dài $SO$ chính là chiều cao của kim tự tháp Cheops, ta tính được $SO \\approx %s m$' % so_wrong
            list_d = [d_true, d_false]
            vdc_da_1 = random.choice(list_d)
            loigiai_vdc_1 = ('''Ta có $AC$ là đường chéo hình vuông cạnh $%s$ nên $AC = %s\\sqrt{2} \\Rightarrow OC = \\frac{AC}{2} = \\frac{%s\\sqrt{2}}{2}$. Xét tam giác $SOC$ vuông tại $O$: \\\\ $SO = \\sqrt{SC^2 - OC^2} = \\sqrt{%s^2 - \\left( \\frac{%s\\sqrt{2}}{2} \\right)^2} \\approx %s m$.''' 
                             %(a_val, a_val, a_val, l_val, a_val, so_str))

            # Xử lý xáo trộn và chọn đáp án
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_a)
                ans_b = random.choice(list_b)
                ans_c = random.choice(list_c)
                ans_d = random.choice(list_d)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break



            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

