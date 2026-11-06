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


def bt_dang33_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # BƯỚC 1 & 2: THIẾT LẬP THÔNG SỐ NGẪU NHIÊN
            # Chiều rộng W nên là số chẵn để tọa độ x_A, x_B nguyên (W/2)
            W = random.randrange(4, 12, 2)  # Ví dụ: 4, 6, 8, 10
            L = random.randint(5, 15)       # Chiều dài lều
            H = random.randint(3, 6)        # Chiều cao đỉnh parabol

            # Tính toán các hệ số parabol y = ax^2 + bx + c
            # Đỉnh C(0, H) => c = H, b = 0
            # Đi qua điểm B(W/2, 0) => a*(W/2)^2 + H = 0 => a = -H / (W/2)^2
            x_B = Rational(W, 2)
            h_so_a = -Rational(H, x_B**2)
            parabol_expr = h_so_a * x**2 + H

            # Tính diện tích mặt trước (Tích phân)
            S_mat_truoc = integrate(parabol_expr, (x, -x_B, x_B))
            # Tính thể tích
            V_leu = S_mat_truoc * L
            # Diện tích nền
            S_nen = W * L

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Để chuẩn bị cơ sở vật chất phục vụ công tác phòng chống dịch bệnh, các chiến sĩ dự định dựng một cái lều trại có dạng hình lăng trụ. 
                             \begin{center}
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            \draw   (201.94,101.02) .. controls (180.1,1.21) and (156.76,0.86) .. (131.94,99.97) ; 
            \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (97,17.5) -- (167,17.5) -- (167,106.4) -- (97,106.4) -- cycle ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}] (201.94,101.02) .. controls (180.1,1.21) and (156.76,0.86) .. (131.94,99.97) ;
            \draw   (122.44,135.02) .. controls (100.6,35.21) and (77.26,34.86) .. (52.44,133.97) ;
            \draw    (52.44,133.97) -- (122.44,135.02) ; 
            \draw    (122.44,135.02) -- (201.94,101.02) ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (131.94,99.97) -- (201.94,101.02) ; 
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (131.94,99.97) -- (52.44,133.97) ;
            \draw    (88.56,59.9) -- (168.06,25.9) ;
            \draw   (382.94,102.52) .. controls (361.1,2.71) and (337.76,2.36) .. (312.94,101.47) ;
            \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (278,19) -- (348,19) -- (348,107.9) -- (278,107.9) -- cycle ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}] (382.94,102.52) .. controls (361.1,2.71) and (337.76,2.36) .. (312.94,101.47) ;
            \draw   (303.44,136.52) .. controls (281.6,36.71) and (258.26,36.36) .. (233.44,135.47) ;
            \draw    (233.44,135.47) -- (303.44,136.52) ;
            \draw    (303.44,136.52) -- (382.94,102.52) ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (312.94,101.47) -- (382.94,102.52) ;
            \draw  [dash pattern={on 4.5pt off 4.5pt}]  (312.94,101.47) -- (233.44,135.47) ;
            \draw    (269.56,61.4) -- (349.06,27.4) ;
            \draw    (268.44,136) -- (368.6,137.37) ;
            \draw [shift={(370.6,137.4)}, rotate = 180.79] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            \draw    (268.44,136) -- (268.11,26.4) ;
            \draw [shift={(268.1,24.4)}, rotate = 89.83] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            \draw (349.5,144) node [anchor=north west][inner sep=0.75pt]    {$x$};
            \draw (248,21.5) node [anchor=north west][inner sep=0.75pt]    {$y$};
            \draw (259,134.5) node [anchor=north west][inner sep=0.75pt]    {$O$};
            \end{tikzpicture}		
            \end{center} Biết rằng mặt trước và mặt sau của trại là hai parabol bằng nhau, nằm trên hai mặt phẳng song song với nhau và cùng vuông góc với mặt nền. Nền của lều trại là một hình chữ nhật có kích thước chiều rộng là $%s$ m, chiều dài là $%s$ m, đỉnh parabol cách nền $%s$ m.''' 
                             % (latex(W), latex(L), latex(H)))

            ########################################################################
            # Nhận biết: Diện tích nền
            nb_da_1_d = r'\True Diện tích nền của lều trại là $%s \text{ m}^2$' % (latex(S_nen))
            nb_da_1_s = r'Diện tích nền của lều trại là $%s \text{ m}^2$' % (latex(S_nen + 2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'''Nền của lều trại là hình chữ nhật nên diện tích là $%s \cdot %s = %s (\text{m}^2)$.''' % (latex(W), latex(L), latex(S_nen))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Phương trình Parabol
            th_da_1_d = r'\True Parabol mặt trước có phương trình $y = %s$' % (latex(parabol_expr))
            th_da_1_s = r'Parabol mặt trước có phương trình $y = %s$' % (latex(-h_so_a * x**2 + H))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Chọn hệ trục $Oxy$, đỉnh $C(0;%s)$, qua $A(-%s;0)$ và $B(%s;0)$. 
                            Ta tìm được parabol $(P): y = %s$.''' 
                            % (latex(H), latex(x_B), latex(x_B), latex(parabol_expr)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Diện tích mặt trước
            vd_da_1_d = r'\True Diện tích mặt trước của lều trại là $%s \text{ m}^2$' % (latex(S_mat_truoc))
            vd_da_1_s = r'Diện tích mặt trước của lều trại là $%s \text{ m}^2$' % (latex(Rational(2,3)*W*H + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Diện tích mặt trước là $S = \int_{-%s}^{%s} \left( %s \right) \text{d}x = %s (\text{m}^2)$.''' 
                            % (latex(x_B), latex(x_B), latex(parabol_expr), latex(S_mat_truoc)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Thể tích lều
            vdc_da_1_d = r'\True Thể tích phần không gian bên trong lều là $%s \text{ m}^3$' % (latex(V_leu))
            vdc_da_1_s = r'Thể tích phần không gian bên trong lều là $%s \text{ m}^3$' % (latex(S_mat_truoc * (L-1)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Thể tích khối lăng trụ là $V = S_{\text{đáy}} \cdot h = \int_{0}^{%s} %s \text{d}x = %s (\text{m}^3)$.''' 
                             % (latex(L), latex(S_mat_truoc), latex(V_leu)))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp xáo trộn đáp án đúng/sai
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Đóng gói và xuất kết quả
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

