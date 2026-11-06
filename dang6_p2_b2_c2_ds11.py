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


def bt_dang6_p2_b2_c2_ds11(self):
            # Khai báo biến
            R = randint(2, 10) 
            R_sq = R**2  # R^2
            Pi = Symbol('\\pi') # Sử dụng ký hiệu Pi trong sympy

            # Nội dung câu hỏi
            noidungcauhoi = ('''Gọi $C$ là nửa đường tròn đường kính $AB = %s$, $C_n$ là đường gồm $2^n$ nửa đường tròn đường kính $\\frac{AB}{2^n}$. Gọi $p_n$ là độ dài của $C_n$, $S_n$ là diện tích hình phẳng giới hạn bởi $C_n$ và đoạn thẳng $AB$.'''
                            '''\\begin{center}
                            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.6]
            	\\clip(-1,-0.1) rectangle (8.1,4.1);
            	\\draw [shift={(4,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*4*cos(\\t r)+0*4*sin(\\t r)},{0*4*cos(\\t r)+1*4*sin(\\t r)});
            	\\draw [shift={(2,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*2*cos(\\t r)+0*2*sin(\\t r)},{0*2*cos(\\t r)+1*2*sin(\\t r)});
            	\\draw [shift={(6,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*2*cos(\\t r)+0*2*sin(\\t r)},{0*2*cos(\\t r)+1*2*sin(\\t r)});
            	\\draw [shift={(1,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*1*cos(\\t r)+0*1*sin(\\t r)},{0*1*cos(\\t r)+1*1*sin(\\t r)});
            	\\draw [shift={(3,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*1*cos(\\t r)+0*1*sin(\\t r)},{0*1*cos(\\t r)+1*1*sin(\\t r)});
            	\\draw [shift={(5,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*1*cos(\\t r)+0*1*sin(\\t r)},{0*1*cos(\\t r)+1*1*sin(\\t r)});
            	\\draw [shift={(7,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*1*cos(\\t r)+0*1*sin(\\t r)},{0*1*cos(\\t r)+1*1*sin(\\t r)});
            	\\draw [shift={(0.5,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*0.5*cos(\\t r)+0*0.5*sin(\\t r)},{0*0.5*cos(\\t r)+1*0.5*sin(\\t r)});
            	\\draw [shift={(1.5,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*0.5*cos(\\t r)+0*0.5*sin(\\t r)},{0*0.5*cos(\\t r)+1*0.5*sin(\\t r)});
            	\\draw [shift={(2.5,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*0.5*cos(\\t r)+0*0.5*sin(\\t r)},{0*0.5*cos(\\t r)+1*0.5*sin(\\t r)});
            	\\draw [shift={(3.5,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*0.5*cos(\\t r)+0*0.5*sin(\\t r)},{0*0.5*cos(\\t r)+1*0.5*sin(\\t r)});
            	\\draw [shift={(4.5,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*0.5*cos(\\t r)+0*0.5*sin(\\t r)},{0*0.5*cos(\\t r)+1*0.5*sin(\\t r)});
            	\\draw [shift={(5.5,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*0.5*cos(\\t r)+0*0.5*sin(\\t r)},{0*0.5*cos(\\t r)+1*0.5*sin(\\t r)});
            	\\draw [shift={(6.5,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*0.5*cos(\\t r)+0*0.5*sin(\\t r)},{0*0.5*cos(\\t r)+1*0.5*sin(\\t r)});
            	\\draw [shift={(7.5,0)},line width=1.2pt]  plot[domain=0:3.141592653589793,variable=\\t]({1*0.5*cos(\\t r)+0*0.5*sin(\\t r)},{0*0.5*cos(\\t r)+1*0.5*sin(\\t r)});
            	\\draw [line width=1.2pt] (0,0)-- (8,0);
            \\end{tikzpicture}
                            \\end{center}'''
                             %(latex(2*R)))

            ######################################################################## Nhận biết (Tính pn) ############################################

            # Đáp án đúng: pn = Pi * R
            pn_d = Pi * R
            nb_da_1_d = '\\True Độ dài $p_n$ là $%s$' %(latex(pn_d))
            # Đáp án sai: pn = 2 * Pi * R (Nhầm với chu vi cả đường tròn lớn)
            nb_da_1_s = 'Độ dài $p_n$ là $%s$' %(latex(2*Pi*R)) 
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            # Lời giải
            loigiai_nb_1 = ('''Độ dài của $2^n$ nửa đường tròn, mỗi nửa có bán kính\\\\ \n'''
                            ''' $r_n = \\frac{R}{2^n}$ là: $p_n = 2^n \\cdot (\\pi r_n) = 2^n \\cdot \\pi \\frac{R}{2^n} = \\pi R = %s$.''' %(latex(pn_d)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################Thông hiểu (Tính S1) ############################################
            # Diện tích nửa hình tròn lớn ban đầu (S0)
            S0 = Pi * R_sq / 2 
            # Diện tích S1: n=1. S1 = S0/2 = Pi * R^2 / 4
            S1 = S0 / 2 

            # Đáp án đúng
            th_da_1_d = '\\True Diện tích $S_1$ là $%s$' %(latex(S1))
            # Đáp án sai: S1 = S0 (bỏ qua hệ số 1/2)
            th_da_1_s = 'Diện tích $S_1$ là $%s$' %(latex(S0)) 
            list_th_da_1=[th_da_1_d,th_da_1_s]
            # Lời giải
            loigiai_th_1 = ('''Với $n=1$, $S_1$ là tổng diện tích 2 nửa hình tròn bán kính\\\\ \n'''
                            ''' $\\frac{R}{2}$: $S_1 = 2 \\cdot \\frac{1}{2} \\pi \\left(\\frac{R}{2}\\right)^2 = \\frac{\\pi R^2}{4} = %s$.''' %(latex(S1)))
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng (Công thức Sn) ############################################
            # Sn = (Pi * R^2 / 2) * (1/2)^n 
            # Ta viết lại: Sn = (Pi * R^2 / 4) * (1/2)^(n-1) = S1 * (1/2)^(n-1)
            q = Rational(1, 2)
            S_n = S1 * q**(Symbol('n')-1)

            # Đáp án đúng
            vd_da_1_d = '\\True Công thức diện tích $S_n$ là $S_n=%s \\cdot \\left( %s \\right)^{n-1}$' %(latex(S1), latex(q))
            # Đáp án sai: Công thức sai q = 1/4
            vd_da_1_s = 'Công thức diện tích $S_n$ là $S_n=%s \\cdot \\left( %s \\right)^{n-1}$' %(latex(S1), latex(Rational(1, 4))) 
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            # Lời giải
            loigiai_vd_1 = ('''Dãy diện tích $(S_n)$ là cấp số nhân lùi vô hạn với số hạng đầu $S_1=%s$ và công bội $q=\\frac{1}{2}$. Công thức là $S_n = S_1 \\cdot q^{n-1} = %s \\cdot \\left(\\frac{1}{2}\\right)^{n-1}$.'''
                        %(latex(S1), latex(S1)))
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao (Tổng vô hạn S) ############################################
            # Tính tổng vô hạn của Sn (n từ 1 đến vô hạn)
            # Tổng S_inf = S1 / (1 - q) = (Pi * R^2 / 4) / (1/2) = Pi * R^2 / 2 = S0
            S_inf = S1 / (1 - q) 

            # Đáp án đúng
            vdc_da_1_d = '\\True Tổng diện tích $\\sum_{n=1}^{\\infty} S_n$ là $%s$' %(latex(S_inf))
            # Đáp án sai: Chỉ lấy S1 + S2
            S1_S2 = S1 + S1/2
            vdc_da_1_s = 'Tổng diện tích $\\sum_{n=1}^{\\infty} S_n$ là $%s$' %(latex(S1_S2)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            # Lời giải
            loigiai_vdc_1 = ('''Tổng diện tích của chuỗi nửa đường tròn là tổng cấp số nhân lùi vô hạn:\\\\ \n'''
                        '''$S = \\sum_{n=1}^{\\infty} S_n = \\frac{S_1}{1-q} = \\frac{%s}{1-\\frac{1}{2}} = 2 S_1 = %s$.'''
                        %(latex(S1), latex(S_inf)))
            list_vdc_2 = [loigiai_vdc_1]


            ######################################################################## Logic chọn và xáo trộn ############################################

            def count_true_answers(answers):
                # Hàm đếm số đáp án đúng
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi 4 đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (đảm bảo đáp án được chọn ngẫu nhiên)
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            # Kết hợp đáp án và lời giải cho từng cấp độ
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

