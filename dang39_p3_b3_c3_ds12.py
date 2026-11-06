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


def bt_dang39_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Ngẫu nhiên hóa bài toán - Thay đổi độ dài cạnh hình lục giác
                a_val = random.randint(2, 8)  # Cạnh hình lục giác từ 3 đến 8 cm

                # Tính toán diện tích theo công thức S = (a^2 * sqrt(3)) / 2
                # Một phần diện tích giới hạn bởi 1 parabol và 2 bán kính là:
                # S_i = integral_{-a/2}^{a/2} ( (sqrt(3)/a)*x^2 + (a*sqrt(3))/4 ) dx - S_triangle

                a = symbols('a')
                x = symbols('x')

                # Parabol đi qua A(a/2, a*sqrt(3)/2) và B(-a/2, a*sqrt(3)/2) 
                # và tiếp xúc với OA: y = sqrt(3)x, OB: y = -sqrt(3)x
                # Phương trình parabol: y = (sqrt(3)/a)*x^2 + (a*sqrt(3))/4
                f_parabol = (sqrt(3)/a) * x**2 + (a*sqrt(3))/4

                # Tích phân phần parabol
                tp = integrate(f_parabol.subs(a, a_val), (x, -a_val/2, a_val/2))

                # Diện tích tam giác đều OAB
                s_tri = Rational(a_val**2, 4) * sqrt(3)

                # Diện tích 1 phần tô đậm
                s_one = tp - s_tri

                # Tổng diện tích 6 phần
                s_total = 6 * s_one

                # Tính giá trị xấp xỉ
                kq_val = float(s_total.evalf())
                kq_str = str(Decimal(str(kq_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Bước 4: Điều chỉnh các phương án sai
                da = kq_str

                # Tạo các đáp án nhiễu
                offsets = [-2.5, -1.2, 1.5, 2.8, 3.4, -3.1]
                random.shuffle(offsets)
                s = []
                for offset in offsets:
                    val = round(kq_val + offset, 1)
                    val_str = str(val).replace('.', ',')
                    if val_str != da:
                        s.append('$%s$' % val_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Trong hình bên là một chiếc đồng hồ treo tường cao cấp được thiết kế có phần ở giữa (phần tô đậm) dát vàng. Phần này được thiết kế như sau: \\\\
                - Vẽ hình lục giác đều $ABCDEF$ tâm $O$ và có cạnh bằng $%s$ cm;\\\\
                - Vẽ parabol $\\left(C_1\\right)$ tiếp xúc với các đường thẳng $OA, OB$ lần lượt tại $A$ và $B$;\\\\
                - Tương tự vẽ parabol $\\left(C_2\\right)$ tiếp xúc với các đường thẳng $OB, OC$ lần lượt tại $B$ và $C$; ...; parabol $\\left(C_6\\right)$ tiếp xúc với các đường thẳng $OF, OA$ lần lượt tại $F$ và $A$. }
                    { \\begin{tikzpicture}[scale=1, line width=1pt, >=stealth]
                        \\def\\r{%s}
                        \\foreach \\i in {0,60,120,180,240,300} {
                            \\draw (\\i:\\r) -- (\\i+60:\\r);
                            \\draw[dashed] (0,0) -- (\\i:\\r);
                            \\fill[yellow!50] (0,0) -- (\\i:\\r) .. controls ({\\i+30}:{\\r*0.2}) .. (\\i+60:\\r) -- cycle;
                            \\draw (\\i:\\r) .. controls ({\\i+30}:{\\r*0.2}) .. (\\i+60:\\r);
                        }
                        \\node at (60:\\r+0.4) {$A$}; \\node at (120:\\r+0.4) {$B$}; \\node at (180:\\r+0.4) {$C$};
                        \\node at (240:\\r+0.4) {$D$}; \\node at (300:\\r+0.4) {$E$}; \\node at (0:\\r+0.4) {$F$};
                        \\node at (0.3,-0.3) {$O$};
                        \\node at (0,1.2) {$(C_1)$};
                    \\end{tikzpicture} }
            Hình phẳng $\\left(H\\right)$ được giới hạn bởi sáu parabol $\\left(C_1\\right), \\left(C_2\\right), \\left(C_3\\right), \\left(C_4\\right), \\left(C_5\\right), \\left(C_6\\right)$ là phần sẽ được dát vàng. Hỏi phần dát vàng này có diện tích bằng bao nhiêu centimet vuông (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng phần chục)?'''
                                 % (latex(a_val),2))

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''\\begin{center} \\begin{tikzpicture}[scale=1, line width=1pt, >=stealth]
                        \\def\\r{%s}
                        \\foreach \\i in {0,60,120,180,240,300} {
                            \\draw (\\i:\\r) -- (\\i+60:\\r);
                            \\draw[dashed] (0,0) -- (\\i:\\r);
                            \\fill[yellow!50] (0,0) -- (\\i:\\r) .. controls ({\\i+30}:{\\r*0.2}) .. (\\i+60:\\r) -- cycle;
                            \\draw (\\i:\\r) .. controls ({\\i+30}:{\\r*0.2}) .. (\\i+60:\\r);
                        }
                        \\node at (60:\\r+0.4) {$A$}; \\node at (120:\\r+0.4) {$B$}; \\node at (170:\\r+0.4) {$C$};
                        \\node at (240:\\r+0.4) {$D$}; \\node at (300:\\r+0.4) {$E$}; \\node at (10:\\r+0.4) {$F$};
                        \\node at (0.3,-0.3) {$O$};
                        \\node at (0,1.2) {$(C_1)$};
                        \\draw[->] (-3,0) -- (3,0) node[right] {$x$};
                        \\draw[->] (0,-2.5) -- (0,2.5) node[right] {$y$};
                    \\end{tikzpicture} \\end{center}
                    Chọn hệ trục tọa độ sao cho gốc tọa độ trùng với tâm $O$ của lục giác đều. \\\\
            Xét phần diện tích giới hạn bởi parabol $\\left(C_1\\right)$ và hai đoạn thẳng $OA, OB$. \\\\
            Do $ABCDEF$ là lục giác đều cạnh $a=%s$ nên tam giác $OAB$ là tam giác đều. \\\\
            Tọa độ các đỉnh là $A\\left(\\frac{%s}{2}; \\frac{%s\\sqrt{3}}{2}\\right)$ và $B\\left(-\\frac{%s}{2}; \\frac{%s\\sqrt{3}}{2}\\right)$. \\\\
            Đường thẳng $OA$ có phương trình $y=\\sqrt{3}x$ và $OB$ có phương trình $y=-\\sqrt{3}x$. \\\\
            Parabol $\\left(C_1\\right)$ có dạng $y=kx^2+c$. Vì tiếp xúc với $OA$ tại $A$ nên đạo hàm $y'\\left(\\frac{%s}{2}\\right) = \\sqrt{3}$. \\\\
            Ta có $y'=2kx \\Rightarrow 2k \\cdot \\frac{%s}{2} = \\sqrt{3} \\Rightarrow k = \\frac{\\sqrt{3}}{%s}$. \\\\
            Vì parabol đi qua $A$ nên $\\frac{%s\\sqrt{3}}{2} = \\frac{\\sqrt{3}}{%s} \\cdot \\left(\\frac{%s}{2}\\right)^2 + c \\Rightarrow c = \\frac{%s\\sqrt{3}}{4}$. \\\\
            Vậy phương trình parabol $\\left(C_1\\right)$ là $y=\\frac{\\sqrt{3}}{%s}x^2 + \\frac{%s\\sqrt{3}}{4}$. \\\\
            Diện tích một phần tô đậm là $S_1 = \\int_{-\\frac{%s}{2}}^{\\frac{%s}{2}} \\left(\\frac{\\sqrt{3}}{%s}x^2 + \\frac{%s\\sqrt{3}}{4}\\right) \\text{d}x - S_{\\triangle OAB}$. \\\\
            Ta có $S_{\\triangle OAB} = \\frac{%s^2\\sqrt{3}}{4} = %s\\sqrt{3}$. \\\\
            Tính tích phân: $\\int_{-\\frac{%s}{2}}^{\\frac{%s}{2}} \\left(\\frac{\\sqrt{3}}{%s}x^2 + \\frac{%s\\sqrt{3}}{4}\\right) \\text{d}x = \\left. \\left(\\frac{\\sqrt{3}}{%s}x^3 + \\frac{%s\\sqrt{3}}{4}x\\right) \\right|_{-\\frac{%s}{2}}^{\\frac{%s}{2}} = \\frac{%s\\sqrt{3}}{3}$. \\\\
            Suy ra $S_1 = \\frac{%s\\sqrt{3}}{3} - %s\\sqrt{3} = \\frac{%s\\sqrt{3}}{12}$. \\\\
            Tổng diện tích phần dát vàng là $S = 6S_1 = \\frac{%s\\sqrt{3}}{2} = %s\\sqrt{3} \\approx %s$ cm$^2$.'''
                           % (latex(2),latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val),
                              latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val),
                              latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val),
                              latex(a_val), latex(Rational(a_val**2, 4)),
                              latex(a_val), latex(a_val), latex(3*a_val), latex(a_val), latex(9*a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val**2),
                              latex(a_val**2), latex(Rational(a_val**2, 4)), latex(a_val**2),
                              latex(a_val**2), latex(Rational(a_val**2, 2)), da))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(da))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

