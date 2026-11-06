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


def bt_dang37_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Random bài toán bằng cách thay đổi tọa độ các điểm
                # Parabol P1: y = a1*x^2 đi qua (x_lim, y_p1)
                x_lim = 4
                y_p1 = random.randint(7, 9) 
                a1 = Rational(y_p1, x_lim**2)
                f1 = a1 * x**2

                # Parabol P2: y = a2*x^2 + b2*x + c2 đi qua 3 điểm A, B, C
                # Điểm A(-4, yA), B(-2, yB), C(4, yC)
                yA = random.randint(5, 7)
                yB = random.randint(2, 4)
                yC = random.randint(4, 6)

                # Giải hệ phương trình tìm a2, b2, c2
                a2, b2, c2 = symbols('a2 b2 c2')
                eq1 = a2*(-4)**2 + b2*(-4) + c2 - yA
                eq2 = a2*(-2)**2 + b2*(-2) + c2 - yB
                eq3 = a2*(4)**2 + b2*(4) + c2 - yC
                sol = solve((eq1, eq2, eq3), (a2, b2, c2))

                f2 = sol[a2]*x**2 + sol[b2]*x + sol[c2]

                # B4: Tính diện tích S và làm tròn
                # Tính tích phân trị tuyệt đối từ -4 đến 4
                dien_tich_val = integrate(Abs(f1 - f2), (x, -4, 4))
                kq_float = float(dien_tich_val.evalf())

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % kq_str

                # Tạo các phương án sai (đảm bảo không trùng)
                s = []
                while len(s) < 3:
                    sai_val = kq_decimal + Decimal(str(random.uniform(-3, 3))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    sai_str = '$%s$' % str(sai_val).replace('.', ',')
                    if sai_str != da_dung and sai_str not in s:
                        s.append(sai_str)

                # Câu hỏi
                noidungcauhoi = ('''Trong lưới ô vuông có hai đường parabol như hình vẽ. Biết rằng mỗi ô vuông nhỏ có cạnh bằng $2$ cm. Diện tích của hình phẳng trong lưới ô vuông được giới hạn bởi hai đường parabol (phần gạch chéo) bằng bao nhiêu centimet vuông? (kết quả làm tròn đến hàng phần chục).
            \\begin{center} \\scalebox{0.6}{ 
            \\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1cm,y=1cm]
            \\draw[color=gray!30,dashed] (-5,-1) grid (5,9);
            \\draw[->] (-5,0) -- (5,0) node[right] {$x$};
            \\draw[->] (0,-1) -- (0,9) node[above] {$y$};
            \\node at (0.3,-0.3) {$O$};
            \\node at (-4,-0.4) {$-4$};
            \\node at (2,-0.4) {$2$};
            \\draw[thick,blue,samples=100,domain=-4.2:4.2] plot (\\x,{%s*(\\x)^2});
            \\draw[thick,red,samples=100,domain=-4.2:4.5] plot (\\x,{%s*(\\x)^2 + (%s)*\\x + (%s)});
            \\fill[pattern=north east lines,pattern color=blue!50,domain=-4:4,samples=100] 
                plot (\\x,{%s*(\\x)^2}) -- plot[domain=4:-4] (\\x,{%s*(\\x)^2 + (%s)*\\x + (%s)}) -- cycle;
            \\end{tikzpicture} }
            \\end{center}''' % (latex(float(a1)), latex(float(sol[a2])), latex(float(sol[b2])), latex(float(sol[c2])),
                                 latex(float(a1)), latex(float(sol[a2])), latex(float(sol[b2])), latex(float(sol[c2]))))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(s[0])
                da_s2 = str(s[1]) 
                da_s3 = str(s[2]) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Đã sửa lỗi thiếu %s)
                loigiai = ('''Ta đặt hệ trục tọa độ như hình vẽ. \\\\
                            Dựa vào hình vẽ, parabol $(P_1)$ có đỉnh tại gốc tọa độ $O(0;0)$ nên có dạng $y=ax^2$. \\\\
                            $(P_1)$ đi qua điểm $(4; %s)$ nên $%s = a \\cdot 4^2 \\Rightarrow a = %s$. \\\\
                            Vậy $(P_1): y = %s x^2$. \\\\
                            Parabol $(P_2)$ đi qua các điểm $(-4; %s)$, $(-2; %s)$ và $(4; %s)$. \\\\
                            Giả sử $(P_2): y = ax^2 + bx + c$. Thay tọa độ 3 điểm ta được hệ phương trình: \\\\
                            $\\left\\{\\begin{matrix} 16a - 4b + c = %s \\\\ 4a - 2b + c = %s \\\\ 16a + 4b + c = %s \\end{matrix}\\right. \\Rightarrow \\left\\{\\begin{matrix} a = %s \\\\ b = %s \\\\ c = %s \\end{matrix}\\right.$. \\\\
                            Vậy $(P_2): y = %s x^2 %s %s x + %s$. \\\\
                            Diện tích phần giới hạn bởi hai parabol từ $x=-4$ đến $x=4$ là: \\\\
                            $S = \\int\\limits_{-4}^{4} \\left| %s x^2 - \\left( %s x^2 %s %s x + %s \\right) \\right| dx \\approx %s$.'''
                            %(latex(y_p1), latex(y_p1), latex(a1), latex(a1), # 4 biến
                              latex(yA), latex(yB), latex(yC), # 3 biến
                              latex(yA), latex(yB), latex(yC), # 3 biến
                              latex(sol[a2]), latex(sol[b2]), latex(sol[c2]), # 3 biến
                              latex(sol[a2]), '+' if sol[b2]>=0 else '', latex(sol[b2]), latex(sol[c2]), # 4 biến (đã thêm %s ở trên)
                              latex(a1), latex(sol[a2]), '+' if sol[b2]>=0 else '', latex(sol[b2]), latex(sol[c2]), # 5 biến (đã thêm %s ở trên)
                              kq_str # 1 biến -> Tổng 23
                            ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

