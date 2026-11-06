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


def bt_dang28_p2_b3_c1_ds11(self):
            # Khai báo biến
            t = symbols('t')

            # B3-Suy nghĩ tìm cách random bài toán
            # Đề gốc: x = 1.5 * cos(t*pi / 4)
            # Ta random biên độ A lấy giá trị thập phân (1,5 hoặc 2,5 hoặc 3,5)
            A_val = random.choice([1.5, 2.5, 3.5])
            A_str = str(A_val).replace('.', ',')

            # Random mẫu số của góc quét pha (ví dụ: 2, 4, 6) để tính toán chu kỳ tuần hoàn tương ứng
            mau_so = random.choice([2, 4, 6])
            # Chu kỳ T = 2*pi / omega = 2*pi / (pi/mau_so) = 2 * mau_so
            T_chu_ky = 2 * mau_so

            # Các mốc thời gian động theo chu kỳ cho câu b và d
            t_b = int(2.5 * mau_so)  # Trong đề gốc mẫu=4 -> t_b = 10
            t_d = int(5 * mau_so)    # Trong đề gốc mẫu=4 -> t_d = 20


            so_lan_xa_vtcb_dung = 3
            so_lan_xa_vtcb_sai = 2


            so_lan_vtcb_dung = 5
            so_lan_vtcb_sai = 4

            # Tạo chuỗi latex cho phương trình
            expr_goc = "%s\\cos\\left( \\frac{t\\pi}{%s} \\right)" % (A_str, latex(mau_so))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một nghệ sĩ xiếc dao động xung quanh vị trí cân bằng theo phương trình $x = %s$; trong đó $t$ là thời gian được tính bằng giây và quãng đường $h = |x|$ được tính bằng mét là khoảng cách theo phương ngang của chất điểm đối với vị trí cân bằng. Khi đó:
                             \\begin{center} \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                             	\\draw  [fill={rgb, 255:red, 239; green, 206; blue, 152 }  ,fill opacity=1 ][line width=1]  (236,158.26) -- (233.15,161.37) -- (228.75,156.97) -- (234.95,152.29) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (231.3,161.55) -- (235.48,163.04) -- (239.07,169.32) -- (237.27,176.79) -- (227.41,173.2) -- (224.12,170.81) -- (225.92,163.64) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (230.7,173.8) -- (237.27,176.79) -- (231.6,195.62) -- (228.01,198.61) -- (222.93,206.08) -- (220.51,204.94) -- (217.85,203.69) -- (219.34,201.3) -- (217.55,197.41) -- (213.37,196.21) -- (210.38,193.23) -- (204.4,187.55) -- (215.16,185.46) -- (222.63,180.08) -- cycle ;
                             	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (226.16,188.05) -- (235.33,175.95) -- (228.75,189.08) -- (222.01,191.67) -- (213.21,190.38) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (230.3,164.99) -- (230.7,173.8) -- (226.16,174.58) -- (224.12,170.81) -- (227.71,164.74) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 239; green, 206; blue, 152 }  ,fill opacity=1 ][line width=1]  (231.3,161.55) -- (229.44,165.05) -- (227.41,162.32) -- (228.97,159.48) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=1]  (223.1,205.2) -- (220.46,212.13) -- (220.46,212.13) -- (219.42,210.32) -- (220.51,204.94) -- cycle ;
                             	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=1]  (234.95,152.29) .. controls (235.27,153.19) and (235.74,154.72) .. (235.13,155.12) .. controls (232.65,154.9) and (229.28,155.35) .. (231.53,160.07) .. controls (229.89,159.68) and (228.39,156.87) .. (227.03,156.58) .. controls (222.75,156.81) and (218.81,157.3) .. (214.76,154.22) .. controls (224.78,158.27) and (227.59,150.62) .. (234.95,152.29) -- cycle ;
                             	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (266.02,25.53) -- (266.02,237.47) ;
                             	\\draw [shift={(266.02,25.53)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]      (0, 0) circle [x radius= 4.36, y radius= 4.36]   ;
                             	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (266.02,25.53) -- (375.73,185.52) ;
                             	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (266.02,25.53) -- (163.07,186.9) ;
                             	\\draw [line width=1]    (163.07,186.9) .. controls (226.59,224.18) and (294.26,235.23) .. (375.73,185.52) ;
                             	\\draw [shift={(375.73,185.52)}, rotate = 328.61] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]      (0, 0) circle [x radius= 4.36, y radius= 4.36]   ;
                             	\\draw [shift={(163.07,186.9)}, rotate = 30.41] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]      (0, 0) circle [x radius= 4.36, y radius= 4.36]   ;
                             	\\draw [line width=1]    (266.02,25.53) -- (218.4,210.13) ;
                             	\\draw [shift={(218.4,210.13)}, rotate = 104.46] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]      (0, 0) circle [x radius= 4.36, y radius= 4.36]   ;
                             	\\draw [line width=1]    (261.73,210.13) -- (227.07,210.13) ;
                             	\\draw [shift={(223.07,210.13)}, rotate = 360] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                             	\\draw [shift={(265.73,210.13)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                             	\\draw (239.33,187.67) node [anchor=north west][inner sep=0.75pt]    {$h$};
                             \\end{tikzpicture} \\end{center}''' % (expr_goc))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Người đó ở xa vị trí cân bằng nhất nghĩa là $h = %s\\text{ m}$' % (A_str)
            nb_da_1_s = 'Người đó ở xa vị trí cân bằng nhất nghĩa là $h = 0\\text{ m}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Khoảng cách từ người đó đến vị trí cân bằng là $h = |x| = \\left| %s \\right|$.\\\\
            Do $\\left|\\cos\\left( \\frac{t\\pi}{%s} \\right)\\right| \\le 1$ nên $h \\le %s$.\\\\
            Vậy người đó ở xa vị trí cân bằng nhất khi $h = %s\\text{ m}$''' 
                            % (expr_goc, latex(mau_so), A_str, A_str))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = 'Trong $%s$ giây đầu tiên, có %s thời điểm người đó ở xa vị trí cân bằng nhất' % (latex(t_b), latex(so_lan_xa_vtcb_sai))
            th_da_1_s = '\\True Trong $%s$ giây đầu tiên, có %s thời điểm người đó ở xa vị trí cân bằng nhất' % (latex(t_b), latex(so_lan_xa_vtcb_dung))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Người đó ở xa vị trí cân bằng nhất khi $\\left|\\cos\\left( \\frac{t\\pi}{%s} \\right)\\right| = 1 \\Leftrightarrow \\frac{t\\pi}{%s} = k\\pi \\Leftrightarrow t = k \\cdot %s$ với $k \\in \\mathbb{Z}$.\\\\
            Xét khoảng thời gian $%s$ giây đầu tiên ($0 \\le t \\le %s$), ta có:\\\\
            $0 \\le k \\cdot %s \\le %s \\Leftrightarrow 0 \\le k \\le 2,5$.\\\\
            Vì $k \\in \\mathbb{Z}$ nên $k \\in \\{0; 1; 2\\}$, tương ứng với các thời điểm $t = 0\\text{ s}$, $t = %s\\text{ s}$, $t = %s\\text{ s}$.\\\\
            Vậy có tất cả %s thời điểm người đó ở xa vị trí cân bằng nhất.''' 
                            % (latex(mau_so), latex(mau_so), latex(mau_so), latex(t_b), latex(t_b), latex(mau_so), latex(t_b), latex(mau_so), latex(2 * mau_so), latex(so_lan_xa_vtcb_dung)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Khi người đó ở vị trí cân bằng thì $\\cos\\left( \\frac{t\\pi}{%s} \\right) = 0$' % (latex(mau_so))
            vd_da_1_s = 'Khi người đó ở vị trí cân bằng thì $\\cos\\left( \\frac{t\\pi}{%s} \\right) = 1$' % (latex(mau_so))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Khi người đó ở vị trí cân bằng, li độ của người đó bằng $0$, tức là $x = 0$.\\\\
            Từ phương trình dao động ta suy ra: $%s = 0 \\Leftrightarrow \\cos\\left( \\frac{t\\pi}{%s} \\right) = 0$.''' 
                            % (expr_goc, latex(mau_so)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = 'Trong khoảng từ $0$ đến $%s$ giây thì người đó đi qua vị trí cân bằng %s lần' % (latex(t_d), latex(so_lan_vtcb_sai))
            vdc_da_1_s = '\\True Trong khoảng từ $0$ đến $%s$ giây thì người đó đi qua vị trí cân bằng %s lần' % (latex(t_d), latex(so_lan_vtcb_dung))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Người đó đi qua vị trí cân bằng khi $x = 0 \\Leftrightarrow \\cos\\left( \\frac{t\\pi}{%s} \\right) = 0 \\Leftrightarrow \\frac{t\\pi}{%s} = \\frac{\\pi}{2} + k\\pi \\Leftrightarrow t = \\frac{%s}{2} + k \\cdot %s$ ($k \\in \\mathbb{Z}$).\\\\
            Xét khoảng thời gian từ $0$ đến $%s$ giây ($0 < t < %s$), ta có:\\\\
            $0 < \\frac{%s}{2} + k \\cdot %s < %s \\Leftrightarrow -\\frac{1}{2} < k < 5 - \\frac{1}{2} \\Leftrightarrow -0,5 < k < 4,5$.\\\\
            Do $k \\in \\mathbb{Z}$ nên $k \\in \\{0; 1; 2; 3; 4\\}$.\\\\
            Vậy trong khoảng thời gian trên, người đó đi qua vị trí cân bằng %s lần.''' 
                             % (latex(mau_so), latex(mau_so), latex(mau_so), latex(mau_so), latex(t_d), latex(t_d), latex(mau_so), latex(mau_so), latex(t_d), latex(so_lan_vtcb_dung)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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

