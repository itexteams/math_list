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


def bt_dang35_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Ngẫu nhiên thông số để đảm bảo bán kính r và chiều cao h là số nguyên cho đẹp
            # Chọn b, sau đó chọn L là bội của b để R = (a/b)*L nguyên
            b = random.choice([2, 3, 4, 5])
            a = random.randint(1, b - 1) 
            L = b * random.randint(1, 3) 

            f_x = Rational(a, b) * x
            R = (a * L) // b
            h = L
            the_tich_v = Rational(1, 3) * (R**2) * h

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho $D$ là hình phẳng giới hạn bởi đồ thị $y = f(x) = %s$, trục hoành và đường thẳng $x = %s$ (như hình minh họa). 
                             \begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw    (22.5,118.5) -- (206.6,118.93) ;
            		\draw [shift={(208.6,118.94)}, rotate = 180.14] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ; 
            		\draw    (52.24,141.43) -- (53.32,22.73) ;
            		\draw [shift={(53.33,20.73)}, rotate = 90.52] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            		\draw    (52.24,117.84) -- (205.31,42.13) ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (174.04,57.49) -- (52.24,118.39) -- (174.04,118.39) -- cycle ;
            		\draw    (129.05,118.39) -- (128.77,79.98) ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (52.79,81.08) -- (128.77,79.98) ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (52.79,56.94) -- (174.04,57.49) ;
            		\draw    (306.24,84.87) -- (459.31,9.16) ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (428.04,24.52) -- (306.24,85.42) -- (428.04,85.42) -- cycle ; 
            		\draw    (383.05,85.42) -- (382.77,47.01) ;
            		\draw  [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (428.04,135.9) -- (306.24,85.42) -- (428.04,85.42) -- cycle ;
            		\draw    (306.24,85.42) -- (460.3,148.9) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (409.39,79.96) .. controls (409.39,49.89) and (417.74,25.52) .. (428.04,25.52) .. controls (438.34,25.52) and (446.69,49.89) .. (446.69,79.96) .. controls (446.69,110.03) and (438.34,134.4) .. (428.04,134.4) .. controls (417.74,134.4) and (409.39,110.03) .. (409.39,79.96) -- cycle ;
            		\draw    (428.04,85.97) -- (480.6,85.97) ;
            		\draw [shift={(482.6,85.97)}, rotate = 180] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            		\draw    (428.04,25.52) -- (428.04,135.9) ;
            		\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][dash pattern={on 4.5pt off 4.5pt}] (369.14,82.78) .. controls (369.14,64.34) and (375.1,49.4) .. (382.47,49.4) .. controls (389.83,49.4) and (395.8,64.34) .. (395.8,82.78) .. controls (395.8,101.21) and (389.83,116.16) .. (382.47,116.16) .. controls (375.1,116.16) and (369.14,101.21) .. (369.14,82.78) -- cycle ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (306.24,85.97) -- (428.04,85.97) ; 
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (382.47,49.4) -- (382.47,116.16) ; 
            		\draw  [draw opacity=0] (385.72,115.16) .. controls (384.68,115.81) and (383.59,116.16) .. (382.47,116.16) .. controls (375.1,116.16) and (369.14,101.24) .. (369.14,82.83) .. controls (369.14,64.42) and (375.1,49.5) .. (382.47,49.5) .. controls (383.11,49.5) and (383.74,49.61) .. (384.36,49.83) -- (382.47,82.83) -- cycle ; \draw   (385.72,115.16) .. controls (384.68,115.81) and (383.59,116.16) .. (382.47,116.16) .. controls (375.1,116.16) and (369.14,101.24) .. (369.14,82.83) .. controls (369.14,64.42) and (375.1,49.5) .. (382.47,49.5) .. controls (383.11,49.5) and (383.74,49.61) .. (384.36,49.83) ;  
            		\draw (141.93,83.91) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (30.56,120.67) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (183.37,122.62) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\draw (33.15,16.97) node [anchor=north west][inner sep=0.75pt]    {$y$};
            		\draw (340.93,66.93) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (286.56,75.19) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (464.37,91.65) node [anchor=north west][inner sep=0.75pt]    {$x$};
            	\end{tikzpicture}
            \end{center} Quay hình $D$ xung quanh trục $Ox$ thì được một khối tròn xoay, kí hiệu là $N$.''' 
                             % (latex(f_x), latex(L)))

            ########################################################################
            # Nhận biết
            nb_da_1_d = r'\True Khối tròn xoay được tạo ra là khối nón'
            nb_da_1_s = r'Khối tròn xoay được tạo ra là khối trụ'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = r'''Khi quay một tam giác vuông quanh một cạnh góc vuông (ở đây là trục $Ox$), ta thu được một khối nón.'''

            ########################################################################
            # Thông hiểu
            th_da_1_d = r'\True Mặt cắt của khối $N$ khi cắt bởi mặt phẳng vuông góc với trục $Ox$ là một hình tròn'
            th_da_1_s = r'Mặt cắt của khối $N$ khi cắt bởi mặt phẳng vuông góc với trục $Ox$ là một hình vuông'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = r'''Vì $N$ là khối tròn xoay có trục là $Ox$ nên mọi mặt cắt vuông góc với trục đều là hình tròn.'''

            ########################################################################
            # Vận dụng
            he_so_S = Rational(a**2, b**2)
            vd_da_1_d = r'\True Hình tròn được tạo ra tại vị trí $x$ có bán kính $r = %s$ nên có diện tích bằng $S = %s \pi x^2$' % (latex(f_x), latex(he_so_S))
            vd_da_1_s = r'Hình tròn được tạo ra tại vị trí $x$ có bán kính $r = %s$ nên có diện tích bằng $S = %s \pi x$' % (latex(f_x), latex(he_so_S))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = r'''Tại vị trí $x$, bán kính mặt cắt là $r = |f(x)| = %s$. Diện tích là $S = \pi r^2 = \pi \left(%s\right)^2 = %s \pi x^2$.''' % (latex(f_x), latex(f_x), latex(he_so_S))

            ########################################################################
            # Vận dụng cao
            vdc_da_1_d = r'\True Thể tích khối tròn xoay là $V = %s \pi$' % (latex(the_tich_v))
            vdc_da_1_s = r'Thể tích khối tròn xoay là $V = %s \pi$' % (latex(the_tich_v + 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Lời giải chi tiết cho Vận dụng cao (bao gồm công thức nón và tích phân)
            loigiai_vdc_1 = (r'''Chiều cao khối nón $h = %s$, bán kính đáy $r = f(%s) = %s$. \\
                             Thể tích $V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi \cdot %s^2 \cdot %s = %s \pi$. \\
                             Tính theo tích phân: $I = \pi \int_{0}^{%s} \left(%s\right)^2 \text{d}x = \pi \int_{0}^{%s} %s x^2 \text{d}x = \pi \left[ %s \frac{x^3}{3} \right]_{0}^{%s} = %s \pi$.''' 
                             % (latex(h), latex(L), latex(R), latex(R), latex(h), latex(the_tich_v), 
                                latex(L), latex(f_x), latex(L), latex(he_so_S), latex(he_so_S), latex(L), latex(the_tich_v)))

            ########################################################################
            # Xử lý trộn và xuất kết quả tương tự mẫu
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

