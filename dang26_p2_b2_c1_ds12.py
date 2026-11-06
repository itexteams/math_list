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


def bt_dang26_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Chọn ngẫu nhiên cạnh của lục giác đều lớn ban đầu (chọn số chẵn để số liệu tính toán đẹp)
            a_val = random.choice([4, 6, 8, 10, 12])

            # Tính toán các đại lượng hình học theo a_val
            # 1. Thể tích cực đại: V_max = a^3 / 3
            V_max_exact = Rational(a_val**3, 3)
            latex_V_max = latex(V_max_exact)

            # Thể tích sai để làm nhiễu phương án a
            V_max_wrong = latex(Rational(a_val**3 * 6, 25))

            # 2. Chiều cao h của khối chóp: h = sqrt(a^2 - 4*x^2/3)
            h_expr = sqrt(a_val**2 - Rational(4, 3) * x**2)
            latex_h = latex(h_expr)

            # Chiều cao sai để làm nhiễu phương án b
            latex_h_wrong = latex(sqrt(a_val**2 - 3 * x**2))

            # 3. Cạnh đáy d của khối chóp: d = (2*sqrt(3)*x)/3
            d_expr = (2 * sqrt(3) * x) / 3
            latex_d = latex(d_expr)

            # Cạnh đáy sai để làm nhiễu phương án d
            latex_d_wrong = latex((sqrt(3) * x) / 3)
            hinhve=r'''\scalebox{0.7}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (303.86,145.82) -- (246.97,244.35) -- (133.19,244.35) -- (76.3,145.82) -- (133.19,47.29) -- (246.97,47.29) -- cycle ;
            	\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (222.29,164.42) -- (190.08,183.01) -- (157.87,164.42) -- (157.87,127.22) -- (190.08,108.63) -- (222.29,127.22) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (133.19,47.29) -- (246.97,244.35) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (246.97,47.29) -- (133.19,244.35) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (76.3,145.82) -- (303.86,145.82) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (246.97,47.29) -- (190.08,108.63) -- (133.19,47.29) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (303.86,145.82) -- (222.29,127.22) -- (246.97,47.29) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (246.97,244.35) -- (222.29,164.42) -- (303.86,145.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (246.97,244.35) -- (190.08,183.01) -- (133.19,244.35) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (133.19,47.29) -- (157.87,127.22) -- (76.3,145.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (157.87,164.42) -- (133.19,244.35) -- (76.3,145.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=1]  (156.03,145.65) .. controls (156.03,144.74) and (156.77,144) .. (157.68,144) .. controls (158.59,144) and (159.33,144.74) .. (159.33,145.65) .. controls (159.33,146.56) and (158.59,147.3) .. (157.68,147.3) .. controls (156.77,147.3) and (156.03,146.56) .. (156.03,145.65) -- cycle ;
            	\draw (56.08,131.05) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (121.03,246.4) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (245.1,242.87) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (305.7,134.19) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\draw (247.36,24.73) node [anchor=north west][inner sep=0.75pt]    {$E$};
            	\draw (119.46,22.77) node [anchor=north west][inner sep=0.75pt]    {$F$};
            	\draw (196.74,129) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (133.88,143.45) node [anchor=north west][inner sep=0.75pt]    {$M$};
            \end{tikzpicture} }'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Từ một tấm bìa mỏng hình lục giác đều $ABCDEF$ cạnh %s cm, bên trong có một lục giác đều nhỏ hơn. Các đường chéo $AD, BE, CF$ cắt nhau tại $O$, cắt cạnh lục giác đều nhỏ tại $M$. Đặt $OM = x$ (cm). Người ta cắt bỏ 6 tam giác cân bằng nhau có cạnh đáy là cạnh của lục giác đều ban đầu và đỉnh là đỉnh của lục giác đều nhỏ phía trong rồi gấp lên sao cho các đỉnh $A, B, C, D, E, F$ trùng nhau tạo thành một khối chóp lục giác đều.}{%s}'''              
                             %(a_val, hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = 'Tam giác $OAB$ vuông cân tại $O$'
            nb_da_1_s = '\\True Tam giác $OAB$ là tam giác đều'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Với lục giác đều cạnh %s thì $OA = OB = AB = %s$ nên tam giác $OAB$ là tam giác đều.'''
                        % (a_val, a_val))

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
            th_da_1_d = '\\True Cạnh đáy của khối chóp lục giác đều bằng $%s$ (cm)' % (latex_d)  
            th_da_1_s = 'Cạnh đáy của khối chóp lục giác đều bằng $%s$ (cm)' % (latex_d_wrong)   
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Khoảng cách từ tâm đến cạnh của lục giác đều đáy là $OM = x$. Do đó cạnh đáy của khối chóp lục giác đều bằng $\\frac{x}{\\cos 30^\\circ} = %s$ (cm).'''       
                       % (latex_d))

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
            vd_da_1_d = '\\True Đường cao của khối chóp lục giác đều bằng $%s$ (cm)' % (latex_h)  
            vd_da_1_s = 'Đường cao của khối chóp lục giác đều bằng $%s$ (cm)' % (latex_h_wrong)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có cạnh bên bằng %s và bán kính ngoại tiếp đáy bằng cạnh đáy là $%s$, nên đường cao là $h = \\sqrt{%s^2 - \\left(%s\\right)^2} = %s$ (cm).'''  
                       % (a_val, latex_d, a_val, latex_d, latex_h))

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
            vdc_da_1_d = '\\True Thể tích lớn nhất của khối chóp lục giác đều có thể đạt được là $%s$ (cm$^3$)' % (latex_V_max) 
            vdc_da_1_s = 'Thể tích lớn nhất của khối chóp lục giác đều có thể đạt được là $%s$ (cm$^3$)' % (V_max_wrong) 
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có thể tích khối chóp là: \\\\
            $V(x) = \\frac{1}{3} S_{\\text{đáy}} \\cdot h = \\frac{1}{3} \\cdot 6 \\cdot \\frac{\\left(%s\\right)^2 \\sqrt{3}}{4} \\cdot %s = \\frac{2\\sqrt{3}}{3} x^2 %s$. \\\\
            Xét hàm số $f(x) = x^4 \\left(%s^2 - \\frac{4}{3}x^2\\right) = %s x^4 - \\frac{4}{3} x^6$. \\\\
            Lấy đạo hàm và tìm cực đại ta thu được thể tích lớn nhất bằng $%s$ (cm$^3$).'''
                       % (latex_d, latex_h, latex_h, a_val, a_val**2, latex_V_max))

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
                '\\begin{ex}\n' +
            str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

