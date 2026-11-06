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


def bt_dang46_p2_b3_c3_ds12(self):
    # ================= Khai báo và sinh thông số ngẫu nhiên =================
    # Chiều cao tổng: H, cạnh lập phương: a, đường kính khối cầu: d = a => bán kính R = a/2
    # Chiều cao chỏm cầu nhô lên: h = H - a (phải thỏa mãn 0 < h <= 2*R = a)
    while True:
        a_val = random.choice([6, 8, 10])
        R_val = a_val // 2
        # Chọn H sao cho chiều cao chỏm cầu h nằm trong khoảng (R, 2R) hoặc (0, 2R)
        # Trong đề gốc: a = 8, H = 14 => h = 6, R = 4
        h_val = random.choice([R_val + 1, R_val + 2])
        H_val = a_val + h_val
        if h_val < 2 * R_val:
            break

    # Thể tích khối lập phương: V_cube = a^3
    V_cube = a_val**3


    V_chom_num = float(math.pi * (h_val**2) * (R_val - h_val / 3.0))
    V_total_float = V_cube + V_chom_num
    V_total_round = int(Decimal(str(V_total_float)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

    # Phần bù chìm trong lập phương có chiều cao là: h_chim = 2*R - h = a - h
    h_chim = 2 * R_val - h_val


    tikz_code =('''\\begin{center}
    	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
    		\\draw  [fill={rgb, 255:red, 203; green, 199; blue, 199 }  ,fill opacity=1 ][line width=0.75]  (111.73,81.47) -- (223.93,85.4) -- (180.93,128.4) -- (63.43,128.4) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]  (97.37,106.4) .. controls (97.37,95.91) and (118.49,87.4) .. (144.55,87.4) .. controls (170.61,87.4) and (191.73,95.91) .. (191.73,106.4) .. controls (191.73,116.89) and (170.61,125.4) .. (144.55,125.4) .. controls (118.49,125.4) and (97.37,116.89) .. (97.37,106.4) -- cycle ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]  [dash pattern={on 4.5pt off 4.5pt}]  (106.83,84.5) -- (201.93,84.9) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]  [dash pattern={on 4.5pt off 4.5pt}]  (106.83,84.5) -- (90.93,101.9) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (90.93,101.9) -- (63.43,128.4) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (63.43,128.4) -- (180.93,128.4) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (180.93,128.4) -- (223.93,85.4) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (223.93,85.4) -- (201.93,84.9) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (63.43,128.4) -- (63.93,241.9) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (223.93,85.4) -- (224.43,198.9) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (180.93,128.4) -- (180.43,242.4) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (224.43,198.9) -- (180.43,242.4) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (63.93,241.9) -- (180.43,242.4) ;
    		\\draw  [draw opacity=0][line width=1]  (347.97,109.87) .. controls (341.92,100.74) and (338.4,89.78) .. (338.4,78) .. controls (338.4,46.08) and (364.28,20.2) .. (396.2,20.2) .. controls (428.12,20.2) and (454,46.08) .. (454,78) .. controls (454,88.86) and (451,99.02) .. (445.79,107.7) -- (396.2,78) -- cycle ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  (347.97,109.87) .. controls (341.92,100.74) and (338.4,89.78) .. (338.4,78) .. controls (338.4,46.08) and (364.28,20.2) .. (396.2,20.2) .. controls (428.12,20.2) and (454,46.08) .. (454,78) .. controls (454,88.86) and (451,99.02) .. (445.79,107.7) ;  
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (338.17,76.67) -- (453.27,77.07) ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (338.17,76.57) .. controls (338.17,64.69) and (363.93,55.07) .. (395.72,55.07) .. controls (427.5,55.07) and (453.27,64.69) .. (453.27,76.57) .. controls (453.27,88.44) and (427.5,98.07) .. (395.72,98.07) .. controls (363.93,98.07) and (338.17,88.44) .. (338.17,76.57) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (347.97,106.07) .. controls (347.97,95.57) and (369.87,87.07) .. (396.88,87.07) .. controls (423.9,87.07) and (445.79,95.57) .. (445.79,106.07) .. controls (445.79,116.56) and (423.9,125.07) .. (396.88,125.07) .. controls (369.87,125.07) and (347.97,116.56) .. (347.97,106.07) -- cycle ;
    		\\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (446.03,107.31) .. controls (435.98,124.36) and (417.43,135.8) .. (396.2,135.8) .. controls (376.27,135.8) and (358.7,125.71) .. (348.31,110.37) -- (396.2,78) -- cycle ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (446.03,107.31) .. controls (435.98,124.36) and (417.43,135.8) .. (396.2,135.8) .. controls (376.27,135.8) and (358.7,125.71) .. (348.31,110.37) ;  
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (359.17,84.17) -- (454.27,84.57) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (360.67,199.67) -- (475.77,200.07) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (360.67,199.67) -- (359.17,84.17) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (360.67,199.67) -- (316.27,241.57) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (359.17,84.17) -- (343.27,101.57) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (343.27,101.57) -- (315.77,128.07) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (315.77,128.07) -- (433.27,128.07) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (433.27,128.07) -- (476.27,85.07) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (476.27,85.07) -- (454.27,84.57) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (315.77,128.07) -- (316.27,241.57) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (476.27,85.07) -- (476.77,198.57) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (433.27,128.07) -- (432.77,242.07) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (476.77,198.57) -- (432.77,242.07) ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (316.27,241.57) -- (432.77,242.07) ;
    		\\draw    (507.4,242.07) -- (448.73,242.07) ;
    		\\draw    (505.4,20.07) -- (392.73,20.07) ;
    		\\draw    (496.07,23.07) -- (496.07,238.8) ;
    		\\draw [shift={(496.07,241.8)}, rotate = 270] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
    		\\draw [shift={(496.07,20.07)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=0.75]  (96.31,109.21) .. controls (90.26,100.07) and (86.73,89.11) .. (86.73,77.33) .. controls (86.73,45.41) and (112.61,19.53) .. (144.53,19.53) .. controls (176.46,19.53) and (202.33,45.41) .. (202.33,77.33) .. controls (202.33,88.2) and (199.34,98.36) .. (194.13,107.04) -- (144.53,77.33) -- cycle ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]  (96.31,109.21) .. controls (90.26,100.07) and (86.73,89.11) .. (86.73,77.33) .. controls (86.73,45.41) and (112.61,19.53) .. (144.53,19.53) .. controls (176.46,19.53) and (202.33,45.41) .. (202.33,77.33) .. controls (202.33,88.2) and (199.34,98.36) .. (194.13,107.04) ;  
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=0.75]  (96.31,109.21) .. controls (116.31,99.21) and (91.73,77.13) .. (144.53,77.33) .. controls (158.4,83.8) and (174.13,77.04) .. (194.13,107.04) .. controls (182.4,131.13) and (112.4,131.13) .. (96.31,109.21) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.3 ][line width=0.75]  (109.07,69.67) .. controls (109.07,46.03) and (128.23,26.87) .. (151.87,26.87) .. controls (175.5,26.87) and (194.67,46.03) .. (194.67,69.67) .. controls (194.67,93.3) and (175.5,112.47) .. (151.87,112.47) .. controls (128.23,112.47) and (109.07,93.3) .. (109.07,69.67) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.3 ][line width=0.75]  (134.4,61) .. controls (134.4,47.3) and (145.5,36.2) .. (159.2,36.2) .. controls (172.9,36.2) and (184,47.3) .. (184,61) .. controls (184,74.7) and (172.9,85.8) .. (159.2,85.8) .. controls (145.5,85.8) and (134.4,74.7) .. (134.4,61) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (155.73,52) .. controls (155.73,46.59) and (160.12,42.2) .. (165.53,42.2) .. controls (170.95,42.2) and (175.33,46.59) .. (175.33,52) .. controls (175.33,57.41) and (170.95,61.8) .. (165.53,61.8) .. controls (160.12,61.8) and (155.73,57.41) .. (155.73,52) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 203; green, 199; blue, 199 }  ,fill opacity=1 ][line width=0.75]  (63.43,128.4) -- (180.93,128.4) -- (180.43,242.4) -- (63.93,241.9) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 184; green, 182; blue, 182 }  ,fill opacity=1 ][line width=0.75]  (223.93,85.4) -- (180.93,128.4) -- (180.43,242.4) -- (224.43,198.9) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ][line width=0.75]  (63.93,241.9) -- (150.4,128.13) -- (180.93,128.4) -- (225.73,202.13) -- (180.4,246.8) -- cycle ;
    		\\draw (504.33,118.67) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$ cm};
    		\\draw (357.67,246.67) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$ cm};
    		\\draw (281,169.67) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$ cm};
    		\\draw (379,59) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$ cm};
    	\\end{tikzpicture}
    \\end{center}''' %(str(H_val), str(a_val), str(a_val), str(a_val)))

    # Nội dung câu hỏi tuân thủ chuẩn định dạng %s
    noidungcauhoi = ('''Một đồ lưu niệm bằng thủy tinh có chiều cao bằng $%s\\text{ cm}$, được thiết kế gồm hai phần, phần dưới là một khối lập phương cạnh bằng $%s\\text{ cm}$ và phần trên là một phần của khối cầu có đường kính bằng $%s\\text{ cm}$ (tham khảo hình vẽ).
    %s''' % (str(H_val), str(a_val), str(a_val), tikz_code))

    #########################################################################
    # Nhận biết: Bán kính và chiều cao phần khối cầu
    #########################################################################
    nb_da_1_d = '\\True Phần khối cầu có bán kính $%s\\text{ cm}$ và chiều cao là $%s\\text{ cm}$' % (str(R_val), str(h_val))
    nb_da_1_s = 'Phần khối cầu có bán kính $%s\\text{ cm}$ và chiều cao là $%s\\text{ cm}$' % (str(a_val), str(h_val))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Khối cầu có đường kính bằng $%s\\text{ cm}$ nên có bán kính là $R = \\frac{%s}{2} = %s\\text{ cm}$.\\\\ Chiều cao của phần khối cầu nhô lên là $h = %s - %s = %s\\text{ cm}$.''' % (str(a_val), str(a_val), str(R_val), str(H_val), str(a_val), str(h_val)))
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    #########################################################################
    # Thông hiểu: Thể tích khối lập phương
    #########################################################################
    V_cube_false = V_cube + random.choice([-100, -50, 50, 100])
    th_da_1_d = '\\True Khối lập phương có thể tích bằng $%s\\text{ (cm}^3\\text{)}$' % (str(V_cube))
    th_da_1_s = 'Khối lập phương có thể tích bằng $%s\\text{ (cm}^3\\text{)}$' % (str(V_cube_false))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Thể tích của khối lập phương cạnh $%s\\text{ cm}$ là:\\\\ $V_1 = %s^3 = %s\\text{ (cm}^3\\text{)}$.''' % (str(a_val), str(a_val), str(V_cube)))
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    #########################################################################
    # Vận dụng: Thể tích của cả đồ lưu niệm làm tròn đến hàng đơn vị
    #########################################################################
    V_total_false = V_total_round + random.choice([-15, -10, 10, 15])
    vd_da_1_d = '\\True Thể tích của đồ lưu niệm đó (làm tròn kết quả đến hàng đơn vị) là $%s\\text{ (cm}^3\\text{)}$' % (str(V_total_round))
    vd_da_1_s = 'Thể tích của đồ lưu niệm đó (làm tròn kết quả đến hàng đơn vị) là $%s\\text{ (cm}^3\\text{)}$' % (str(V_total_false))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    # Tính chi tiết số học cho lời giải
    V_chom_str = str(round(V_chom_num, 2)).replace('.', ',')
    loigiai_vd_1 = ('''Thể tích chỏm cầu có bán kính $R = %s\\text{ cm}$ và chiều cao $h = %s\\text{ cm}$ là:\\\\ $V_2 = \\pi h^2 \\left(R - \\frac{h}{3}\\right) = \\pi \\cdot %s^2 \\cdot \\left(%s - \\frac{%s}{3}\\right) \\approx %s\\text{ (cm}^3\\text{)}$.\\\\ Thể tích của đồ lưu niệm bằng tổng thể tích của khối lập phương và phần chỏm cầu:\\\\ $V = V_1 + V_2 = %s + %s \\approx %s\\text{ (cm}^3\\text{)}$.\\\\ Làm tròn đến hàng đơn vị ta được $V \\approx %s\\text{ (cm}^3\\text{)}$.''' % (str(R_val), str(h_val), str(h_val), str(R_val), str(h_val), V_chom_str, str(V_cube), V_chom_str, str(round(V_total_float, 2)).replace('.', ','), str(V_total_round)))
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    #########################################################################
    # Vận dụng cao: Công thức tính tích phân tròn xoay
    # Khẳng định sai vì thiếu hệ số \pi ở phía trước dấu tích phân
    #########################################################################
    vdc_da_1_d = '\\True Quay hình phẳng giới hạn bởi đồ thị hàm số $y = \\sqrt{%sx - x^2}$, trục hoành và hai đường thẳng $x = 0, x = %s$ quanh trục hoành ta thu được khối tròn xoay có thể tích $V = \\pi \\int_0^{%s} \\left(\\sqrt{%sx - x^2}\\right)^2 \\mathrm{d}x$' % (str(a_val), str(h_chim), str(h_chim), str(a_val))
    vdc_da_1_s = 'Quay hình phẳng giới hạn bởi đồ thị hàm số $y = \\sqrt{%sx - x^2}$, trục hoành và hai đường thẳng $x = 0, x = %s$ quanh trục hoành ta thu được khối tròn xoay có thể tích $V = \\int_0^{%s} \\left(\\sqrt{%sx - x^2}\\right)^2 \\mathrm{d}x$' % (str(a_val), str(h_chim), str(h_chim), str(a_val))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Công thức tính thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành và hai đường thẳng $x = a, x = b$ quanh trục hoành là $V = \\pi \\int_a^b [f(x)]^2 \\mathrm{d}x$.\\\\ Do đó, công thức đúng phải có hệ số $\\pi$, tức là $V = \\pi \\int_0^{%s} \\left(\\sqrt{%sx - x^2}\\right)^2 \\mathrm{d}x$. Khẳng định thiếu $\\pi$ là khẳng định sai.''' % (str(h_chim), str(a_val)))
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
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content

