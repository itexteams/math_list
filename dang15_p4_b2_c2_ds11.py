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


def bt_dang15_p4_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':

                # 1. Random tham số a (có thể là một số nguyên hoặc phân số)
                a_val = random.choice([3, 5, 10, Rational(1, 2), Rational(3, 4)])
                a = a_val

                # 2. Random góc alpha (30 độ hoặc 60 độ)
                alpha_deg = random.choice([30])
                alpha_rad = alpha_deg * pi / 180

                # 3. Tính toán công bội và tổng
                q = cos(alpha_rad) # Công bội

                # Số hạng đầu tiên của chuỗi: u1 = A1A2 = a
                u1 = a

                # Tổng độ dài đường gấp khúc L = u1 / (1 - q)
                L = simplify(u1 / (1 - q))

                # Xử lý kết quả cho Latex và đáp án
                if alpha_deg == 30:
                    # q = sqrt(3)/2, L = a * 2 / (2 - sqrt(3)) = 2*a*(2 + sqrt(3))
                    # Sử dụng biểu thức chính xác để đảm bảo tính đúng đắn của phép toán
                    L_final = 2*a*(2 + sqrt(3))
                    q_latex = '\\frac{\\sqrt{3}}{2}'
                    cos_alpha_latex = '\\cos 30^\\circ'
                elif alpha_deg == 60:
                    # q = 1/2, L = a * 2 / (2 - 1) = 2*a
                    L_final = 2*a
                    q_latex = '\\frac{1}{2}'
                    cos_alpha_latex = '\\cos 60^\\circ'

                kq = L_final
                latex_kq = latex(kq)

                # Các đáp án trắc nghiệm (Tạo 4 đáp án bao gồm 1 đáp án đúng và 3 đáp án sai)
                # Đáp án đúng
                du = ['$%s$'%(latex_kq),]
                da = random.choice(du)

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $\\text{O}\\text{A}_2\\text{A}_1$ vuông tại $\\text{A}_2$, $\\text{A}_2\\text{A}_1 = %s$ và $\\widehat{\\text{A}_1\\text{O}\\text{A}_2} = %s^\\circ$. Hạ các đường vuông góc $\\text{A}_2\\text{A}_3 \\perp \\text{O}\\text{A}_1$, $\\text{A}_3\\text{A}_4 \\perp \\text{O}\\text{A}_2$, $\\text{A}_4\\text{A}_5 \\perp \\text{O}\\text{A}_1,\\dots$ Tiếp tục quá trình này, ta nhận được đường gấp khúc $\\text{A}_1\\text{A}_2\\text{A}_3\\text{A}_4\\text{A}_5\\dots$ Tính độ dài đường gấp khúc này.'''
                                  '''\\begin{center}
                                  \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.8]
            				\\clip(-0.9,-0.7) rectangle (8,4.7);
            				\\draw [shift={(0,0)},line width=1.2pt] (0,0) -- (0:0.4877325396752661) arc (0:29.74488129694222:0.4877325396752661) -- cycle;
            				\\draw [line width=1.2pt] (0,0)-- (7,4);
            				\\draw [line width=1.2pt] (7,4)-- (7,0);
            				\\draw [line width=1.2pt] (7,0)-- (0,0);
            				\\draw [line width=1.2pt] (7,0)-- (5.276923076923077,3.0153846153846153);
            				\\draw [line width=1.2pt] (5.276923076923077,3.0153846153846153)-- (5.276923076923077,0);
            				\\draw [line width=1.2pt] (5.276923076923077,0)-- (3.977988165680473,2.2731360946745562);
            				\\draw [line width=1.2pt] (3.977988165680473,2.2731360946745562)-- (3.977988165680473,0);
            				\\draw [line width=1.2pt] (2.9987910787437415,1.713594902139281)-- (3.977988165680473,0);
            				\\draw (-0.6765015919913508,0) node[anchor=north west] {$O$};
            				\\draw (6.737033011072693,0) node[anchor=north west] {$A_2$};
            				\\draw (2.379955656640316,2.5) node[anchor=north west] {$A_7$};
            				\\draw (3.4692249952484104,3.2) node[anchor=north west] {$A_5$};
            				\\draw (4.769845101049119,3.9) node[anchor=north west] {$A_3$};
            				\\draw (6.672002005782657,4.8) node[anchor=north west] {$A_1$};
            				\\draw (0.819211529679465,0.8) node[anchor=north west] {$30^0$};
            				\\draw (7,2.345306490091056) node[anchor=north west] {$%s$};
            				\\draw (3.61554475715099,0) node[anchor=north west] {$A_6$};
            				\\draw (4.997453619564244,0) node[anchor=north west] {$A_4$};
            			\\end{tikzpicture}
                                  \\end{center}'''
                                 %(latex(a_val), latex(alpha_deg), latex(a)))


                # Nội dung lời giải
                loigiai=('''Các góc $\\widehat{\\text{A}_1\\text{A}_2\\text{A}_3}, \\widehat{\\text{A}_2\\text{A}_3\\text{A}_4}, \\dots$ đều bằng góc $\\widehat{\\text{A}_1\\text{O}\\text{A}_2}=%s^\\circ$.
                \\\\
                Các đoạn thẳng của đường gấp khúc là $\\text{A}_1\\text{A}_2, \\text{A}_2\\text{A}_3, \\text{A}_3\\text{A}_4, \\dots$
                \\begin{enumerate}
                \\item Số hạng đầu: $\\text{A}_1\\text{A}_2 = a = %s$.
                \\item $\\text{A}_2\\text{A}_3 = \\text{A}_1\\text{A}_2 \\cdot %s = a \\cdot %s.$
                \\item $\\text{A}_3\\text{A}_4 = \\text{A}_2\\text{A}_3 \\cdot %s = a \\cdot \\left(%s\\right)^2.$
                \\end{enumerate}
                Độ dài các đoạn $\\text{A}_1\\text{A}_2, \\text{A}_2\\text{A}_3, \\text{A}_3\\text{A}_4, \\dots$ tạo thành cấp số nhân lùi vô hạn với số hạng đầu $u_1 = %s$ và công bội $q = %s$.
                \\\\
                Độ dài đường gấp khúc $\\text{L}$ là tổng của cấp số nhân lùi vô hạn:
                $$\\text{L} = \\frac{u_1}{1 - q} = \\frac{%s}{1 - %s} = %s.$$
                '''
                %(latex(alpha_deg), latex(a_val), cos_alpha_latex, q_latex, cos_alpha_latex, q_latex, latex(a_val), q_latex, latex(a_val), q_latex, latex_kq)
                )

            if dang=='2':

                # 1. Random tham số a (có thể là một số nguyên hoặc phân số)
                a_val = random.choice([3, 5, 10, Rational(1, 2), Rational(3, 4)])
                a = a_val

                # 2. Random góc alpha (30 độ hoặc 60 độ)
                alpha_deg = random.choice([60])
                alpha_rad = alpha_deg * pi / 180

                # 3. Tính toán công bội và tổng
                q = cos(alpha_rad) # Công bội

                # Số hạng đầu tiên của chuỗi: u1 = A1A2 = a
                u1 = a

                # Tổng độ dài đường gấp khúc L = u1 / (1 - q)
                L = simplify(u1 / (1 - q))

                # Xử lý kết quả cho Latex và đáp án
                if alpha_deg == 30:
                    # q = sqrt(3)/2, L = a * 2 / (2 - sqrt(3)) = 2*a*(2 + sqrt(3))
                    # Sử dụng biểu thức chính xác để đảm bảo tính đúng đắn của phép toán
                    L_final = 2*a*(2 + sqrt(3))
                    q_latex = '\\frac{\\sqrt{3}}{2}'
                    cos_alpha_latex = '\\cos 30^\\circ'
                elif alpha_deg == 60:
                    # q = 1/2, L = a * 2 / (2 - 1) = 2*a
                    L_final = 2*a
                    q_latex = '\\frac{1}{2}'
                    cos_alpha_latex = '\\cos 60^\\circ'

                kq = L_final
                latex_kq = latex(kq)

                # Các đáp án trắc nghiệm (Tạo 4 đáp án bao gồm 1 đáp án đúng và 3 đáp án sai)
                # Đáp án đúng
                du = ['$%s$'%(latex_kq),]
                da = random.choice(du)

                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                    '''Cho tam giác $\\text{O}\\text{A}_2\\text{A}_1$ vuông tại $\\text{A}_2$, $\\text{A}_2\\text{A}_1 = %s$ và $\\widehat{\\text{A}_1\\text{O}\\text{A}_2} = %s^\\circ$. Hạ các đường vuông góc $\\text{A}_2\\text{A}_3 \\perp \\text{O}\\text{A}_1$, $\\text{A}_3\\text{A}_4 \\perp \\text{O}\\text{A}_2$, $\\text{A}_4\\text{A}_5 \\perp \\text{O}\\text{A}_1,\\dots$ Tiếp tục quá trình này, ta nhận được đường gấp khúc $\\text{A}_1\\text{A}_2\\text{A}_3\\text{A}_4\\text{A}_5\\dots$ Tính độ dài đường gấp khúc này.'''
                                  '}{'
                    '''\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.5]
            				\\clip(-1,-1) rectangle (9,13.6);
            	\\draw [shift={(0,0)},line width=1.2pt] (0,0) -- (0:0.7826286340356788) arc (0:60.204046114415014:0.7826286340356788) -- cycle;
            	\\draw [line width=1.2pt] (0,0)-- (6.9867157696595035,12.201491345278876);
            	\\draw [line width=1.2pt] (6.9867157696595035,12.201491345278876)-- (7,0);
            	\\draw [line width=1.2pt] (7,0)-- (0,0);
            	\\draw [line width=1.2pt] (7,0)-- (1.7284554801986745,3.018547666405467);
            	\\draw [line width=1.2pt] (1.7284554801986745,3.018547666405467)-- (1.7284554801986745,0);
            	\\draw [line width=1.2pt] (1.7284554801986745,0)-- (0.42679404957554706,0.745346465177064);
            	\\draw (-1.0740780222509183,0) node[anchor=north west] {$O$};
            	\\draw (6.726120696971347,0) node[anchor=north west] {$A_2$};
            	\\draw (-0.7088513263676015,2.329386072170219) node[anchor=north west] {$A_5$};
            	\\draw (0.6998802148966203,4.416395762932027) node[anchor=north west] {$A_3$};
            	\\draw (6.386981622222553,13.75576412909112) node[anchor=north west] {$A_1$};
            	\\draw (7,6.503405453693835) node[anchor=north west] {$%s$};
            	\\draw (1.4042459855287313,0) node[anchor=north west] {$A_4$};
            \\end{tikzpicture}}'''
                                 %(latex(a_val), latex(alpha_deg), latex(a)))


                # Nội dung lời giải
                loigiai=('''Các góc $\\widehat{\\text{A}_1\\text{A}_2\\text{A}_3}, \\widehat{\\text{A}_2\\text{A}_3\\text{A}_4}, \\dots$ đều bằng góc $\\widehat{\\text{A}_1\\text{O}\\text{A}_2}=%s^\\circ$.
                \\\\
                Các đoạn thẳng của đường gấp khúc là $\\text{A}_1\\text{A}_2, \\text{A}_2\\text{A}_3, \\text{A}_3\\text{A}_4, \\dots$
                \\begin{enumerate}
                \\item Số hạng đầu: $\\text{A}_1\\text{A}_2 = a = %s$.
                \\item $\\text{A}_2\\text{A}_3 = \\text{A}_1\\text{A}_2 \\cdot %s = a \\cdot %s.$
                \\item $\\text{A}_3\\text{A}_4 = \\text{A}_2\\text{A}_3 \\cdot %s = a \\cdot \\left(%s\\right)^2.$
                \\end{enumerate}
                Độ dài các đoạn $\\text{A}_1\\text{A}_2, \\text{A}_2\\text{A}_3, \\text{A}_3\\text{A}_4, \\dots$ tạo thành cấp số nhân lùi vô hạn với số hạng đầu $u_1 = %s$ và công bội $q = %s$.
                \\\\
                Độ dài đường gấp khúc $\\text{L}$ là tổng của cấp số nhân lùi vô hạn:
                $$\\text{L} = \\frac{u_1}{1 - q} = \\frac{%s}{1 - %s} = %s.$$
                '''
                %(latex(alpha_deg), latex(a_val), cos_alpha_latex, q_latex, cos_alpha_latex, q_latex, latex(a_val), q_latex, latex(a_val), q_latex, latex_kq)
                )


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

