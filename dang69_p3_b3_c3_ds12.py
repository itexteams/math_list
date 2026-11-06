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


def bt_dang69_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các hệ số đảm bảo nghiệm đẹp
                m = random.choice([2, 3, 4, 5]) # Hệ số tỉ lệ SH = m*EH

                # Chọn bề rộng w1 sao cho diện tích S1 là một số nguyên (S1 = w1^2 * (m+1) / 3)
                if m in [2, 5]:
                    w1 = random.choice([4, 5, 6, 8])
                else:
                    w1 = random.choice([3, 6, 9])

                k = random.choice([2, 3]) # Hệ số đồng dạng đáy lớn và đáy bé
                w2 = k * w1

                # Chiều dài kho hàng, chọn bội của 3 để thể tích đẹp
                h = random.choice([15, 30, 45, 60])

                # Tính toán các thông số của Parabol dựa trên công thức tổng quát
                b = 2 * m - 2
                a_frac = Rational(-(2 * m - 1), w1)

                # Diện tích thiết diện tại đầu nhỏ (B) và đầu lớn (A)
                S1 = Rational(w1**2 * (m + 1), 3)
                S2 = k**2 * S1
                while Rational(h, 3) * S1 * (1 + k + k**2)>9999:
                    m = random.choice([2, 3, 4, 5]) # Hệ số tỉ lệ SH = m*EH

                    # Chọn bề rộng w1 sao cho diện tích S1 là một số nguyên (S1 = w1^2 * (m+1) / 3)
                    if m in [2, 5]:
                        w1 = random.choice([4, 5, 6, 8])
                    else:
                        w1 = random.choice([3, 6, 9])

                    k = random.choice([2, 3]) # Hệ số đồng dạng đáy lớn và đáy bé
                    w2 = k * w1

                    # Chiều dài kho hàng, chọn bội của 3 để thể tích đẹp
                    h = random.choice([15, 30, 45, 60])

                    # Tính toán các thông số của Parabol dựa trên công thức tổng quát
                    b = 2 * m - 2
                    a_frac = Rational(-(2 * m - 1), w1)

                    # Diện tích thiết diện tại đầu nhỏ (B) và đầu lớn (A)
                    S1 = Rational(w1**2 * (m + 1), 3)
                    S2 = k**2 * S1        
                # Thể tích đúng theo công thức khối chóp cụt
                ans_true = Rational(h, 3) * S1 * (1 + k + k**2)

                # Thuật toán tạo các phương án nhiễu sai (dựa trên lỗi sai phổ biến)
                wrong_set = set()
                ans_w1 = h * S1 * (1 + k + k**2)             # Quên nhân 1/3
                ans_w2 = Rational(h, 3) * (S1 + S2)          # Quên cộng phần căn bậc 2
                ans_w3 = Rational(h, 2) * (S1 + S2)          # Dùng nhầm công thức diện tích trung bình
                ans_w4 = h * S2                              # Tính như hình lăng trụ đáy lớn
                ans_w5 = Rational(h, 3) * S1 * (1 + k**2)    # Sai công thức chóp cụt phần căn

                for w in [ans_w1, ans_w2, ans_w3, ans_w4, ans_w5]:
                    if w != ans_true and w > 0:
                        wrong_set.add(w)

                wrong_list = list(wrong_set)
                random.shuffle(wrong_list)
                wrong_list = wrong_list[:3] # Lấy 3 phương án nhiễu duy nhất

                # Hàm định dạng dấu phẩy cho số thập phân (nếu có)
                def format_num(val):
                    return str(val).replace('.', ',')

                # Định dạng chuỗi đa thức cho phương trình Parabol hiển thị đẹp
                x_sym = symbols('x')
                poly_expr = a_frac * x_sym**2 + b * x_sym + w1
                poly_str = latex(poly_expr).replace('.', ',')

                # Câu hỏi
                noidungcauhoi = ('''Một kho chứa hàng có mặt đáy là một hình thang $ABCD$ vuông tại $A$ và $B$ với $AD // BC$. Xét một thiết diện bất kì của kho hàng vuông góc với trục $AB$ tại điểm $K$. Thiết diện thu được là một hình phẳng giới hạn bởi vòm cong $(P)$, đoạn thẳng mặt nền $KE$ và đoạn tường thẳng đứng $KF$. Giả sử $(P)$ là một nhánh của parabol có đỉnh $S$, $H$ là hình chiếu vuông góc của $S$ lên mặt nền, $E$ là chân của vòm parabol ($E$ thuộc $(P)$ và mặt đáy), $SH = %s EH$. 
                                 \\begin{center}
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (297.59,134.61) -- (371.4,170.26) ;
                		\\draw [line width=1]    (158.52,247.58) -- (371.4,170.26) ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (297.59,134.61) -- (116.85,226.99) ;
                		\\draw [line width=1]    (116.85,226.99) -- (158.52,247.58) ;
                		\\draw [line width=1]    (297.59,134.61) -- (297.59,58.8) ;
                		\\draw [line width=1]    (116.85,226.99) -- (116.35,189.84) ;
                		\\draw [line width=1]    (116.35,189.84) -- (297.59,58.8) ;
                		\\draw [line width=1]    (116.35,189.84) .. controls (131.41,129.09) and (148.98,198.88) .. (158.52,247.58) ;
                		\\draw [line width=1]    (128.9,180.3) .. controls (143.96,119.55) and (162.54,193.86) .. (172.08,242.56) ;
                		\\draw [line width=1]    (141.45,170.26) .. controls (155.51,105.99) and (179.11,184.32) .. (186.64,237.54) ;
                		\\draw [line width=1]    (154,161.22) .. controls (169.07,100.47) and (187.64,165.74) .. (200.19,231.51) ;
                		\\draw [line width=1]    (166.56,152.18) .. controls (181.62,91.43) and (200.7,146.66) .. (214.25,226.49) ;
                		\\draw [line width=1]    (178.6,144.15) .. controls (192.16,83.4) and (213.75,137.12) .. (228.31,221.47) ;
                		\\draw [line width=1]    (192.16,133.61) .. controls (205.72,71.85) and (228.31,122.06) .. (242.37,215.44) ;
                		\\draw [line width=1]    (203.71,126.08) .. controls (218.77,65.33) and (234.33,90.43) .. (256.93,209.92) ;
                		\\draw [line width=1]    (215.76,115.03) .. controls (232.33,55.29) and (249.4,82.9) .. (270.98,205.91) ;
                		\\draw [line width=1]    (226.3,109.51) .. controls (243.37,48.76) and (260.44,57.8) .. (286.05,200.38) ;
                		\\draw [line width=1]    (249.9,93.44) .. controls (264.96,32.69) and (292.57,29.68) .. (313.66,190.84) ;
                		\\draw [line width=1]    (264.46,81.9) .. controls (279.52,21.15) and (298.6,16.12) .. (329.22,184.32) ;
                		\\draw [line width=1]    (276.51,73.86) .. controls (288.05,11.61) and (314.16,6.59) .. (344.29,178.79) ;
                		\\draw [line width=1]    (288.05,65.83) .. controls (300.61,1.56) and (326.71,-12.99) .. (358.34,174.28) ;
                		\\draw [line width=1]    (297.59,58.8) .. controls (312.66,-1.95) and (340.77,-30.57) .. (371.4,170.26) ;
                		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.42 ][line width=1]  (259.44,61.81) .. controls (277.51,63.32) and (290.57,156.2) .. (300.1,193.86) .. controls (274,184.82) and (261.95,177.79) .. (237.35,166.74) .. controls (238.85,104.99) and (236.34,75.87) .. (259.44,61.81) -- cycle ;
                		\\draw [line width=1]    (124.88,230.51) -- (133.92,226.49) ;
                		\\draw [line width=1]    (133.92,226.49) -- (126.39,222.47) ;
                		\\draw [line width=1]    (297.09,144.15) -- (306.13,140.13) ;
                		\\draw [line width=1]    (289.06,140.13) -- (297.09,144.15) ;
                		\\draw [line width=1]    (259.44,61.81) -- (260.94,178.29) ;
                		\\draw (249.43,37.56) node [anchor=north west][inner sep=0.75pt]    {$S$};
                		\\draw (238.38,98.06) node [anchor=north west][inner sep=0.75pt]    {$F$};
                		\\draw (216.92,151.02) node [anchor=north west][inner sep=0.75pt]    {$K$};
                		\\draw (246.8,178.64) node [anchor=north west][inner sep=0.75pt]    {$H$};
                		\\draw (298.63,193.95) node [anchor=north west][inner sep=0.75pt]    {$E$};
                		\\draw (374.32,157.55) node [anchor=north west][inner sep=0.75pt]    {$D$};
                		\\draw (146.63,247.67) node [anchor=north west][inner sep=0.75pt]    {$C$};
                		\\draw (99.31,214.54) node [anchor=north west][inner sep=0.75pt]    {$B$};
                		\\draw (296.38,113.87) node [anchor=north west][inner sep=0.75pt]    {$A$};
                	\\end{tikzpicture}
                \\end{center}
                Biết rằng một mặt bên của nhà kho là một bức tường phẳng vuông góc với đáy và tại mọi vị trí mặt cắt thì chiều cao của tường luôn bằng với bề rộng của nền nhà kho tại vị trí đó, nghĩa là $KF = KE$ và $F \\in (P)$. Cho chiều dài trục $AB = %s$ (m), bề rộng hai đầu hồi lần lượt là $AD = %s$ (m) và $BC = %s$ (m). Thể tích không gian bên trong khu nhà kho này theo đơn vị mét khối?''' 
                                % (m, h, w2, w1))

                # Các đáp án
                da_d = ('\\True $%s$' % format_num(ans_true))
                da_s1 = ('$%s$' % format_num(wrong_list[0]))
                da_s2 = ('$%s$' % format_num(wrong_list[1]))
                da_s3 = ('$%s$' % format_num(wrong_list[2]))

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính hằng số tự do cho bước phương trình trong lời giải
                const_term = w1 * (m - 1)

                # Nội dung lời giải chi tiết (Áp dụng đúng logic giải tay casio trong ảnh)
                loigiai = ('''Xét thiết diện tại $B$, gắn hệ trục tọa độ với $B \\equiv O(0;0)$, tia $BC$ trùng chiều dương trục $Ox$. Khi đó $E(%s; 0)$, tường thẳng đứng tại $B$ có chiều cao bằng $BC = %s$ nên $F(0; %s)$.\\\\
                Phương trình parabol $(P): y = ax^2 + bx + c$.\\\\
                Do $F(0; %s) \\in (P) \\Rightarrow c = %s$.\\\\
                Do $E(%s; 0) \\in (P) \\Rightarrow a \\cdot %s^2 + b \\cdot %s + %s = 0 \\Rightarrow %s a + %s b + %s = 0 \\Rightarrow b = -%s a - 1$.\\\\
                Gọi $S$ là đỉnh parabol, hoành độ điểm $H$ (hình chiếu của $S$ lên $Ox$) là $x_H = x_S = -\\frac{b}{2a}$.\\\\
                Theo giả thiết $SH = %s EH \\Leftrightarrow f\\left(-\\frac{b}{2a}\\right) = %s \\left(%s - \\left(-\\frac{b}{2a}\\right)\\right)$.\\\\
                Đặt $t = -\\frac{b}{2a}$, ta có phương trình: $at^2 + bt + %s = %s(%s - t) \\Leftrightarrow at^2 + (b+%s)t - %s = 0$.\\\\
                Kết hợp với $b = -%s a - 1$, giải hệ phương trình ta được $a = %s; b = %s$ (chọn $a < 0$ để vòm cong úp xuống).\\\\
                Vậy $(P): y = %s$.\\\\
                Diện tích thiết diện tại $B$ là: $S_B = \\int_0^{%s} \\left(%s\\right) \\text{d}x = %s$.\\\\
                Thiết diện tại $A$ và $B$ là hai hình phẳng đồng dạng với tỉ số đồng dạng $k = \\frac{AD}{BC} = \\frac{%s}{%s} = %s$.\\\\
                Suy ra diện tích thiết diện tại $A$ là $S_A = k^2 S_B = %s^2 \\cdot %s = %s$.\\\\
                Áp dụng công thức tính thể tích khối chóp cụt, thể tích kho chứa hàng là:\\\\
                $V = \\frac{1}{3} AB (S_A + S_B + \\sqrt{S_A S_B}) = \\frac{1}{3} \\cdot %s \\left(%s + %s + \\sqrt{%s \\cdot %s}\\right) = %s$.'''
                % (w1, w1, w1,
                   w1, w1,
                   w1, w1, w1, w1, w1**2, w1, w1, w1,
                   m, m, w1,
                   w1, m, w1, m, const_term,
                   w1, latex(a_frac), b,
                   poly_str,
                   w1, poly_str, latex(S1),
                   w2, w1, k,
                   k, latex(S1), latex(S2),
                   h, latex(S2), latex(S1), latex(S2), latex(S1), format_num(ans_true)))
                dapan='\\shortans[0]{$%s$}\n'%(format_num(ans_true))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

