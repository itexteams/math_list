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


def bt_dang31_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập tham số ngẫu nhiên dựa trên bộ số Pytago (3, 4, 5) để số liệu đẹp
                # k là hệ số tỉ lệ
                k = random.choice([1, 2, 3]) 

                r_val = 5 * k        # Bán kính hình tròn R
                side_val = 8 * k     # Độ dài cạnh hình vuông
                a_val = side_val // 2 # Nửa cạnh hình vuông (a = 4k)
                x0_val = 3 * k       # Điểm giao nhau trên trục hoành (x0 = sqrt(R^2 - a^2))

                # Tính toán thể tích V1 (Khối cầu bán kính R)
                # V1 = 4/3 * pi * R^3
                v1_num = 4 * (r_val**3)
                v1_rational = Rational(v1_num, 3)

                # Tính toán thể tích V2 (Phần hình vuông nằm ngoài hình tròn khi xoay)
                # V2 = 2 * pi * tích phân từ x0 đến a của [a^2 - (R^2 - x^2)] dx
                x = symbols('x')
                f_integ = a_val**2 - (r_val**2 - x**2)
                v2_integ = integrate(f_integ, (x, x0_val, a_val))
                v2_res = 2 * v2_integ # Nhân 2 vì có 2 phần đối xứng qua trục tung (hoặc theo công thức tích phân)

                # Tổng thể tích V = V1 + V2
                v_total = v1_rational + v2_res

                # Đáp án đúng
                da_dung = '$V = %s\\pi$' % latex(v_total)

                # Tạo các đáp án nhiễu
                s = [
                    '$V = %s\\pi$' % latex(v1_rational), # Chỉ tính khối cầu
                    '$V = %s\\pi$' % latex(v_total + Rational(10*k**3, 3)),
                    '$V = %s\\pi$' % latex(v_total - Rational(10*k**3, 3)),
                    '$V = %s\\pi$' % latex(simplify(v_total * Rational(3, 4))),
                ]

                # Trộn đáp án
                random.shuffle(s)
                if da_dung in s: s.remove(da_dung)
                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (r'''\immini{Cho hình vuông có độ dài cạnh bằng $%s\text{cm}$ và một hình tròn có bán kính $%s\text{cm}$ được xếp chồng lên nhau sao cho tâm của hình tròn trùng với tâm của hình vuông như hình vẽ bên. Tính thể tích $V$ của vật thể tròn xoay tạo thành khi quay mô hình trên quanh trục $XY$.}
                                 {\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw   (114.67,76.47) -- (234.67,76.47) -- (234.67,196.47) -- (114.67,196.47) -- cycle ;
            	\draw   (99.67,136.47) .. controls (99.67,95.05) and (133.25,61.47) .. (174.67,61.47) .. controls (216.09,61.47) and (249.67,95.05) .. (249.67,136.47) .. controls (249.67,177.89) and (216.09,211.47) .. (174.67,211.47) .. controls (133.25,211.47) and (99.67,177.89) .. (99.67,136.47) -- cycle ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (99.67,136.47) -- (249.67,136.47) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (128.4,196.29) -- (114.67,196.47) -- (115.07,182.96) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (234.62,182.96) -- (220.96,195.96) -- (234.67,196.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (220.96,76.51) -- (234.62,89.84) -- (234.67,76.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (128.96,76.51) -- (114.96,90.18) -- (114.67,76.47) -- cycle ;
            	\draw (82,124.13) node [anchor=north west][inner sep=0.75pt]    {$X$};
            	\draw (253.33,124.13) node [anchor=north west][inner sep=0.75pt]    {$Y$};
            \end{tikzpicture}}''' % (latex(side_val), latex(r_val)))

                # Nội dung lời giải
                loigiai = (r'''\begin{center}
            				\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            					\draw   (114.67,76.47) -- (234.67,76.47) -- (234.67,196.47) -- (114.67,196.47) -- cycle ;
            					\draw   (99.67,136.47) .. controls (99.67,95.05) and (133.25,61.47) .. (174.67,61.47) .. controls (216.09,61.47) and (249.67,95.05) .. (249.67,136.47) .. controls (249.67,177.89) and (216.09,211.47) .. (174.67,211.47) .. controls (133.25,211.47) and (99.67,177.89) .. (99.67,136.47) -- cycle ;
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (99.67,136.47) -- (249.67,136.47) ;
            					\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (128.4,196.29) -- (114.67,196.47) -- (115.07,182.96) -- cycle ;
            					\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (234.62,182.96) -- (220.96,195.96) -- (234.67,196.47) -- cycle ;
            					\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (220.96,76.51) -- (234.62,89.84) -- (234.67,76.47) -- cycle ;
            					\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (128.96,76.51) -- (114.96,90.18) -- (114.67,76.47) -- cycle ;
            					\draw    (70.47,136.67) -- (282.13,136.34) ;
            					\draw [shift={(284.13,136.33)}, rotate = 179.91] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw    (174.1,231.9) -- (175.58,41.9) ;
            					\draw [shift={(175.6,39.9)}, rotate = 90.45] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw (79.33,113.47) node [anchor=north west][inner sep=0.75pt]    {$X$};
            					\draw (252,113.47) node [anchor=north west][inner sep=0.75pt]    {$Y$};
            					\draw (260.5,138) node [anchor=north west][inner sep=0.75pt]    {$x$};
            					\draw (155.5,35) node [anchor=north west][inner sep=0.75pt]    {$y$};
            					\draw (157,135.5) node [anchor=north west][inner sep=0.75pt]    {$O$};
            				\end{tikzpicture}
            			\end{center}
                        Chọn hệ trục tọa độ $Oxy$ có gốc $O$ trùng với tâm hình vuông, trục $Ox$ trùng với trục $XY$. \\
            Khi đó phương trình đường tròn là $x^2 + y^2 = %s \Rightarrow y^2 = %s - x^2$.\\
            Cạnh hình vuông nằm trên các đường thẳng $y = \pm %s$ và $x = \pm %s$.\\
            Giao điểm của cạnh hình vuông $y = %s$ và đường tròn là $x^2 + %s^2 = %s \Rightarrow x = \pm %s$.\\
            Thể tích vật thể gồm:\\
            - Thể tích khối cầu bán kính $R = %s$: $V_1 = \frac{4}{3}\pi R^3 = \frac{4}{3}\pi \cdot %s^3 = %s\pi$.\\
            - Thể tích phần nhô ra của hình vuông (giới hạn bởi $y=%s$ và $y=\sqrt{%s-x^2}$ từ $x=%s$ đến $x=%s$):\\
            $V_2 = 2 \cdot \pi \int_{%s}^{%s} \left| %s^2 - (%s - x^2) \right| \text{d}x = 2\pi \int_{%s}^{%s} (x^2 - %s) \text{d}x = %s\pi$.\\
            Vậy thể tích cần tìm là $V = V_1 + V_2 = %s\pi + %s\pi = %s\pi$.''' 
                % (r_val**2, r_val**2, a_val, a_val, a_val, a_val, r_val**2, x0_val,
                   r_val, r_val, latex(v1_rational), 
                   a_val, r_val**2, x0_val, a_val,
                   x0_val, a_val, a_val, r_val**2, x0_val, a_val, x0_val**2, latex(v2_res),
                   latex(v1_rational), latex(v2_res), latex(v_total)))

                # Xuất câu trắc nghiệm
                list_1 = ['\\True ' + da_dung, das1, das2, das3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + 
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

